import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Label } from "@/components/ui/label";
import { fetchProjects, createProject } from '@/store/slices/projectsSlice';
import { setCurrentProject } from '@/store/slices/userSlice'; // Assuming this is where setCurrentProject is exported from
import { toast } from 'react-toastify';
import { Loader2 } from 'lucide-react';

const ProjectManagementPage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { projects, status, error } = useSelector(state => state.projects);
  const currentClientId = useSelector(state => state.user.currentClientId);
  const [newProjectName, setNewProjectName] = useState('');
  const [isCreatingProject, setIsCreatingProject] = useState(false);

  useEffect(() => {
    if (currentClientId) {
      dispatch(fetchProjects(currentClientId));
    } else {
      navigate('/clients');
    }
  }, [dispatch, currentClientId, navigate]);

  useEffect(() => {
    if (error) {
      toast.error(`Error: ${error}`);
    }
  }, [error]);

  const handleCreateProject = async () => {
    if (newProjectName && currentClientId) {
      setIsCreatingProject(true);
      try {
        await dispatch(createProject({ clientId: currentClientId, projectData: { name: newProjectName } })).unwrap();
        setNewProjectName('');
        toast.success('Project created successfully!');
      } catch (err) {
        toast.error(`Failed to create project: ${err.message}`);
      } finally {
        setIsCreatingProject(false);
      }
    }
  };

  const handleSelectProject = async (projectId) => {
    try {
      await dispatch(setCurrentProject(projectId)).unwrap();
      navigate('/dashboard');
    } catch (err) {
      toast.error(`Failed to select project: ${err.message}`);
    }
  };

  if (status === 'loading') {
    return (
      <div className="flex justify-center items-center h-screen">
        <Loader2 className="h-8 w-8 animate-spin" />
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Select a Project</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {projects.map(project => (
          <Card key={project.id} className="hover:shadow-lg transition-shadow duration-300">
            <CardHeader>
              <CardTitle>{project.name}</CardTitle>
              <CardDescription>Created on: {new Date(project.createdAt).toLocaleDateString()}</CardDescription>
            </CardHeader>
            <CardContent>
              <p>Metrics: {project.metricsCount || 0}</p>
              <p>Last updated: {new Date(project.updatedAt).toLocaleDateString()}</p>
            </CardContent>
            <CardFooter>
              <Button onClick={() => handleSelectProject(project.id)} className="w-full">Select Project</Button>
            </CardFooter>
          </Card>
        ))}
        
        <Dialog>
          <DialogTrigger asChild>
            <Card className="flex items-center justify-center cursor-pointer hover:bg-gray-100 hover:shadow-lg transition-all duration-300">
              <CardContent>
                <p className="text-2xl">+ Create New Project</p>
              </CardContent>
            </Card>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Create New Project</DialogTitle>
              <DialogDescription>
                Enter a name for your new project.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <div className="grid grid-cols-4 items-center gap-4">
                <Label htmlFor="name" className="text-right">
                  Name
                </Label>
                <Input 
                  id="name" 
                  value={newProjectName}
                  onChange={(e) => setNewProjectName(e.target.value)}
                  className="col-span-3"
                />
              </div>
            </div>
            <DialogFooter>
              <Button onClick={handleCreateProject} disabled={isCreatingProject}>
                {isCreatingProject ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Creating...
                  </>
                ) : (
                  'Create Project'
                )}
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>
      </div>
    </div>
  );
};

export default ProjectManagementPage;