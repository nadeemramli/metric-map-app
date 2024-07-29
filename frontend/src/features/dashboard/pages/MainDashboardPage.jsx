import React from 'react';

const MainDashboardPage = ({ projectId }) => {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Main Dashboard</h1>
      <p>Project ID: {projectId}</p>
      <p>Dashboard content will be implemented later.</p>
    </div>
  );
};

export default MainDashboardPage;

/*
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Button } from "@/components/ui/button";
import { Loader2 } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { fetchMetrics } from '@/store/slices/metricsSlice';
import fetchExperiments from '@/store/slices/actionRemarksSlice';
import { fetchForecastsForAllMetrics } from '@/store/slices/forecastsSlice';

const MainDashboardPage = ({ projectId }) => {
  const dispatch = useDispatch();
  const metrics = useSelector(state => state.metrics.metrics);
  const experiments = useSelector(state => state.experiments.experiments);
  const forecasts = useSelector(state => state.forecasts.forecasts);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchDashboardData = async () => {
      setIsLoading(true);
      try {
        await Promise.all([
          dispatch(fetchMetrics(projectId)),
          dispatch(fetchExperiments(projectId)),
          dispatch(fetchForecastsForAllMetrics(projectId))
        ]);
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchDashboardData();
  }, [dispatch, projectId]);

  if (isLoading) {
    return <div className="flex justify-center items-center h-screen"><Loader2 className="h-8 w-8 animate-spin" /></div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Project Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
        <Card>
          <CardHeader>
            <CardTitle>Key Metrics</CardTitle>
          </CardHeader>
          <CardContent>
            {metrics.slice(0, 3).map(metric => (
              <div key={metric.id} className="mb-2">
                <p>{metric.name}: {metric.value}</p>
                <Progress value={metric.progress} className="w-full" />
              </div>
            ))}
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>
            <CardTitle>Active Experiments</CardTitle>
          </CardHeader>
          <CardContent>
            {experiments.slice(0, 3).map(experiment => (
              <div key={experiment.id} className="mb-2">
                <p>{experiment.name}</p>
                <Progress value={experiment.progress} className="w-full" />
              </div>
            ))}
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>
            <CardTitle>Quick Actions</CardTitle>
          </CardHeader>
          <CardContent>
            <Button className="w-full mb-2">Create New Metric</Button>
            <Button className="w-full mb-2">Start New Experiment</Button>
            <Button className="w-full">Generate Report</Button>
          </CardContent>
        </Card>
      </div>
      
      <Card>
        <CardHeader>
          <CardTitle>Metrics Forecast</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={forecasts}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              {metrics.slice(0, 3).map((metric, index) => (
                <Line 
                  key={metric.id} 
                  type="monotone" 
                  dataKey={metric.name} 
                  stroke={`hsl(${index * 120}, 70%, 50%)`} 
                />
              ))}
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
};

export default MainDashboardPage;
*/