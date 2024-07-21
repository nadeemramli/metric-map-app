import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import CreatableSelect from 'react-select/creatable';
import makeAnimated from 'react-select/animated';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {fetchTags, selectAllTags} from '@/store/slices/tagsSlice.js';
import {selectAllMetrics,addMetric,updateMetric} from '@/store/slices/metricsSlice.js';
import {selectAllCategories} from '@/store/slices/categoriesSlice.js'

const animatedComponents = makeAnimated();

const customStyles = {
  control: (provided) => ({
    ...provided,
    backgroundColor: 'white',
    borderColor: 'gray',
    color: 'black'
  }),
  input: (provided) => ({
    ...provided,
    color: 'black',
  }),
  placeholder: (provided) => ({
    ...provided,
    color: 'gray',
  }),
  singleValue: (provided) => ({
    ...provided,
    color: 'black',
  }),
  menu: (provided) => ({
    ...provided,
    backgroundColor: 'white',
    color: 'black'
  }),
  multiValue: (provided) => ({
    ...provided,
    backgroundColor: 'lightgray',
  }),
  multiValueLabel: (provided) => ({
    ...provided,
    color: 'black',
  }),
  multiValueRemove: (provided) => ({
    ...provided,
    color: 'black',
    ':hover': {
      backgroundColor: 'darkgray',
      color: 'white',
    },
  }),
};

const MetricForm = ({ initialMetric = null, onSubmit }) => {
  const dispatch = useDispatch();
  const existingMetrics = useSelector(selectAllMetrics);
  const categories = useSelector(selectAllCategories);
  const allTags = useSelector(selectAllTags);
  
  const [metric, setMetric] = useState(initialMetric || {
    name: '',
    type: 'KPI',
    category: '',
    confidence: 'Average',
    description: '',
    hypothesis: '',
    valueType: 'Value',
    rhythm: 'Daily',
    tags: [],
    technicalDescription: '',
    connections: []
  });

  const [loading, setLoading] = useState(false);
  const [submitSuccess, setSubmitSuccess] = useState(false);
  const tagInputRef = useRef(null);

  useEffect(() => {
    dispatch(fetchTags());
  }, [dispatch]);

  useEffect(() => {
    if (initialMetric) {
      const connectedIds = existingMetrics
        .filter(m => m.connections.includes(initialMetric.id))
        .map(m => m.id);
      setMetric({ ...initialMetric, connections: connectedIds });
    }
  }, [initialMetric, existingMetrics]);

  const handleChange = useCallback((e) => {
    const { name, value, type, checked } = e.target;
    if (name === 'connections') {
      const updatedConnections = checked
        ? [...new Set([...(metric.connections || []), parseInt(value)])]
        : (metric.connections || []).filter(id => id !== parseInt(value));
      setMetric(prev => ({ ...prev, connections: updatedConnections }));
    } else {
      setMetric(prev => ({ ...prev, [name]: value }));
    }
  }, [metric.connections]);

  const handleTagChange = useCallback((newValue) => {
    setMetric(prev => ({
      ...prev,
      tags: newValue || []
    }));
  }, []);

  const handleCreateTag = useCallback((inputValue) => {
    const newTag = { label: inputValue, value: inputValue.toLowerCase().replace(/\W/g, '') };
    setMetric(prev => ({
        ...prev,
        tags: [...prev.tags, newTag]
    }));
    tagInputRef.current.focus();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const cleanedType = metric.type.replace(/^"|"$/g, '');
    
    const metricToSubmit = {
      ...metric,
      type: cleanedType,
      tags: metric.tags.map(tag => tag.value),
    };

    try {
      if (initialMetric) {
        await dispatch(updateMetric(metricToSubmit)).unwrap();
      } else {
        await dispatch(addMetric(metricToSubmit)).unwrap();
      }
      setSubmitSuccess(true);
      onSubmit();
      toast.success('Metric successfully submitted!');
    } catch (error) {
      console.error('Error submitting metric:', error);
      toast.error(`Error: ${error.message || "Check data"}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md max-w-2xl mx-auto">
      {loading && <div className="loading-spinner">Loading...</div>}
      <div className="mb-4">
        <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">Metric Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={metric.name}
          onChange={handleChange}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>

      <div className="mb-4">
        <span className="block text-sm font-medium text-gray-700 mb-1">Type of Metric</span>
        <div className="flex flex-wrap gap-4">
          {['KPI', 'North Star', 'Input Metric', 'Diagnosis', 'Output Metric'].map((type) => (
            <label key={type} className="inline-flex items-center">
              <input
                type="radio"
                name="type"
                value={type}
                checked={metric.type === type}
                onChange={handleChange}
                className="form-radio text-blue-600"
              />
              <span className="ml-2 text-sm text-gray-700">{type}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="mb-4">
        <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">Description</label>
        <textarea
          id="description"
          name="description"
          value={metric.description}
          onChange={handleChange}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          rows="3"
        ></textarea>
      </div>

      <div className="mb-4">
        <label htmlFor="technicalDescription" className="block text-sm font-medium text-gray-700 mb-1">Technical Description</label>
        <textarea
          id="technicalDescription"
          name="technicalDescription"
          value={metric.technicalDescription}
          onChange={handleChange}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          rows="3"
        ></textarea>
      </div>

      <div className="flex space-x-4 mb-4">
        <div className="flex-1">
          <label htmlFor="category" className="block text-sm font-medium text-gray-700 mb-1">Category</label>
          <select
            id="category"
            name="category"
            value={metric.category}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm text-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          >
            <option value="">Select a category</option>
            {categories.map(category => (
              <option key={category.id} value={category.id}>{category.name}</option>
            ))}
          </select>
        </div>

        <div className="flex-1">
          <label htmlFor="value" className="block text-sm font-medium text-gray-700 mb-1">Value</label>
          <select
            name="valueType"
            value={metric.valueType}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm text-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          >
            <option value="Count">Count</option>
            <option value="Percentage">Percentage</option>
            <option value="Currency">Currency</option>
            <option value="Ratio">Ratio</option>
          </select>
        </div>

        <div className="flex-1">
          <label htmlFor="rhythm" className="block text-sm font-medium text-gray-700 mb-1">Rhythm</label>
          <select
            name="rhythm"
            value={metric.rhythm}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm text-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          >
            <option value="Daily">Daily</option>
            <option value="Weekly">Weekly</option>
            <option value="Bi-Weekly">Bi-Weekly</option>
            <option value="Monthly">Monthly</option>
            <option value="Quarterly">Quarterly</option>
          </select>
        </div>
      </div>

      <div className="mb-4">
        <label htmlFor="hypothesis" className="block text-sm font-medium text-gray-700 mb-1">Hypothesis/Goal</label>
        <textarea
          id="hypothesis"
          name="hypothesis"
          value={metric.hypothesis}
          onChange={handleChange}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          rows="3"
        ></textarea>
      </div>

      <div className="mb-4">
        <span className="block text-sm font-medium text-gray-700 mb-1">Confidence</span>
        <div className="flex flex-wrap gap-4">
          {['Very Low', 'Below Average', 'Average', 'Above Average', 'Very High'].map((level) => (
            <label key={level} className="inline-flex items-center">
              <input
                type="radio"
                name="confidence"
                value={level}
                checked={metric.confidence === level}
                onChange={handleChange}
                className="form-radio text-blue-600"
              />
              <span className="ml-2 text-sm text-gray-700">{level}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="mb-4">
        <label htmlFor="tags" className="block text-sm font-medium text-gray-700 mb-1">Tags</label>
        <CreatableSelect
          ref={tagInputRef}
          components={animatedComponents}
          isMulti
          value={metric.tags}
          onChange={handleTagChange}
          onCreateOption={handleCreateTag}
          options={allTags.map(tag => ({ value: tag.id, label: tag.name }))}
          className="basic-multi-select"
          classNamePrefix="select"
          placeholder="Select or create tags"
          styles={customStyles}
        />
      </div>

      <div className="mb-4">
        <span className="block text-sm font-medium text-gray-700 mb-1">Connections (effects on other metrics)</span>
        <div className="flex flex-wrap gap-2">
          {existingMetrics.filter(m => m.id !== metric.id).map((m) => (
            <label key={m.id} className="inline-flex items-center bg-gray-100 px-3 py-1 rounded-full">
              <input
                type="checkbox"
                name="connections"
                value={m.id}
                checked={metric.connections.includes(m.id)}
                onChange={handleChange}
                className="form-checkbox text-blue-600"
              />
              <span className="ml-2 text-sm text-gray-700">{m.name}</span>
            </label>
          ))}
        </div>
      </div>

      <button type="submit" className="w-full bg-blue-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors duration-300">
        {initialMetric ? 'Update Metric' : 'Add Metric'}
      </button>

      {submitSuccess && (
        <div className="mt-4 p-2 bg-green-100 text-green-700 rounded">
          Metric successfully submitted!
        </div>
      )}
    </form>
  );
};

export default MetricForm;
