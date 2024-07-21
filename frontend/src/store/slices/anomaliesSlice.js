import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const detectAnomalies = createAsyncThunk('anomalies/detectAnomalies', 
  async ({ clientId, projectId, metricId }) => await api.detectAnomalies(clientId, projectId, metricId)
);

export const fetchAnomalies = createAsyncThunk('anomalies/fetchAnomalies', 
  async ({ clientId, projectId, metricId }) => await api.fetchAnomalies(clientId, projectId, metricId)
);

const anomaliesSlice = createSlice({
  name: 'anomalies',
  initialState: {
    anomalies: {},
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(detectAnomalies.fulfilled, (state, action) => {
        state.anomalies[action.meta.arg.metricId] = action.payload;
      })
      .addCase(fetchAnomalies.fulfilled, (state, action) => {
        state.anomalies[action.meta.arg.metricId] = action.payload;
      });
  }
});

export const selectAnomaliesByMetricId = (state, metricId) => state.anomalies.anomalies[metricId] || [];

export default anomaliesSlice.reducer;