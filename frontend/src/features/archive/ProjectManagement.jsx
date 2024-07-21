import React, { useState, useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createProject, switchProject, selectAllProjects } from '../store/slices/projectsSlice';

const ProjectManagement = () => {
  const dispatch = useDispatch();
  const projects = useSelector(selectAllProjects);
  const [newProjectName, setNewProjectName] = useState('');

  const handleCreateProject = useCallback(() => {
    if (newProjectName) {
      dispatch(createProject(newProjectName));
      setNewProjectName('');
    }
  }, [dispatch, newProjectName]);

  const handleSwitchProject = useCallback((projectId) => {
    dispatch(switchProject(projectId));
  }, [dispatch]);

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-4">Project Management</h2>
      <div className="mb-4">
        <input
          type="text"
          value={newProjectName}
          onChange={(e) => setNewProjectName(e.target.value)}
          placeholder="New project name"
          className="mr-2 p-1 border rounded"
        />
        <button onClick={handleCreateProject} className="px-3 py-1 bg-blue-500 text-white rounded">
          Create Project
        </button>
      </div>
      <ul>
        {projects.map(project => (
          <li key={project.id} className="mb-2">
            {project.name}
            <button
              onClick={() => handleSwitchProject(project.id)}
              className="ml-2 px-2 py-1 bg-gray-200 rounded"
            >
              Switch to this project
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default React.memo(ProjectManagement);