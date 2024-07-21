import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';



export const fetchClients = createAsyncThunk(
  'clients/fetchClients',
  async (_, { rejectWithValue }) => {
    try {
      const data = await api.fetchClients();
      // Make sure to return only the results array which contains the clients
      return data.results;
    } catch (error) {
      return rejectWithValue(error.response?.data || 'An error occurred');
    }
  }
);

export const createClient = createAsyncThunk('clients/createClient', 
  async (clientData) => await api.createClient(clientData)
);

export const updateClient = createAsyncThunk('clients/updateClient', 
  async ({ clientId, clientData }) => await api.updateClient(clientId, clientData)
);

export const deleteClient = createAsyncThunk('clients/deleteClient', 
  async (clientId) => {
    await api.deleteClient(clientId);
    return clientId;
  }
);

const clientsSlice = createSlice({
  name: 'clients',
  initialState: {
    clients: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchClients.pending, (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addCase(fetchClients.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.clients = action.payload;
      })
      .addCase(fetchClients.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload;
      })
      .addCase(createClient.fulfilled, (state, action) => {
        state.clients.push(action.payload);
      })
      .addCase(updateClient.fulfilled, (state, action) => {
        const index = state.clients.findIndex(client => client.id === action.payload.id);
        if (index !== -1) {
          state.clients[index] = action.payload;
        }
      })
      .addCase(deleteClient.fulfilled, (state, action) => {
        state.clients = state.clients.filter(client => client.id !== action.payload);
      });
  }
});

export const selectAllClients = (state) => state.clients.clients;
export const selectClientById = (state, clientId) => 
  state.clients.clients.find(client => client.id === clientId);
export const selectClientsStatus = (state) => state.clients.status;
export const selectClientsError = (state) => state.clients.error;

export default clientsSlice.reducer;