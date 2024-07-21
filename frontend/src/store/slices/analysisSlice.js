import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchAnalysis = createAsyncThunk('analysis/fetchAnalysis', 
  async ({ clientId, projectId, metricId, analysisType }) => await api.analyzeMetric(clientId, projectId, metricId, analysisType)
);

const analysisSlice = createSlice({
  name: 'analysis',
  initialState: {
    analysisResults: {},
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAnalysis.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchAnalysis.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.analysisResults[`${action.meta.arg.metricId}-${action.meta.arg.analysisType}`] = action.payload;
      })
      .addCase(fetchAnalysis.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      });
  }
});

export default analysisSlice.reducer;