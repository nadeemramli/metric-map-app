import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const MetricDetails = ({ metric, onUpdate, onClose }) => {
  const [editedMetric, setEditedMetric] = useState(metric);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEditedMetric(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdate(editedMetric);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <Label htmlFor="name">Name</Label>
        <Input
          id="name"
          name="name"
          value={editedMetric.name}
          onChange={handleChange}
        />
      </div>
      <div>
        <Label htmlFor="description">Description</Label>
        <Input
          id="description"
          name="description"
          value={editedMetric.description}
          onChange={handleChange}
        />
      </div>
      <div>
        <Label htmlFor="type">Type</Label>
        <Input
          id="type"
          name="type"
          value={editedMetric.type}
          onChange={handleChange}
        />
      </div>
      <div className="flex justify-end space-x-2">
        <Button type="button" variant="outline" onClick={onClose}>Cancel</Button>
        <Button type="submit">Update Metric</Button>
      </div>
    </form>
  );
};

export default MetricDetails;