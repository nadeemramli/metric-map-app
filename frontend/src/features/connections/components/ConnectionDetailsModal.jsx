import React, { useState } from 'react';
import { useMetrics } from '../contexts/MetricsContext';

const ConnectionDetailsModal = ({ connectionId, onClose }) => {
  const { getConnectionById, updateConnection } = useMetrics();
  const connection = getConnectionById(connectionId);
  const [notes, setNotes] = useState(connection.notes || '');

  const handleSubmit = (e) => {
    e.preventDefault();
    updateConnection(connectionId, { notes });
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-lg w-1/2">
        <h2 className="text-xl font-semibold mb-4">Connection Details</h2>
        <p><strong>From:</strong> {connection.from_metric.name}</p>
        <p><strong>To:</strong> {connection.to_metric.name}</p>
        <p><strong>Correlation:</strong> {connection.correlation_coefficient?.toFixed(2) || 'N/A'}</p>
        <form onSubmit={handleSubmit}>
          <label className="block mt-4">
            Notes:
            <textarea
              className="w-full border rounded p-2 mt-1"
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              rows="4"
            />
          </label>
          <div className="flex justify-end mt-4">
            <button type="button" onClick={onClose} className="mr-2 px-4 py-2 border rounded">Cancel</button>
            <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded">Save</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ConnectionDetailsModal;