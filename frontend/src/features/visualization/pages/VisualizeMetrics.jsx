import React, { useState, useEffect, useMemo } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import MetricVisualization from './MetricVisualization.jsx';
import MetricDetailsPopup from '../../dashboard/pages/Dashboard.jsx'; 
import VisualizationCanvas from '../components/VisualizationCanvas.jsx';
import { selectAllMetrics, updateMetric } from '../../../store/slices/metricsSlice';
import { selectAllConnections, updateConnection, deleteConnection } from '../../../store/slices/connectionsSlice.js';

const VisualizeMetrics = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);
  const isLoading = useSelector(state => state.metrics.status === 'loading');

  const [selectedMetric, setSelectedMetric] = useState(null);
  const [selectedMetricsForCorrelation, setSelectedMetricsForCorrelation] = useState([]);
  const [correlations, setCorrelations] = useState({});

  useEffect(() => {
    calculateCorrelations();
  }, [metrics, connections]);

  const calculateCorrelations = () => {
    const newCorrelations = {};
    connections.forEach(conn => {
      const sourceMetric = metrics.find(m => m.id === conn.from);
      const targetMetric = metrics.find(m => m.id === conn.to);
      if (sourceMetric && targetMetric && sourceMetric.historicalData && targetMetric.historicalData) {
        const correlation = calculateCorrelationCoefficient(sourceMetric.historicalData, targetMetric.historicalData);
        newCorrelations[conn.id] = correlation;
      }
    });
    setCorrelations(newCorrelations);
  };

  const calculateCorrelationCoefficient = (dataA, dataB) => {
    // Implementation remains the same
    // ...
  };

  const handleMetricClick = (metric) => {
    setSelectedMetric(metric);
  };

  const handleMetricUpdate = (updatedMetric) => {
    dispatch(updateMetric(updatedMetric));
    setSelectedMetric(null);
  };

  const handleConnectionUpdate = (updatedConnection) => {
    dispatch(updateConnection(updatedConnection));
  };

  const handleConnectionRemove = (connectionId) => {
    dispatch(deleteConnection(connectionId));
  };

  const handleMetricSelectForCorrelation = (metric) => {
    setSelectedMetricsForCorrelation(prev => 
      prev.includes(metric) 
        ? prev.filter(m => m !== metric)
        : prev.length < 2 ? [...prev, metric] : [prev[1], metric]
    );
  };

  const connectionsWithCorrelations = useMemo(() => {
    return connections.map(conn => ({
      ...conn,
      correlation: correlations[conn.id] || 0
    }));
  }, [connections, correlations]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!metrics.length || !connections.length) {
    return <div>No data available to visualize.</div>;
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Visualize Metrics</h1>
      
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Metric Relationships</h2>
        <MetricVisualization 
          metrics={metrics} 
          connections={connectionsWithCorrelations}
          onMetricClick={handleMetricClick}
          onConnectionUpdate={handleConnectionUpdate}
          onConnectionRemove={handleConnectionRemove}
        />
        <VisualizationCanvas />
      </div>
      
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Correlation Analysis</h2>
        <div className="flex flex-wrap gap-2 mb-4">
          {metrics.map(metric => (
            <button
              key={metric.id}
              onClick={() => handleMetricSelectForCorrelation(metric)}
              className={`px-3 py-1 rounded ${
                selectedMetricsForCorrelation.includes(metric) 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-200'
              }`}
            >
              {metric.name}
            </button>
          ))}
        </div>
        {selectedMetricsForCorrelation.length === 2 && (
          <CorrelationAnalysis 
            metric1={selectedMetricsForCorrelation[0]} 
            metric2={selectedMetricsForCorrelation[1]} 
          />
        )}
      </div>
      
      {selectedMetric && (
        <MetricDetailsPopup
          metric={selectedMetric}
          onClose={() => setSelectedMetric(null)}
          onUpdate={handleMetricUpdate}
          connections={connections}
          metrics={metrics}
          addHistoricalData={(metricId, newData) => {
            const updatedMetric = {
              ...selectedMetric, 
              historicalData: [...(selectedMetric.historicalData || []), newData]
            };
            dispatch(updateMetric(updatedMetric));
          }}
        />
      )}
    </div>
  );
};

export default VisualizeMetrics;