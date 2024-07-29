import axios from 'axios';
import { API_BASE_URL } from './config';
import authApi from './auth';

const TIMEOUT = 10000; // 10 seconds

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add a request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = 'Bearer ' + token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add a response interceptor to handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post(`${API_BASE_URL}/auth/token/refresh/`, { refresh: refreshToken });
        const { access } = response.data;
        localStorage.setItem('token', access);
        api.defaults.headers['Authorization'] = 'Bearer ' + access;
        return api(originalRequest);
      } catch (refreshError) {
        // Handle refresh token failure (e.g., logout user)
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);


// Ensure your axios instance is configured to send CSRF token. For auth purposes
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// Error handling helper function
const handleError = (error) => {
  if (error.response) {
    console.error('Server responded with an error:', error.response.status, error.response.data);
  } else if (error.request) {
    console.error('No response received:', error.request);
  } else {
    console.error('Error setting up the request:', error.message);
  }
  throw error;
};

// Helper function to make API calls
const apiCall = async (method, endpoint, data = null) => {
  try {
    const config = {
      method,
      url: endpoint,
    };
    if (data) {
      config.data = data;
    }
    const response = await api(config);
    return response.data;
  } catch (error) {
    return handleError(error);
  }
};

// Client (Tenant) Management
export const fetchClients = async () => {
  try {
    console.log('Fetching clients...');
    const response = await authApi.get('/clients/');
    console.log('Response received:', response);
    return response.data;
  } catch (error) {
    console.error('Error fetching clients:', error);
    if (error.response) {
      console.error('Response data:', error.response.data);
      console.error('Response status:', error.response.status);
      console.error('Response headers:', error.response.headers);
    } else if (error.request) {
      console.error('No response received:', error.request);
    } else {
      console.error('Error setting up the request:', error.message);
    }
    throw error;
  }
};
export const createClient = (clientData) => apiCall('post', '/clients/', clientData);
export const updateClient = (clientId, clientData) => apiCall('put', `/clients/${clientId}/`, clientData);
export const deleteClient = (clientId) => apiCall('delete', `/clients/${clientId}/`);

// Project Management
export const fetchProjects = (clientId) => apiCall('get', `/clients/${clientId}/projects/`);
export const createProject = (clientId, projectData) => apiCall('post', `/clients/${clientId}/projects/`, projectData);
export const updateProject = (clientId, projectId, projectData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/`, projectData);
export const deleteProject = (clientId, projectId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/`);

// Metric Management
export const fetchMetrics = (clientId, projectId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metrics/`);
export const createMetric = (clientId, projectId, metricData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/metrics/`, metricData);
export const updateMetric = (clientId, projectId, metricId, metricData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/`, metricData);
export const deleteMetric = (clientId, projectId, metricId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/`);

// Categories
export const fetchCategories = (clientId, projectId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/categories/`);
export const createCategory = (clientId, projectId, categoryData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/categories/`, categoryData);
export const updateCategory = (clientId, projectId, categoryId, categoryData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/categories/${categoryId}/`, categoryData);
export const deleteCategory = (clientId, projectId, categoryId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/categories/${categoryId}/`);

// Tags
export const fetchTags = (clientId, projectId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/tags/`);
export const createTag = (clientId, projectId, tagData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/tags/`, tagData);
export const updateTag = (clientId, projectId, tagId, tagData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/tags/${tagId}/`, tagData);
export const deleteTag = (clientId, projectId, tagId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/tags/${tagId}/`);

// Historical Data
export const fetchHistoricalData = (clientId, projectId, metricId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/historical-data/`);
export const addHistoricalData = (clientId, projectId, metricId, data) => apiCall('post', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/historical-data/`, data);
export const addBulkHistoricalData = (clientId, projectId, metricId, dataArray) => apiCall('post', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/historical-data/bulk/`, dataArray);

// Metric Connections
export const fetchMetricConnections = (clientId, projectId, metricId) => {
  if (!clientId || !projectId || !metricId) {
    console.error(`Invalid parameters: clientId=${clientId}, projectId=${projectId}, metricId=${metricId}`);
    return Promise.reject(new Error('Invalid clientId, projectId, or metricId'));
  }
  const url = `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/connections/`;
  console.log(`Fetching metric connections with URL: ${url}`);
  return apiCall('get', url);
};

export const createMetricConnection = (clientId, projectId, metricId, connectionData) => 
  apiCall('post', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/connections/`, connectionData);

export const updateMetricConnection = (clientId, projectId, metricId, connectionId, connectionData) => 
  apiCall('put', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/connections/${connectionId}/`, connectionData);

export const deleteMetricConnection = (clientId, projectId, metricId, connectionId) => 
  apiCall('delete', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/connections/${connectionId}/`);

// Dashboard Management
export const fetchDashboards = (clientId, projectId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/dashboards/`);
export const createDashboard = (clientId, projectId, dashboardData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/dashboards/`, dashboardData);
export const updateDashboard = (clientId, projectId, dashboardId, dashboardData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/dashboards/${dashboardId}/`, dashboardData);
export const deleteDashboard = (clientId, projectId, dashboardId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/dashboards/${dashboardId}/`);

// Dashboard Layout
export const fetchDashboardLayouts = (clientId, projectId, dashboardId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/dashboards/${dashboardId}/layouts/`);
export const saveDashboardLayout = (clientId, projectId, dashboardId, layoutData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/dashboards/${dashboardId}/layouts/`, layoutData);

// Reports
export const generateReport = (clientId, projectId, reportConfig) => apiCall('post', `/clients/${clientId}/projects/${projectId}/reports/`, reportConfig);
export const fetchReports = (clientId, projectId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/reports/`);

// Data Analysis
export const analyzeMetric = (clientId, projectId, metricId, analysisType) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/analyze/`, { params: { type: analysisType } });
export const generateForecast = (clientId, projectId, metricId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/forecast/`);

// Targets
export const setTarget = (clientId, projectId, metricId, targetData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/targets/`, targetData);
export const updateTarget = (clientId, projectId, metricId, targetId, targetData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/targets/${targetId}/`, targetData);
export const deleteTarget = (clientId, projectId, metricId, targetId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/targets/${targetId}/`);

// Action Remarks
export const fetchActionRemarks = (clientId, projectId, metricId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/action-remarks/`);
export const addActionRemark = (clientId, projectId, metricId, remarkData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/action-remarks/`, remarkData);
export const updateActionRemark = (clientId, projectId, metricId, remarkId, remarkData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/action-remarks/${remarkId}/`, remarkData);
export const deleteActionRemark = (clientId, projectId, metricId, remarkId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/action-remarks/${remarkId}/`);

// Insights
export const fetchInsights = (clientId, projectId, metricId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/insights/`);
export const addInsight = (clientId, projectId, metricId, insightData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/insights/`, insightData);
export const updateInsight = (clientId, projectId, metricId, insightId, insightData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/insights/${insightId}/`, insightData);
export const deleteInsight = (clientId, projectId, metricId, insightId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/insights/${insightId}/`);

// Experiments
export const fetchExperiments = (clientId, projectId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/experiments/`);
export const createExperiment = (clientId, projectId, experimentData) => apiCall('post', `/clients/${clientId}/projects/${projectId}/experiments/`, experimentData);
export const updateExperiment = (clientId, projectId, experimentId, experimentData) => apiCall('put', `/clients/${clientId}/projects/${projectId}/experiments/${experimentId}/`, experimentData);
export const deleteExperiment = (clientId, projectId, experimentId) => apiCall('delete', `/clients/${clientId}/projects/${projectId}/experiments/${experimentId}/`);
export const getExperimentDetails = (clientId, projectId, experimentId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/experiments/${experimentId}/`);
export const runExperiment = (clientId, projectId, experimentId) => apiCall('post', `/clients/${clientId}/projects/${projectId}/experiments/${experimentId}/run_experiment/`);

// Metric Relationships
export const fetchMetricRelationships = (clientId, projectId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metric-relationships/`);

// Performance Metrics
export const fetchPerformanceMetrics = (clientId, projectId, metricId) => apiCall('get', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/performance/`);

// Metric Position
export const updateMetricPosition = (clientId, projectId, metricId, position) => apiCall('patch', `/clients/${clientId}/projects/${projectId}/metrics/${metricId}/position/`, { position });

export default api;