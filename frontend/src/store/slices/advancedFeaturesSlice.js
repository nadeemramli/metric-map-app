import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const runABTest = createAsyncThunk('advancedFeatures/runABTest', 
  async ({ clientId, projectId, testConfig }) => await api.runABTest(clientId, projectId, testConfig)
);
export const detectAnomalies = createAsyncThunk('advancedFeatures/detectAnomalies', 
  async ({ clientId, projectId, metricId }) => await api.detectAnomalies(clientId, projectId, metricId)
);
export const predictiveGoalSetting = createAsyncThunk('advancedFeatures/predictiveGoalSetting', 
  async ({ clientId, projectId, metricId }) => await api.predictiveGoalSetting(clientId, projectId, metricId)
);
export const performScenarioModeling = createAsyncThunk('advancedFeatures/performScenarioModeling', 
  async ({ clientId, projectId, scenarioData }) => await api.performScenarioModeling(clientId, projectId, scenarioData)
);

const advancedFeaturesSlice = createSlice({
  name: 'advancedFeatures',
  initialState: {
    abTests: [],
    anomalies: {},
    predictiveGoals: {},
    scenarioModels: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(runABTest.fulfilled, (state, action) => {
        state.abTests.push(action.payload);
      })
      .addCase(detectAnomalies.fulfilled, (state, action) => {
        state.anomalies[action.meta.arg.metricId] = action.payload;
      })
      .addCase(predictiveGoalSetting.fulfilled, (state, action) => {
        state.predictiveGoals[action.meta.arg.metricId] = action.payload;
      })
      .addCase(performScenarioModeling.fulfilled, (state, action) => {
        state.scenarioModels.push(action.payload);
      });
  }
});

export default advancedFeaturesSlice.reducer;