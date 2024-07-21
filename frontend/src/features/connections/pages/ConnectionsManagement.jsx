import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import MetricCard from '../../visualization/components/MetricCard.jsx';
import ConnectionEditSidebar from '../components/ConnectionEditSidebar.jsx';
import EnhancedConnectionsTable from '../components/EnhancedConnectionsTable.jsx';
import { selectAllMetrics, fetchMetricsAndConnections } from '../../../store/slices/metricsSlice';
import { selectAllConnections, updateConnection } from '../../../store/slices/connectionsSlice.js'; 

const ConnectionsManagement = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);

  const [selectedConnection, setSelectedConnection] = useState(null);
  const [selectedMetrics, setSelectedMetrics] = useState([]);

  useEffect(() => {
    loadData();
  }, [dispatch]);

  const loadData = async () => {
    try {
      await dispatch(fetchMetricsAndConnections()).unwrap();
      console.log('Fetched Metrics:', metrics);
      console.log('Fetched Connections:', connections);
    } catch (error) {
      console.error('Error loading data:', error);
    }
  };

  const handleUpdateConnection = async (connectionId, updatedData) => {
    try {
      await dispatch(updateConnection({ id: connectionId, ...updatedData })).unwrap();
      setSelectedConnection(null);
    } catch (error) {
      console.error('Error updating connection:', error);
    }
  };

  const getConnectedMetric = (connection, currentMetricId) => {
    const connectedMetricId = connection.from_metric === currentMetricId ? connection.to_metric : connection.from_metric;
    return metrics.find(m => m.id === connectedMetricId);
  };

  const handleMetricSelect = (metric) => {
    setSelectedMetrics(prev => 
      prev.includes(metric) 
        ? prev.filter(m => m !== metric)
        : prev.length < 2 ? [...prev, metric] : [prev[1], metric]
    );
  };

  return (
    <div className="min-h-screen bg-gray-200 p-8 relative">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">Metric Connections</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {metrics.map(metric => {
          const metricConnections = connections.filter(conn => 
            conn.from_metric === metric.id || conn.to_metric === metric.id
          );
          console.log(`Connections for metric ${metric.name}:`, metricConnections);
          return (
            <MetricCard
              key={metric.id}
              metric={metric}
              connections={metricConnections}
              getConnectedMetric={(conn) => getConnectedMetric(conn, metric.id)}
              onEditConnection={setSelectedConnection}
            />
          );
        })}
      </div>
      {selectedConnection && (
        <ConnectionEditSidebar
          connection={selectedConnection}
          fromMetric={metrics.find(m => m.id === selectedConnection.from_metric)}
          toMetric={metrics.find(m => m.id === selectedConnection.to_metric)}
          onClose={() => setSelectedConnection(null)}
          onUpdate={handleUpdateConnection}
        />
      )}
      
      <div className="mt-8">
        <h2 className="text-2xl font-bold mb-4">Connections Table</h2>
        <EnhancedConnectionsTable />
      </div>

      <div className="mt-8">
        <h2 className="text-xl font-semibold mb-2">Correlation Analysis</h2>
        <div className="flex space-x-4 mb-2">
          {metrics.map(metric => (
            <button
              key={metric.id}
              onClick={() => handleMetricSelect(metric)}
              className={`px-3 py-1 rounded ${
                selectedMetrics.includes(metric) 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-200'
              }`}
            >
              {metric.name}
            </button>
          ))}
        </div>
        {selectedMetrics.length === 2 && (
          <CorrelationAnalysis 
            metric1={selectedMetrics[0]} 
            metric2={selectedMetrics[1]} 
          />
        )}
      </div>
    </div>
  );
};

export default ConnectionsManagement;