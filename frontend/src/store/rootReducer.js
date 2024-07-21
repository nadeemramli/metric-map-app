import { combineReducers } from '@reduxjs/toolkit';
import projectsReducer from './slices/projectsSlice';
import metricsReducer from './slices/metricsSlice';
import connectionsReducer from './slices/connectionsSlice';
import dashboardsReducer from './slices/dashboardsSlice';
import reportsReducer from './slices/reportsSlice';
import categoriesReducer from './slices/categoriesSlice';
import tagsReducer from './slices/tagsSlice';
import analysisReducer from './slices/analysisSlice';
import targetsReducer from './slices/targetsSlice';
import actionRemarksReducer from './slices/actionRemarksSlice';
import advancedFeaturesReducer from './slices/advancedFeaturesSlice';
import userReducer from './slices/userSlice';
import clientsReducer from './slices/clientsSlice';
import forecastsReducer from './slices/forecastsSlice';
import anomaliesReducer from './slices/anomaliesSlice';
import trendsReducer from './slices/trendsSlice';

const rootReducer = combineReducers({
  projects: projectsReducer,
  metrics: metricsReducer,
  connections: connectionsReducer,
  dashboards: dashboardsReducer,
  reports: reportsReducer,
  categories: categoriesReducer,
  tags: tagsReducer,
  analysis: analysisReducer,
  targets: targetsReducer,
  actionRemarks: actionRemarksReducer,
  advancedFeatures: advancedFeaturesReducer,
  user: userReducer,
  clients: clientsReducer,
  forecasts: forecastsReducer,
  anomalies: anomaliesReducer,
  trends: trendsReducer,
});

export default rootReducer;