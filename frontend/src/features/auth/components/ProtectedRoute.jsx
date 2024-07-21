import React from 'react';
import { useSelector } from 'react-redux';
import { Navigate, Outlet } from 'react-router-dom';

const ProtectedRoute = ({ requiredAuth, requiredClient, requiredProject }) => {
  const isAuthenticated = useSelector(state => state.user.isAuthenticated);
  const currentClientId = useSelector(state => state.user.currentClientId);
  const currentProjectId = useSelector(state => state.projects.currentProjectId);

  if (requiredAuth && !isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  if (requiredClient && !currentClientId) {
    return <Navigate to="/clients" replace />;
  }

  if (requiredProject && !currentProjectId) {
    return <Navigate to="/projects" replace />;
  }

  return <Outlet />;
};

export default ProtectedRoute;