"""
Recommender Systems
===================

This module provides functions for building and evaluating recommender systems.
"""

from sklearn.neighbors import NearestNeighbors

def recommend_items(data, item_id, n_recommendations):
    """
    Recommend items similar to the given item based on nearest neighbors.

    Parameters:
    data (array-like): The input data for recommendation.
    item_id (int): The ID of the item to base the recommendations on.
    n_recommendations (int): The number of recommendations to generate.

    Returns:
    array: The IDs of the recommended items.
    """
    model = NearestNeighbors(n_neighbors=n_recommendations)
    model.fit(data)
    
    distances, indices = model.kneighbors(data[item_id].reshape(1, -1), n_neighbors=n_recommendations+1)
    
    print("Distances of recommendations:", distances[0])
    return indices[0][1:], distances[0][1:]  # Exclude the first item (input item)