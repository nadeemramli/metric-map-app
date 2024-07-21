"""
Clustering
==========

This module provides functions for clustering analysis.
"""

from sklearn.cluster import KMeans

def kmeans_clustering(data, n_clusters):
    """
    Perform KMeans clustering on the given data.

    Parameters:
    data (array-like): The input data for clustering.
    n_clusters (int): The number of clusters.

    Returns:
    array: The cluster labels for each data point.
    """
    model = KMeans(n_clusters=n_clusters)
    model.fit(data)
    return model.labels_
