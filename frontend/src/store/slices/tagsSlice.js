import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchTags = createAsyncThunk('tags/fetchTags', 
  async ({ clientId, projectId }) => await api.fetchTags(clientId, projectId)
);
export const createTag = createAsyncThunk('tags/createTag', 
  async ({ clientId, projectId, tagData }) => await api.createTag(clientId, projectId, tagData)
);
export const updateTag = createAsyncThunk('tags/updateTag', 
  async ({ clientId, projectId, tagId, tagData }) => await api.updateTag(clientId, projectId, tagId, tagData)
);
export const deleteTag = createAsyncThunk('tags/deleteTag', 
  async ({ clientId, projectId, tagId }) => {
    await api.deleteTag(clientId, projectId, tagId);
    return tagId;
  }
);

const tagsSlice = createSlice({
    name: 'tags',
    initialState: {
      tags: [],
      status: 'idle',
      error: null
    },
    reducers: {},
    extraReducers: (builder) => {
      builder
      .addCase(fetchTags.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchTags.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.tags = action.payload;
      })
      .addCase(fetchTags.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(createTag.fulfilled, (state, action) => {
        state.tags.push(action.payload);
      })
      .addCase(updateTag.fulfilled, (state, action) => {
        const index = state.tags.findIndex(tag => tag.id === action.payload.id);
        if (index !== -1) {
          state.tags[index] = action.payload;
        }
      })
      .addCase(deleteTag.fulfilled, (state, action) => {
        state.tags = state.tags.filter(tag => tag.id !== action.payload);
      });
  }
});

// Export the reducer
export default tagsSlice.reducer;

// Export a selector to get all tags
export const selectAllTags = (state) => state.tags.tags;

// Export a selector to get a specific tag by ID
export const selectTagById = (state, tagId) => 
  state.tags.tags.find(tag => tag.id === tagId);