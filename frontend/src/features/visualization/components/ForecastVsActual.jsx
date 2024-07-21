// src/components/ForecastVsActual.jsx
import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import Select from 'react-select';

const ForecastVsActual = () => {
  const metrics = useSelector(state => state.metrics);
  const [selectedMetric, setSelectedMetric] = useState(null);

  const options = metrics.map(metric => ({ value: metric.id, label: metric.name }));

  const chartData = selectedMetric
    ? metrics.find(m => m.id === selectedMetric.value).data.map(d => ({
        date: d.date,
        actual: d.value,
        forecast: d.forecastedValue,
      }))
    : [];

  return (
    <div>
      <h2>Forecast vs Actual Analysis</h2>
      <Select
        options={options}
        value={selectedMetric}
        onChange={setSelectedMetric}
        placeholder="Select a metric"
      />
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={chartData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="actual" stroke="#8884d8" name="Actual" />
          <Line type="monotone" dataKey="forecast" stroke="#82ca9d" name="Forecast" strokeDasharray="5 5" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ForecastVsActual;