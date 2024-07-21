import pytest
import numpy as np
from metrics.computations.relationships_utils.recommender_systems import recommend_items

def test_recommend_items():
    # Create a sample dataset
    data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15]
    ])
    
    item_id = 2
    n_recommendations = 3
    
    indices, distances = recommend_items(data, item_id, n_recommendations)
    
    assert len(indices) == n_recommendations
    assert len(distances) == n_recommendations
    assert item_id not in indices[:n_recommendations]
    assert all(0 <= idx < len(data) for idx in indices)
    assert all(dist >= 0 for dist in distances)