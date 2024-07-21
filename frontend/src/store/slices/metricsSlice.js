import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchMetrics = createAsyncThunk('metrics/fetchMetrics', 
  async ({ clientId, projectId }) => await api.fetchMetrics(clientId, projectId)
);

export const createMetric = createAsyncThunk('metrics/createMetric', 
  async ({ clientId, projectId, metricData }) => await api.createMetric(clientId, projectId, metricData)
);
export const updateMetric = createAsyncThunk('metrics/updateMetric', 
  async ({ clientId, projectId, metricId, metricData }) => await api.updateMetric(clientId, projectId, metricId, metricData)
);
export const deleteMetric = createAsyncThunk('metrics/deleteMetric', 
  async ({ clientId, projectId, metricId }) => {
    await api.deleteMetric(clientId, projectId, metricId);
    return metricId;
  }
);

export const fetchHistoricalData = createAsyncThunk('metrics/fetchHistoricalData', 
  async ({ clientId, projectId, metricId }) => {
    const response = await api.fetchHistoricalData(clientId, projectId, metricId);
    return { metricId, data: response };
  }
);

export const addHistoricalData = createAsyncThunk('metrics/addHistoricalData', 
  async ({ clientId, projectId, metricId, data }) => {
    const response = await api.addHistoricalData(clientId, projectId, metricId, data);
    return { metricId, data: response };
  }
);

export const addBulkHistoricalData = createAsyncThunk('metrics/addBulkHistoricalData', 
  async ({ clientId, projectId, metricId, dataArray }) => {
    const response = await api.addBulkHistoricalData(clientId, projectId, metricId, dataArray);
    return { metricId, data: response };
  }
);

export const fetchPerformanceMetrics = createAsyncThunk(
  'metrics/fetchPerformanceMetrics',
  async ({ clientId, projectId, metricId }) => {
    const response = await api.fetchPerformanceMetrics(clientId, projectId, metricId);
    return { metricId, data: response };
  }
);

export const fetchMetricsAndConnections = createAsyncThunk(
  'metrics/fetchMetricsAndConnections',
  async ({ clientId, projectId }, { dispatch }) => {
    try {
      const [metrics, connections] = await Promise.all([
        api.fetchMetrics(clientId, projectId),
        api.fetchMetricConnections(clientId, projectId)
      ]);
      dispatch(setMetrics(metrics));
      dispatch(setConnections(connections));
      return { metrics, connections };
    } catch (error) {
      console.error('Error fetching metrics and connections:', error);
      throw error;
    }
  }
);

export const updateMetricPosition = createAsyncThunk(
  'metrics/updateMetricPosition',
  async ({ clientId, projectId, metricId, position }, { rejectWithValue }) => {
    try {
      const response = await api.updateMetricPosition(clientId, projectId, metricId, position);
      return response;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

const metricsSlice = createSlice({
  name: 'metrics',
  initialState: {
    metrics: [],
    connections: [],
    historicalData: {},
    insights: [],
    actionRemarks: [],
    performanceMetrics: {},
    status: 'idle',
    currentProjectId: null,
    error: null
  },
  reducers: {
    setMetrics: (state, action) => {
      state.metrics = action.payload;
    },
    setConnections: (state, action) => {
      state.connections = action.payload;
    },
    setCurrentProject: (state, action) => {
      state.currentProjectId = action.payload;
    },
    // ... other reducers},
  },
  extraReducers: (builder) => {
    builder
      .addCase(createMetric.fulfilled, (state, action) => {
        state.metrics.push(action.payload);
      })
      .addCase(updateMetric.fulfilled, (state, action) => {
        const index = state.metrics.findIndex(metric => metric.id === action.payload.id);
        if (index !== -1) {
          state.metrics[index] = action.payload;
        }
      })
      .addCase(deleteMetric.fulfilled, (state, action) => {
        state.metrics = state.metrics.filter(metric => metric.id !== action.payload);
      })
      .addCase(fetchHistoricalData.fulfilled, (state, action) => {
        state.historicalData[action.payload.metricId] = action.payload.data;
      })
      .addCase(addHistoricalData.fulfilled, (state, action) => {
        if (!state.historicalData[action.payload.metricId]) {
          state.historicalData[action.payload.metricId] = [];
        }
        state.historicalData[action.payload.metricId].push(action.payload.data);
      })
      .addCase(addBulkHistoricalData.fulfilled, (state, action) => {
        if (!state.historicalData[action.payload.metricId]) {
          state.historicalData[action.payload.metricId] = [];
        }
        state.historicalData[action.payload.metricId].push(...action.payload.data);
      })
      .addCase(fetchPerformanceMetrics.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchPerformanceMetrics.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.performanceMetrics[action.payload.metricId] = action.payload.data;
      })
      .addCase(fetchPerformanceMetrics.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(fetchMetricsAndConnections.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchMetricsAndConnections.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.metrics = action.payload.metrics;
        state.connections = action.payload.connections;
      })
      .addCase(fetchMetricsAndConnections.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(fetchMetrics.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchMetrics.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.metrics = action.payload;
      })
      .addCase(fetchMetrics.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(updateMetricPosition.fulfilled, (state, action) => {
        const index = state.metrics.findIndex(metric => metric.id === action.payload.id);
        if (index !== -1) {
          state.metrics[index].position = action.payload.position;
        }
      });
  }
});

// Export the actions
export const { addMetric } = metricsSlice.actions;

export const { setMetrics, setConnections } = metricsSlice.actions;

export const { setCurrentProject } = metricsSlice.actions;

// Export a selector to get all metrics
export const selectAllMetrics = (state) => state.metrics.metrics;

// Export a selector to get a specific metric by ID
export const selectMetricById = (state, metricId) => 
state.metrics.metrics.find(metric => metric.id === metricId);

// Export a selector to get historical data for a specific metric
export const selectHistoricalDataByMetricId = (state, metricId) => 
state.metrics.historicalData[metricId] || [];

export const selectPerformanceMetrics = (state, metricId) => state.metrics.performanceMetrics[metricId];

export const SelectMetricsByProject = (state) => 
  state.metrics.metrics.filter(metric => metric.projectId === state.metrics.currentProjectId);

export const selectAllConnections = (state) => state.metrics.connections;

export const selectActionRemarksByMetricId = (state, metricId) =>
  state.metrics.actionRemarks.filter(remark => remark.metricId === metricId);

export const selectInsightsByMetricId = (state, metricId) =>
  state.metrics.insights.filter(insight => insight.metricId === metricId);

// Export the reducer
export default metricsSlice.reducer;
