import React from 'react';
import MetricForm from '../components/MetricForm';

const InputMetrics = ({ addMetric, metrics, connections, categories }) => {
    const handleSubmit = (metricData) => {
        addMetric(metricData);
    };

    // Assume initialMetric is meant to be null for new entries unless you have a way to set it
    // Make sure metrics, connections, and categories are properly passed from the parent component
    return (
        <div className="min-h-screen bg-gray-900 py-8">
            <div className="container mx-auto px-4">
                <h2 className="text-2xl font-bold mb-6 text-white">Input Metrics</h2>
                <MetricForm onSubmit={handleSubmit} initialMetric={null} existingMetrics={metrics} connections={connections} categories={categories} />
            </div>
        </div>
    );
};

export default InputMetrics;
