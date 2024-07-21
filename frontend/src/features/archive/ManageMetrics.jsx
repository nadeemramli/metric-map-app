import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import MetricTable from '../components/MetricTable';
import ConnectionEditSidebar from '../connections/components/ConnectionEditSidebar';
import {
  selectAllMetrics,
  selectMetricById,
  updateMetric,
  deleteMetric,
  fetchMetrics
} from '@/store/slices/metricsSlice.js';

import { selectAllConnections, updateConnection, fetchConnections} from '@/store/slices/connectionsSlice.js';

const ManageMetrics = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);
  const isLoading = useSelector(state => state.metrics.status === 'loading');
  const error = useSelector(state => state.metrics.error);

  const [searchParams, setSearchParams] = useSearchParams();
  const metricId = searchParams.get('metricId');
  const [selectedMetric, setSelectedMetric] = useState(null);
  const [selectedConnection, setSelectedConnection] = useState(null);

  useEffect(() => {
    dispatch(fetchMetrics());
    dispatch(fetchConnections());
  }, [dispatch]);

  useEffect(() => {
    if (metricId) {
      const metric = selectMetricById({ metrics }, metricId);
      setSelectedMetric(metric || null);
    } else {
      setSelectedMetric(null);
    }
  }, [metricId, metrics]);

  const handleEdit = (metric) => {
    setSearchParams({ metricId: metric.id });
  };

  const handleCloseSidebar = () => {
    setSearchParams({});
    setSelectedMetric(null);
    setSelectedConnection(null);
  };

  const handleUpdateMetricDetails = (updatedMetric) => {
    dispatch(updateMetric(updatedMetric));
    handleCloseSidebar();
  };

  const handleEditConnection = (connection) => {
    setSelectedConnection(connection);
    setSearchParams({ connectionId: connection.id });
  };

  const handleDeleteMetric = (metricId) => {
    dispatch(deleteMetric(metricId));
  };

  const handleUpdateConnection = (updatedConnection) => {
    dispatch(updateConnection(updatedConnection));
    setSelectedConnection(null);
  };

  const getConnectedMetric = (connection, currentMetricId) => {
    const connectedMetricId = connection.from_metric === currentMetricId ? connection.to_metric : connection.from_metric;
    return metrics.find(m => m.id === connectedMetricId);
  };

  if (isLoading) {
    return <div>Loading metrics data...</div>;
  }

  if (error) {
    return <div className="text-red-500">Error: {error}</div>;
  }

  if (!metrics || metrics.length === 0) {
    return <div>No metrics available.</div>;
  }

  return (
    <div className="flex">
      <div className="flex-1">
        <h2 className="text-2xl font-bold mb-6">Manage Metrics</h2>
        <MetricTable 
          metrics={metrics} 
          onEdit={handleEdit} 
          onDelete={handleDeleteMetric} 
          connections={connections}
        />
      </div>
      {selectedConnection && (
        <ConnectionEditSidebar
          connection={selectedConnection}
          onClose={() => setSelectedConnection(null)}
          onUpdate={handleUpdateConnection}
        />
      )}
    </div>
  );
};

export default ManageMetrics;