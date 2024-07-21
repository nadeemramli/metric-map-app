import os
import sys

# Get the absolute path to the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the correct computations directory
computations_path = os.path.abspath(os.path.join(current_dir, '../metricMapAPI/metrics/computations'))

# Ensure the path to your backend/metricMapAPI/metrics/computations directory is correctly set
sys.path.insert(0, computations_path)

print("Current Python Path:", sys.path)  # Debugging statement

# Print the contents of the computations directory
print("Contents of computations:", os.listdir(computations_path))

# Print the contents of the forecasting directory within computations
print("Contents of forecasting:", os.listdir(os.path.join(computations_path, 'forecasting_utils')))

try:
    import forecasting_utils.classification_models
    import forecasting_utils.ensemble_models
    import forecasting_utils.forecasting
    import forecasting_utils.regression_models
    import forecasting_utils.survival_analysis
    import forecasting_utils.time_series_models
    import impact_utils.anomaly_detection
    import impact_utils.change_detection
    import impact_utils.experimentation
    import impact_utils.impact_analysis
    import impact_utils.predictive_maintenance
    import impact_utils.technical_indicators
    import impact_utils.trend_analysis
    import relationships_utils.causal_inference
    import relationships_utils.clustering
    import relationships_utils.correlation_analysis
    import relationships_utils.network_analysis
    import relationships_utils.recommender_systems
    import statistics_utils.basic_stats
    import statistics_utils.advanced_stats
    import statistics_utils.variance_analysis
    import statistics_utils.time_series_stats
    import utils.data_preprocessing
    print("All imports successful")
except ImportError as e:
    print(f"ImportError: {e}")
