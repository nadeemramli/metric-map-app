import React from 'react';
import { useDispatch } from 'react-redux';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { createConnection, deleteConnection } from '@/store/slices/connectionsSlice';
import { toast } from 'react-toastify';

const MetricNode = ({ metric, isCenter, onConnect }) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: 'metric',
    item: { id: metric.id },
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  const [, drop] = useDrop(() => ({
    accept: 'metric',
    drop: (item) => {
      if (item.id !== metric.id) {
        onConnect(item.id, metric.id);
      }
    },
  }));

  return (
    <div
      ref={isCenter ? null : (node) => drag(drop(node))}
      style={{
        padding: '10px',
        margin: '5px',
        backgroundColor: isCenter ? 'lightblue' : 'lightgray',
        border: '1px solid gray',
        borderRadius: '5px',
        opacity: isDragging ? 0.5 : 1,
        cursor: isCenter ? 'default' : 'move',
      }}
    >
      {metric.name}
    </div>
  );
};

const ConnectionsVisualizer = ({ currentMetric, connectedMetrics, allMetrics, clientId, projectId }) => {
  const dispatch = useDispatch();

  const handleConnect = async (sourceId, targetId) => {
    try {
      await dispatch(createConnection({ 
        clientId, 
        projectId, 
        connectionData: { fromMetric: sourceId, toMetric: targetId } 
      })).unwrap();
      toast.success('Connection created successfully');
    } catch (error) {
      toast.error(`Failed to create connection: ${error.message}`);
    }
  };

  const handleDisconnect = async (sourceId, targetId) => {
    try {
      const connection = currentMetric.connections.find(
        c => (c.fromMetric === sourceId && c.toMetric === targetId) ||
             (c.fromMetric === targetId && c.toMetric === sourceId)
      );
      if (connection) {
        await dispatch(deleteConnection({ 
          clientId, 
          projectId, 
          connectionId: connection.id 
        })).unwrap();
        toast.success('Connection deleted successfully');
      }
    } catch (error) {
      toast.error(`Failed to delete connection: ${error.message}`);
    }
  };

  return (
    <DndProvider backend={HTML5Backend}>
      <Card>
        <CardHeader>
          <CardTitle>Metric Connections</CardTitle>
        </CardHeader>
        <CardContent>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <MetricNode metric={currentMetric} isCenter={true} />
            <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center' }}>
              {connectedMetrics.map((metric) => (
                <div key={metric.id} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                  <MetricNode metric={metric} onConnect={handleConnect} />
                  <Button variant="destructive" size="sm" onClick={() => handleDisconnect(currentMetric.id, metric.id)}>
                    Disconnect
                  </Button>
                </div>
              ))}
            </div>
          </div>
          <div className="mt-4">
            <h3>Available Metrics to Connect:</h3>
            <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center' }}>
              {allMetrics
                .filter(m => m.id !== currentMetric.id && !connectedMetrics.some(cm => cm.id === m.id))
                .map(metric => (
                  <MetricNode key={metric.id} metric={metric} onConnect={(sourceId) => handleConnect(sourceId, currentMetric.id)} />
                ))
              }
            </div>
          </div>
        </CardContent>
      </Card>
    </DndProvider>
  );
};

export default ConnectionsVisualizer;