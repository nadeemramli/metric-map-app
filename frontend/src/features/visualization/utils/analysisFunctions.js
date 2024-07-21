export const calculateTrend = (historicalData, period) => {
    if (historicalData.length < 2) return 'Not enough data';
  
    const sortedData = historicalData.sort((a, b) => new Date(a.date) - new Date(b.date));
    const currentValue = sortedData[sortedData.length - 1].value;
    const pastValue = sortedData[0].value;
    const percentageChange = ((currentValue - pastValue) / pastValue) * 100;
    return percentageChange.toFixed(2) + '%';
  };
  
  export const calculateCorrelation = (data1, data2) => {
    const pairedData = data1.map(d1 => {
      const d2 = data2.find(d => d.date === d1.date);
      return d2 ? [d1.value, d2.value] : null;
    }).filter(pair => pair !== null);
  
    const n = pairedData.length;
    if (n < 2) return 'Not enough data';
  
    const [sumX, sumY] = pairedData.reduce(
      ([sx, sy], [x, y]) => [sx + x, sy + y],
      [0, 0]
    );
    const [sumXX, sumYY, sumXY] = pairedData.reduce(
      ([sxx, syy, sxy], [x, y]) => [sxx + x * x, syy + y * y, sxy + x * y],
      [0, 0, 0]
    );
  
    const numerator = n * sumXY - sumX * sumY;
    const denominator = Math.sqrt((n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY));
  
    return (numerator / denominator).toFixed(2);
  };