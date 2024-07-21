import React from 'react';
import { useMetrics } from '../contexts/MetricsContext';

const Connections = () => {
  const { metrics, connections, addConnection, removeConnection } = useMetrics();

  const handleConnectionChange = (fromId, toId, isChecked) => {
    if (isChecked) {
      addConnection(fromId, toId);
    } else {
      removeConnection(fromId, toId);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">Manage Connections</h3>
      <table className="w-full">
        <thead>
          <tr>
            <th className="text-left">Metric</th>
            {metrics.map(m => (
              <th key={m.id} className="text-center">{m.name}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {metrics.map(fromMetric => (
              <tr key={fromMetric.id}>
                <td className="font-medium">{fromMetric.name}</td>
                {metrics.map(toMetric => (
                  <td key={toMetric.id} className="text-center">
                    {fromMetric.id !== toMetric.id && (
                      <input
                        type="checkbox"
                        checked={connections.some(
                          conn => 
                            (conn.from === fromMetric.id && conn.to === toMetric.id) ||
                            (conn.from === toMetric.id && conn.to === fromMetric.id)
                        )}
                        onChange={(e) => handleConnectionChange(fromMetric.id, toMetric.id, e.target.checked)}
                        className="form-checkbox text-blue-600"
                      />
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Connections;