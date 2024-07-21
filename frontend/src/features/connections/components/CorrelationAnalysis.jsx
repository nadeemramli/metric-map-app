import React from 'react';
import { calculateCorrelation } from '../utils/correlationAnalysis';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const CorrelationAnalysis = ({ metric1, metric2 }) => {
  const correlationData = metric1.data.map((d, i) => ({
    x: d.value,
    y: metric2.data[i].value,
  }));

  const correlationCoefficient = calculateCorrelation(
    metric1.data.map(d => d.value),
    metric2.data.map(d => d.value)
  );

  return (
    <div>
      <h3>Correlation Analysis</h3>
      <p>Correlation Coefficient: {correlationCoefficient.toFixed(2)}</p>
      <ResponsiveContainer width="100%" height={300}>
        <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
          <CartesianGrid />
          <XAxis type="number" dataKey="x" name={metric1.name} />
          <YAxis type="number" dataKey="y" name={metric2.name} />
          <Tooltip cursor={{ strokeDasharray: '3 3' }} />
          <Scatter name="Correlation" data={correlationData} fill="#8884d8" />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default CorrelationAnalysis;