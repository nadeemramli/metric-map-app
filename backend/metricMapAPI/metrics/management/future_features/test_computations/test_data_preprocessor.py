import pytest
from metrics.computations.data_preprocessor import DataPreprocessor
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'value': np.random.randint(1000, 10000, 366)
    })

def test_remove_outliers(sample_data):
    preprocessor = DataPreprocessor(sample_data)
    cleaned_data = preprocessor.remove_outliers(method='zscore')
    assert len(cleaned_data) <= len(sample_data)

def test_handle_missing_values(sample_data):
    sample_data.loc[10:20, 'value'] = np.nan
    preprocessor = DataPreprocessor(sample_data)
    filled_data = preprocessor.handle_missing_values(method='interpolate')
    assert filled_data.isnull().sum().sum() == 0

def test_normalize_data(sample_data):
    preprocessor = DataPreprocessor(sample_data)
    normalized_data = preprocessor.normalize_data(method='minmax')
    assert normalized_data['value'].min() >= 0
    assert normalized_data['value'].max() <= 1

def test_encode_categorical(sample_data):
    sample_data['category'] = np.random.choice(['A', 'B', 'C'], 366)
    preprocessor = DataPreprocessor(sample_data)
    encoded_data = preprocessor.encode_categorical(columns=['category'])
    assert 'category_A' in encoded_data.columns
    assert 'category_B' in encoded_data.columns
    assert 'category_C' in encoded_data.columns