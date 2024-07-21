// src/components/CustomizableChart.jsx
import React, { useState } from 'react';
import { LineChart, Line, BarChart, Bar, AreaChart, Area, PieChart, Pie, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const chartTypes = ['Line', 'Bar', 'Area', 'Pie'];
const colorSchemes = ['Default', 'Pastel', 'Vibrant', 'Monochrome'];

const CustomizableChart = ({ data, dataKeys }) => {
  const [chartType, setChartType] = useState('Line');
  const [colorScheme, setColorScheme] = useState('Default');

  const getColors = (scheme) => {
    switch(scheme) {
      case 'Pastel': return ['#FFB3BA', '#BAFFC9', '#BAE1FF', '#FFFFBA'];
      case 'Vibrant': return ['#FF1493', '#00FF00', '#1E90FF', '#FFD700'];
      case 'Monochrome': return ['#000000', '#404040', '#808080', '#C0C0C0'];
      default: return ['#8884d8', '#82ca9d', '#ffc658', '#ff7300'];
    }
  };

  const renderChart = () => {
    const colors = getColors(colorScheme);

    switch(chartType) {
      case 'Bar':
        return (
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            {dataKeys.map((key, index) => (
              <Bar key={key} dataKey={key} fill={colors[index % colors.length]} />
            ))}
          </BarChart>
        );
      case 'Area':
        return (
          <AreaChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            {dataKeys.map((key, index) => (
              <Area key={key} type="monotone" dataKey={key} fill={colors[index % colors.length]} stroke={colors[index % colors.length]} />
            ))}
          </AreaChart>
        );
      case 'Pie':
        return (
          <PieChart>
            <Pie data={data} dataKey={dataKeys[0]} nameKey="name" fill="#8884d8" label />
            <Tooltip />
          </PieChart>
        );
      default:
        return (
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            {dataKeys.map((key, index) => (
              <Line key={key} type="monotone" dataKey={key} stroke={colors[index % colors.length]} />
            ))}
          </LineChart>
        );
    }
  };

  return (
    <div>
      <div>
        <select value={chartType} onChange={(e) => setChartType(e.target.value)}>
          {chartTypes.map(type => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>
        <select value={colorScheme} onChange={(e) => setColorScheme(e.target.value)}>
          {colorSchemes.map(scheme => (
            <option key={scheme} value={scheme}>{scheme}</option>
          ))}
        </select>
      </div>
      <ResponsiveContainer width="100%" height={400}>
        {renderChart()}
      </ResponsiveContainer>
    </div>
  );
};

export default CustomizableChart;