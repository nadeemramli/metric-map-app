// src/utils/dataProcessingUtils.js
export const processMetricData = (rawData) => {
    return rawData.map(item => ({
      ...item,
      value: parseFloat(item.value),
      date: new Date(item.date)
    }));
  };
  
  export const aggregateMetricData = (data, aggregationType) => {
    // Implement aggregation logic (e.g., daily, weekly, monthly)
  };
  
  export const normalizeMetricData = (data) => {
    // Implement normalization logic
  };