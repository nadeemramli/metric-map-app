import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const createTarget = createAsyncThunk('targets/createTarget', 
  async ({clientId, projectId, metricId, targetData}) => await api.setTarget(clientId, projectId, metricId, targetData)
);

export const setTarget = createAsyncThunk('targets/setTarget', 
  async ({clientId, projectId, metricId, targetData}) => await api.setTarget(clientId, projectId, metricId, targetData)
);

export const updateTarget = createAsyncThunk('targets/updateTarget', 
  async ({clientId, projectId, metricId, targetId, targetData}) => await api.updateTarget(clientId, projectId, metricId, targetId, targetData)
);

export const deleteTarget = createAsyncThunk('targets/deleteTarget', 
  async ({clientId, projectId, metricId, targetId}) => {
    await api.deleteTarget(clientId, projectId, metricId, targetId);
    return { metricId, targetId };
  }
);

const targetsSlice = createSlice({
  name: 'targets',
  initialState: {
    targets: {},
    status: {
      create: 'idle',
      set: 'idle',
      update: 'idle',
      delete: 'idle'
    },
    error: {
      create: null,
      set: null,
      update: null,
      delete: null
    }
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(createTarget.pending, (state) => {
        state.status.create = 'loading';
        state.error.create = null;
      })
      .addCase(createTarget.fulfilled, (state, action) => {
        state.status.create = 'succeeded';
        if (!state.targets[action.payload.metricId]) {
          state.targets[action.payload.metricId] = [];
        }
        state.targets[action.payload.metricId].push(action.payload);
      })
      .addCase(createTarget.rejected, (state, action) => {
        state.status.create = 'failed';
        state.error.create = action.error.message;
      })
      .addCase(setTarget.pending, (state) => {
        state.status.set = 'loading';
        state.error.set = null;
      })
      .addCase(setTarget.fulfilled, (state, action) => {
        state.status.set = 'succeeded';
        if (!state.targets[action.payload.metricId]) {
          state.targets[action.payload.metricId] = [];
        }
        state.targets[action.payload.metricId].push(action.payload);
      })
      .addCase(setTarget.rejected, (state, action) => {
        state.status.set = 'failed';
        state.error.set = action.error.message;
      })
      .addCase(updateTarget.pending, (state) => {
        state.status.update = 'loading';
        state.error.update = null;
      })
      .addCase(updateTarget.fulfilled, (state, action) => {
        state.status.update = 'succeeded';
        const metricTargets = state.targets[action.payload.metricId];
        if (metricTargets) {
          const index = metricTargets.findIndex(target => target.id === action.payload.id);
          if (index !== -1) {
            metricTargets[index] = action.payload;
          }
        }
      })
      .addCase(updateTarget.rejected, (state, action) => {
        state.status.update = 'failed';
        state.error.update = action.error.message;
      })
      .addCase(deleteTarget.pending, (state) => {
        state.status.delete = 'loading';
        state.error.delete = null;
      })
      .addCase(deleteTarget.fulfilled, (state, action) => {
        state.status.delete = 'succeeded';
        const { metricId, targetId } = action.payload;
        if (state.targets[metricId]) {
          state.targets[metricId] = state.targets[metricId].filter(target => target.id !== targetId);
        }
      })
      .addCase(deleteTarget.rejected, (state, action) => {
        state.status.delete = 'failed';
        state.error.delete = action.error.message;
      });
  }
});

export const selectTargetsByMetricId = (state, metricId) => state.targets.targets[metricId] || [];
export const selectTargetsStatus = (state) => state.targets.status;
export const selectTargetsError = (state) => state.targets.error;

export default targetsSlice.reducer;