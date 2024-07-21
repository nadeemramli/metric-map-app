import React, { useState, useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { selectAllMetrics } from '@/store/slices/metricsSlice.js';
import { setTarget } from '@/store/slices/targetsSlice.js';


const ProgressTracking = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const [selectedMetric, setSelectedMetric] = useState(null);
  const [newTarget, setNewTarget] = useState('');

  const handleSetTarget = useCallback(() => {
    if (selectedMetric && newTarget) {
      dispatch(setTarget({ id: selectedMetric, target: parseFloat(newTarget) }));
      setNewTarget('');
    }
  }, [dispatch, selectedMetric, newTarget]);

  const calculateProgress = useCallback((metric) => {
    const latestValue = metric.data[metric.data.length - 1]?.value || 0;
    return metric.target ? (latestValue / metric.target) * 100 : 0;
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-4">Progress Tracking</h2>
      <div className="mb-4">
        <select 
          onChange={(e) => setSelectedMetric(e.target.value)}
          className="mr-2 p-2 border rounded"
        >
          <option value="">Select a metric</option>
          {metrics.map(metric => (
            <option key={metric.id} value={metric.id}>{metric.name}</option>
          ))}
        </select>
        <input
          type="number"
          value={newTarget}
          onChange={(e) => setNewTarget(e.target.value)}
          placeholder="New target"
          className="mr-2 p-2 border rounded"
        />
        <button onClick={handleSetTarget} className="p-2 bg-blue-500 text-white rounded">
          Set Target
        </button>
      </div>
      {metrics.map(metric => (
        <div key={metric.id} className="mb-2">
          <h3 className="text-lg font-semibold">{metric.name}</h3>
          <div className="w-full bg-gray-200 rounded-full h-2.5">
            <div 
              className="bg-blue-600 h-2.5 rounded-full" 
              style={{ width: `${calculateProgress(metric)}%` }}
            ></div>
          </div>
          <p>Progress: {calculateProgress(metric).toFixed(2)}%</p>
        </div>
      ))}
    </div>
  );
};

export default React.memo(ProgressTracking);