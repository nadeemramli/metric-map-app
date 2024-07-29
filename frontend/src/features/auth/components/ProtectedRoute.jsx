import React from 'react';
import { useSelector } from 'react-redux';
import { Navigate, Outlet } from 'react-router-dom';

const ProtectedRoute = ({ requiredAuth, requiredClient, requiredProject, currentProjectId }) => {
  const isAuthenticated = useSelector(state => state.user.isAuthenticated);
  const currentClientId = useSelector(state => state.user.currentClientId);

  console.log("ProtectedRoute checks initiated", { requiredAuth, requiredClient, requiredProject, isAuthenticated, currentClientId, currentProjectId });

  if (requiredAuth && !isAuthenticated) {
    console.log("User is not authenticated, redirecting to login", { isAuthenticated });
    return <Navigate to="/login" replace />;
  }

  if (requiredClient && !currentClientId) {
    console.log("No client selected, redirecting to client selection", { currentClientId });
    return <Navigate to="/clients" replace />;
  }

  if (requiredProject && !currentProjectId) {
    console.log("No project selected, redirecting to project selection", { currentProjectId });
    return <Navigate to="/projects" replace />;
  }

  console.log("User meets all required conditions, rendering Outlet");
  return <Outlet />;
};

export default ProtectedRoute;
