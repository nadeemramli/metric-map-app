# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
# Get the absolute path to the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the correct computations directory
computations_path = os.path.abspath(os.path.join(current_dir, '../../metrics/computations'))

# Ensure the path to your backend/metricMapAPI/metrics/computations directory is correctly set
sys.path.insert(0, computations_path)

print("Current Python Path:", sys.path)  # Debugging statement

# Print the contents of the computations directory
print("Contents of computations:", os.listdir(computations_path))

# Print the contents of the forecasting directory within computations
print("Contents of forecasting:", os.listdir(os.path.join(computations_path, 'forecasting_utils')))
  # Adjust the path to your src directory

project = 'metricMapAPI'
copyright = '2024, Nadeem'
author = 'Nadeem'
release = '12 June 2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
