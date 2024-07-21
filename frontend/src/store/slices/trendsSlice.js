import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const analyzeTrends = createAsyncThunk('trends/analyzeTrends', 
  async ({ clientId, projectId, metricId }) => await api.analyzeTrends(clientId, projectId, metricId)
);

export const fetchTrends = createAsyncThunk('trends/fetchTrends', 
  async ({ clientId, projectId, metricId }) => await api.fetchTrends(clientId, projectId, metricId)
);

const trendsSlice = createSlice({
  name: 'trends',
  initialState: {
    trends: {},
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(analyzeTrends.fulfilled, (state, action) => {
        state.trends[action.meta.arg.metricId] = action.payload;
      })
      .addCase(fetchTrends.fulfilled, (state, action) => {
        state.trends[action.meta.arg.metricId] = action.payload;
      });
  }
});

export const selectTrendsByMetricId = (state, metricId) => state.trends.trends[metricId] || [];

export default trendsSlice.reducer;