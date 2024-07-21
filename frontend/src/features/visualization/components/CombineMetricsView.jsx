import React, { useState, useMemo } from 'react';
import { useSelector } from 'react-redux';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import Select from 'react-select';
import { selectAllMetrics } from '../store/slices/metricsSlice';

const CombinedMetricsView = () => {
  const metrics = useSelector(selectAllMetrics);
  const [selectedMetrics, setSelectedMetrics] = useState([]);

  const options = useMemo(() => 
    metrics.map(metric => ({ value: metric.id, label: metric.name })),
    [metrics]
  );

  const combinedData = useMemo(() => {
    if (selectedMetrics.length === 0) return [];

    const baseMetric = metrics.find(m => m.id === selectedMetrics[0].value);
    if (!baseMetric) return [];

    return baseMetric.data.map((d, i) => ({
      date: d.date,
      ...selectedMetrics.reduce((acc, m) => {
        const metric = metrics.find(met => met.id === m.value);
        if (metric && metric.data[i]) {
          acc[m.label] = metric.data[i].value;
        }
        return acc;
      }, {})
    }));
  }, [selectedMetrics, metrics]);

  const colors = ['#8884d8', '#82ca9d', '#ffc658', '#ff7300', '#00C49F'];

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-4">Combined Metrics View</h2>
      <Select
        isMulti
        options={options}
        value={selectedMetrics}
        onChange={setSelectedMetrics}
        className="mb-4"
        placeholder="Select metrics to compare"
      />
      {combinedData.length > 0 ? (
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={combinedData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Legend />
            {selectedMetrics.map((metric, index) => (
              <Line
                key={metric.value}
                type="monotone"
                dataKey={metric.label}
                stroke={colors[index % colors.length]}
                dot={false}
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      ) : (
        <p className="text-center text-gray-500">Select metrics to view the chart</p>
      )}
    </div>
  );
};

export default CombinedMetricsView;