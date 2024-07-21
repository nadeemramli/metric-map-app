import pytest
import networkx as nx
from metrics.computations.relationships_utils.network_analysis import build_metric_network, centrality_measures

@pytest.fixture
def sample_network():
    metrics = ['A', 'B', 'C', 'D']
    connections = [
        {'from_metric': 'A', 'to_metric': 'B', 'weight': 1},
        {'from_metric': 'B', 'to_metric': 'C', 'weight': 2},
        {'from_metric': 'C', 'to_metric': 'D', 'weight': 3},
        {'from_metric': 'D', 'to_metric': 'A', 'weight': 4}
    ]
    return metrics, connections

def test_build_metric_network(sample_network):
    metrics, connections = sample_network
    G = build_metric_network(metrics, connections)
    
    assert isinstance(G, nx.Graph)
    assert len(G.nodes) == len(metrics)
    assert len(G.edges) == len(connections)
    assert all(G.has_edge(conn['from_metric'], conn['to_metric']) for conn in connections)

def test_centrality_measures(sample_network):
    metrics, connections = sample_network
    G = build_metric_network(metrics, connections)
    centrality = centrality_measures(G)
    
    assert isinstance(centrality, dict)
    assert 'degree_centrality' in centrality
    assert 'betweenness_centrality' in centrality
    assert 'eigenvector_centrality' in centrality
    assert all(len(measure) == len(metrics) for measure in centrality.values())