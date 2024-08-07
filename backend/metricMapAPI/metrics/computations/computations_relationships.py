# computations_relationships.py

import pandas as pd
import numpy as np
from scipy import stats
import networkx as nx
from typing import List, Dict, Tuple, Any
import logging
from .data_preparation import DataPreparation
from .feature_engineering import FeatureEngineering
from django.apps import apps

logger = logging.getLogger(__name__)

class RelationshipAnalyzer:
    def __init__(self, metric_id: int, prepared_data=None, dynamic_params=None, engineered_features=None):
        self.metric_id = metric_id
        if prepared_data is not None:
            self.df, self.metadata = prepared_data
        else:
            Metric = apps.get_model('metrics', 'Metric')
            metric = Metric.objects.get(id=metric_id)
            data_prep = DataPreparation(metric_id, metric.tenant)
            self.df, self.metadata = data_prep.prepare_data()
        
        self.fe = FeatureEngineering(metric_id)
        self.features = engineered_features if engineered_features is not None else self.fe.engineer_features()
        self.dynamic_params = dynamic_params if dynamic_params is not None else self.fe.compute_dynamic_parameters()
        self.metric = self.get_metric()
        self.tenant = self.metric.tenant
        self.project = self.metric.project

    def get_metric(self):
        Metric = apps.get_model('metrics', 'Metric')
        return Metric.objects.get(id=self.metric_id)

    def analyze_relationships(self, other_metric_ids: List[int]) -> List[Dict]:
        correlations = []
        for other_metric_id in other_metric_ids:
            if other_metric_id != self.metric_id:
                pearson_result = self.calculate_correlation(other_metric_id, 'pearson')
                spearman_result = self.calculate_correlation(other_metric_id, 'spearman')
                correlations.append({
                    'metric_id': other_metric_id,
                    'pearson': pearson_result.get('correlation'),
                    'spearman': spearman_result.get('correlation')
                })
        return correlations

    def detect_lagged_relationships(self, other_metric_ids: List[int]) -> List[Dict]:
        lagged_correlations = []
        for other_metric_id in other_metric_ids:
            if other_metric_id != self.metric_id:
                lagged_results = self.calculate_lagged_correlation(other_metric_id)
                lagged_correlations.append({
                    'metric_id': other_metric_id,
                    'lagged_correlations': lagged_results
                })
        return lagged_correlations
    
    def calculate_correlation(self, other_metric_id: int, method: str) -> Dict[str, float]:
        try:
            Metric = apps.get_model('metrics', 'Metric')
            other_metric = Metric.objects.get(id=other_metric_id)
            data_prep = DataPreparation(other_metric_id, other_metric.tenant)
            df2, _ = data_prep.prepare_data()

             # Ensure the DataFrames have the same index
            common_index = self.df.index.intersection(df2.index)
            df1 = self.df.loc[common_index]
            df2 = df2.loc[common_index]
            
            merged_df = pd.merge(self.df, df2, left_index=True, right_index=True, suffixes=('_1', '_2'))
            if method == 'pearson':
                corr, p_value = stats.pearsonr(merged_df['value_1'], merged_df['value_2'])
            elif method == 'spearman':
                corr, p_value = stats.spearmanr(merged_df['value_1'], merged_df['value_2'])
            else:
                raise ValueError(f"Unsupported correlation method: {method}")

            logger.info(f"Calculated {method} correlation between metrics {self.metric_id} and {other_metric_id}")
            return {'correlation': corr, 'p_value': p_value}
        except Exception as e:
            logger.error(f"Error calculating {method} correlation between metrics {self.metric_id} and {other_metric_id}: {str(e)}")
            return {'correlation': None, 'p_value': None}

    def analyze_connections(self) -> None:
        try:
            connections = self.metric.connections_from.filter(project=self.project, tenant=self.tenant).select_related('to_metric')
            for conn in connections:
                pearson_result = self.calculate_correlation(conn.to_metric.id, 'pearson')
                spearman_result = self.calculate_correlation(conn.to_metric.id, 'spearman')
                
                # Update connection strength based on correlations
                pearson_corr = pearson_result.get('correlation', 0)
                spearman_corr = spearman_result.get('correlation', 0)
                conn.strength = (abs(pearson_corr) + abs(spearman_corr)) / 2
                conn.save()
            
            logger.info(f"Analyzed connections for metric {self.metric.id}")
        except Exception as e:
            logger.error(f"Error analyzing connections for metric {self.metric.id}: {str(e)}")

    def calculate_lagged_correlation(self, other_metric_id: int) -> List[Dict[str, float]]:
        try:
            Metric = apps.get_model('metrics', 'Metric')
            other_metric = Metric.objects.get(id=other_metric_id)
            data_prep = DataPreparation(other_metric_id, other_metric.tenant)
            df2, _ = data_prep.prepare_data()

            max_lag = self.dynamic_params.get('max_lag', 10)
            results = []
            for lag in range(-max_lag, max_lag + 1):
                if lag < 0:
                    corr, p_value = self.df['value'].corr(df2['value'].shift(-lag)), 0  # p-value calculation omitted for simplicity
                else:
                    corr, p_value = df2['value'].corr(self.df['value'].shift(-lag)), 0  # p-value calculation omitted for simplicity
                results.append({'lag': lag, 'correlation': corr, 'p_value': p_value})

            logger.info(f"Calculated lagged correlations between metrics {self.metric_id} and {other_metric_id}")
            return results
        except Exception as e:
            logger.error(f"Error calculating lagged correlations between metrics {self.metric_id} and {other_metric_id}: {str(e)}")
            return []

    def analyze_metric_network(self, correlation_threshold: float = 0.5) -> Dict[str, Any]:
        try:
            G = nx.Graph()
            
            # Add nodes
            G.add_node(self.metric_id, name=self.metadata['metric_name'])

            # Add edges based on correlations
            for other_metric_id in self.dynamic_params.get('related_metrics', []):
                corr_result = self.calculate_correlation(other_metric_id)
                if abs(corr_result['correlation']) >= correlation_threshold:
                    G.add_edge(self.metric_id, other_metric_id, weight=abs(corr_result['correlation']))

            # Calculate network metrics
            pagerank = nx.pagerank(G)
            communities = list(nx.community.greedy_modularity_communities(G))
            centrality = nx.degree_centrality(G)

            # Prepare results
            results = {
                'pagerank': pagerank,
                'communities': [list(c) for c in communities],
                'centrality': centrality,
                'num_nodes': G.number_of_nodes(),
                'num_edges': G.number_of_edges(),
                'average_clustering': nx.average_clustering(G),
                'graph_density': nx.density(G)
            }

            logger.info("Completed metric network analysis")
            return results
        except Exception as e:
            logger.error(f"Error in metric network analysis: {str(e)}")
            return {}

    def identify_key_influencers(self, top_n: int = 5) -> List[Tuple[int, float]]:
        try:
            network_analysis = self.analyze_metric_network()
            pagerank = network_analysis['pagerank']
            
            # Sort metrics by PageRank score
            sorted_influencers = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
            
            top_influencers = sorted_influencers[:top_n]
            
            logger.info(f"Identified top {top_n} influencing metrics")
            return top_influencers
        except Exception as e:
            logger.error(f"Error identifying key influencers: {str(e)}")
            return []

    def generate_relationship_summary(self) -> Dict[str, Any]:
        try:
            network_analysis = self.analyze_metric_network()
            top_influencers = self.identify_key_influencers()

            summary = {
                'network_stats': {
                    'num_metrics': network_analysis['num_nodes'],
                    'num_relationships': network_analysis['num_edges'],
                    'network_density': network_analysis['graph_density'],
                    'avg_clustering': network_analysis['average_clustering']
                },
                'top_influencers': [
                    {
                        'metric_id': metric_id,
                        'metric_name': self.metadata['metric_name'] if metric_id == self.metric_id else get_prepared_data(metric_id)[1]['metric_name'],
                        'influence_score': score
                    }
                    for metric_id, score in top_influencers
                ],
                'communities': [
                    [self.metadata['metric_name'] if metric_id == self.metric_id else get_prepared_data(metric_id)[1]['metric_name'] for metric_id in community]
                    for community in network_analysis['communities']
                ]
            }

            logger.info("Generated relationship summary")
            return summary
        except Exception as e:
            logger.error(f"Error generating relationship summary: {str(e)}")
            return {}