import pytest
import numpy as np
from metrics.computations.relationships_utils.clustering import kmeans_clustering

def test_kmeans_clustering():
    data = np.random.rand(100, 2)
    n_clusters = 3
    labels = kmeans_clustering(data, n_clusters)
    assert len(labels) == len(data)
    assert len(set(labels)) == n_clusters
    assert all(isinstance(label, (int, np.integer)) for label in labels)