import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { selectMetricById, fetchMetrics, addHistoricalData, fetchHistoricalData, selectHistoricalDataByMetricId } from '@/store/slices/metricsSlice';
import { toast } from 'react-toastify';
import { Loader2 } from 'lucide-react';

const HistoricalDataManagementPage = () => {
  const { metricId } = useParams();
  const dispatch = useDispatch();
  const metric = useSelector(state => selectMetricById(state, metricId));
  const historicalData = useSelector(state => selectHistoricalDataByMetricId(state, metricId));
  const status = useSelector(state => state.historicalData.status);
  const error = useSelector(state => state.historicalData.error);
  const [newDataPoint, setNewDataPoint] = useState({ date: '', value: '' });

  const currentClientId = useSelector(state => state.user.currentClientId);
  const currentProjectId = useSelector(state => state.projects.currentProjectId);

  useEffect(() => {
    if (currentClientId && currentProjectId && metricId) {
      dispatch(fetchMetrics({ clientId: currentClientId, projectId: currentProjectId, metricId }));
      dispatch(fetchHistoricalData({ clientId: currentClientId, projectId: currentProjectId, metricId }));
    }
  }, [dispatch, currentClientId, currentProjectId, metricId]);

  const handleAddDataPoint = async (e) => {
    e.preventDefault();
    try {
      await dispatch(addHistoricalData({ 
        clientId: currentClientId, 
        projectId: currentProjectId, 
        metricId, 
        data: newDataPoint 
      })).unwrap();
      setNewDataPoint({ date: '', value: '' });
      toast.success('Data point added successfully');
    } catch (err) {
      toast.error(`Failed to add data point: ${err.message}`);
    }
  };

  if (status === 'loading') {
    return <div className="flex justify-center items-center h-screen"><Loader2 className="h-8 w-8 animate-spin" /></div>;
  }

  if (error) {
    return <div className="text-red-500">Error: {error}</div>;
  }

  if (!metric) return <div>Metric not found</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">{metric.name} - Historical Data</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardHeader>
            <CardTitle>Data Visualization</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={historicalData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="value" stroke="#8884d8" />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Add New Data Point</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleAddDataPoint} className="space-y-4">
              <div>
                <Label htmlFor="date">Date</Label>
                <Input
                  id="date"
                  type="date"
                  value={newDataPoint.date}
                  onChange={(e) => setNewDataPoint({...newDataPoint, date: e.target.value})}
                />
              </div>
              <div>
                <Label htmlFor="value">Value</Label>
                <Input
                  id="value"
                  type="number"
                  value={newDataPoint.value}
                  onChange={(e) => setNewDataPoint({...newDataPoint, value: e.target.value})}
                />
              </div>
              <Button type="submit">Add Data Point</Button>
            </form>
          </CardContent>
        </Card>
      </div>

      <Card className="mt-4">
        <CardHeader>
          <CardTitle>Historical Data</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Date</TableHead>
                <TableHead>Value</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {historicalData.map((dataPoint, index) => (
                <TableRow key={index}>
                  <TableCell>{dataPoint.date}</TableCell>
                  <TableCell>{dataPoint.value}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
};

export default HistoricalDataManagementPage;