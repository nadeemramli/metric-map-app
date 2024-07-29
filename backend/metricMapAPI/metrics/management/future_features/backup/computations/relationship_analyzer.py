# relationship_analyzer.py

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.cluster import KMeans
import networkx as nx
from typing import List, Dict, Union, Any
import json

class RelationshipData:
    def __init__(self, relationship_id: int, data: pd.DataFrame):
        self.relationship_id = relationship_id
        self.data = data

class RelationshipResult:
    def __init__(self, relationship_id: int, analysis_type: str, result: Dict[str, Any]):
        self.relationship_id = relationship_id
        self.analysis_type = analysis_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'relationship_id': self.relationship_id,
            'analysis_type': self.analysis_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class RelationshipAnalyzer:
    def __init__(self, data: RelationshipData):
        self.data = data

    def lagged_correlation_test(self, x: str, y: str, max_lag: int = 10) -> RelationshipResult:
        results = {}
        x_series = self.data.data[x]
        y_series = self.data.data[y]
        for lag in range(1, max_lag + 1):
            correlation = x_series.corr(y_series.shift(-lag))
            p_value = self.pearsonr(x_series[:-lag], y_series[lag:])[1]
            results[lag] = {'correlation': correlation, 'p_value': p_value}
        return RelationshipResult(
            self.data.relationship_id,
            'lagged_correlation',
            {'results': results}
        )

    def pearsonr(self, x: np.ndarray, y: np.ndarray) -> tuple:
        n = len(x)
        r = np.corrcoef(x, y)[0,1]
        t = r * np.sqrt(n - 2) / np.sqrt(1 - r**2)
        p = 2 * (1 - stats.t.cdf(abs(t), n - 2))
        return r, p

    def kmeans_clustering(self, features: List[str], n_clusters: int) -> RelationshipResult:
        data = self.data.data[features]
        model = KMeans(n_clusters=n_clusters)
        labels = model.fit_predict(data)
        return RelationshipResult(
            self.data.relationship_id,
            'kmeans_clustering',
            {
                'labels': labels.tolist(),
                'cluster_centers': model.cluster_centers_.tolist(),
                'features': features
            }
        )

    def pearson_correlation(self, x: str, y: str) -> RelationshipResult:
        x_data = self.data.data[x]
        y_data = self.data.data[y]
        correlation = x_data.corr(y_data, method='pearson')
        return RelationshipResult(
            self.data.relationship_id,
            'pearson_correlation',
            {'correlation': correlation}
        )

    def spearman_correlation(self, x: str, y: str) -> RelationshipResult:
        x_data = self.data.data[x]
        y_data = self.data.data[y]
        correlation = x_data.corr(y_data, method='spearman')
        return RelationshipResult(
            self.data.relationship_id,
            'spearman_correlation',
            {'correlation': correlation}
        )

    def build_metric_network(self, metrics: List[str], connections: List[Dict]) -> RelationshipResult:
        graph = nx.Graph()
        for metric in metrics:
            graph.add_node(metric)
        for connection in connections:
            graph.add_edge(connection['from_metric'], 
                           connection['to_metric'], 
                           weight=connection['weight'])
        return RelationshipResult(
            self.data.relationship_id,
            'metric_network',
            {'network': nx.node_link_data(graph)}
        )

    def centrality_measures(self, network: Dict) -> RelationshipResult:
        graph = nx.node_link_graph(network)
        centrality = {
            'degree_centrality': nx.degree_centrality(graph),
            'betweenness_centrality': nx.betweenness_centrality(graph),
            'eigenvector_centrality': nx.eigenvector_centrality(graph)
        }
        return RelationshipResult(
            self.data.relationship_id,
            'centrality_measures',
            {'centrality': centrality}
        )

    @classmethod
    def run_analysis(cls, relationship_id: int, analysis_type: str, **kwargs) -> RelationshipResult:
        data = cls.get_relationship_data(relationship_id)
        analyzer = cls(data)
        
        if analysis_type == 'lagged_correlation':
            return analyzer.lagged_correlation_test(kwargs['x'], kwargs['y'], kwargs.get('max_lag', 10))
        elif analysis_type == 'kmeans_clustering':
            return analyzer.kmeans_clustering(kwargs['features'], kwargs['n_clusters'])
        elif analysis_type == 'pearson_correlation':
            return analyzer.pearson_correlation(kwargs['x'], kwargs['y'])
        elif analysis_type == 'spearman_correlation':
            return analyzer.spearman_correlation(kwargs['x'], kwargs['y'])
        elif analysis_type == 'metric_network':
            return analyzer.build_metric_network(kwargs['metrics'], kwargs['connections'])
        elif analysis_type == 'centrality_measures':
            return analyzer.centrality_measures(kwargs['network'])
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")

    @staticmethod
    def get_relationship_data(relationship_id: int) -> RelationshipData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy RelationshipData object
        dummy_data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=100),
            'metric1': np.random.rand(100),
            'metric2': np.random.rand(100),
            'metric3': np.random.rand(100)
        })
        return RelationshipData(relationship_id, dummy_data)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)