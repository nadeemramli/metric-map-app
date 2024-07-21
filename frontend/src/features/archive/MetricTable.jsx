import React, { useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Edit, Trash2 } from 'lucide-react';
import { selectAllMetrics, deleteMetric } from '@/store/slices/metricsSlice.js';
import { selectAllConnections } from '@/store/slices/connectionsSlice.js';

const MetricTable = ({ onEdit }) => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);

  const getConnectedMetrics = useCallback((metricId) => {
    const connectedIds = connections
      .filter(conn => conn.from === metricId || conn.to === metricId)
      .map(conn => conn.from === metricId ? conn.to : conn.from);
    return metrics.filter(m => connectedIds.includes(m.id));
  }, [connections, metrics]);

  const handleDelete = useCallback((id) => {
    dispatch(deleteMetric(id));
  }, [dispatch]);

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white">
        <thead>
          <tr className="bg-gray-100 text-gray-600 uppercase text-sm leading-normal">
            <th className="py-3 px-6 text-left">Name</th>
            <th className="py-3 px-6 text-left">Type</th>
            <th className="py-3 px-6 text-left">Confidence</th>
            <th className="py-3 px-6 text-left">Description</th>
            <th className="py-3 px-6 text-left">Hypothesis/Goal</th>
            <th className="py-3 px-6 text-left">Results</th>
            <th className="py-3 px-6 text-left">Connections</th>
            <th className="py-3 px-6 text-left">Actions</th>
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {metrics.map((metric) => (
            <tr key={metric.id} className="border-b border-gray-200 hover:bg-gray-100">
              <td className="py-3 px-6 text-left whitespace-nowrap">{metric.name}</td>
              <td className="py-3 px-6 text-left">{metric.type}</td>
              <td className="py-3 px-6 text-left">{metric.confidence}</td>
              <td className="py-3 px-6 text-left">{metric.description}</td>
              <td className="py-3 px-6 text-left">{metric.hypothesis}</td>
              <td className="py-3 px-6 text-left">{`${metric.results} ${metric.resultType}`}</td>
              <td className="py-3 px-6 text-left">{getConnectedMetrics(metric.id).map(m => m.name).join(', ')}</td>
              <td className="py-3 px-6 text-left">
                <button onClick={() => onEdit(metric)} className="text-blue-600 hover:text-blue-900 mr-2">
                  <Edit size={18} />
                </button>
                <button onClick={() => handleDelete(metric.id)} className="text-red-600 hover:text-red-900">
                  <Trash2 size={18} />
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default React.memo(MetricTable);