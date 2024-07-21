import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const generateReport = createAsyncThunk('reports/generateReport', 
  async ({ clientId, projectId, reportConfig }) => await api.generateReport(clientId, projectId, reportConfig)
);
export const fetchReports = createAsyncThunk('reports/fetchReports', 
  async ({ clientId, projectId }) => await api.fetchReports(clientId, projectId)
);

const reportsSlice = createSlice({
  name: 'reports',
  initialState: {
    reports: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(generateReport.fulfilled, (state, action) => {
        state.reports.push(action.payload);
      })
      .addCase(fetchReports.fulfilled, (state, action) => {
        state.reports = action.payload;
      });
  }
});

export default reportsSlice.reducer;