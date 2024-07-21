import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { selectAllMetrics, fetchMetrics } from '@/store/slices/metricsSlice';
import { selectAllExperiments, fetchExperiments } from '@/store/slices/actionRemarksSlice';
import { fetchForecastsForAllMetrics, selectForecastsByMetricId } from '@/store/slices/forecastsSlice';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Loader2 } from 'lucide-react';

const ExperimentCard = ({ experiment }) => (
  <Card>
    <CardHeader>
      <CardTitle>{experiment.name}</CardTitle>
    </CardHeader>
    <CardContent>
      <p>Status: {experiment.status}</p>
      <p>Progress:</p>
      <Progress value={experiment.progress} className="w-full" />
    </CardContent>
  </Card>
);

const MetricUpdateCard = ({ metric }) => (
  <Card>
    <CardHeader>
      <CardTitle>{metric.name}</CardTitle>
    </CardHeader>
    <CardContent>
      <p>Current Value: {metric.currentValue}</p>
      <p>Last Updated: {new Date(metric.lastUpdated).toLocaleDateString()}</p>
    </CardContent>
  </Card>
);

const ForecastVsActualChart = ({ data }) => (
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

const MainDashboardPage = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const experiments = useSelector(selectAllExperiments);
  const forecasts = useSelector(state => selectForecastsByMetricId(state, metrics[0]?.id)); // Assuming we want forecasts for the first metric
  const currentClientId = useSelector(state => state.user.currentClientId);
  const currentProjectId = useSelector(state => state.projects.currentProjectId);
  const metricsStatus = useSelector(state => state.metrics.status);
  const experimentsStatus = useSelector(state => state.actionRemarks.experimentsStatus);
  const forecastsStatus = useSelector(state => state.forecasts.status);

  useEffect(() => {
    if (currentClientId && currentProjectId) {
      dispatch(fetchMetrics({ clientId: currentClientId, projectId: currentProjectId }));
      dispatch(fetchExperiments({ clientId: currentClientId, projectId: currentProjectId }));
      dispatch(fetchForecastsForAllMetrics({ clientId: currentClientId, projectId: currentProjectId }));
    }
  }, [dispatch, currentClientId, currentProjectId]);

  if (metricsStatus === 'loading' || experimentsStatus === 'loading' || forecastsStatus === 'loading') {
    return <div className="flex justify-center items-center h-screen"><Loader2 className="h-8 w-8 animate-spin" /></div>;
  }

  const forecastVsActualData = forecasts.map(forecast => ({
    date: forecast.date,
    actual: forecast.actualValue,
    forecast: forecast.forecastValue,
  }));

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <Card>
          <CardHeader>
            <CardTitle>Ongoing Experiments</CardTitle>
          </CardHeader>
          <CardContent>
            {experiments.map(experiment => (
              <ExperimentCard key={experiment.id} experiment={experiment} />
            ))}
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>
            <CardTitle>Recent Metric Updates</CardTitle>
          </CardHeader>
          <CardContent>
            {metrics.slice(0, 5).map(metric => (
              <MetricUpdateCard key={metric.id} metric={metric} />
            ))}
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Forecast vs Actual</CardTitle>
        </CardHeader>
        <CardContent>
          <ForecastVsActualChart data={forecastVsActualData} />
        </CardContent>
      </Card>
    </div>
  );
};

export default MainDashboardPage;