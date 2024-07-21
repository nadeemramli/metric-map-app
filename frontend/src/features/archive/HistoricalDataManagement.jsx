import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import {
  selectMetricById,
  addHistoricalData,
  addBulkHistoricalData,
  selectHistoricalDataByMetricId
} from '../../store/slices/metricsSlice';

const HistoricalDataManagement = () => {
  const { metricId } = useParams();
  const dispatch = useDispatch();
  
  const metric = useSelector(state => selectMetricById(state, metricId));
  const historicalData = useSelector(state => selectHistoricalDataByMetricId(state, metricId));
  const isLoading = useSelector(state => state.metrics.isLoading);
  const error = useSelector(state => state.metrics.error);

  const [newEntry, setNewEntry] = useState({
    date: '',
    value: '',
    forecasted_value: ''
  });
  const [bulkData, setBulkData] = useState('');

  useEffect(() => {
    dispatch(selectMetricById(metricId));
  }, [dispatch, metricId]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewEntry(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await dispatch(addHistoricalData({ metricId, data: newEntry })).unwrap();
      setNewEntry({ date: '', value: '', forecasted_value: '' });
    } catch (error) {
      console.error('Error adding historical data:', error);
    }
  };

  const handleBulkSubmit = async (e) => {
    e.preventDefault();
    const rows = bulkData.split('\n').map(row => {
      const [date, value, forecasted_value] = row.split('\t');
      return { date, value, forecasted_value };
    });
    try {
      await dispatch(addBulkHistoricalData({ metricId, data: rows })).unwrap();
      setBulkData('');
    } catch (error) {
      console.error('Error adding bulk historical data:', error);
    }
  };

  if (isLoading) return <div className="container mx-auto px-4 py-8">Loading...</div>;
  if (error) return <div className="container mx-auto px-4 py-8 text-red-500">{error}</div>;
  if (!metric) return <div className="container mx-auto px-4 py-8">Metric not found</div>;

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">{metric.name} - Historical Data</h1>
        <Link
          to={`/manage?metricId=${metricId}&openSidebar=true`}
          className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
          Back to Metric Details
        </Link>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <h2 className="text-xl font-semibold mb-4">Add New Entry</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">Date</label>
              <input
                type="date"
                name="date"
                value={newEntry.date}
                onChange={handleInputChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Value</label>
              <input
                type="number"
                name="value"
                value={newEntry.value}
                onChange={handleInputChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Forecasted Value (optional)</label>
              <input
                type="number"
                name="forecasted_value"
                value={newEntry.forecasted_value}
                onChange={handleInputChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </div>
            <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
              Add Entry
            </button>
          </form>
        </div>

        <div>
          <h2 className="text-xl font-semibold mb-4">Bulk Import</h2>
          <form onSubmit={handleBulkSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">
                Paste data (format: date\tvalue\tforecasted_value)
              </label>
              <textarea
                value={bulkData}
                onChange={(e) => setBulkData(e.target.value)}
                rows="10"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                placeholder="2023-01-01&#9;100&#9;110&#10;2023-01-02&#9;105&#9;115"/>
            </div>
            <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
              Import Bulk Data
            </button>
          </form>
        </div>
      </div>

      <div className="mt-12">
        <h2 className="text-2xl font-semibold mb-4">Historical Data</h2>
        {historicalData.length > 0 ? (
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Value</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Forecasted Value</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {historicalData.map((data, index) => (
                <tr key={index}>
                  <td className="px-6 py-4 whitespace-nowrap">{data.date}</td>
                  <td className="px-6 py-4 whitespace-nowrap">{data.value}</td>
                  <td className="px-6 py-4 whitespace-nowrap">{data.forecasted_value || '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>No historical data available.</p>
        )}
      </div>
    </div>
  );
};

export default HistoricalDataManagement;