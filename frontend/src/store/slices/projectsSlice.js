import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchProjects = createAsyncThunk(
  'projects/fetchProjects',
  async (clientId, { rejectWithValue }) => {
    try {
      const response = await api.fetchProjects(clientId);
      return response;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

export const createProject = createAsyncThunk(
  'projects/createProject',
  async ({ clientId, projectData }, { rejectWithValue }) => {
    try {
      const response = await api.createProject(clientId, projectData);
      return response;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

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
  reducers: {
    setCurrentProject: (state, action) => {
    state.currentProjectId = action.payload;
    }},
  extraReducers: (builder) => {
    builder
      .addCase(fetchProjects.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchProjects.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.projects = action.payload.results;
        state.totalCount = action.payload.count;
      })
      .addCase(fetchProjects.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(createProject.fulfilled, (state, action) => {
        console.log("Create project fulfilled. Payload:", action.payload);
        console.log("Current state projects:", state.projects);
        state.status = 'succeeded';
        if (Array.isArray(action.payload.results)) {
          state.projects = action.payload.results;
          state.totalCount = action.payload.count;
        } else if (action.payload.id) {
          state.projects.push(action.payload);
          state.totalCount += 1;
        }
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

//Action
export const { setCurrentProject } = projectsSlice.actions;

// Selectors
export const selectAllProjects = (state) => state.projects.projects;
export const selectProjectById = (state, projectId) => 
  state.projects.projects.find(project => project.id === projectId);

export default projectsSlice.reducer;