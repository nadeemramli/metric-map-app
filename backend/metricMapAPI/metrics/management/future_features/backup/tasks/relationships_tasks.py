from metricMapAPI.celery_app.celery import app
from metrics.computations import (
    lagged_correlation_test, pearsonr, kmeans_clustering,
    pearson_correlation, spearman_correlation, build_metric_network,
    centrality_measures, recommend_items
)

@app.task
def granger_causality_test_task(x, y, max_lag=12):
    return granger_causality_test(x, y, max_lag)

@app.task
def kmeans_clustering_task(data, n_clusters):
    return kmeans_clustering(data, n_clusters)

@app.task
def lagged_correlation_test_task(x, y, max_lag):
    return lagged_correlation_test(x, y, max_lag)

@app.task
def pearsonr_task(x, y):
    return pearsonr(x, y)

@app.task
def pearson_correlation_task(data):
    return pearson_correlation(data)

@app.task
def spearman_correlation_task(data):
    return spearman_correlation(data)

@app.task
def build_metric_network_task(metrics_data):
    return build_metric_network(metrics_data)

@app.task
def centrality_measures_task(network):
    return centrality_measures(network)

@app.task
def recommend_items_task(user_item_matrix, user_id):
    return recommend_items(user_item_matrix, user_id)