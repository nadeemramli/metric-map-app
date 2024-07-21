import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchDashboards = createAsyncThunk('dashboards/fetchDashboards', 
  async ({ clientId, projectId }) => await api.fetchDashboards(clientId, projectId)
);
export const createDashboard = createAsyncThunk('dashboards/createDashboard', 
  async ({ clientId, projectId, dashboardData }) => await api.createDashboard(clientId, projectId, dashboardData)
);
export const updateDashboard = createAsyncThunk('dashboards/updateDashboard', 
  async ({ clientId, projectId, dashboardId, dashboardData }) => await api.updateDashboard(clientId, projectId, dashboardId, dashboardData)
);
export const deleteDashboard = createAsyncThunk('dashboards/deleteDashboard', 
  async ({ clientId, projectId, dashboardId }) => {
    await api.deleteDashboard(clientId, projectId, dashboardId);
    return dashboardId;
  }
);

const dashboardsSlice = createSlice({
  name: 'dashboards',
  initialState: {
    dashboards: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchDashboards.fulfilled, (state, action) => {
        state.dashboards = action.payload;
      })
      .addCase(createDashboard.fulfilled, (state, action) => {
        state.dashboards.push(action.payload);
      })
      .addCase(updateDashboard.fulfilled, (state, action) => {
        const index = state.dashboards.findIndex(dash => dash.id === action.payload.id);
        if (index !== -1) {
          state.dashboards[index] = action.payload;
        }
      })
      .addCase(deleteDashboard.fulfilled, (state, action) => {
        state.dashboards = state.dashboards.filter(dash => dash.id !== action.payload);
      });
  }
});

export default dashboardsSlice.reducer;