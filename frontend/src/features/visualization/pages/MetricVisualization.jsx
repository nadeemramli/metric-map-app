import React, { useMemo, useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { ResponsiveNetwork } from '@nivo/network';
import { selectAllMetrics } from '@/store/slices/metricsSlice.js';
import { updateConnection, selectAllConnections } from '@/store/slices/connectionsSlice.js'; // Assuming you have this action

const getColorByType = (type) => {
  const colors = {
    'KPI': '#4299E1',
    'North Star': '#F6E05E',
    'Input (Leading)': '#68D391',
    'Diagnosis': '#F687B3',
    'Output (Laggard)': '#FC8181'
  };
  return colors[type] || '#A0AEC0';
};

const MetricCard = React.memo(({ metric, onClick }) => (
  <div 
    className="p-2 rounded shadow-sm cursor-pointer text-xs" 
    style={{ backgroundColor: getColorByType(metric.type), width: '120px', height: '80px' }}
    onClick={() => onClick(metric)}
  >
    <h3 className="font-bold truncate text-white">{metric.name}</h3>
    <p className="truncate text-white">Type: {metric.type}</p>
    <p className="truncate text-white">Value: {metric.value}</p>
  </div>
));

const MetricVisualization = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const connections = useSelector(selectAllConnections);

  const data = useMemo(() => {
    if (!metrics || !connections || metrics.length === 0 || connections.length === 0) {
      return { nodes: [], links: [] };
    }

    const nodes = metrics.map(metric => ({
      id: metric.id.toString(),
      color: getColorByType(metric.type),
      data: metric
    }));

    const links = connections
      .filter(conn => 
        conn.from && conn.to && 
        metrics.some(m => m.id.toString() === conn.from.toString()) &&
        metrics.some(m => m.id.toString() === conn.to.toString())
      )
      .map(connection => ({
        source: connection.from.toString(),
        target: connection.to.toString(),
        data: connection
      }));

    return { nodes, links };
  }, [metrics, connections]);

  const handleMetricClick = useCallback((metric) => {
    console.log('Metric clicked:', metric);
    // Implement your logic here, e.g., open a modal or navigate to a detail page
  }, []);

  const handleConnectionUpdate = useCallback((connection) => {
    dispatch(updateConnection(connection));
  }, [dispatch]);

  if (data.nodes.length === 0 || data.links.length === 0) {
    return <div>No data to visualize</div>;
  }

  return (
    <div style={{ height: 'calc(100vh - 100px)', width: '100%' }}>
      <ResponsiveNetwork
        data={data}
        margin={{ top: 0, right: 0, bottom: 0, left: 0 }}
        linkDistance={e => 200}
        centeringStrength={0.3}
        repulsivity={6}
        nodeSize={n => 120}
        activeNodeSize={n => 130}
        linkThickness={l => 2}
        linkBlendMode="multiply"
        motionStiffness={160}
        motionDamping={12}
        nodeColor={node => node.color}
        nodeComponent={({ node }) => (
          <foreignObject x={node.x - 60} y={node.y - 40} width={120} height={80}>
            <MetricCard metric={node.data} onClick={handleMetricClick} />
          </foreignObject>
        )}
        linkComponent={({ link }) => (
          <g>
            <line
              x1={link.source.x}
              y1={link.source.y}
              x2={link.target.x}
              y2={link.target.y}
              stroke="#999"
              strokeWidth={2}
              onClick={() => handleConnectionUpdate(link.data)}
            />
            <text
              x={(link.source.x + link.target.x) / 2}
              y={(link.source.y + link.target.y) / 2}
              textAnchor="middle"
              fill="#666"
              fontSize={10}
            >
              {link.data.relationship || ''}
            </text>
          </g>
        )}
      />
    </div>
  );
};

export default React.memo(MetricVisualization);