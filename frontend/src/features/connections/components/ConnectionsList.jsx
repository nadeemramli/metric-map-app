import React from 'react';
import { ArrowsRightLeftIcon, XMarkIcon } from '../../../assets/icons/CustomIcons';

const ConnectionsList = ({ connections, availableMetrics, onAddConnection, onRemoveConnection }) => {
  // Use empty arrays as defaults directly in the parameter destructuring to ensure they are always arrays
  connections = connections || [];
  availableMetrics = availableMetrics || [];

  console.log("Available Metrics:", availableMetrics);

  return (
    <div className="space-y-2">
      {connections.map((connection) => (
        // Ensure the key is a unique identifier
        <div key={connection.id} className="flex items-center justify-between bg-gray-50 p-2 rounded">
          <div className="flex items-center space-x-2">
            <ArrowsRightLeftIcon className="h-5 w-5 text-gray-500" />
            <span className="text-gray-700">{connection.name}</span>
          </div>
          <button
            onClick={() => onRemoveConnection(connection.id)}
            className="text-red-600 hover:text-red-800">
            <XMarkIcon className="h-5 w-5" />
          </button>
        </div>
      ))}
      <div className="mt-2">
        <select
          onChange={(e) => {
            const value = parseInt(e.target.value, 10);
            if (value) {
              onAddConnection(value);
            }
          }}
          className="w-full p-2 border rounded"
        >
          <option value="">Add a connection</option>
          {availableMetrics.map((metric) => (
            // Make sure metric.name is a string. Adjust the following line if metric.name is structured differently.
            <option key={metric.id} value={metric.id}>{metric.name.toString()}</option>
          ))}
        </select>
      </div>
    </div>
  );
};

export default ConnectionsList;
