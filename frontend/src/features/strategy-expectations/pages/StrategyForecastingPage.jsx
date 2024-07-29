import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { LineChart, Line, BarChart, Bar, PieChart, Pie, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { fetchMetrics, selectAllMetrics, selectInsightsByMetricId } from '@/store/slices/metricsSlice';
import { selectAllConnections, fetchMetricConnections } from '@/store/slices/connectionsSlice';
import { selectActionRemarksByMetricId, fetchActionRemarks } from '@/store/slices/actionRemarksSlice';

const ChartTypes = {
  LINE: 'line',
  BAR: 'bar',
  PIE: 'pie',
};

const StrategyForecastingPage = () => {
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);
  const [selectedMetric, setSelectedMetric] = useState(metrics[0]?.id);
  const [chartType, setChartType] = useState(ChartTypes.LINE);

  const metric = metrics.find(m => m.id === selectedMetric);
  const actionRemarks = useSelector(state => selectActionRemarksByMetricId(state, selectedMetric));
  const insights = useSelector(state => selectInsightsByMetricId(state, selectedMetric));

  useEffect(() => {
    dispatch(fetchMetrics({ clientId, projectId }));
    dispatch(fetchMetricConnections({ clientId, projectId }));
    dispatch(fetchActionRemarks({ clientId, projectId }));
  }, [dispatch, clientId, projectId]);

  const renderChart = () => {
    if (!metric) return null;

    const data = metric.historicalData.map(d => ({
      date: d.date,
      actual: d.value,
      forecast: d.forecastedValue,
    }));

    if (metricStatus === 'loading' || connectionStatus === 'loading') {
      return <div className="flex justify-center items-center h-screen"><Loader2 className="h-8 w-8 animate-spin" /></div>;
    }
    
    if (metricError || connectionError) {
      return <div>Error: {metricError || connectionError}</div>;
    }

    switch (chartType) {
      case ChartTypes.LINE:
        return (
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="actual" stroke="#8884d8" />
              <Line type="monotone" dataKey="forecast" stroke="#82ca9d" />
            </LineChart>
          </ResponsiveContainer>
        );
      case ChartTypes.BAR:
        return (
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="actual" fill="#8884d8" />
              <Bar dataKey="forecast" fill="#82ca9d" />
            </BarChart>
          </ResponsiveContainer>
        );
      case ChartTypes.PIE:
        const pieData = [
          { name: 'Actual', value: data[data.length - 1]?.actual },
          { name: 'Forecast', value: data[data.length - 1]?.forecast },
        ];
        return (
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie data={pieData} dataKey="value" nameKey="name" fill="#8884d8" label />
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        );
      default:
        return null;
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Strategy and Forecasting</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
        <Select value={selectedMetric} onValueChange={setSelectedMetric}>
          <SelectTrigger>
            <SelectValue placeholder="Select a metric" />
          </SelectTrigger>
          <SelectContent>
            {metrics.map(metric => (
              <SelectItem key={metric.id} value={metric.id}>{metric.name}</SelectItem>
            ))}
          </SelectContent>
        </Select>

        <Select value={chartType} onValueChange={setChartType}>
          <SelectTrigger>
            <SelectValue placeholder="Select chart type" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value={ChartTypes.LINE}>Line Chart</SelectItem>
            <SelectItem value={ChartTypes.BAR}>Bar Chart</SelectItem>
            <SelectItem value={ChartTypes.PIE}>Pie Chart</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <Card className="mb-4">
        <CardHeader>
          <CardTitle>{metric?.name} - Performance</CardTitle>
        </CardHeader>
        <CardContent>
          {renderChart()}
        </CardContent>
      </Card>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardHeader>
            <CardTitle>Connected Metrics</CardTitle>
          </CardHeader>
          <CardContent>
            <ul>
              {connections
                .filter(conn => conn.fromMetric === selectedMetric || conn.toMetric === selectedMetric)
                .map(conn => {
                  const connectedMetric = metrics.find(m => m.id === (conn.fromMetric === selectedMetric ? conn.toMetric : conn.fromMetric));
                  return (
                    <li key={conn.id}>
                      {connectedMetric.name} - {conn.relationship}
                    </li>
                  );
                })
              }
            </ul>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Action Remarks</CardTitle>
          </CardHeader>
          <CardContent>
            <ul>
              {actionRemarks.map(remark => (
                <li key={remark.id}>{remark.date}: {remark.description}</li>
              ))}
            </ul>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Insights</CardTitle>
          </CardHeader>
          <CardContent>
            <ul>
              {insights.map(insight => (
                <li key={insight.id}>{insight.date}: {insight.description}</li>
              ))}
            </ul>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default StrategyForecastingPage;