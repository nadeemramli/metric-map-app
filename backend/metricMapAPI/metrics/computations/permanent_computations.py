"""Module for performing permanent computations on metrics data."""

from typing import Dict, List, Optional
import logging
from django.db import transaction
from django.core.exceptions import ValidationError

from .data_preparation import DataPreparation
from .feature_engineering import FeatureEngineering
from .computations_analyzer import Analyzer
from .computations_forecaster import Forecaster
from .computations_anomalies import AnomalyDetector
from .computations_relationships import RelationshipAnalyzer
from ..models import Metric, ComputationResult, Trend, TechnicalIndicator, Forecast, Anomaly, Correlation
from utils import log_exceptions, validate_metadata
from config import config

logger = logging.getLogger(__name__)

class PermanentComputations:
    def __init__(self, metric_ids: List[int]):
        self.metric_ids = metric_ids
        self.results = {}

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
        
        # Data Preparation
        data_prep = self.perform_data_preparation(metric_id)
        if not data_prep:
            return

        # Feature Engineering
        fe = self.perform_feature_engineering(metric_id, data_prep)
        if not fe:
            return

        # Analysis
        analysis_results = self.perform_analysis(metric_id, fe)
        self.save_analysis_results(metric_id, analysis_results)

        # Forecasting
        forecast_results = self.perform_forecasting(metric_id, fe)
        self.save_forecast_results(metric_id, forecast_results)

        # Anomaly Detection
        anomaly_results = self.perform_anomaly_detection(metric_id, fe)
        self.save_anomaly_results(metric_id, anomaly_results)

        # Relationship Analysis
        relationship_results = self.perform_relationship_analysis(metric_id, fe)
        self.save_relationship_results(metric_id, relationship_results)

        # Store results
        self.results[metric_id] = {
            'analysis': analysis_results,
            'forecast': forecast_results,
            'anomalies': anomaly_results,
            'relationships': relationship_results
        }

        # Generate and save report
        report = self.generate_markdown_report(metric_id, self.results[metric_id])
        self.save_report(metric_id, report)

    def perform_data_preparation(self, metric_id: int) -> Optional[DataPreparation]:
        try:
            data_prep = DataPreparation(metric_id)
            cleaned_df, metadata = data_prep.prepare_data()
            
            logger.info(f"Data preparation statistics for metric {metric_id}:")
            logger.info(f"Outliers handled: {metadata.get('outliers_handled', 0)}")
            logger.info(f"Missing values imputed: {metadata.get('missing_values_imputed', 0)}")
            logger.info(f"Data quality score: {metadata.get('data_quality_score', 0)}")

            if metadata.get('data_quality_score', 0) < config.MIN_DATA_QUALITY_SCORE:
                logger.warning(f"Data quality score too low for metric {metric_id}. Skipping further computations.")
                return None

            return data_prep
        except Exception as e:
            logger.error(f"Error in data preparation for metric {metric_id}: {str(e)}")
            return None

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
            analyzer = Analyzer(metric_id)
            trend_analysis = analyzer.analyze_trend()
            technical_indicators = analyzer.calculate_technical_indicators()
            return {'trend': trend_analysis, 'technical_indicators': technical_indicators}
        except Exception as e:
            logger.error(f"Error in analysis for metric {metric_id}: {str(e)}")
            return {}

    def perform_forecasting(self, metric_id: int, fe: FeatureEngineering) -> Dict:
        try:
            forecaster = Forecaster(metric_id)
            sarima_forecast = forecaster.sarima_forecast()
            prophet_forecast = forecaster.prophet_forecast()
            return {'sarima': sarima_forecast, 'prophet': prophet_forecast}
        except Exception as e:
            logger.error(f"Error in forecasting for metric {metric_id}: {str(e)}")
            return {}

    def perform_anomaly_detection(self, metric_id: int, fe: FeatureEngineering) -> Dict:
        try:
            anomaly_detector = AnomalyDetector(metric_id)
            anomalies = anomaly_detector.detect_anomalies()
            return {'anomalies': anomalies}
        except Exception as e:
            logger.error(f"Error in anomaly detection for metric {metric_id}: {str(e)}")
            return {}

    def perform_relationship_analysis(self, metric_id: int, fe: FeatureEngineering) -> Dict:
        try:
            relationship_analyzer = RelationshipAnalyzer(metric_id)
            correlations = relationship_analyzer.analyze_relationships(self.metric_ids)
            lagged_correlations = relationship_analyzer.detect_lagged_relationships(self.metric_ids)
            return {'correlations': correlations, 'lagged_correlations': lagged_correlations}
        except Exception as e:
            logger.error(f"Error in relationship analysis for metric {metric_id}: {str(e)}")
            return {}

    def save_analysis_results(self, metric_id: int, results: Dict):
        metric = Metric.objects.get(id=metric_id)
        
        # Save trend
        Trend.objects.update_or_create(
            metric=metric,
            tenant=self.tenant,
            defaults={
                'trend_type': results['trend']['trend_type'],
                'start_date': results['trend']['start_date'],
                'end_date': results['trend']['end_date'],
                'trend_value': results['trend']['trend_value'],
                'notes': results['trend']['notes'],
                'slope': results['trend']['slope']
            }
        )
        
        # Save technical indicators
        for indicator in results['technical_indicators']:
            TechnicalIndicator.objects.update_or_create(
                metric=metric,
                tenant=self.tenant,
                date=indicator['date'],
                defaults={
                    'stochastic_value': indicator['stochastic_value'],
                    'rsi_value': indicator['rsi_value'],
                    'percent_change': indicator['percent_change'],
                    'moving_average': indicator['moving_average']
                }
            )

    def save_forecast_results(self, metric_id: int, results: Dict):
        metric = Metric.objects.get(id=metric_id)
        
        for model, forecasts in results.items():
            for forecast in forecasts:
                Forecast.objects.update_or_create(
                    metric=metric,
                    tenant=self.tenant,
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
        metric = Metric.objects.get(id=metric_id)
        
        for anomaly in results['anomalies']:
            Anomaly.objects.update_or_create(
                metric=metric,
                tenant=self.tenant,
                detection_date=anomaly['date'],
                defaults={
                    'anomaly_value': anomaly['value'],
                    'anomaly_score': anomaly['score'],
                    'notes': anomaly.get('notes', ''),
                    'anomaly_type': anomaly.get('type', AnomalyType.IGNORE.name),
                    'quality': anomaly.get('quality', QualityType.LOW.name)
                }
            )

    def save_relationship_results(self, metric_id: int, results: Dict):
        metric = Metric.objects.get(id=metric_id)
        
        for correlation in results['correlations']:
            Correlation.objects.update_or_create(
                metric1=metric,
                metric2=Metric.objects.get(id=correlation['metric_id']),
                tenant=self.tenant,
                lag=correlation['lag'],
                defaults={
                    'pearson_correlation': correlation['pearson'],
                    'spearman_correlation': correlation['spearman']
                }
            )

    def generate_markdown_report(self, metric_id: int, result: Dict) -> str:
        metric = Metric.objects.get(id=metric_id)
        report = f"# Analysis Report for {metric.name}\n\n"
        
        # Trend Analysis
        report += "## Trend Analysis\n"
        trend = result['analysis']['trend']
        report += f"- Trend Type: {trend['trend_type']}\n"
        report += f"- Period: {trend['start_date']} to {trend['end_date']}\n"
        report += f"- Trend Value: {trend['trend_value']:.2f}\n"
        report += f"- Slope: {trend['slope']:.2f}\n\n"
        
        # Technical Indicators
        report += "## Technical Indicators\n"
        indicators = result['analysis']['technical_indicators'][-1]  # Most recent
        report += f"- Date: {indicators['date']}\n"
        report += f"- Stochastic: {indicators['stochastic_value']:.2f}\n"
        report += f"- RSI: {indicators['rsi_value']:.2f}\n"
        report += f"- Percent Change: {indicators['percent_change']:.2f}%\n"
        report += f"- Moving Average: {indicators['moving_average']:.2f}\n\n"
        
        # Forecasting
        report += "## Forecasting\n"
        for model, forecasts in result['forecast'].items():
            report += f"### {model.upper()} Model\n"
            latest_forecast = forecasts[-1]  # Most recent forecast
            report += f"- Date: {latest_forecast['date']}\n"
            report += f"- Forecast Value: {latest_forecast['value']:.2f}\n"
            report += f"- Confidence Interval: ({latest_forecast['lower_bound']:.2f}, {latest_forecast['upper_bound']:.2f})\n\n"
        
        # Anomalies
        report += "## Anomalies\n"
        anomalies = result['anomalies']['anomalies']
        if anomalies:
            for anomaly in anomalies[:5]:  # Show up to 5 recent anomalies
                report += f"- Date: {anomaly['date']}\n"
                report += f"  Value: {anomaly['value']:.2f}\n"
                report += f"  Score: {anomaly['score']:.2f}\n"
                report += f"  Type: {anomaly['type']}\n\n"
        else:
            report += "No significant anomalies detected.\n\n"
        
        # Relationships
        report += "## Relationships\n"
        correlations = result['relationships']['correlations']
        if correlations:
            for corr in correlations[:5]:  # Show top 5 correlations
                related_metric = Metric.objects.get(id=corr['metric_id'])
                report += f"- Related Metric: {related_metric.name}\n"
                report += f"  Pearson Correlation: {corr['pearson']:.2f}\n"
                report += f"  Spearman Correlation: {corr['spearman']:.2f}\n\n"
        else:
            report += "No significant correlations found.\n\n"
        
        return report

    def save_report(self, metric_id: int, report: str):
        metric = Metric.objects.get(id=metric_id)
        ComputationResult.objects.update_or_create(
            metric=metric,
            tenant=self.tenant,
            defaults={
                'report': report
            }
        )
        logger.info(f"Saved computation report for metric {metric_id}")

    @transaction.atomic
    def compile_and_store_results(self):
        for metric_id, result in self.results.items():
            try:
                metric = Metric.objects.get(id=metric_id)
                report = self.generate_markdown_report(metric_id, result)
                
                ComputationResult.objects.update_or_create(
                    metric=metric,
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
    pc = PermanentComputations(metric_ids)
    pc.run_all_computations()