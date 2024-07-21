import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { selectMetricById, selectPerformanceMetrics, fetchPerformanceMetrics } from '@/store/slices/metricsSlice';
import ForecastVsActual from '../components/ForecastVsActual';
import ActionRemarks from '@/features/action-remarks/pages/ActionRemarks';
import ProgressTracking from '../components/ProgressTracking';

const Performance = ({ metricId }) => {
  const dispatch = useDispatch();
  const metric = useSelector(state => selectMetricById(state, metricId));
  const performanceMetrics = useSelector(state => selectPerformanceMetrics(state, metricId));
  const status = useSelector(state => state.metrics.status);

  useEffect(() => {
    if (metricId && !performanceMetrics) {
      dispatch(fetchPerformanceMetrics(metricId));
    }
  }, [dispatch, metricId, performanceMetrics]);

  if (!metric) return <div>Metric not found</div>;
  if (status === 'loading') return <div>Loading...</div>;
  if (status === 'failed') return <div>Error loading performance metrics</div>;

  const formatPercentage = (value) => {
    if (value === null || value === undefined) return 'N/A';
    return `${value > 0 ? '+' : ''}${value.toFixed(2)}%`;
  };

  const getPercentageColor = (value) => {
    if (value === null || value === undefined) return 'text-gray-500';
    if (value > 0) return 'text-green-500';
    if (value < 0) return 'text-red-500';
    return 'text-gray-500';
  };

  return (
    <div className="bg-white shadow rounded-lg p-4">
      <h2 className="text-xl font-semibold mb-4">{metric.name} Performance</h2>
      
      {performanceMetrics && (
        <div className="grid grid-cols-3 gap-4 mb-6">
          <div>
            <p className="text-sm font-medium text-gray-500">Week-over-week</p>
            <p className={`text-2xl font-bold ${performanceMetrics.wow_change >= 0 ? 'text-green-500' : 'text-red-500'}`}>
              {performanceMetrics.wow_change.toFixed(2)}%
            </p>
          </div>
          <div>
            <p className="text-sm font-medium text-gray-500">Month-over-month</p>
            <p className={`text-2xl font-bold ${performanceMetrics.mom_change >= 0 ? 'text-green-500' : 'text-red-500'}`}>
              {performanceMetrics.mom_change.toFixed(2)}%
            </p>
          </div>
          <div>
            <p className="text-sm font-medium text-gray-500">Week vs. lifetime avg</p>
            <p className={`text-2xl font-bold ${performanceMetrics.week_vs_avg_weekly >= 0 ? 'text-green-500' : 'text-red-500'}`}>
              {performanceMetrics.week_vs_avg_weekly.toFixed(2)}%
            </p>
          </div>
        </div>
      )}

      <ForecastVsActual data={metric.forecastData} />
      <ActionRemarks metricId={metricId} remarks={metric.remarks || []} />
      <ProgressTracking current={metric.currentValue} target={metric.target} />
      </div>
  );
};

export default Performance;