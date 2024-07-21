import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import PropTypes from 'prop-types';
import { XMarkIcon } from '../../../assets/icons/CustomIcons';
import { selectMetricById } from '@/store/slices/metricsSlice.js';
import {
  selectConnectionById,
  updateConnection
} from '@/store/slices/connectionsSlice.js';

const ConnectionEditSidebar = ({ connectionId, onClose }) => {
  const dispatch = useDispatch();
  const connection = useSelector(state => selectConnectionById(state, connectionId));
  const fromMetric = useSelector(state => selectMetricById(state, connection?.from_metric));
  const toMetric = useSelector(state => selectMetricById(state, connection?.to_metric));

  const [notes, setNotes] = useState('');
  const [relationship, setRelationship] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    if (connection) {
      setNotes(connection.notes || '');
      setRelationship(connection.relationship || '');
    } else {
      setError('Connection not found.');
    }
  }, [connection]);

  if (error) {
    return <div className="sidebar error">{error}</div>;
  }

  if (!connection) {
    return <div className="sidebar">Loading...</div>;
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await dispatch(updateConnection({
        id: connectionId,
        notes,
        relationship
      })).unwrap();
      onClose();
    } catch (err) {
      setError('Failed to update connection. Please try again.');
    }
  };

  return (
    <div className="fixed inset-y-0 right-0 w-96 bg-white shadow-lg p-6 overflow-auto z-50">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Edit Connection</h2>
        <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
          <XMarkIcon className="h-6 w-6" />
        </button>
      </div>
      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700">From Metric</label>
          <p className="mt-1 text-sm text-gray-500">{fromMetric ? fromMetric.name : 'Loading...'}</p>
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">To Metric</label>
          <p className="mt-1 text-sm text-gray-500">{toMetric ? toMetric.name : 'Loading...'}</p>
        </div>
        <div>
          <label htmlFor="relationship" className="block text-sm font-medium text-gray-700">Relationship</label>
          <input
            type="text"
            id="relationship"
            value={relationship}
            onChange={(e) => setRelationship(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          />
        </div>
        <div>
          <label htmlFor="notes" className="block text-sm font-medium text-gray-700">Notes</label>
          <textarea
            id="notes"
            rows={4}
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
        >
          Save Changes
        </button>
      </form>
    </div>
  );
};

ConnectionEditSidebar.propTypes = {
  connectionId: PropTypes.number.isRequired,
  onClose: PropTypes.func.isRequired,
};

export default ConnectionEditSidebar;