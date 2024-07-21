// src/hooks/useMetrics.js
import { useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import * as actions from '../store/actions/metricsActions';

export const useMetrics = () => {
  const dispatch = useDispatch();
  const {
    metrics,
    connections,
    categories,
    tags,
    selectedConnection,
    isLoading,
    error
  } = useSelector(state => state.metrics);

  const fetchMetricsData = useCallback(() => {
    dispatch(actions.fetchData());
  }, [dispatch]);

  const addMetric = useCallback((metric) => {
    dispatch(actions.addMetric({ ...metric, id: Date.now().toString(), historicalData: [] }));
  }, [dispatch]);

  const updateMetric = useCallback((metric) => {
    dispatch(actions.updateMetric(metric));
  }, [dispatch]);

  const deleteMetric = useCallback((id) => {
    dispatch(actions.deleteMetric(id));
  }, [dispatch]);

  const addConnection = useCallback((fromId, toId) => {
    const newConnection = {
      id: `${fromId}-${toId}`,
      from: fromId,
      to: toId,
      relationship: ''
    };
    dispatch(actions.addConnection(newConnection));
  }, [dispatch]);

  const updateConnection = useCallback((connection) => {
    dispatch(actions.updateConnection(connection));
  }, [dispatch]);

  const removeConnection = useCallback((id) => {
    dispatch(actions.removeConnection(id));
  }, [dispatch]);

  const addHistoricalData = useCallback((metricId, newData) => {
    const metric = metrics.find(m => m.id === metricId);
    if (metric) {
      const updatedMetric = {
        ...metric,
        historicalData: [...(metric.historicalData || []), newData]
      };
      dispatch(actions.updateMetric(updatedMetric));
    }
  }, [dispatch, metrics]);

  const addBulkHistoricalData = useCallback((metricId, newDataArray) => {
    const metric = metrics.find(m => m.id === metricId);
    if (metric) {
      const updatedMetric = {
        ...metric,
        historicalData: [...(metric.historicalData || []), ...newDataArray]
      };
      dispatch(actions.updateMetric(updatedMetric));
    }
  }, [dispatch, metrics]);

  const addCategory = useCallback((category) => {
    dispatch(actions.addCategory({ ...category, id: Date.now().toString() }));
  }, [dispatch]);

  const updateCategory = useCallback((category) => {
    dispatch(actions.updateCategory(category));
  }, [dispatch]);

  const deleteCategory = useCallback((id) => {
    dispatch(actions.deleteCategory(id));
  }, [dispatch]);

  const addTag = useCallback((tag) => {
    dispatch(actions.addTag({ ...tag, id: Date.now().toString() }));
  }, [dispatch]);

  const updateTag = useCallback((tag) => {
    dispatch(actions.updateTag(tag));
  }, [dispatch]);

  const deleteTag = useCallback((id) => {
    dispatch(actions.deleteTag(id));
  }, [dispatch]);

  const handleCloseSidebar = useCallback(() => {
    dispatch(actions.setSelectedConnection(null));
  }, [dispatch]);

  const handleEditConnection = useCallback((connection) => {
    dispatch(actions.setSelectedConnection(connection));
  }, [dispatch]);

  const getMetricById = useCallback((id) => {
    return metrics.find(m => m.id.toString() === id.toString());
  }, [metrics]);

  const getConnectionById = useCallback((id) => {
    return connections.find(c => c.id === id);
  }, [connections]);

  const getHistoricalData = useCallback((metricId) => {
    const metric = getMetricById(metricId);
    return metric ? metric.historicalData || [] : [];
  }, [getMetricById]);

  return {
    metrics,
    connections,
    categories,
    tags,
    selectedConnection,
    isLoading,
    error,
    fetchMetricsData,
    addMetric,
    updateMetric,
    deleteMetric,
    addConnection,
    updateConnection,
    removeConnection,
    addHistoricalData,
    addBulkHistoricalData,
    addCategory,
    updateCategory,
    deleteCategory,
    addTag,
    updateTag,
    deleteTag,
    handleCloseSidebar,
    handleEditConnection,
    getMetricById,
    getConnectionById,
    getHistoricalData
  };
};