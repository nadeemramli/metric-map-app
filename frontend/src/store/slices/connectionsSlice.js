import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchConnections = createAsyncThunk('connections/fetchConnections', 
  async ({ clientId, projectId }) => await api.fetchMetricConnections(clientId, projectId)
);
export const createConnection = createAsyncThunk('connections/createConnection', 
  async ({ clientId, projectId, connectionData }) => await api.createMetricConnection(clientId, projectId, connectionData)
);
export const updateConnection = createAsyncThunk('connections/updateConnection', 
  async ({ clientId, projectId, connectionId, connectionData }) => await api.updateMetricConnection(clientId, projectId, connectionId, connectionData)
);
export const deleteConnection = createAsyncThunk('connections/deleteConnection', 
  async ({ clientId, projectId, connectionId }) => {
    await api.deleteMetricConnection(clientId, projectId, connectionId);
    return connectionId;
  }
);

const connectionsSlice = createSlice({
  name: 'connections',
  initialState: {
    connections: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchConnections.fulfilled, (state, action) => {
        state.connections = action.payload;
      })
      .addCase(createConnection.fulfilled, (state, action) => {
        state.connections.push(action.payload);
      })
      .addCase(updateConnection.fulfilled, (state, action) => {
        const index = state.connections.findIndex(conn => conn.id === action.payload.id);
        if (index !== -1) {
          state.connections[index] = action.payload;
        }
      })
      .addCase(deleteConnection.fulfilled, (state, action) => {
        state.connections = state.connections.filter(conn => conn.id !== action.payload);
      });
  }
});

// Add this selector
export const selectAllConnections = (state) => state.connections.connections;

// You might also want to add this selector for future use
export const selectConnectionById = (state, connectionId) => 
  state.connections.connections.find(connection => connection.id === connectionId);

export default connectionsSlice.reducer;
