import React, { useState, useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { selectAllMetrics, selectAllConnections } from '@/store/slices/metricsSlice';
import { createConnection, updateConnection, deleteConnection } from '@/store/slices/connectionsSlice';

const MetricNode = ({ metric, position, onMove, onStartConnection, onEndConnection }) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: 'metric',
    item: { id: metric.id, ...position },
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  const [, drop] = useDrop(() => ({
    accept: 'connection',
    drop: (item) => onEndConnection(item.sourceId, metric.id),
  }));

  return (
    <div
      ref={(node) => drag(drop(node))}
      style={{
        position: 'absolute',
        left: position.x,
        top: position.y,
        opacity: isDragging ? 0.5 : 1,
        cursor: 'move',
        backgroundColor: 'lightblue',
        padding: '10px',
        borderRadius: '5px',
      }}
    >
      {metric.name}
      <button onClick={() => onStartConnection(metric.id)}>+</button>
    </div>
  );
};

const ConnectionLine = ({ start, end }) => (
  <svg style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', pointerEvents: 'none' }}>
    <line x1={start.x} y1={start.y} x2={end.x} y2={end.y} stroke="black" />
  </svg>
);

const VisualizationCanvas = ({ metrics, connections, onUpdateMetricPosition, onCreateConnection }) => {
  const [tempConnection, setTempConnection] = useState(null);
  const [, drop] = useDrop(() => ({ accept: 'metric' }));

  const handleStartConnection = (sourceId) => {
    const sourceMetric = metrics.find(m => m.id === sourceId);
    setTempConnection({ sourceId, x: sourceMetric.position.x, y: sourceMetric.position.y });
  };

  const handleEndConnection = (sourceId, targetId) => {
    if (sourceId !== targetId) {
      onCreateConnection({ fromMetric: sourceId, toMetric: targetId, relationship: 'connected' });
    }
    setTempConnection(null);
  };

  const handleCanvasMouseMove = (e) => {
    if (tempConnection) {
      setTempConnection(prev => ({ ...prev, x: e.clientX, y: e.clientY }));
    }
  };

  return (
    <div ref={drop} style={{ position: 'relative', width: '100%', height: '600px' }} onMouseMove={handleCanvasMouseMove}>
      {metrics.map((metric) => (
        <MetricNode
          key={metric.id}
          metric={metric}
          position={metric.position}
          onMove={(position) => onUpdateMetricPosition(metric.id, position)}
          onStartConnection={handleStartConnection}
          onEndConnection={handleEndConnection}
        />
      ))}
      {connections.map((connection, index) => {
        const start = metrics.find(m => m.id === connection.fromMetric).position;
        const end = metrics.find(m => m.id === connection.toMetric).position;
        return <ConnectionLine key={index} start={start} end={end} />;
      })}
      {tempConnection && (
        <ConnectionLine
          start={{ x: tempConnection.x, y: tempConnection.y }}
          end={{ x: tempConnection.x, y: tempConnection.y }}
        />
      )}
    </div>
  );
};

const RelationshipsVisualizationPage = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);
  const [selectedNode, setSelectedNode] = useState(null);
  const [newConnection, setNewConnection] = useState({ source: '', target: '', relationship: '' });

  useEffect(() => {
    dispatch(fetchMetrics());
    dispatch(fetchConnections());
  }, [dispatch]);
  
  const handleUpdateMetricPosition = useCallback(async (metricId, newPosition) => {
    try {
      await dispatch(updateMetricPosition({ metricId, position: newPosition })).unwrap();
      toast.success('Metric position updated');
    } catch (error) {
      toast.error(`Failed to update metric position: ${error.message}`);
    }
  }, [dispatch]);
  
  const handleCreateConnection = useCallback(async (connectionData) => {
    try {
      await dispatch(createConnection({ clientId, projectId, connectionData })).unwrap();
      toast.success('Connection created');
    } catch (error) {
      toast.error(`Failed to create connection: ${error.message}`);
    }
  }, [dispatch, clientId, projectId]);

  const handleAddConnection = () => {
    dispatch(createConnection(newConnection));
    setNewConnection({ source: '', target: '', relationship: '' });
  };

  const handleRemoveConnection = (connectionId) => {
    dispatch(deleteConnection(connectionId));
  };

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="flex h-screen">
        <div className="flex-1">
          <VisualizationCanvas
            metrics={metrics}
            connections={connections}
            onUpdateMetricPosition={handleUpdateMetricPosition}
            onCreateConnection={handleCreateConnection}
          />
        </div>
        <div className="w-1/4 p-4 bg-gray-100 overflow-y-auto">
          <Card>
            <CardHeader>
              <CardTitle>Manage Connections</CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={(e) => { e.preventDefault(); handleAddConnection(); }} className="space-y-4">
                <div>
                  <Label htmlFor="source">Source Metric</Label>
                  <Select 
                    value={newConnection.source}
                    onValueChange={(value) => setNewConnection({...newConnection, source: value})}
                  >
                    <SelectTrigger>
                      <SelectValue placeholder="Select source metric" />
                    </SelectTrigger>
                    <SelectContent>
                      {metrics.map(metric => (
                        <SelectItem key={metric.id} value={metric.id}>{metric.name}</SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
                <div>
                  <Label htmlFor="target">Target Metric</Label>
                  <Select
                    value={newConnection.target}
                    onValueChange={(value) => setNewConnection({...newConnection, target: value})}
                  >
                    <SelectTrigger>
                      <SelectValue placeholder="Select target metric" />
                    </SelectTrigger>
                    <SelectContent>
                      {metrics.map(metric => (
                        <SelectItem key={metric.id} value={metric.id}>{metric.name}</SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
                <div>
                  <Label htmlFor="relationship">Relationship</Label>
                  <Input
                    id="relationship"
                    value={newConnection.relationship}
                    onChange={(e) => setNewConnection({...newConnection, relationship: e.target.value})}
                  />
                </div>
                <Button type="submit">Add Connection</Button>
              </form>
            </CardContent>
          </Card>

          {selectedNode && (
            <Card className="mt-4">
              <CardHeader>
                <CardTitle>{selectedNode.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <h3 className="font-semibold mb-2">Connected Metrics:</h3>
                <ul>
                  {connections
                    .filter(conn => conn.fromMetric === selectedNode.id || conn.toMetric === selectedNode.id)
                    .map(conn => {
                      const connectedMetric = metrics.find(m => m.id === (conn.fromMetric === selectedNode.id ? conn.toMetric : conn.fromMetric));
                      return (
                        <li key={conn.id} className="mb-2">
                          <p>{connectedMetric.name} - {conn.relationship}</p>
                          <Button 
                            variant="destructive" 
                            size="sm"
                            onClick={() => handleRemoveConnection(conn.id)}
                          >
                            Remove
                          </Button>
                        </li>
                      );
                    })
                  }
                </ul>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </DndProvider>
  );
};

export default RelationshipsVisualizationPage;