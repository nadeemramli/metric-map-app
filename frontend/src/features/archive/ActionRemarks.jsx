import React, { useState, useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { selectAllMetrics, selectMetricById } from '../../store/slices/metricsSlice';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine, ResponsiveContainer } from 'recharts';

const ActionRemarks = ({ metricId }) => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const selectedMetric = useSelector(state => selectMetricById(state, metricId));
  const actionRemarks = useSelector(state => selectActionRemarksByMetricId(state, metricId));

  const [newRemark, setNewRemark] = useState({ date: '', description: '' });

  const handleAddRemark = useCallback(() => {
    if (newRemark.date && newRemark.description) {
      dispatch(addActionRemark({ metricId, ...newRemark }));
      setNewRemark({ date: '', description: '' });
    }
  }, [dispatch, metricId, newRemark]);

  const chartData = selectedMetric
    ? selectedMetric.data.map(d => ({
        date: d.date,
        value: d.value,
        remarks: actionRemarks.filter(r => r.date === d.date),
      }))
    : [];

  return (
    <div className="p-4">
      <h3 className="text-lg font-semibold mb-2">Action Remarks</h3>
      <div className="mb-4">
        <input
          type="date"
          value={newRemark.date}
          onChange={(e) => setNewRemark({ ...newRemark, date: e.target.value })}
          className="mr-2 p-1 border rounded"
        />
        <input
          type="text"
          value={newRemark.description}
          onChange={(e) => setNewRemark({ ...newRemark, description: e.target.value })}
          placeholder="Remark description"
          className="mr-2 p-1 border rounded"
        />
        <button onClick={handleAddRemark} className="px-3 py-1 bg-blue-500 text-white rounded">Add</button>
      </div>
      <ul className="mb-4">
        {actionRemarks.map((remark, index) => (
          <li key={index} className="mb-1">
            {remark.date}: {remark.description}
          </li>
        ))}
      </ul>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={chartData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="value" stroke="#8884d8" />
          {chartData.map((entry, index) => 
            entry.remarks.map((remark, remarkIndex) => (
              <ReferenceLine
                key={`${index}-${remarkIndex}`}
                x={entry.date}
                stroke="red"
                label={{ value: remark.description, position: 'insideTopRight' }}
              />
            ))
          )}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default React.memo(ActionRemarks);