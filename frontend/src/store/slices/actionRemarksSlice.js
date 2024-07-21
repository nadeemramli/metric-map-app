import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

// Action Remarks
export const fetchActionRemarks = createAsyncThunk('actionRemarks/fetchActionRemarks',
  async ({ clientId, projectId, metricId }) => await api.fetchActionRemarks(clientId, projectId, metricId)
);
export const createActionRemark = createAsyncThunk('actionRemarks/createActionRemark', 
  async ({ clientId, projectId, metricId, remarkData }) => await api.addActionRemark(clientId, projectId, metricId, remarkData)
);
export const addActionRemark = createAsyncThunk('actionRemarks/addActionRemark', 
  async ({ clientId, projectId, metricId, remarkData }) => await api.addActionRemark(clientId, projectId, metricId, remarkData)
);
export const updateActionRemark = createAsyncThunk('actionRemarks/updateActionRemark', 
  async ({ clientId, projectId, metricId, remarkId, remarkData }) => await api.updateActionRemark(clientId, projectId, metricId, remarkId, remarkData)
);
export const deleteActionRemark = createAsyncThunk('actionRemarks/deleteActionRemark', 
  async ({ clientId, projectId, metricId, remarkId }) => {
    await api.deleteActionRemark(clientId, projectId, metricId, remarkId);
    return { metricId, remarkId };
  }
);

// Experiments
export const fetchExperiments = createAsyncThunk('actionRemarks/fetchExperiments',
  async ({ clientId, projectId }) => await api.fetchExperiments(clientId, projectId)
);
export const createExperiment = createAsyncThunk('actionRemarks/createExperiment', 
  async ({ clientId, projectId, experimentData }) => await api.createExperiment(clientId, projectId, experimentData)
);
export const updateExperiment = createAsyncThunk('actionRemarks/updateExperiment', 
  async ({ clientId, projectId, experimentId, experimentData }) => await api.updateExperiment(clientId, projectId, experimentId, experimentData)
);
export const deleteExperiment = createAsyncThunk('actionRemarks/deleteExperiment', 
  async ({ clientId, projectId, experimentId }) => {
    await api.deleteExperiment(clientId, projectId, experimentId);
    return experimentId;
  }
);
export const runExperiment = createAsyncThunk(
  'actionRemarks/runExperiment',
  async ({ clientId, projectId, experimentId }) => await api.runExperiment(clientId, projectId, experimentId)
);

// Insights
export const fetchInsights = createAsyncThunk('actionRemarks/fetchInsights',
  async ({ clientId, projectId, metricId }) => await api.fetchInsights(clientId, projectId, metricId)
);
export const addInsight = createAsyncThunk('actionRemarks/addInsight', 
  async ({ clientId, projectId, metricId, insightData }) => await api.addInsight(clientId, projectId, metricId, insightData)
);
export const updateInsight = createAsyncThunk('actionRemarks/updateInsight', 
  async ({ clientId, projectId, metricId, insightId, insightData }) => await api.updateInsight(clientId, projectId, metricId, insightId, insightData)
);
export const deleteInsight = createAsyncThunk('actionRemarks/deleteInsight', 
  async ({ clientId, projectId, metricId, insightId }) => {
    await api.deleteInsight(clientId, projectId, metricId, insightId);
    return { metricId, insightId };
  }
);

const actionRemarksSlice = createSlice({
  name: 'actionRemarks',
  initialState: {
    remarks: {},
    experiments: [],
    insights: {},
    status: {
      remarks: 'idle',
      experiments: 'idle',
      insights: 'idle'
    },
    error: {
      remarks: null,
      experiments: null,
      insights: null
    }
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      // Action Remarks
      .addCase(fetchActionRemarks.pending, (state) => {
        state.status.remarks = 'loading';
      })
      .addCase(fetchActionRemarks.fulfilled, (state, action) => {
        state.status.remarks = 'succeeded';
        state.remarks[action.meta.arg.metricId] = action.payload;
      })
      .addCase(fetchActionRemarks.rejected, (state, action) => {
        state.status.remarks = 'failed';
        state.error.remarks = action.error.message;
      })
      .addCase(createActionRemark.fulfilled, (state, action) => {
        if (!state.remarks[action.meta.arg.metricId]) {
          state.remarks[action.meta.arg.metricId] = [];
        }
        state.remarks[action.meta.arg.metricId].push(action.payload);
      })
      .addCase(addActionRemark.fulfilled, (state, action) => {
        if (!state.remarks[action.meta.arg.metricId]) {
          state.remarks[action.meta.arg.metricId] = [];
        }
        state.remarks[action.meta.arg.metricId].push(action.payload);
      })
      .addCase(updateActionRemark.fulfilled, (state, action) => {
        const metricRemarks = state.remarks[action.meta.arg.metricId];
        if (metricRemarks) {
          const index = metricRemarks.findIndex(remark => remark.id === action.payload.id);
          if (index !== -1) {
            metricRemarks[index] = action.payload;
          }
        }
      })
      .addCase(deleteActionRemark.fulfilled, (state, action) => {
        const { metricId, remarkId } = action.payload;
        if (state.remarks[metricId]) {
          state.remarks[metricId] = state.remarks[metricId].filter(remark => remark.id !== remarkId);
        }
      })
      // Experiments
      .addCase(fetchExperiments.pending, (state) => {
        state.status.experiments = 'loading';
      })
      .addCase(fetchExperiments.fulfilled, (state, action) => {
        state.status.experiments = 'succeeded';
        state.experiments = action.payload;
      })
      .addCase(fetchExperiments.rejected, (state, action) => {
        state.status.experiments = 'failed';
        state.error.experiments = action.error.message;
      })
      .addCase(createExperiment.fulfilled, (state, action) => {
        state.experiments.push(action.payload);
      })
      .addCase(updateExperiment.fulfilled, (state, action) => {
        const index = state.experiments.findIndex(exp => exp.id === action.payload.id);
        if (index !== -1) {
          state.experiments[index] = action.payload;
        }
      })
      .addCase(deleteExperiment.fulfilled, (state, action) => {
        state.experiments = state.experiments.filter(exp => exp.id !== action.payload);
      })
      .addCase(runExperiment.fulfilled, (state, action) => {
        const index = state.experiments.findIndex(exp => exp.id === action.payload.id);
        if (index !== -1) {
          state.experiments[index] = action.payload;
        }
      })
      // Insights
      .addCase(fetchInsights.pending, (state) => {
        state.status.insights = 'loading';
      })
      .addCase(fetchInsights.fulfilled, (state, action) => {
        state.status.insights = 'succeeded';
        state.insights[action.meta.arg.metricId] = action.payload;
      })
      .addCase(fetchInsights.rejected, (state, action) => {
        state.status.insights = 'failed';
        state.error.insights = action.error.message;
      })
      .addCase(addInsight.fulfilled, (state, action) => {
        if (!state.insights[action.meta.arg.metricId]) {
          state.insights[action.meta.arg.metricId] = [];
        }
        state.insights[action.meta.arg.metricId].push(action.payload);
      })
      .addCase(updateInsight.fulfilled, (state, action) => {
        const metricInsights = state.insights[action.meta.arg.metricId];
        if (metricInsights) {
          const index = metricInsights.findIndex(insight => insight.id === action.payload.id);
          if (index !== -1) {
            metricInsights[index] = action.payload;
          }
        }
      })
      .addCase(deleteInsight.fulfilled, (state, action) => {
        const { metricId, insightId } = action.payload;
        if (state.insights[metricId]) {
          state.insights[metricId] = state.insights[metricId].filter(insight => insight.id !== insightId);
        }
      });
  }
});

// Selectors
export const selectActionRemarksByMetricId = (state, metricId) => state.actionRemarks.remarks[metricId] || [];
export const selectAllExperiments = (state) => state.actionRemarks.experiments;
export const selectInsightsByMetricId = (state, metricId) => state.actionRemarks.insights[metricId] || [];

export const selectExperimentsByMetricId = (state, metricId) => 
  state.actionRemarks.experiments.filter(experiment => experiment.metricId === metricId);
export const selectExperimentById = (state, experimentId) => 
  state.actionRemarks.experiments.find(experiment => experiment.id === experimentId);

export const selectActionRemarksStatus = (state) => state.actionRemarks.status;
export const selectActionRemarksError = (state) => state.actionRemarks.error;

export default actionRemarksSlice.reducer;