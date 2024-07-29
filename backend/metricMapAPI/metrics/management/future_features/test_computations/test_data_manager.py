import pytest
from metrics.computations.data_manager import DataManager
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'value': np.random.randint(1000, 10000, 366)
    })

def test_load_data(sample_data):
    manager = DataManager()
    loaded_data = manager.load_data(sample_data)
    assert isinstance(loaded_data, pd.DataFrame)
    assert 'date' in loaded_data.columns
    assert 'value' in loaded_data.columns

def test_clean_data(sample_data):
    manager = DataManager()
    cleaned_data = manager.clean_data(sample_data)
    assert cleaned_data.isnull().sum().sum() == 0

def test_transform_data(sample_data):
    manager = DataManager()
    transformed_data = manager.transform_data(sample_data, transformation='log')
    assert (transformed_data['value'] > 0).all()

def test_export_data(sample_data, tmp_path):
    manager = DataManager()
    file_path = tmp_path / "test_export.csv"
    manager.export_data(sample_data, str(file_path))
    assert file_path.exists()