"""Module for performing permanent computations on metrics data."""

from typing import Dict, List, Optional, Union
import logging
from django.db import transaction
import pandas as pd
from django.core.exceptions import ValidationError
from django.apps import apps
from .utils import log_exceptions, validate_metadata
from .config import Config
from .data_preparation import DataPreparation
from .feature_engineering import FeatureEngineering

logger = logging.getLogger(__name__)

class PermanentComputations:
    def __init__(self, metric_ids: Union[int, List[int]], client):
        print(f"Initializing PermanentComputations with metric_ids: {metric_ids}")
        self.metric_ids = [metric_ids] if isinstance(metric_ids, int) else metric_ids
        self.client = client
        if not self.client:
            raise ValueError("Client must be provided")
        self.results = {}
        print("Finished initializing PermanentComputations")

    @log_exceptions
    def run_all_computations(self):
        logger.info(f"Starting all computations for metrics: {self.metric_ids}")
        for metric_id in self.metric_ids:
            try:
                self.run_computations_for_metric(metric_id)
            except Exception as e:
                logger.error(f"Failed to complete computations for metric {metric_id}: {str(e)}")
        self.compile_and_store_results()

    def run_computations_for_metric(self, metric_id: int):
        logger.info(f"Starting computations for metric {metric_id}")
        
        try:
            Metric = apps.get_model('metrics', 'Metric')
            metric = Metric.objects.get(id=metric_id)
        except Metric.DoesNotExist:
            raise ValueError(f"Invalid metric ID: {metric_id}")
        
        try:
            # Data Preparation
            logger.info(f"Starting data preparation for metric {metric_id}")
            try:
                data_prep = DataPreparation(metric_id, self.client)
                prepared_data, metadata = data_prep.prepare_data()
            except ValueError as ve:
                logger.warning(f"Data preparation failed for metric {metric_id}: {str(ve)}")
                self.results[metric_id] = {'error': str(ve)}
                return
            logger.info(f"Data preparation completed for metric {metric_id}")

            # Feature Engineering
            logger.info(f"Starting feature engineering for metric {metric_id}")
            fe = self.perform_feature_engineering(metric_id, data_prep)
            if not fe:
                logger.error(f"Feature engineering failed for metric {metric_id}. Skipping further computations.")
                return
            dynamic_params = fe.compute_dynamic_parameters()
            engineered_features = fe.engineer_features()
            logger.info(f"Feature engineering completed for metric {metric_id}")

            # Initialize results dictionary
            self.results[metric_id] = {
                'analysis': {},
                'trend': {},
                'forecast': {},
                'anomalies': {},
                'relationships': {}
            }

            # Analysis
            try:
                from .computations_analyzer import Analyzer
                logger.info(f"Starting analysis for metric {metric_id}")
                analyzer = Analyzer(metric_id, prepared_data, dynamic_params, engineered_features)
                analysis_results = analyzer.analyze()
                self.save_analysis_results(metric_id, analysis_results)
                self.results[metric_id]['analysis'] = analysis_results
                self.results[metric_id]['trend'] = analysis_results.get('trend', {})
                logger.info(f"Analysis completed for metric {metric_id}")
            except Exception as e:
                logger.error(f"Error in analysis for metric {metric_id}: {str(e)}")
                self.results[metric_id]['analysis'] = {'error': str(e)}
                self.results[metric_id]['trend'] = {'error': str(e)}

            # Forecasting
            try:
                from .computations_forecaster import Forecaster
                logger.info(f"Starting forecasting for metric {metric_id}")
                forecaster = Forecaster(metric_id, prepared_data, dynamic_params, engineered_features)
                forecast_results = forecaster.forecast()
                self.save_forecast_results(metric_id, forecast_results)
                self.results[metric_id]['forecast'] = forecast_results
                logger.info(f"Forecasting completed for metric {metric_id}")
            except Exception as e:
                logger.error(f"Error in forecasting for metric {metric_id}: {str(e)}")
                self.results[metric_id]['forecast'] = {'error': str(e)}

            # Anomaly Detection
            try:
                from .computations_anomalies import AnomalyDetector
                logger.info(f"Starting anomaly detection for metric {metric_id}")
                anomaly_detector = AnomalyDetector(metric_id, prepared_data, dynamic_params, engineered_features)
                anomaly_results = anomaly_detector.detect_anomalies()
                self.save_anomaly_results(metric_id, anomaly_results)
                self.results[metric_id]['anomalies'] = anomaly_results
                logger.info(f"Anomaly detection completed for metric {metric_id}")
            except Exception as e:
                logger.error(f"Error in anomaly detection for metric {metric_id}: {str(e)}")
                self.results[metric_id]['anomalies'] = {'error': str(e)}

            # Relationship Analysis
            try:
                from .computations_relationships import RelationshipAnalyzer
                logger.info(f"Starting relationship analysis for metric {metric_id}")
                relationship_analyzer = RelationshipAnalyzer(metric_id, prepared_data, dynamic_params, engineered_features)
                relationship_results = relationship_analyzer.analyze_relationships()
                self.save_relationship_results(metric_id, relationship_results)
                self.results[metric_id]['relationships'] = relationship_results
                logger.info(f"Relationship analysis completed for metric {metric_id}")
            except Exception as e:
                logger.error(f"Error in relationship analysis for metric {metric_id}: {str(e)}")
                self.results[metric_id]['relationships'] = {'error': str(e)}

            # Generate and save report
            try:
                logger.info(f"Generating report for metric {metric_id}")
                report = self.generate_markdown_report(metric_id, self.results[metric_id])
                self.save_report(metric_id, report)
                logger.info(f"Report generated and saved for metric {metric_id}")
            except Exception as e:
                logger.error(f"Error generating or saving report for metric {metric_id}: {str(e)}")

            logger.info(f"All computations completed for metric {metric_id}")
        except Exception as e:
            logger.error(f"Unexpected error in computations for metric {metric_id}: {str(e)}")
            self.results[metric_id] = {'error': str(e)}

    def perform_data_preparation(self, metric_id: int) -> Optional[DataPreparation]:
        logger.info(f"Starting data preparation for metric {metric_id}")
        
        try:
            data_prep = DataPreparation(metric_id, self.client)
            logger.info(f"DataPreparation object created: {data_prep}")
            cleaned_df, metadata = data_prep.prepare_data()
            logger.info(f"prepare_data() called, returned DataFrame of shape {cleaned_df.shape}")
            
            logger.info(f"Data preparation statistics for metric {metric_id}:")
            logger.info(f"Data quality score: {metadata.get('data_quality_score', 0)}")
            logger.info(f"Number of data points: {len(cleaned_df)}")
            
            logger.info(f"Cleaned DataFrame shape: {cleaned_df.shape if cleaned_df is not None else 'None'}")
            logger.info(f"Metadata: {metadata}")
            
            if cleaned_df.empty:
                raise ValueError(f"No data available for metric {metric_id}")
            
            date_range = f"{cleaned_df.index.min()} to {cleaned_df.index.max()}"
            logger.info(f"Date range: {date_range}")
            
            if metadata.get('data_quality_score', 0) < Config.MIN_DATA_QUALITY_SCORE:
                raise ValueError(f"Data quality score ({metadata.get('data_quality_score', 0)}) is below threshold ({Config.MIN_DATA_QUALITY_SCORE}) for metric {metric_id}")

            return data_prep
        except ValueError as ve:
            logger.warning(f"No data available for metric {metric_id}: {str(ve)}")
            raise  # Re-raise the ValueError
        except Exception as e:
            logger.error(f"Unexpected error in data preparation for metric {metric_id}: {str(e)}")
            logger.exception("Full traceback:")
            raise ValueError(f"Error in data preparation: {str(e)}")

    def perform_feature_engineering(self, metric_id: int, data_prep: DataPreparation) -> Optional[FeatureEngineering]:
        try:
            fe = FeatureEngineering(metric_id)
            fe.engineer_features()
            data_profile = fe.profile_data()
            
            logger.info(f"Data profile for metric {metric_id}:")
            for key, value in data_profile.items():
                logger.info(f"{key}: {value}")

            return fe
        except Exception as e:
            logger.error(f"Error in feature engineering for metric {metric_id}: {str(e)}")
            return None

    def perform_analysis(self, metric_id: int, fe: FeatureEngineering) -> Dict:
        try:
            from .computations_analyzer import Analyzer
            analyzer = Analyzer(metric_id)
            trend_analysis = analyzer.analyze_trend()
            technical_indicators = analyzer.calculate_technical_indicators()
            seasonality = analyzer.detect_seasonality()
            return {
                'trend': trend_analysis, 
                'technical_indicators': technical_indicators,
                'seasonality': seasonality
            }
        except Exception as e:
            logger.error(f"Error in analysis for metric {metric_id}: {str(e)}")
            return {
                'trend': {
                    'trend_type': 'unknown',
                    'start_date': None,
                    'end_date': None,
                    'trend_value': None,
                    'slope': None,
                    'notes': f"Error occurred: {str(e)}"
                },
                'technical_indicators': [],
                'seasonality': {},
                'error': str(e)
            }

    def perform_forecasting(self, metric_id: int, data_prep: DataPreparation) -> Dict:
        logger.info(f"Starting forecasting for metric {metric_id}")
        try:
            from .computations_forecaster import Forecaster
            forecaster = Forecaster(data_prep.cleaned_df, data_prep.metadata)
            forecast_results = forecaster.forecast()
            if not forecast_results:
                logger.warning(f"No forecast results generated for metric {metric_id}")
                return {'error': 'No forecast results generated'}
            
            # Add confidence interval to each forecast
            for model, forecasts in forecast_results.items():
                logger.info(f"Processing forecasts for model: {model}")
                for forecast in forecasts:
                    forecast['confidence_interval'] = (forecast['lower_bound'], forecast['upper_bound'])
            
            return forecast_results
        except Exception as e:
            logger.error(f"Error in forecasting for metric {metric_id}: {str(e)}")
            return {'error': str(e)}

    def _validate_forecast(self, forecast):
        if not isinstance(forecast, list) or not forecast:
            return None
        validated_forecast = []
        for f in forecast:
            if isinstance(f, dict) and all(key in f for key in ['date', 'value', 'lower_bound', 'upper_bound']):
                validated_forecast.append(f)
        return validated_forecast if validated_forecast else None

    def perform_anomaly_detection(self, metric_id: int, fe: FeatureEngineering) -> Dict:
        try:
            from .computations_anomalies import AnomalyDetector
            anomaly_detector = AnomalyDetector(metric_id)
            anomalies = anomaly_detector.detect_anomalies()
            if isinstance(anomalies, pd.DataFrame):
                return {'anomalies': anomalies.to_dict('records')}
            else:
                logger.warning(f"Unexpected result from anomaly detection for metric {metric_id}")
                return {'anomalies': []}
        except Exception as e:
            logger.error(f"Error in anomaly detection for metric {metric_id}: {str(e)}")
            return {'anomalies': []}

    def perform_relationship_analysis(self, metric_id: int, fe: FeatureEngineering) -> Dict:
        try:
            from .computations_relationships import RelationshipAnalyzer
            relationship_analyzer = RelationshipAnalyzer(metric_id)
            correlations = relationship_analyzer.analyze_relationships(self.metric_ids)
            lagged_correlations = relationship_analyzer.detect_lagged_relationships(self.metric_ids)
            
            relationships = {
                'correlations': correlations,
                'lagged_correlations': lagged_correlations
            }
            
            return relationships
        except Exception as e:
            logger.error(f"Error in relationship analysis for metric {metric_id}: {str(e)}")
            return {'correlations': [], 'lagged_correlations': []}

    def save_analysis_results(self, metric_id: int, results: Dict):
        try:
            Metric = apps.get_model('metrics', 'Metric')
            metric = Metric.objects.get(id=metric_id)
            
            with transaction.atomic():
                # Save trend
                Trend = apps.get_model('metrics', 'Trend')
                Trend.objects.update_or_create(
                    metric=metric,
                    client=self.client,
                    defaults={
                        'trend_type': results['trend']['trend_type'],
                        'start_date': results['trend']['start_date'],
                        'end_date': results['trend']['end_date'],
                        'trend_value': results['trend']['trend_value'],
                        'notes': results['trend'].get('notes', ''),
                        'slope': results['trend']['slope']
                    }
                )
                
                # Save technical indicators
                TechnicalIndicator = apps.get_model('metrics', 'TechnicalIndicator')
                for indicator in results['technical_indicators']:
                    TechnicalIndicator.objects.update_or_create(
                        metric=metric,
                        client=self.client,
                        date=indicator['date'],
                        defaults={
                            'stochastic_value': indicator.get('stochastic_value'),
                            'rsi_value': indicator.get('rsi_value'),
                            'percent_change': indicator.get('percent_change'),
                            'moving_average': indicator.get('moving_average')
                        }
                    )
            
            logger.info(f"Successfully saved analysis results for metric {metric_id}")
        except Metric.DoesNotExist:
            logger.error(f"Metric with id {metric_id} does not exist")
        except KeyError as e:
            logger.error(f"Missing key in results dictionary for metric {metric_id}: {str(e)}")
        except ValidationError as e:
            logger.error(f"Validation error while saving analysis results for metric {metric_id}: {str(e)}")
        except transaction.TransactionManagementError as e:
            logger.error(f"Transaction error while saving analysis results for metric {metric_id}: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error saving analysis results for metric {metric_id}: {str(e)}")

    def save_forecast_results(self, metric_id: int, results: Dict):
        Metric = apps.get_model('metrics', 'Metric')
        metric = Metric.objects.get(id=metric_id)
        
        Forecast = apps.get_model('metrics', 'Forecast')
        for model, forecasts in results.items():
            for forecast in forecasts:
                Forecast.objects.update_or_create(
                    metric=metric,
                    client=self.client,
                    forecast_date=forecast['date'],
                    model_used=model,
                    defaults={
                        'forecast_value': forecast['value'],
                        'lower_bound': forecast['lower_bound'],
                        'upper_bound': forecast['upper_bound'],
                        'confidence_interval': forecast['confidence_interval'],
                        'accuracy': forecast.get('accuracy'),
                        'variance': forecast.get('variance')
                    }
                )

    def save_anomaly_results(self, metric_id: int, results: Dict):
        try:
            Metric = apps.get_model('metrics', 'Metric')
            metric = Metric.objects.get(id=metric_id)
            
            Anomaly = apps.get_model('metrics', 'Anomaly')
            for anomaly in results['anomalies']:
                Anomaly.objects.update_or_create(
                    metric=metric,
                    client=self.client,
                    detection_date=anomaly['date'],
                    defaults={
                        'anomaly_value': anomaly['value'],
                        'anomaly_score': anomaly['score'],
                        'notes': anomaly.get('notes', ''),
                        'anomaly_type': anomaly.get('type', 'UNKNOWN'),
                        'quality': anomaly.get('quality', 'LOW')
                    }
                )
            logger.info(f"Successfully saved anomaly results for metric {metric_id}")
        except Metric.DoesNotExist:
            logger.error(f"Metric with id {metric_id} does not exist")
        except KeyError as e:
            logger.error(f"Missing key in anomaly results for metric {metric_id}: {str(e)}")
        except Exception as e:
            logger.error(f"Error in saving anomaly results for metric {metric_id}: {str(e)}")

    def save_relationship_results(self, metric_id: int, results: Dict):
        Metric = apps.get_model('metrics', 'Metric')
        metric = Metric.objects.get(id=metric_id)
        
        Correlation = apps.get_model('metrics', 'Correlation')
        for correlation in results['correlations']:
            Correlation.objects.update_or_create(
                metric1=metric,
                metric2=Metric.objects.get(id=correlation['metric_id']),
                client=self.client,
                lag=correlation['lag'],
                defaults={
                    'pearson_correlation': correlation['pearson'],
                    'spearman_correlation': correlation['spearman']
                }
            )

    def generate_markdown_report(self, metric_id: int, result: Dict) -> str:
        Metric = apps.get_model('metrics', 'Metric')
        metric = Metric.objects.get(id=metric_id)
        report = f"# Analysis Report for {metric.name}\n\n"
        
        # Trend Analysis
        report += "## Trend Analysis\n"
        trend = result.get('trend', {})
        if 'error' in trend:
            report += f"Error in trend analysis: {trend['error']}\n\n"
        else:
            report += f"- Trend Type: {trend.get('trend_type', 'Unknown')}\n"
            report += f"- Period: {trend.get('start_date', 'Unknown')} to {trend.get('end_date', 'Unknown')}\n"
            report += f"- Trend Value: {trend.get('trend_value', 'Unknown')}\n"
            report += f"- Slope: {trend.get('slope', 'Unknown')}\n\n"
        
        # Technical Indicators
        report += "## Technical Indicators\n"
        indicators = result.get('analysis', {}).get('technical_indicators', [])
        if indicators:
            latest = indicators[-1]  # Most recent
            report += f"- Date: {latest.get('date', 'Unknown')}\n"
            report += f"- Stochastic: {latest.get('stochastic_value', 'Unknown')}\n"
            report += f"- RSI: {latest.get('rsi_value', 'Unknown')}\n"
            report += f"- Percent Change: {latest.get('percent_change', 'Unknown')}%\n"
            report += f"- Moving Average: {latest.get('moving_average', 'Unknown')}\n\n"
        else:
            report += "No technical indicators available.\n\n"
        
        # Forecasting
        report += "## Forecasting\n"
        forecasts = result.get('forecast', {})
        if 'error' in forecasts:
            report += f"Error in forecasting: {forecasts['error']}\n\n"
        else:
            for model, model_forecasts in forecasts.items():
                report += f"### {model.upper()} Model\n"
                if model_forecasts:
                    latest = model_forecasts[-1]  # Most recent forecast
                    report += f"- Date: {latest.get('date', 'Unknown')}\n"
                    report += f"- Forecast Value: {latest.get('value', 'Unknown')}\n"
                    report += f"- Confidence Interval: ({latest.get('lower_bound', 'Unknown')}, {latest.get('upper_bound', 'Unknown')})\n\n"
                else:
                    report += "No valid forecast available for this model.\n\n"
        
        # Anomalies
        report += "## Anomalies\n"
        anomalies = result.get('anomalies', {}).get('anomalies', [])
        if 'error' in result.get('anomalies', {}):
            report += f"Error in anomaly detection: {result['anomalies']['error']}\n\n"
        elif anomalies:
            for anomaly in anomalies[:5]:  # Show up to 5 recent anomalies
                report += f"- Date: {anomaly.get('date', 'Unknown')}\n"
                report += f"  Value: {anomaly.get('value', 'Unknown')}\n"
                report += f"  Score: {anomaly.get('score', 'Unknown')}\n"
                report += f"  Type: {anomaly.get('type', 'Unknown')}\n\n"
        else:
            report += "No significant anomalies detected.\n\n"
        
        # Relationships
        report += "## Relationships\n"
        correlations = result.get('relationships', {}).get('correlations', [])
        if 'error' in result.get('relationships', {}):
            report += f"Error in relationship analysis: {result['relationships']['error']}\n\n"
        elif correlations:
            for corr in correlations[:5]:  # Show top 5 correlations
                try:
                    related_metric = Metric.objects.get(id=corr['metric_id'])
                    report += f"- Related Metric: {related_metric.name}\n"
                except Metric.DoesNotExist:
                    report += f"- Related Metric: Unknown (ID: {corr['metric_id']})\n"
                report += f"  Pearson Correlation: {corr.get('pearson', 'Unknown')}\n"
                report += f"  Spearman Correlation: {corr.get('spearman', 'Unknown')}\n\n"
        else:
            report += "No significant correlations found.\n\n"
        
        return report

    def save_report(self, metric_id: int, report: str):
        Metric = apps.get_model('metrics', 'Metric')
        metric = Metric.objects.get(id=metric_id)
        Report = apps.get_model('metrics', 'Report')
        Report.objects.update_or_create(
            metric=metric,
            client=self.client,
            defaults={
                'report': report
            }
        )
        logger.info(f"Saved computation report for metric {metric_id}")

    @transaction.atomic
    def compile_and_store_results(self):
        for metric_id, result in self.results.items():
            try:
                Metric = apps.get_model('metrics', 'Metric')
                metric = Metric.objects.get(id=metric_id)
                report = self.generate_markdown_report(metric_id, result)
                
                Report = apps.get_model('metrics', 'Report')
                Report.objects.update_or_create(
                    metric=metric,
                    client=self.client,
                    defaults={
                        'analysis_result': result['analysis'],
                        'forecast_result': result['forecast'],
                        'anomaly_result': result['anomalies'],
                        'relationship_result': result['relationships'],
                        'report': report
                    }
                )
                logger.info(f"Stored computation results for metric {metric_id}")
            except Metric.DoesNotExist:
                logger.error(f"Metric with id {metric_id} does not exist")
            except Exception as e:
                logger.error(f"Error storing results for metric {metric_id}: {str(e)}")

def run_permanent_computations(metric_ids: List[int]):
    import pdb; pdb.set_trace()  # This will force a breakpoint
    pc = PermanentComputations(metric_ids)
    pc.run_all_computations()

"""
PermanentComputations class for performing comprehensive analysis on metric data.

This class orchestrates the entire computation process for metrics, including:
- Data preparation
- Feature engineering
- Trend analysis
- Forecasting
- Anomaly detection
- Relationship analysis

Data Flow:
1. Initialize with metric IDs and client
2. For each metric:
   a. Prepare data
   b. Engineer features
   c. Perform analysis (trend, technical indicators)
   d. Generate forecasts
   e. Detect anomalies
   f. Analyze relationships with other metrics
3. Compile and store results
4. Generate and save markdown report

Output Format:
A dictionary containing results for each metric ID, with the following structure:
{
    metric_id: {
        'analysis': {
            'trend': {...},
            'technical_indicators': [...]
        },
        'forecast': {
            'sarima': [...],
            'prophet': [...]
        },
        'anomalies': {
            'anomalies': [...]
        },
        'relationships': {
            'correlations': [...],
            'lagged_correlations': [...]
        }
    }
}

Output Example:
{
    1: {
        'analysis': {
            'trend': {
                'trend_type': 'increasing',
                'start_date': '2023-01-01',
                'end_date': '2023-12-31',
                'trend_value': 10.5,
                'slope': 0.5
            },
            'technical_indicators': [
                {
                    'date': '2023-12-31',
                    'stochastic_value': 75.5,
                    'rsi_value': 60.2,
                    'percent_change': 2.5,
                    'moving_average': 105.3
                }
            ]
        },
        'forecast': {
            'sarima': [
                {
                    'date': '2024-01-01',
                    'value': 110.5,
                    'lower_bound': 105.2,
                    'upper_bound': 115.8
                }
            ],
            'prophet': [
                {
                    'date': '2024-01-01',
                    'value': 111.2,
                    'lower_bound': 106.5,
                    'upper_bound': 116.9
                }
            ]
        },
        'anomalies': {
            'anomalies': [
                {
                    'date': '2023-06-15',
                    'value': 150.0,
                    'score': 0.95,
                    'type': 'SPIKE'
                }
            ]
        },
        'relationships': {
            'correlations': [
                {
                    'metric_id': 2,
                    'pearson': 0.85,
                    'spearman': 0.82
                }
            ],
            'lagged_correlations': [
                {
                    'metric_id': 3,
                    'lag': 2,
                    'correlation': 0.75
                }
            ]
        }
    }
}
"""