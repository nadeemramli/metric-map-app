import axios from 'axios';
import { API_BASE_URL } from './config';

const authApi = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const login = async (credentials) => {
  try {
    const response = await authApi.post('/token/', credentials);
    const { access, refresh } = response.data;
    localStorage.setItem('token', access);
    localStorage.setItem('refreshToken', refresh);
    return response.data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};

export const logout = () => {
  localStorage.removeItem('token');
  delete authApi.defaults.headers.common['Authorization'];
};

export const refreshToken = async () => {
  const refreshToken = localStorage.getItem('refreshToken');
  try {
    const response = await authApi.post('/token/refresh/', { refresh: refreshToken });
    const { access } = response.data;
    localStorage.setItem('token', access);
    return access;
  } catch (error) {
    console.error('Token refresh error:', error);
    throw error;
  }
};

export const setupInterceptors = () => {
  authApi.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  }, (error) => Promise.reject(error));

  authApi.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        try {
          const newToken = await refreshToken();
          originalRequest.headers['Authorization'] = `Bearer ${newToken}`;
          return authApi(originalRequest);
        } catch (refreshError) {
          // Handle refresh token failure (e.g., logout user)
          localStorage.removeItem('token');
          localStorage.removeItem('refreshToken');
          // Instead of dispatching an action, we'll throw an error
          // that can be caught by the global error handler
          throw new Error('Session expired. Please log in again.');
        }
      }
      return Promise.reject(error);
    }
  );
};

export default authApi;