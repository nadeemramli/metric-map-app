import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchProjects = createAsyncThunk('projects/fetchProjects', 
  async (clientId) => await api.fetchProjects(clientId));
export const createProject = createAsyncThunk('projects/createProject', api.createProject);
export const updateProject = createAsyncThunk('projects/updateProject', 
  async ({projectId, projectData}) => await api.updateProject(projectId, projectData));
export const deleteProject = createAsyncThunk('projects/deleteProject', api.deleteProject);

const projectsSlice = createSlice({
  name: 'projects',
  initialState: {
    projects: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchProjects.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchProjects.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.projects = action.payload;
      })
      .addCase(fetchProjects.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(createProject.fulfilled, (state, action) => {
        state.projects.push(action.payload);
      })
      .addCase(updateProject.fulfilled, (state, action) => {
        const index = state.projects.findIndex(project => project.id === action.payload.id);
        if (index !== -1) {
          state.projects[index] = action.payload;
        }
      })
      .addCase(deleteProject.fulfilled, (state, action) => {
        state.projects = state.projects.filter(project => project.id !== action.payload);
      });
  }
});

export default projectsSlice.reducer;