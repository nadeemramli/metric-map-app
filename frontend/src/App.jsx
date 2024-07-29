import React, { useEffect, Suspense } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import ErrorBoundary from './common/ErrorBoundary.jsx'; 
import Sidebar from './common/Sidebar.jsx';
import ProtectedRoute from './features/auth/components/ProtectedRoute.jsx';
import Login from './features/auth/pages/Login.jsx';
import ProjectManagementPage from './features/project-management/pages/ProjectManagementPage.jsx';
import ClientSelector from './features/auth/pages/ClientSelectorPage.jsx';
import MainDashboardPage from '@/features/dashboard/pages/MainDashboardPage.jsx';
import MetricsManagementPage from '@/features/metrics/pages/MetricsManagementPage.jsx';
import MetricDetailsPage from '@/features/metrics/pages/MetricDetailsPage.jsx';
import StrategyForecastingPage from '@/features/strategy-expectations/pages/StrategyForecastingPage.jsx';
import ExecutionPage from '@/features/execution/pages/ExecutionPage.jsx';
import RelationshipsVisualizationPage from '@/features/visualization/pages/RelationshipsVisualizationPage.jsx';
import HistoricalDataManagementPage from '@/features/historical-data/pages/HistoricalDataManagementPage.jsx';
import SettingsPage from '@/common/SettingsPage.jsx';
import { TooltipProvider } from "@/components/ui/tooltip";
import LoadingSpinner from './common/LoadingSpinner.jsx';
import { setupInterceptors } from './services/auth';
import { logout } from './store/slices/userSlice';


const App = () => {
  const dispatch = useDispatch();
  const isAuthenticated = useSelector(state => state.user.isAuthenticated);
  const currentProjectId = useSelector(state => state.user.currentProjectId);

  useEffect(() => {
    setupInterceptors();
    
    // Global error handler
    const handleError = (error) => {
      if (error.message === 'Session expired. Please log in again.') {
        dispatch(logout());
        toast.error('Your session has expired. Please log in again.');
      }
    };

    // Add event listener for unhandled promise rejections
    window.addEventListener('unhandledrejection', (event) => handleError(event.reason));

    // Cleanup
    return () => {
      window.removeEventListener('unhandledrejection', handleError);
    };
  }, [dispatch]);

  return (
    <ErrorBoundary showDetails={process.env.NODE_ENV === 'development'}>
      <TooltipProvider>
        <Router>
          <Suspense fallback={<LoadingSpinner />}>
            <div className="flex h-screen bg-gray-900 text-white">
              {isAuthenticated && <Sidebar />}
              <main className="flex-1 overflow-y-auto p-6">
                <Routes>
                  <Route path="/login" element={!isAuthenticated ? <Login /> : <Navigate to="/clients" replace />} />
                  
                  <Route element={<ProtectedRoute requiredAuth />}>
                    <Route path="/clients" element={<ClientSelector />} />
                    
                    <Route element={<ProtectedRoute requiredClient />}>
                      <Route path="/projects" element={<ProjectManagementPage />} />
                      
                      <Route element={<ProtectedRoute requiredProject currentProjectId={currentProjectId} />}>
                        <Route path="/dashboard" element={<MainDashboardPage currentProjectId={currentProjectId}/>} />
                        <Route path="/metrics" element={<MetricsManagementPage currentProjectId={currentProjectId}/>} />
                        <Route path="/metrics/new" element={<MetricDetailsPage currentProjectId={currentProjectId}/>} />
                        <Route path="/metrics/:metricId" element={<MetricDetailsPage />} />
                        <Route path="/metrics/:metricId/historical-data" element={<HistoricalDataManagementPage currentProjectId={currentProjectId}/>} />
                        <Route path="/strategy" element={<StrategyForecastingPage currentProjectId={currentProjectId}/>} />
                        <Route path="/execution" element={<ExecutionPage currentProjectId={currentProjectId}/>} />
                        <Route path="/relationships" element={<RelationshipsVisualizationPage currentProjectId={currentProjectId}/>} />
                        <Route path="/settings" element={<SettingsPage currentProjectId={currentProjectId}/>} />
                      </Route>
                    </Route>
                  </Route>

                  <Route path="*" element={<Navigate to={isAuthenticated ? "/clients" : "/login"} replace />} />
                </Routes>
              </main>
            </div>
            <ToastContainer position='top-right' autoClose={5000} />
          </Suspense>
        </Router>
      </TooltipProvider>
    </ErrorBoundary>
  );
};


export default App;