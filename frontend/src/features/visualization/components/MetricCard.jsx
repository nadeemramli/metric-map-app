import React from 'react';
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ArrowUp, ArrowDown } from "lucide-react";

const MetricCard = ({ metric, onClick }) => {
  const latestValue = metric.data[metric.data.length - 1]?.value;
  const previousValue = metric.data[metric.data.length - 2]?.value;
  const percentageChange = previousValue
    ? ((latestValue - previousValue) / previousValue) * 100
    : 0;

  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>{metric.name}</CardTitle>
        <CardDescription>{metric.type}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{latestValue}</div>
        <div className={`flex items-center ${percentageChange >= 0 ? 'text-green-600' : 'text-red-600'}`}>
          {percentageChange >= 0 ? (
            <ArrowUp className="w-4 h-4 mr-1" />
          ) : (
            <ArrowDown className="w-4 h-4 mr-1" />
          )}
          <span>{Math.abs(percentageChange).toFixed(2)}%</span>
        </div>
      </CardContent>
      <CardFooter>
        <Button onClick={() => onClick(metric)}>View Details</Button>
      </CardFooter>
    </Card>
  );
};

export default MetricCard;