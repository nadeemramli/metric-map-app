import { useState, useEffect } from 'react';
import { analyzeMetricTrend } from '../utils/analysisUtils';

export const useMetricAnalysis = (metricData) => {
  const [trend, setTrend] = useState(null);
  const [forecast, setForecast] = useState(null);

  useEffect(() => {
    const { trendResult, forecastResult } = analyzeMetricTrend(metricData);
    setTrend(trendResult);
    setForecast(forecastResult);
  }, [metricData]);

  return { trend, forecast };
};