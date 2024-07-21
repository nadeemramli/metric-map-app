import React from 'react';
import { ArrowsRightLeftIcon, PencilIcon } from '../../../assets/icons/CustomIcons';

const MetricCard = ({ metric, connections, getConnectedMetric, onEditConnection }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 border border-gray-200 hover:shadow-lg transition-shadow duration-300">
      <h3 className="text-xl font-semibold mb-4 text-gray-800">{metric.name}</h3>
      {connections.length === 0 ? (
        <div className="text-gray-500 flex flex-col items-center justify-center h-24">
          <ArrowsRightLeftIcon className="h-8 w-8 mb-2" />
          <p>No connections yet</p>
        </div>
      ) : (
        <div className="space-y-3">
          {connections.map(connection => {
            const connectedMetric = getConnectedMetric(connection);
            return (
              <div key={connection.id} className="flex items-center justify-between bg-gray-50 p-2 rounded">
                <div className="flex items-center space-x-2">
                  <ArrowsRightLeftIcon className="h-5 w-5 text-gray-500" />
                  <span className="text-gray-700">{connectedMetric ? connectedMetric.name : 'Unknown Metric'}</span>
                </div>
                <button
                  onClick={() => onEditConnection(connection)}
                  className="text-blue-600 hover:text-blue-800"
                >
                  <PencilIcon className="h-5 w-5" />
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default MetricCard;