import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';

export const fetchCategories = createAsyncThunk('categories/fetchCategories', 
  async ({ clientId, projectId }) => await api.fetchCategories(clientId, projectId)
);
export const createCategory = createAsyncThunk('categories/createCategory', 
  async ({ clientId, projectId, categoryData }) => await api.createCategory(clientId, projectId, categoryData)
);
export const updateCategory = createAsyncThunk('categories/updateCategory', 
  async ({ clientId, projectId, categoryId, categoryData }) => await api.updateCategory(clientId, projectId, categoryId, categoryData)
);
export const deleteCategory = createAsyncThunk('categories/deleteCategory', 
  async ({ clientId, projectId, categoryId }) => {
    await api.deleteCategory(clientId, projectId, categoryId);
    return categoryId;
  }
);

const categoriesSlice = createSlice({
  name: 'categories',
  initialState: {
    categories: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
    .addCase(fetchCategories.pending, (state) => {
      state.status = 'loading';
    })
    .addCase(fetchCategories.fulfilled, (state, action) => {
      state.status = 'succeeded';
      state.categories = action.payload;
    })
    .addCase(fetchCategories.rejected, (state, action) => {
      state.status = 'failed';
      state.error = action.error.message;
    })
    .addCase(createCategory.fulfilled, (state, action) => {
      state.categories.push(action.payload);
    })
    .addCase(updateCategory.fulfilled, (state, action) => {
      const index = state.categories.findIndex(cat => cat.id === action.payload.id);
      if (index !== -1) {
        state.categories[index] = action.payload;
      }
    })
    .addCase(deleteCategory.fulfilled, (state, action) => {
      state.categories = state.categories.filter(cat => cat.id !== action.payload);
    });
  }
});

// Export the reducer
export default categoriesSlice.reducer;

// Export a selector to get all categories
export const selectAllCategories = (state) => state.categories.categories;

// Export a selector to get a specific category by ID
export const selectCategoryById = (state, categoryId) => 
state.categories.categories.find(category => category.id === categoryId);