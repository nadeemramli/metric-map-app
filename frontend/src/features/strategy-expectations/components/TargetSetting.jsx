import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { createTarget, updateTarget, deleteTarget } from '@/store/slices/targetsSlice';
import { toast } from 'react-toastify';

const TargetSetting = ({ metric, clientId, projectId }) => {
  const dispatch = useDispatch();
  const [newTarget, setNewTarget] = useState({ value: '', date: '', remarks: '' });

  const handleSetTarget = async () => {
    try {
      await dispatch(createTarget({ 
        clientId, 
        projectId, 
        metricId: metric.id, 
        targetData: newTarget 
      })).unwrap();
      setNewTarget({ value: '', date: '', remarks: '' });
      toast.success('Target set successfully');
    } catch (error) {
      toast.error(`Failed to set target: ${error.message}`);
    }
  };

  const handleUpdateTarget = async (targetId, updatedData) => {
    try {
      await dispatch(updateTarget({ 
        clientId, 
        projectId, 
        metricId: metric.id, 
        targetId, 
        targetData: updatedData 
      })).unwrap();
      toast.success('Target updated successfully');
    } catch (error) {
      toast.error(`Failed to update target: ${error.message}`);
    }
  };

  const handleDeleteTarget = async (targetId) => {
    try {
      await dispatch(deleteTarget({ 
        clientId, 
        projectId, 
        metricId: metric.id, 
        targetId 
      })).unwrap();
      toast.success('Target deleted successfully');
    } catch (error) {
      toast.error(`Failed to delete target: ${error.message}`);
    }
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle>Set Target</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-2">
          <Input
            type="number"
            placeholder="Target Value"
            value={newTarget.value}
            onChange={(e) => setNewTarget({ ...newTarget, value: e.target.value })}
          />
          <Input
            type="date"
            value={newTarget.date}
            onChange={(e) => setNewTarget({ ...newTarget, date: e.target.value })}
          />
          <Textarea
            placeholder="Remarks"
            value={newTarget.remarks}
            onChange={(e) => setNewTarget({ ...newTarget, remarks: e.target.value })}
          />
          <Button onClick={handleSetTarget}>Set Target</Button>
        </div>
        
        {metric.targets && metric.targets.map((target) => (
          <div key={target.id} className="mt-4 p-4 border rounded">
            <p>Value: {target.value}</p>
            <p>Date: {target.date}</p>
            <p>Remarks: {target.remarks}</p>
            <Button onClick={() => handleUpdateTarget(target.id, { ...target, value: target.value + 10 })}>
              Update Target
            </Button>
            <Button variant="destructive" onClick={() => handleDeleteTarget(target.id)}>
              Delete Target
            </Button>
          </div>
        ))}
      </CardContent>
    </Card>
  );
};

export default TargetSetting;