import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Calendar } from "@/components/ui/calendar";
import { selectAllMetrics, fetchMetrics } from '@/store/slices/metricsSlice';
import { createActionRemark, createExperiment, fetchActionRemarks, fetchExperiments } from '@/store/slices/actionRemarksSlice';
import { toast } from 'react-toastify';

const ExecutionPage = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const [selectedDate, setSelectedDate] = useState(new Date());

  // States for different forms
  const [experiment, setExperiment] = useState({ name: '', hypothesis: '', metricId: '', targetImpact: '' });
  const [actionRemark, setActionRemark] = useState({ date: '', description: '', metricId: '' });

  useEffect(() => {
    dispatch(fetchMetrics());
    dispatch(fetchActionRemarks());
    dispatch(fetchExperiments());
  }, [dispatch]);

  const handleCreateExperiment = async () => {
    try {
      await dispatch(createExperiment({ clientId, projectId, experimentData: experiment })).unwrap();
      setExperiment({ name: '', hypothesis: '', metricId: '', targetImpact: '' });
      toast.success('Experiment created successfully');
    } catch (error) {
      toast.error(`Failed to create experiment: ${error.message}`);
    }
  };

  const handleCreateActionRemark = async () => {
    try {
      await dispatch(createActionRemark({ clientId, projectId, metricId: actionRemark.metricId, remarkData: { ...actionRemark, date: selectedDate } })).unwrap();
      setActionRemark({ date: '', description: '', metricId: '' });
      toast.success('Action remark created successfully');
    } catch (error) {
      toast.error(`Failed to create action remark: ${error.message}`);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Execution Dashboard</h1>

      <Tabs defaultValue="experiments">
        <TabsList>
          <TabsTrigger value="experiments">Experiments</TabsTrigger>
          <TabsTrigger value="actionRemarks">Action Remarks</TabsTrigger>
        </TabsList>

        <TabsContent value="experiments">
          <Card>
            <CardHeader>
              <CardTitle>Experiment Management</CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={(e) => { e.preventDefault(); handleCreateExperiment(); }} className="space-y-4">
                <Input
                  placeholder="Experiment name"
                  value={experiment.name}
                  onChange={(e) => setExperiment({ ...experiment, name: e.target.value })}
                />
                <Textarea
                  placeholder="Hypothesis"
                  value={experiment.hypothesis}
                  onChange={(e) => setExperiment({ ...experiment, hypothesis: e.target.value })}
                />
                <Select
                  value={experiment.metricId}
                  onValueChange={(value) => setExperiment({ ...experiment, metricId: value })}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Related Metric" />
                  </SelectTrigger>
                  <SelectContent>
                    {metrics.map(metric => (
                      <SelectItem key={metric.id} value={metric.id}>{metric.name}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
                <Input
                  placeholder="Target Impact"
                  value={experiment.targetImpact}
                  onChange={(e) => setExperiment({ ...experiment, targetImpact: e.target.value })}
                />
                <Button type="submit">Create Experiment</Button>
              </form>
              {/* Experiment list would go here */}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="actionRemarks">
          <Card>
            <CardHeader>
              <CardTitle>Action Remarks</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <Calendar
                    mode="single"
                    selected={selectedDate}
                    onSelect={setSelectedDate}
                    className="rounded-md border"
                  />
                </div>
                <div>
                  <form onSubmit={(e) => { e.preventDefault(); handleCreateActionRemark(); }} className="space-y-4">
                    <Textarea
                      placeholder="Action Remark"
                      value={actionRemark.description}
                      onChange={(e) => setActionRemark({ ...actionRemark, description: e.target.value })}
                    />
                    <Select
                      value={actionRemark.metricId}
                      onValueChange={(value) => setActionRemark({ ...actionRemark, metricId: value })}
                    >
                      <SelectTrigger>
                        <SelectValue placeholder="Related Metric" />
                      </SelectTrigger>
                      <SelectContent>
                        {metrics.map(metric => (
                          <SelectItem key={metric.id} value={metric.id}>{metric.name}</SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    <Button type="submit">Create Action Remark</Button>
                  </form>
                </div>
              </div>
              {/* Action Remarks list would go here */}
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
};

export default ExecutionPage;