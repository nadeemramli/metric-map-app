import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as api from '@/services/api.js';
import * as authService from '@/services/auth';

export const login = createAsyncThunk('user/login', 
  async (credentials, { rejectWithValue }) => {
    try {
      const userData = await authService.login(credentials);
      return userData;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Login failed');
    }
  }
);

export const logout = createAsyncThunk('user/logout', 
  async () => {
    await authService.logout();
  }
);

export const fetchUserProfile = createAsyncThunk('user/fetchUserProfile', 
  async () => await api.fetchUserProfile()
);

export const updateUserProfile = createAsyncThunk('user/updateUserProfile', 
  async (profileData) => await api.updateUserProfile(profileData)
);

export const changePassword = createAsyncThunk('user/changePassword',
  async (passwordData) => await api.changePassword(passwordData)
);

export const setCurrentProject = createAsyncThunk(
  'user/setCurrentProject',
  async (projectId, { getState, rejectWithValue }) => {
    try {
      const { user } = getState();
      // You might want to make an API call here to update the user's current project on the server
      // For now, we'll just return the projectId
      return projectId;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

export const handleSelectProject = createAsyncThunk(
  'user/handleSelectProject',
  async ({ projectId, navigate }, { getState, dispatch, rejectWithValue }) => {
    console.log("handleSelectProject initiated", { projectId });
    
    const stateBefore = getState();
    console.log("Current user state before setting project:", {
      isAuthenticated: stateBefore.user.isAuthenticated,
      currentClientId: stateBefore.user.currentClientId,
      currentProjectId: stateBefore.user.currentProjectId
    });

    try {
      const result = await dispatch(setCurrentProject(projectId)).unwrap();
      console.log("setCurrentProject successful", { result });

      // Assuming navigate is available in the context where this thunk is called
      console.log("Attempting to navigate to dashboard");
      navigate('/dashboard'); // Adjust based on actual routing in your app
      console.log("Navigation function called, check if URL changed in browser");

      const stateAfter = getState();
      console.log("Current user state after setting project:", {
        isAuthenticated: stateAfter.user.isAuthenticated,
        currentClientId: stateAfter.user.currentClientId,
        currentProjectId: stateAfter.user.currentProjectId
      });
      return result;
    } catch (err) {
      console.error("Error in handleSelectProject", err);
      return rejectWithValue(err);
    } finally {
      console.log("handleSelectProject finished", { projectId });
    }
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    user: null,
    isAuthenticated: false,
    currentClientId: null,
    currentProjectId: null,
    status: {
      login: 'idle',
      logout: 'idle',
      fetchProfile: 'idle',
      updateProfile: 'idle',
      changePassword: 'idle'
    },
    error: {
      login: null,
      logout: null,
      fetchProfile: null,
      updateProfile: null,
      changePassword: null
    }
  },
  reducers: {
    setCurrentClient: (state, action) => {
      state.currentClientId = action.payload;
    },
    setCurrentProject: (state, action) => {
      console.log("Setting current project in state:", action.payload);
      state.currentProjectId = action.payload;
      console.log("New state after setting project:", state);
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state) => {
        state.status.login = 'loading';
        state.error.login = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.status.login = 'succeeded';
        state.isAuthenticated = true;
        state.user = action.payload;
      })
      .addCase(login.rejected, (state, action) => {
        state.status.login = 'failed';
        state.error.login = action.error.message;
      })
      .addCase(logout.pending, (state) => {
        state.status.logout = 'loading';
        state.isAuthenticated = false;
        state.error.logout = null;
      })
      .addCase(logout.fulfilled, (state) => {
        state.status.logout = 'succeeded';
        state.isAuthenticated = false;
        state.user = null;
        state.currentClientId = null;
        state.currentProjectId = null;
      })
      .addCase(logout.rejected, (state, action) => {
        state.status.logout = 'failed';
        state.error.logout = action.error.message;
      })
      .addCase(fetchUserProfile.pending, (state) => {
        state.status.fetchProfile = 'loading';
        state.error.fetchProfile = null;
      })
      .addCase(fetchUserProfile.fulfilled, (state, action) => {
        state.status.fetchProfile = 'succeeded';
        state.user = action.payload;
      })
      .addCase(fetchUserProfile.rejected, (state, action) => {
        state.status.fetchProfile = 'failed';
        state.error.fetchProfile = action.error.message;
      })
      .addCase(updateUserProfile.pending, (state) => {
        state.status.updateProfile = 'loading';
        state.error.updateProfile = null;
      })
      .addCase(updateUserProfile.fulfilled, (state, action) => {
        state.status.updateProfile = 'succeeded';
        state.user = action.payload;
      })
      .addCase(updateUserProfile.rejected, (state, action) => {
        state.status.updateProfile = 'failed';
        state.error.updateProfile = action.error.message;
      })
      .addCase(changePassword.pending, (state) => {
        state.status.changePassword = 'loading';
        state.error.changePassword = null;
      })
      .addCase(changePassword.fulfilled, (state) => {
        state.status.changePassword = 'succeeded';
      })
      .addCase(changePassword.rejected, (state, action) => {
        state.status.changePassword = 'failed';
        state.error.changePassword = action.error.message;
      })
      .addCase(setCurrentProject.fulfilled, (state, action) => {
        console.log("Updating state with new project ID", action.payload);
        state.currentProjectId = action.payload; // This sets the project ID in the state
      });
  }
});

// Export actions
export const { setCurrentClient } = userSlice.actions;

// Export selectors
export const selectUser = (state) => state.user.user;
export const selectIsAuthenticated = (state) => state.user.isAuthenticated;
export const selectCurrentClientId = (state) => state.user.currentClientId;
export const selectCurrentProjectId = (state) => state.user.currentProjectId;
export const selectUserStatus = (state) => state.user.status;
export const selectUserError = (state) => state.user.error;

export default userSlice.reducer;