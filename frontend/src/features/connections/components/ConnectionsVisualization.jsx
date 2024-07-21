import React from 'react';
import { Network } from '@nivo/network';

const ConnectionsVisualization = ({ connections }) => {
  const networkData = {
    nodes: connections.reduce((acc, conn) => {
      if (!acc.some(node => node.id === conn.from_metric.id)) {
        acc.push({ id: conn.from_metric.id, name: conn.from_metric.name });
      }
      if (!acc.some(node => node.id === conn.to_metric.id)) {
        acc.push({ id: conn.to_metric.id, name: conn.to_metric.name });
      }
      return acc;
    }, []),
    links: connections.map(conn => ({
      source: conn.from_metric.id,
      target: conn.to_metric.id,
      value: conn.correlation_coefficient || 0
    }))
  };

  return (
    <div style={{ height: '400px' }}>
      <Network
        data={networkData}
        margin={{ top: 0, right: 0, bottom: 0, left: 0 }}
        linkStrength={link => Math.abs(link.value)}
        nodeColor={node => node.color}
        nodeBorderWidth={1}
        nodeBorderColor={{ from: 'color', modifiers: [['darker', 0.8]] }}
        linkThickness={link => 2 * Math.abs(link.value)}
      />
    </div>
  );
};

export default ConnectionsVisualization;