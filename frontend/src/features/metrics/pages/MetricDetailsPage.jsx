import React, { useState, useEffect, useCallback } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { 
  selectMetricById, 
  createMetric, 
  updateMetric,
  selectAllMetrics,
  updateMetricPosition, 
} from '@/store/slices/metricsSlice';
import { selectAllConnections, createConnection, deleteConnection } from '@/store/slices/connectionsSlice';
import { selectAllTags, createTag } from '@/store/slices/tagsSlice';
import { selectAllCategories, createCategory } from '@/store/slices/categoriesSlice';
import { createTarget, updateTarget, deleteTarget } from '@/store/slices/targetsSlice';
import { 
  selectActionRemarksByMetricId, 
  selectExperimentsByMetricId,
  createActionRemark,
  createExperiment
} from '@/store/slices/actionRemarksSlice';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Calendar } from "@/components/ui/calendar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import CreatableSelect from 'react-select/creatable';
import { toast } from 'react-toastify';
import TargetSetting from '../../strategy-expectations/components/TargetSetting';
import ExperimentationTab from '../../execution/components/ExperimentationTab';
import ConnectionsVisualizer from '../../connections/components/ConnectionsVisualizer';

const MetricDetailsPage = () => {
  const { metricId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const isNewMetric = metricId === 'new';
  
  const currentClientId = useSelector(state => state.user.currentClientId);
  const currentProjectId = useSelector(state => state.projects.currentProjectId);
  const connections = useSelector(selectAllConnections);
  const existingMetric = useSelector(state => selectMetricById(state, metricId));
  const allTags = useSelector(selectAllTags);
  const categories = useSelector(selectAllCategories);
  const allMetrics = useSelector(selectAllMetrics);

  const [metric, setMetric] = useState({
    name: '',
    type: 'KPI',
    category: '',
    confidence: 'Average',
    description: '',
    hypothesis: '',
    valueType: 'Value',
    rhythm: 'Daily',
    tags: [],
    technicalDescription: '',
    connections: []
  });

  useEffect(() => {
    if (!isNewMetric && existingMetric) {
      setMetric(existingMetric);
    }
  }, [isNewMetric, existingMetric]);

  const connectedMetrics = allMetrics.filter(m => 
    connections.some(c => 
      (c.fromMetric === metricId && c.toMetric === m.id) || 
      (c.toMetric === metricId && c.fromMetric === m.id)
    )
  );

  const handleChange = (e) => {
    const { name, value } = e.target;
    setMetric(prev => ({ ...prev, [name]: value }));
  };

  const handleTagChange = (newValue) => {
    setMetric(prev => ({
      ...prev,
      tags: newValue || []
    }));
  };

  const handleCategoryChange = async (newValue) => {
    if (newValue.__isNew__) {
      try {
        const resultAction = await dispatch(createCategory({ clientId: currentClientId, projectId: currentProjectId, categoryData: { name: newValue.label } }));
        if (createCategory.fulfilled.match(resultAction)) {
          setMetric(prev => ({ ...prev, category: resultAction.payload.id }));
        }
      } catch (error) {
        toast.error(`Failed to create category: ${error.message}`);
      }
    } else {
      setMetric(prev => ({ ...prev, category: newValue.value }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isNewMetric) {
        await dispatch(createMetric({ clientId: currentClientId, projectId: currentProjectId, metricData: metric })).unwrap();
        toast.success('Metric created successfully');
      } else {
        await dispatch(updateMetric({ clientId: currentClientId, projectId: currentProjectId, metricId, metricData: metric })).unwrap();
        toast.success('Metric updated successfully');
      }
      navigate('/metrics');
    } catch (error) {
      toast.error(`Failed to ${isNewMetric ? 'create' : 'update'} metric: ${error.message}`);
    }
  };

  const handleConnect = async (sourceId, targetId) => {
    try {
      await dispatch(createConnection({ clientId: currentClientId, projectId: currentProjectId, connectionData: { fromMetric: sourceId, toMetric: targetId } })).unwrap();
      toast.success('Connection created successfully');
    } catch (error) {
      toast.error(`Failed to create connection: ${error.message}`);
    }
  };

  const handleDisconnect = async (sourceId, targetId) => {
    const connectionToDelete = connections.find(
      c => (c.fromMetric === sourceId && c.toMetric === targetId) ||
           (c.fromMetric === targetId && c.toMetric === sourceId)
    );
    if (connectionToDelete) {
      try {
        await dispatch(deleteConnection({ clientId: currentClientId, projectId: currentProjectId, connectionId: connectionToDelete.id })).unwrap();
        toast.success('Connection deleted successfully');
      } catch (error) {
        toast.error(`Failed to delete connection: ${error.message}`);
      }
    }
  };


  return (
    <DndProvider backend={HTML5Backend}>
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">
        {isNewMetric ? 'Create New Metric' : `Edit Metric: ${metric.name}`}
      </h1>
      
      <form onSubmit={handleSubmit}>
        <Tabs defaultValue="details">
          <TabsList>
            <TabsTrigger value="details">Details</TabsTrigger>
            <TabsTrigger value="technical">Technical</TabsTrigger>
            <TabsTrigger value="historical">Performance</TabsTrigger>
            <TabsTrigger value="connections">Connections</TabsTrigger>
            <TabsTrigger value="experimentation">Experimentation</TabsTrigger>
          </TabsList>

          <TabsContent value="details">
            <Card>
              <CardHeader>
                <CardTitle>Metric Details</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div>
                  <Label htmlFor="name">Name</Label>
                  <Input id="name" name="name" value={metric.name} onChange={handleChange} required />
                </div>
                <div>
                  <Label htmlFor="type">Type</Label>
                  <Select id="type" name="type" value={metric.type} onChange={handleChange}>
                    {['KPI', 'North Star', 'Input Metric', 'Diagnosis', 'Output Metric'].map(type => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                  </Select>
                </div>
                <div>
                  <Label htmlFor="category">Category</Label>
                  <CreatableSelect
                    isClearable
                    onChange={handleCategoryChange}
                    options={categories.map(category => ({ value: category.id, label: category.name }))}
                    value={{ value: metric.category, label: categories.find(c => c.id === metric.category)?.name }}
                  />
                </div>
                <div>
                  <Label htmlFor="confidence">Confidence</Label>
                  <Select id="confidence" name="confidence" value={metric.confidence} onChange={handleChange}>
                    {['Very Low', 'Below Average', 'Average', 'Above Average', 'Very High'].map(level => (
                      <option key={level} value={level}>{level}</option>
                    ))}
                  </Select>
                </div>
                <div>
                  <Label htmlFor="description">Description</Label>
                  <Textarea id="description" name="description" value={metric.description} onChange={handleChange} />
                </div>
                <div>
                  <Label htmlFor="hypothesis">Hypothesis</Label>
                  <Textarea id="hypothesis" name="hypothesis" value={metric.hypothesis} onChange={handleChange} />
                </div>
                <div>
                  <Label htmlFor="tags">Tags</Label>
                  <CreatableSelect
                    isMulti
                    value={metric.tags.map(tag => ({ value: tag, label: tag }))}
                    onChange={handleTagChange}
                    options={allTags.map(tag => ({ value: tag.id, label: tag.name }))}
                    onCreateOption={(inputValue) => {
                      dispatch(createTag(inputValue));
                      handleTagChange([...metric.tags, { value: inputValue, label: inputValue }]);
                    }}
                  />
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="technical">
            <Card>
              <CardHeader>
                <CardTitle>Technical Details</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div>
                  <Label htmlFor="technicalDescription">Technical Description</Label>
                  <Textarea id="technicalDescription" name="technicalDescription" value={metric.technicalDescription} onChange={handleChange} />
                </div>
                <div>
                  <Label htmlFor="valueType">Value Type</Label>
                  <Select id="valueType" name="valueType" value={metric.valueType} onChange={handleChange}>
                    {['Value', 'Percentage', 'Currency', 'Ratio'].map(type => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                  </Select>
                </div>
                <div>
                  <Label htmlFor="rhythm">Rhythm</Label>
                  <Select id="rhythm" name="rhythm" value={metric.rhythm} onChange={handleChange}>
                    {['Daily', 'Weekly', 'Bi-Weekly', 'Monthly', 'Quarterly'].map(rhythm => (
                      <option key={rhythm} value={rhythm}>{rhythm}</option>
                    ))}
                  </Select>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="historical">
              <Card>
                <CardHeader>
                  <CardTitle>Performance</CardTitle>
                </CardHeader>
                <CardContent>
                  <p>View and manage historical data for this metric.</p>
                  <div className="mt-4 space-x-2">
                    <Link to={`/metrics/${metricId}/historical-data`}>
                      <Button>Manage Historical Data</Button>
                    </Link>
                    <Link to={`/strategy?metricId=${metricId}`}>
                      <Button variant="outline">View Performance</Button>
                    </Link>
                  </div>
                  <TargetSetting 
                    metric={metric} 
                    clientId={currentClientId}
                    projectId={currentProjectId}
                    onSetTarget={(targetData) => dispatch(createTarget({ clientId: currentClientId, projectId: currentProjectId, metricId, targetData }))}
                  />
                </CardContent>
              </Card>
            </TabsContent>

            <TabsContent value="connections">
              <Card>
                <CardHeader>
                  <CardTitle>Metric Connections</CardTitle>
                </CardHeader>
                <CardContent>
                  <ConnectionsVisualizer
                    currentMetric={metric}
                    connectedMetrics={connectedMetrics}
                    allMetrics={allMetrics}
                    onConnect={handleConnect}
                    onDisconnect={handleDisconnect}
                  />
                </CardContent>
              </Card>
            </TabsContent>

            <TabsContent value="experimentation">
              <ExperimentationTab 
                metricId={metric.id}
                clientId={currentClientId}
                projectId={currentProjectId}
                onCreateExperiment={(experimentData) => dispatch(createExperiment({ clientId: currentClientId, projectId: currentProjectId, metricId: metric.id, experimentData }))}
                onCreateActionRemark={(remarkData) => dispatch(createActionRemark({ clientId: currentClientId, projectId: currentProjectId, metricId: metric.id, remarkData }))}
              />
            </TabsContent>
        </Tabs>

          <div className="mt-4 flex justify-end space-x-2">
            <Button type="button" variant="outline" onClick={() => navigate('/metrics')}>Cancel</Button>
            <Button type="submit">{isNewMetric ? 'Create Metric' : 'Update Metric'}</Button>
          </div>
      </form>
    </div>
    </DndProvider>
  );
};

export default MetricDetailsPage;