"""
This module provides tools for performing network analysis. 
It includes functions to create and analyze network graphs, 
calculate network metrics, and visualize connections.
"""

import networkx as nx

def build_metric_network(metrics, connections):
    """
    Build a network of metrics.

    Parameters:
        metrics: List of metrics.
        connections: List of connections between metrics.

    Returns:
        G: NetworkX graph representing the metric network.
    """
    graph = nx.Graph()
    for metric in metrics:
        graph.add_node(metric)
    for connection in connections:
        graph.add_edge(connection['from_metric'], 
                       connection['to_metric'], 
                       weight=connection['weight'])
    return graph

def centrality_measures(network):
    """
    Calculate centrality measures for the network.

    Parameters:
        network: NetworkX graph representing the metric network.

    Returns:
        centrality: Dictionary of centrality measures.
    """
    centrality = {
        'degree_centrality': nx.degree_centrality(network),
        'betweenness_centrality': nx.betweenness_centrality(network),
        'eigenvector_centrality': nx.eigenvector_centrality(network)
    }
    return centrality
