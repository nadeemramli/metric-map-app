import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { selectAllMetrics } from '@/store/slices/metricsSlice';
import { selectAllConnections } from '@/store/slices/connectionsSlice';
import MetricCard from '@/features/visualization/components/MetricCard.jsx';

const Dashboard = () => {
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);
  const loading = useSelector(state => state.metrics.status === 'loading');
  const error = useSelector(state => state.metrics.error);

  const [selectedMetric, setSelectedMetric] = useState(null);

  const handleMetricClick = (metric) => {
    setSelectedMetric(metric);
  };

  const handleCloseSidebar = () => {
    setSelectedMetric(null);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="dashboard flex h-screen">
      <div className="flex-1 p-6">
        <h1 className="text-2xl font-bold mb-4">Metrics Dashboard</h1>
        <div className="metric-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {metrics.map(metric => (
            <MetricCard 
              key={metric.id} 
              metric={metric} 
              onClick={() => handleMetricClick(metric)}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;