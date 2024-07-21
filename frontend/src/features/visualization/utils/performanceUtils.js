export const calculatePerformanceMetrics = (historicalData) => {
    if (!historicalData || historicalData.length === 0) {
      return {
        weekOverWeek: null,
        monthOverMonth: null,
        weekVsLifetimeAvg: null
      };
    }
  
    const sortedData = [...historicalData].sort((a, b) => new Date(b.date) - new Date(a.date));
    const currentValue = sortedData[0].value;
  
    const getValueAtDate = (daysAgo) => {
      const date = new Date();
      date.setDate(date.getDate() - daysAgo);
      return sortedData.find(d => new Date(d.date) <= date)?.value;
    };
  
    const calculateChange = (oldValue, newValue) => {
      if (oldValue === undefined || newValue === undefined) return null;
      return ((newValue - oldValue) / oldValue) * 100;
    };
  
    const oneWeekAgoValue = getValueAtDate(7);
    const oneMonthAgoValue = getValueAtDate(30);
  
    // Calculate average weekly value
    const weeklyValues = sortedData.filter((_, index) => index % 7 === 0).map(d => d.value);
    const avgWeeklyValue = weeklyValues.reduce((sum, value) => sum + value, 0) / weeklyValues.length;
  
    return {
      weekOverWeek: calculateChange(oneWeekAgoValue, currentValue),
      monthOverMonth: calculateChange(oneMonthAgoValue, currentValue),
      weekVsLifetimeAvg: calculateChange(avgWeeklyValue, currentValue)
    };
  };