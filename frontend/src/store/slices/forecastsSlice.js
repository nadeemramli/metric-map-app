import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const generateForecast = createAsyncThunk('forecasts/generateForecast', 
  async ({ clientId, projectId, metricId }) => await api.generateForecast(clientId, projectId, metricId)
);

export const fetchForecasts = createAsyncThunk('forecasts/fetchForecasts', 
  async ({ clientId, projectId, metricId }) => await api.fetchForecasts(clientId, projectId, metricId)
);

export const fetchForecastsForAllMetrics = createAsyncThunk(
  'forecasts/fetchForecastsForAllMetrics',
  async ({ clientId, projectId, metricIds }, { dispatch }) => {
    const results = {};
    for (const metricId of metricIds) {
      try {
        const forecast = await api.fetchForecasts(clientId, projectId, metricId);
        results[metricId] = forecast;
      } catch (error) {
        // If any forecast fetch fails, throw an error to stop the entire process
        throw new Error(`Failed to fetch forecast for metric ${metricId}: ${error.message}`);
      }
    }
    return results;
  }
);

const forecastsSlice = createSlice({
  name: 'forecasts',
  initialState: {
    forecasts: {},
    status: 'idle',
    error: null,
    allMetricsForecastStatus: 'idle',
    allMetricsForecastError: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(generateForecast.fulfilled, (state, action) => {
        if (!state.forecasts[action.meta.arg.metricId]) {
          state.forecasts[action.meta.arg.metricId] = [];
        }
        state.forecasts[action.meta.arg.metricId].push(action.payload);
      })
      .addCase(fetchForecasts.fulfilled, (state, action) => {
        state.forecasts[action.meta.arg.metricId] = action.payload;
      })
      .addCase(fetchForecastsForAllMetrics.pending, (state) => {
        state.allMetricsForecastStatus = 'loading';
        state.allMetricsForecastError = null;
      })
      .addCase(fetchForecastsForAllMetrics.fulfilled, (state, action) => {
        state.forecasts = { ...state.forecasts, ...action.payload };
        state.allMetricsForecastStatus = 'succeeded';
      })
      .addCase(fetchForecastsForAllMetrics.rejected, (state, action) => {
        state.allMetricsForecastStatus = 'failed';
        state.allMetricsForecastError = action.error.message;
      });
  }
});

export const selectForecastsByMetricId = (state, metricId) => state.forecasts.forecasts[metricId] || [];
export const selectAllMetricsForecastStatus = (state) => state.forecasts.allMetricsForecastStatus;
export const selectAllMetricsForecastError = (state) => state.forecasts.allMetricsForecastError;

export default forecastsSlice.reducer;