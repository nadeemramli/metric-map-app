import React, { useState, useCallback } from 'react';
import { useSelector } from 'react-redux';
import { Stage, Layer, Rect, Text } from 'react-konva';
import { selectAllMetrics } from '../../../store/slices/metricsSlice';

const MetricCard = React.memo(({ metric, x, y, onDragEnd }) => {
  return (
    <React.Fragment>
      <Rect
        x={x}
        y={y}
        width={100}
        height={50}
        fill="white"
        stroke="black"
        strokeWidth={1}
        draggable
        onDragEnd={onDragEnd}
      />
      <Text
        x={x + 5}
        y={y + 5}
        text={metric.name}
        fontSize={12}
        width={90}
        height={40}
      />
    </React.Fragment>
  );
});

const VisualizationCanvas = () => {
  const metrics = useSelector(selectAllMetrics);
  const [metricPositions, setMetricPositions] = useState({});

  const handleDragEnd = useCallback((metricId, e) => {
    setMetricPositions(prev => ({
      ...prev,
      [metricId]: { x: e.target.x(), y: e.target.y() }
    }));
  }, []);

  return (
    <Stage width={window.innerWidth} height={window.innerHeight}>
      <Layer>
        {metrics.map((metric, index) => (
          <MetricCard
            key={metric.id}
            metric={metric}
            x={metricPositions[metric.id]?.x || index * 120}
            y={metricPositions[metric.id]?.y || 50}
            onDragEnd={(e) => handleDragEnd(metric.id, e)}
          />
        ))}
      </Layer>
    </Stage>
  );
};

export default React.memo(VisualizationCanvas);