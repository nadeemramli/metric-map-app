import React from 'react';

const EnhancedConnectionsTable = ({ connections, onViewDetails }) => {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">From Metric</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">To Metric</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Correlation Coefficient</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {connections.map((connection) => (
            <tr key={connection.id}>
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{connection.from_metric.name}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{connection.to_metric.name}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {connection.correlation_coefficient?.toFixed(2) || 'N/A'}
              </td>
              <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button
                  onClick={() => onViewDetails(connection)}
                  className="text-indigo-600 hover:text-indigo-900 bg-indigo-100 hover:bg-indigo-200 px-3 py-1 rounded-full transition duration-150 ease-in-out"
                >
                  View Details
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EnhancedConnectionsTable;