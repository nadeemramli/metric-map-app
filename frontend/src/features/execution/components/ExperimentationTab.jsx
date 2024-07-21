import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { 
  createActionRemark,
  createExperiment,
  selectActionRemarksByMetricId,
  selectExperimentsByMetricId
} from '@/store/slices/actionRemarksSlice';
import { toast } from 'react-toastify';

const ExperimentationTab = ({ metricId, clientId, projectId }) => {
  const dispatch = useDispatch();
  const actionRemarks = useSelector(state => selectActionRemarksByMetricId(state, metricId));
  const experiments = useSelector(state => selectExperimentsByMetricId(state, metricId));

  const [newActionRemark, setNewActionRemark] = useState({ description: '' });
  const [newExperiment, setNewExperiment] = useState({ name: '', hypothesis: '', targetImpact: '' });

  const handleAddActionRemark = async () => {
    try {
      await dispatch(createActionRemark({ 
        clientId, 
        projectId, 
        metricId, 
        remarkData: { ...newActionRemark, date: new Date().toISOString() } 
      })).unwrap();
      setNewActionRemark({ description: '' });
      toast.success('Action remark added successfully');
    } catch (error) {
      toast.error(`Failed to add action remark: ${error.message}`);
    }
  };

  const handleAddExperiment = async () => {
    try {
      await dispatch(createExperiment({ 
        clientId, 
        projectId, 
        metricId, 
        experimentData: newExperiment 
      })).unwrap();
      setNewExperiment({ name: '', hypothesis: '', targetImpact: '' });
      toast.success('Experiment added successfully');
    } catch (error) {
      toast.error(`Failed to add experiment: ${error.message}`);
    }
  };

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle>Action Remarks</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-2">
            <Textarea
              placeholder="Action remark"
              value={newActionRemark.description}
              onChange={(e) => setNewActionRemark({ ...newActionRemark, description: e.target.value })}
            />
            <Button onClick={handleAddActionRemark}>Add Action Remark</Button>
          </div>
          <ul className="mt-4">
            {actionRemarks.map(remark => (
              <li key={remark.id} className="mb-2">{new Date(remark.date).toLocaleDateString()}: {remark.description}</li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Experiments</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-2">
            <Input
              placeholder="Experiment name"
              value={newExperiment.name}
              onChange={(e) => setNewExperiment({ ...newExperiment, name: e.target.value })}
            />
            <Textarea
              placeholder="Hypothesis"
              value={newExperiment.hypothesis}
              onChange={(e) => setNewExperiment({ ...newExperiment, hypothesis: e.target.value })}
            />
            <Input
              placeholder="Target impact"
              value={newExperiment.targetImpact}
              onChange={(e) => setNewExperiment({ ...newExperiment, targetImpact: e.target.value })}
            />
            <Button onClick={handleAddExperiment}>Add Experiment</Button>
          </div>
          <ul className="mt-4">
            {experiments.map(exp => (
              <li key={exp.id} className="mb-2">{exp.name}: {exp.hypothesis} (Target Impact: {exp.targetImpact})</li>
            ))}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
};

export default ExperimentationTab;