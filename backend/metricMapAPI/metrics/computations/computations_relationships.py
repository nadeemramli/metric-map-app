# computations_relationships.py

import pandas as pd
import numpy as np
from scipy import stats
import networkx as nx
from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)

class RelationshipAnalyzer:
    def __init__(self, metrics_data: Dict[int, pd.DataFrame], metadata: Dict[int, dict]):
        """
        Initialize the RelationshipComputer.

        Args:
        metrics_data (Dict[int, pd.DataFrame]): A dictionary of DataFrames, keyed by metric_id
        metadata (Dict[int, dict]): A dictionary of metadata for each metric, keyed by metric_id
        """
        self.metrics_data = metrics_data
        self.metadata = metadata

    def calculate_correlation(self, metric_id1: int, metric_id2: int, correlation_type: str = 'pearson') -> Dict[str, float]:
        """
        Calculate correlation between two metrics.

        Args:
        metric_id1 (int): ID of the first metric
        metric_id2 (int): ID of the second metric
        correlation_type (str): Type of correlation to calculate ('pearson' or 'spearman')

        Returns:
        Dict[str, float]: Dictionary containing correlation and p-value
        """
        try:
            df1 = self.metrics_data[metric_id1]
            df2 = self.metrics_data[metric_id2]

            # Ensure the DataFrames have the same index
            common_index = df1.index.intersection(df2.index)
            df1 = df1.loc[common_index]
            df2 = df2.loc[common_index]

            if correlation_type == 'pearson':
                corr, p_value = stats.pearsonr(df1['value'], df2['value'])
            elif correlation_type == 'spearman':
                corr, p_value = stats.spearmanr(df1['value'], df2['value'])
            else:
                raise ValueError("Correlation type must be 'pearson' or 'spearman'")
            
            logger.info(f"Calculated {correlation_type} correlation between metrics {metric_id1} and {metric_id2}")
            return {'correlation': corr, 'p_value': p_value}
        except Exception as e:
            logger.error(f"Error calculating {correlation_type} correlation between metrics {metric_id1} and {metric_id2}: {str(e)}")
            return {}
 
    def analyze_connections(self) -> None:
            """Analyze connections between this metric and other metrics."""
            try:
                connections = Connection.objects.filter(from_metric=self.metric, project=self.project, tenant=self.tenant).select_related('to_metric') # type: ignore
                for conn in connections:
                    pearson_result = self.calculate_correlation(conn.to_metric, 'pearson')
                    spearman_result = self.calculate_correlation(conn.to_metric, 'spearman')
                    
                    # Update connection strength based on correlations
                    pearson_corr = pearson_result.get('correlation', 0)
                    spearman_corr = spearman_result.get('correlation', 0)
                    conn.strength = (abs(pearson_corr) + abs(spearman_corr)) / 2
                    conn.save()
                
                logger.info(f"Analyzed connections for metric {self.metric.id}")
            except Exception as e:
                logger.error(f"Error analyzing connections for metric {self.metric.id}: {str(e)}")

    def calculate_lagged_correlation(self, metric_id1: int, metric_id2: int, max_lag: int = 10) -> List[Dict[str, float]]:
        """
        Calculate lagged correlations between two metrics.

        Args:
        metric_id1 (int): ID of the first metric
        metric_id2 (int): ID of the second metric
        max_lag (int): Maximum lag to consider

        Returns:
        List[Dict[str, float]]: List of dictionaries containing lag, correlation, and p-value
        """
        try:
            df1 = self.metrics_data[metric_id1]
            df2 = self.metrics_data[metric_id2]

            results = []
            for lag in range(-max_lag, max_lag + 1):
                if lag < 0:
                    corr, p_value = df1['value'].corr(df2['value'].shift(-lag)), 0  # p-value calculation omitted for simplicity
                else:
                    corr, p_value = df1['value'].corr(df2['value'].shift(lag)), 0  # p-value calculation omitted for simplicity
                results.append({'lag': lag, 'correlation': corr, 'p_value': p_value})

            logger.info(f"Calculated lagged correlations between metrics {metric_id1} and {metric_id2}")
            return results
        except Exception as e:
            logger.error(f"Error calculating lagged correlations between metrics {metric_id1} and {metric_id2}: {str(e)}")
            return []

    def analyze_metric_network(self, correlation_threshold: float = 0.5) -> Dict[str, Any]:
        """
        Analyze the network of all metrics based on their correlations.

        Args:
        correlation_threshold (float): Minimum absolute correlation to consider a connection

        Returns:
        Dict[str, Any]: Dictionary containing network analysis results
        """
        try:
            G = nx.Graph()
            
            # Add nodes
            for metric_id in self.metrics_data.keys():
                G.add_node(metric_id, name=self.metadata[metric_id]['metric_name'])

            # Add edges based on correlations
            for metric_id1 in self.metrics_data.keys():
                for metric_id2 in self.metrics_data.keys():
                    if metric_id1 < metric_id2:  # Avoid duplicate calculations
                        corr_result = self.calculate_correlation(metric_id1, metric_id2)
                        if abs(corr_result['correlation']) >= correlation_threshold:
                            G.add_edge(metric_id1, metric_id2, weight=abs(corr_result['correlation']))

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
        """
        Identify the top N influencing metrics based on network analysis.

        Args:
        top_n (int): Number of top influencers to return

        Returns:
        List[Tuple[int, float]]: List of tuples containing metric ID and its influence score
        """
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
        """
        Generate a summary of all metric relationships.

        Returns:
        Dict[str, Any]: Dictionary containing relationship summary
        """
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
                        'metric_name': self.metadata[metric_id]['metric_name'],
                        'influence_score': score
                    }
                    for metric_id, score in top_influencers
                ],
                'communities': [
                    [self.metadata[metric_id]['metric_name'] for metric_id in community]
                    for community in network_analysis['communities']
                ]
            }

            logger.info("Generated relationship summary")
            return summary
        except Exception as e:
            logger.error(f"Error generating relationship summary: {str(e)}")
            return {}