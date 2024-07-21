import React, { useState, useCallback } from 'react';
import { useDispatch } from 'react-redux';
import { addHistoricalData } from '../store/slices/metricsSlice';

const HistoricalDataInput = ({ metricId }) => {
  const dispatch = useDispatch();
  const [date, setDate] = useState('');
  const [value, setValue] = useState('');
  const [forecastedValue, setForecastedValue] = useState('');
  const [bulkData, setBulkData] = useState('');

  const handleSubmit = useCallback(async (e) => {
    e.preventDefault();
    const newData = {
      date,
      value: parseFloat(value),
      forecasted_value: forecastedValue ? parseFloat(forecastedValue) : null
    };
    await dispatch(addHistoricalData({ metricId, data: newData }));
    setDate('');
    setValue('');
    setForecastedValue('');
  }, [dispatch, metricId, date, value, forecastedValue]);

  const handleBulkSubmit = useCallback(async (e) => {
    e.preventDefault();
    const rows = bulkData.split('\n').map(row => row.split('\t'));
    const bulkDataArray = rows.map(([date, value, forecastedValue]) => ({
      date,
      value: parseFloat(value),
      forecasted_value: forecastedValue ? parseFloat(forecastedValue) : null
    }));
    await dispatch(addHistoricalData({ metricId, data: bulkDataArray }));
    setBulkData('');
  }, [dispatch, metricId, bulkData]);

  return (
    <div className="space-y-4">
      <form onSubmit={handleSubmit} className="space-y-2">
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          required
          className="w-full p-2 border rounded"
        />
        <input
          type="number"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder="Value"
          required
          className="w-full p-2 border rounded"
        />
        <input
          type="number"
          value={forecastedValue}
          onChange={(e) => setForecastedValue(e.target.value)}
          placeholder="Forecasted Value (optional)"
          className="w-full p-2 border rounded"
        />
        <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded">Add Data</button>
      </form>

      <form onSubmit={handleBulkSubmit} className="space-y-2">
        <textarea
          value={bulkData}
          onChange={(e) => setBulkData(e.target.value)}
          placeholder="Paste spreadsheet data here (date, value, forecasted_value)"
          className="w-full p-2 border rounded"
          rows="5"
        />
        <button type="submit" className="w-full p-2 bg-green-500 text-white rounded">Add Bulk Data</button>
      </form>
    </div>
  );
};

export default React.memo(HistoricalDataInput);