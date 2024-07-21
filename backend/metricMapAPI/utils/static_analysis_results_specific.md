# Static Analysis Results
## pylint
```
************* Module relationships.network_analysis
metrics/computations/relationships/network_analysis.py:24:49: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/relationships/network_analysis.py:25:47: C0303: Trailing whitespace (trailing-whitespace)
************* Module utils.data_preprocessing
metrics/computations/utils/data_preprocessing.py:28:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/utils/data_preprocessing.py:6:0: E0611: No name 'mean' in module 'statistics' (no-name-in-module)
metrics/computations/utils/data_preprocessing.py:6:0: E0611: No name 'stdev' in module 'statistics' (no-name-in-module)
metrics/computations/utils/data_preprocessing.py:26:8: C0103: Variable name "iqrResultMethod" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/utils/data_preprocessing.py:32:8: C0103: Variable name "zResultMethod" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/utils/data_preprocessing.py:10:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module utils.utils
metrics/computations/utils/utils.py:32:0: C0305: Trailing newlines (trailing-newlines)
metrics/computations/utils/utils.py:5:0: E0611: No name 'mean' in module 'statistics' (no-name-in-module)
************* Module impact.trend_analysis
metrics/computations/impact/trend_analysis.py:5:0: W0611: Unused numpy imported as np (unused-import)
metrics/computations/impact/trend_analysis.py:6:0: W0611: Unused pandas imported as pd (unused-import)
************* Module impact.technical_indicators
metrics/computations/impact/technical_indicators.py:3:0: C0301: Line too long (136/100) (line-too-long)
************* Module impact.impact_analysis
metrics/computations/impact/impact_analysis.py:2:0: C0301: Line too long (134/100) (line-too-long)
metrics/computations/impact/impact_analysis.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/impact_analysis.py:27:64: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/impact_analysis.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/impact_analysis.py:51:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/impact_analysis.py:8:30: W0621: Redefining name 'before_treatment' from outer scope (line 59) (redefined-outer-name)
metrics/computations/impact/impact_analysis.py:8:48: W0621: Redefining name 'after_treatment' from outer scope (line 60) (redefined-outer-name)
metrics/computations/impact/impact_analysis.py:8:65: W0621: Redefining name 'before_control' from outer scope (line 61) (redefined-outer-name)
metrics/computations/impact/impact_analysis.py:8:81: W0621: Redefining name 'after_control' from outer scope (line 62) (redefined-outer-name)
metrics/computations/impact/impact_analysis.py:26:4: W0621: Redefining name 'treatment_effect' from outer scope (line 64) (redefined-outer-name)
metrics/computations/impact/impact_analysis.py:32:27: W0621: Redefining name 'y' from outer scope (line 70) (redefined-outer-name)
metrics/computations/impact/impact_analysis.py:32:30: W0621: Redefining name 'x' from outer scope (line 71) (redefined-outer-name)
metrics/computations/impact/impact_analysis.py:32:33: W0621: Redefining name 'z' from outer scope (line 72) (redefined-outer-name)
************* Module impact.change_detection
metrics/computations/impact/change_detection.py:2:0: C0301: Line too long (109/100) (line-too-long)
************* Module impact.experimentation
metrics/computations/impact/experimentation.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/experimentation.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/experimentation.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/experimentation.py:48:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/experimentation.py:51:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/experimentation.py:1:0: C0114: Missing module docstring (missing-module-docstring)
metrics/computations/impact/experimentation.py:18:4: C0103: Variable name "X_train" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/impact/experimentation.py:18:13: C0103: Variable name "X_test" doesn't conform to snake_case naming style (invalid-name)
************* Module impact.predictive_maintenance
metrics/computations/impact/predictive_maintenance.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/predictive_maintenance.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/predictive_maintenance.py:30:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/impact/predictive_maintenance.py:47:0: C0304: Final newline missing (missing-final-newline)
metrics/computations/impact/predictive_maintenance.py:23:4: C0103: Variable name "X" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/impact/predictive_maintenance.py:26:4: C0103: Variable name "X_train" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/impact/predictive_maintenance.py:26:13: C0103: Variable name "X_test" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/impact/predictive_maintenance.py:26:13: W0612: Unused variable 'X_test' (unused-variable)
metrics/computations/impact/predictive_maintenance.py:26:30: W0612: Unused variable 'y_test' (unused-variable)
metrics/computations/impact/predictive_maintenance.py:8:0: W0611: Unused numpy imported as np (unused-import)
************* Module forecasting.forecasting
metrics/computations/forecasting/forecasting.py:21:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/forecasting/forecasting.py:6:0: E0401: Unable to import 'fbprophet' (import-error)
metrics/computations/forecasting/forecasting.py:5:0: W0611: Unused pandas imported as pd (unused-import)
************* Module forecasting.classification_models
metrics/computations/forecasting/classification_models.py:8:21: C0103: Argument name "X_train" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/classification_models.py:23:31: C0103: Argument name "X_test" doesn't conform to snake_case naming style (invalid-name)
************* Module forecasting.survival_analysis
metrics/computations/forecasting/survival_analysis.py:5:0: E0401: Unable to import 'lifelines' (import-error)
metrics/computations/forecasting/survival_analysis.py:24:0: R1711: Useless return at end of function or method (useless-return)
metrics/computations/forecasting/survival_analysis.py:6:0: W0611: Unused pandas imported as pd (unused-import)
************* Module forecasting.ensemble_models
metrics/computations/forecasting/ensemble_models.py:19:4: C0103: Variable name "X" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/ensemble_models.py:27:35: C0103: Argument name "X_test" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/ensemble_models.py:5:0: W0611: Unused RandomForestRegressor imported from sklearn.ensemble (unused-import)
************* Module forecasting.regression_models
metrics/computations/forecasting/regression_models.py:24:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/forecasting/regression_models.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/forecasting/regression_models.py:29:0: C0303: Trailing whitespace (trailing-whitespace)
metrics/computations/forecasting/regression_models.py:22:4: C0103: Variable name "X" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/regression_models.py:25:4: C0103: Variable name "X_train" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/regression_models.py:25:13: C0103: Variable name "X_test" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/regression_models.py:25:13: W0612: Unused variable 'X_test' (unused-variable)
metrics/computations/forecasting/regression_models.py:25:30: W0612: Unused variable 'y_test' (unused-variable)
metrics/computations/forecasting/regression_models.py:32:37: C0103: Argument name "X_test" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/regression_models.py:5:0: W0611: Unused numpy imported as np (unused-import)
metrics/computations/forecasting/regression_models.py:6:0: W0611: Unused pandas imported as pd (unused-import)
************* Module forecasting.time_series_models
metrics/computations/forecasting/time_series_models.py:6:0: E0401: Unable to import 'tensorflow' (import-error)
metrics/computations/forecasting/time_series_models.py:7:0: E0401: Unable to import 'tensorflow.keras.models' (import-error)
metrics/computations/forecasting/time_series_models.py:8:0: E0401: Unable to import 'tensorflow.keras.layers' (import-error)
metrics/computations/forecasting/time_series_models.py:56:4: C0103: Variable name "X" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/time_series_models.py:60:4: C0103: Variable name "X" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/time_series_models.py:60:11: E0602: Undefined variable 'np' (undefined-variable)
metrics/computations/forecasting/time_series_models.py:60:24: E0602: Undefined variable 'np' (undefined-variable)
metrics/computations/forecasting/time_series_models.py:61:4: C0103: Variable name "X" doesn't conform to snake_case naming style (invalid-name)
metrics/computations/forecasting/time_series_models.py:61:8: E0602: Undefined variable 'np' (undefined-variable)
metrics/computations/forecasting/time_series_models.py:5:0: W0611: Unused pandas imported as pd (unused-import)
metrics/computations/forecasting/time_series_models.py:6:0: W0611: Unused tensorflow imported as tf (unused-import)

------------------------------------------------------------------
Your code has been rated at 5.95/10 (previous run: 5.82/10, +0.13)


```
## flake8
```
metrics/computations/forecasting/classification_models.py:2:80: E501 line too long (81 > 79 characters)
metrics/computations/forecasting/classification_models.py:8:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/classification_models.py:23:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/ensemble_models.py:5:1: F401 'sklearn.ensemble.RandomForestRegressor' imported but unused
metrics/computations/forecasting/ensemble_models.py:8:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/ensemble_models.py:27:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/forecasting.py:5:1: F401 'pandas as pd' imported but unused
metrics/computations/forecasting/forecasting.py:8:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/forecasting.py:21:1: W293 blank line contains whitespace
metrics/computations/forecasting/forecasting.py:26:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/regression_models.py:5:1: F401 'numpy as np' imported but unused
metrics/computations/forecasting/regression_models.py:6:1: F401 'pandas as pd' imported but unused
metrics/computations/forecasting/regression_models.py:11:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/regression_models.py:24:1: W293 blank line contains whitespace
metrics/computations/forecasting/regression_models.py:26:1: W293 blank line contains whitespace
metrics/computations/forecasting/regression_models.py:29:1: W293 blank line contains whitespace
metrics/computations/forecasting/regression_models.py:32:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/survival_analysis.py:6:1: F401 'pandas as pd' imported but unused
metrics/computations/forecasting/survival_analysis.py:8:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/survival_analysis.py:24:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/time_series_models.py:5:1: F401 'pandas as pd' imported but unused
metrics/computations/forecasting/time_series_models.py:6:1: F401 'tensorflow as tf' imported but unused
metrics/computations/forecasting/time_series_models.py:12:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/time_series_models.py:27:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/time_series_models.py:44:1: E302 expected 2 blank lines, found 1
metrics/computations/forecasting/time_series_models.py:60:12: F821 undefined name 'np'
metrics/computations/forecasting/time_series_models.py:60:25: F821 undefined name 'np'
metrics/computations/forecasting/time_series_models.py:61:9: F821 undefined name 'np'
metrics/computations/impact/anomaly_detection.py:11:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/change_detection.py:2:80: E501 line too long (109 > 79 characters)
metrics/computations/impact/change_detection.py:7:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/change_detection.py:23:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/experimentation.py:5:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/experimentation.py:18:80: E501 line too long (100 > 79 characters)
metrics/computations/impact/experimentation.py:20:1: W293 blank line contains whitespace
metrics/computations/impact/experimentation.py:25:1: W293 blank line contains whitespace
metrics/computations/impact/experimentation.py:31:1: W293 blank line contains whitespace
metrics/computations/impact/experimentation.py:34:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/experimentation.py:48:1: W293 blank line contains whitespace
metrics/computations/impact/experimentation.py:51:1: W293 blank line contains whitespace
metrics/computations/impact/impact_analysis.py:2:80: E501 line too long (134 > 79 characters)
metrics/computations/impact/impact_analysis.py:8:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/impact_analysis.py:8:80: E501 line too long (96 > 79 characters)
metrics/computations/impact/impact_analysis.py:13:80: E501 line too long (95 > 79 characters)
metrics/computations/impact/impact_analysis.py:14:80: E501 line too long (93 > 79 characters)
metrics/computations/impact/impact_analysis.py:15:80: E501 line too long (91 > 79 characters)
metrics/computations/impact/impact_analysis.py:16:80: E501 line too long (89 > 79 characters)
metrics/computations/impact/impact_analysis.py:25:1: W293 blank line contains whitespace
metrics/computations/impact/impact_analysis.py:27:65: W291 trailing whitespace
metrics/computations/impact/impact_analysis.py:32:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/impact_analysis.py:47:1: W293 blank line contains whitespace
metrics/computations/impact/impact_analysis.py:51:1: W293 blank line contains whitespace
metrics/computations/impact/impact_analysis.py:59:1: E305 expected 2 blank lines after class or function definition, found 1
metrics/computations/impact/predictive_maintenance.py:8:1: F401 'numpy as np' imported but unused
metrics/computations/impact/predictive_maintenance.py:12:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/predictive_maintenance.py:25:1: W293 blank line contains whitespace
metrics/computations/impact/predictive_maintenance.py:27:1: W293 blank line contains whitespace
metrics/computations/impact/predictive_maintenance.py:30:1: W293 blank line contains whitespace
metrics/computations/impact/predictive_maintenance.py:33:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/predictive_maintenance.py:47:49: W292 no newline at end of file
metrics/computations/impact/technical_indicators.py:3:80: E501 line too long (136 > 79 characters)
metrics/computations/impact/technical_indicators.py:6:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/technical_indicators.py:24:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/trend_analysis.py:5:1: F401 'numpy as np' imported but unused
metrics/computations/impact/trend_analysis.py:6:1: F401 'pandas as pd' imported but unused
metrics/computations/impact/trend_analysis.py:9:1: E302 expected 2 blank lines, found 1
metrics/computations/impact/trend_analysis.py:22:1: E302 expected 2 blank lines, found 1
metrics/computations/relationships/causal_inference.py:5:46: W291 trailing whitespace
metrics/computations/relationships/causal_inference.py:12:1: E302 expected 2 blank lines, found 1
metrics/computations/relationships/causal_inference.py:14:80: E501 line too long (87 > 79 characters)
metrics/computations/relationships/causal_inference.py:22:80: E501 line too long (91 > 79 characters)
metrics/computations/relationships/clustering.py:10:1: E302 expected 2 blank lines, found 1
metrics/computations/relationships/correlation_analysis.py:8:1: E302 expected 2 blank lines, found 1
metrics/computations/relationships/correlation_analysis.py:26:80: E501 line too long (84 > 79 characters)
metrics/computations/relationships/correlation_analysis.py:29:1: E302 expected 2 blank lines, found 1
metrics/computations/relationships/network_analysis.py:2:60: W291 trailing whitespace
metrics/computations/relationships/network_analysis.py:3:60: W291 trailing whitespace
metrics/computations/relationships/network_analysis.py:9:1: E302 expected 2 blank lines, found 1
metrics/computations/relationships/network_analysis.py:24:50: W291 trailing whitespace
metrics/computations/relationships/network_analysis.py:25:48: W291 trailing whitespace
metrics/computations/relationships/network_analysis.py:29:1: E302 expected 2 blank lines, found 1
metrics/computations/relationships/recommender_systems.py:10:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/advanced_stats.py:25:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/advanced_stats.py:37:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/advanced_stats.py:43:80: E501 line too long (84 > 79 characters)
metrics/computations/statistics/basic_stats.py:8:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/basic_stats.py:20:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/basic_stats.py:36:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/basic_stats.py:50:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/basic_stats.py:62:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/time_series_stats.py:10:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/time_series_stats.py:23:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/time_series_stats.py:36:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/time_series_stats.py:42:80: E501 line too long (89 > 79 characters)
metrics/computations/statistics/time_series_stats.py:48:80: E501 line too long (84 > 79 characters)
metrics/computations/statistics/variance_analysis.py:2:78: W291 trailing whitespace
metrics/computations/statistics/variance_analysis.py:3:80: E501 line too long (95 > 79 characters)
metrics/computations/statistics/variance_analysis.py:9:1: E302 expected 2 blank lines, found 1
metrics/computations/statistics/variance_analysis.py:22:1: E302 expected 2 blank lines, found 1
metrics/computations/utils/data_preprocessing.py:2:40: W291 trailing whitespace
metrics/computations/utils/data_preprocessing.py:3:33: W291 trailing whitespace
metrics/computations/utils/data_preprocessing.py:10:1: E302 expected 2 blank lines, found 1
metrics/computations/utils/data_preprocessing.py:26:80: E501 line too long (81 > 79 characters)
metrics/computations/utils/data_preprocessing.py:28:1: W293 blank line contains whitespace
metrics/computations/utils/data_preprocessing.py:35:1: E302 expected 2 blank lines, found 1
metrics/computations/utils/data_preprocessing.py:47:1: E302 expected 2 blank lines, found 1
metrics/computations/utils/utils.py:2:80: E501 line too long (88 > 79 characters)
metrics/computations/utils/utils.py:7:1: E302 expected 2 blank lines, found 1
metrics/computations/utils/utils.py:15:80: E501 line too long (84 > 79 characters)
metrics/computations/utils/utils.py:19:1: E302 expected 2 blank lines, found 1
metrics/computations/utils/utils.py:32:1: W391 blank line at end of file

```
## mypy
```
metrics/computations/relationships/recommender_systems.py:8: error: Skipping analyzing "sklearn.neighbors": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/relationships/network_analysis.py:7: error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/relationships/clustering.py:8: error: Skipping analyzing "sklearn.cluster": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/relationships/causal_inference.py:9: error: Skipping analyzing "statsmodels.tsa.stattools": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/relationships/causal_inference.py:10: error: Library stubs not installed for "pandas"  [import-untyped]
metrics/computations/impact/experimentation.py:1: error: Library stubs not installed for "pandas"  [import-untyped]
metrics/computations/impact/experimentation.py:2: error: Skipping analyzing "sklearn.model_selection": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/impact/experimentation.py:3: error: Skipping analyzing "sklearn.metrics": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/time_series_models.py:5: error: Library stubs not installed for "pandas"  [import-untyped]
metrics/computations/forecasting/time_series_models.py:6: error: Cannot find implementation or library stub for module named "tensorflow"  [import-not-found]
metrics/computations/forecasting/time_series_models.py:7: error: Cannot find implementation or library stub for module named "tensorflow.keras.models"  [import-not-found]
metrics/computations/forecasting/time_series_models.py:8: error: Cannot find implementation or library stub for module named "tensorflow.keras.layers"  [import-not-found]
metrics/computations/forecasting/time_series_models.py:9: error: Skipping analyzing "statsmodels.tsa.seasonal": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/time_series_models.py:10: error: Skipping analyzing "statsmodels.tsa.statespace.sarimax": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/survival_analysis.py:5: error: Cannot find implementation or library stub for module named "lifelines"  [import-not-found]
metrics/computations/forecasting/survival_analysis.py:6: error: Library stubs not installed for "pandas"  [import-untyped]
metrics/computations/forecasting/forecasting.py:5: error: Library stubs not installed for "pandas"  [import-untyped]
metrics/computations/forecasting/forecasting.py:5: note: Hint: "python3 -m pip install pandas-stubs"
metrics/computations/forecasting/forecasting.py:5: note: (or run "mypy --install-types" to install all missing stub packages)
metrics/computations/forecasting/forecasting.py:6: error: Cannot find implementation or library stub for module named "fbprophet"  [import-not-found]
metrics/computations/forecasting/ensemble_models.py:5: error: Skipping analyzing "sklearn.ensemble": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/ensemble_models.py:6: error: Skipping analyzing "sklearn.metrics": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/classification_models.py:5: error: Skipping analyzing "sklearn.ensemble": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/classification_models.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
metrics/computations/forecasting/classification_models.py:6: error: Skipping analyzing "sklearn.metrics": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/statistics/variance_analysis.py:7: error: Skipping analyzing "scipy": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/statistics/advanced_stats.py:9: error: Skipping analyzing "scipy.stats": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/impact/trend_analysis.py:6: error: Library stubs not installed for "pandas"  [import-untyped]
metrics/computations/impact/trend_analysis.py:7: error: Skipping analyzing "statsmodels.tsa.seasonal": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/impact/predictive_maintenance.py:9: error: Skipping analyzing "sklearn.ensemble": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/impact/predictive_maintenance.py:10: error: Skipping analyzing "sklearn.model_selection": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/impact/impact_analysis.py:6: error: Skipping analyzing "statsmodels.api": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/impact/impact_analysis.py:6: error: Skipping analyzing "statsmodels": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/impact/anomaly_detection.py:9: error: Skipping analyzing "sklearn.ensemble": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/regression_models.py:6: error: Library stubs not installed for "pandas"  [import-untyped]
metrics/computations/forecasting/regression_models.py:7: error: Skipping analyzing "sklearn.model_selection": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/regression_models.py:8: error: Skipping analyzing "sklearn.linear_model": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/forecasting/regression_models.py:9: error: Skipping analyzing "sklearn.metrics": module is installed, but missing library stubs or py.typed marker  [import-untyped]
metrics/computations/utils/data_preprocessing.py:8: error: Skipping analyzing "scipy": module is installed, but missing library stubs or py.typed marker  [import-untyped]
Found 36 errors in 18 files (checked 29 source files)

```
## bandit
```
Run started:2024-07-12 11:42:36.997914

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 814
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.10.7

```
## black
```
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/classification_models.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/anomaly_detection.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/survival_analysis.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/change_detection.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/causal_inference.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/forecasting.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/clustering.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/predictive_maintenance.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/regression_models.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/ensemble_models.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/trend_analysis.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/recommender_systems.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/statistics/advanced_stats.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/experimentation.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/technical_indicators.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/utils/utils.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/network_analysis.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/statistics/time_series_stats.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/statistics/basic_stats.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/correlation_analysis.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/statistics/variance_analysis.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/impact_analysis.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/time_series_models.py
would reformat /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/utils/data_preprocessing.py

Oh no! 💥 💔 💥
24 files would be reformatted, 5 files would be left unchanged.

```
## isort
```
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/statistics/time_series_stats.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/statistics/advanced_stats.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/statistics/variance_analysis.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/recommender_systems.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/clustering.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/network_analysis.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/relationships/causal_inference.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/utils/data_preprocessing.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/utils/utils.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/trend_analysis.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/impact_analysis.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/change_detection.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/experimentation.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/anomaly_detection.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/impact/predictive_maintenance.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/forecasting.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/classification_models.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/survival_analysis.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/ensemble_models.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/regression_models.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/forecasting/time_series_models.py Imports are incorrectly sorted and/or formatted.

```
