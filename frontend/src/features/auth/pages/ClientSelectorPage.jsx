import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux';
import { fetchClients, selectAllClients, selectClientsStatus, selectClientsError } from '@/store/slices/clientsSlice';
import { setCurrentClient } from '@/store/slices/userSlice';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import LoadingSpinner from '@/common/LoadingSpinner';

const ClientSelector = () => {
  const dispatch = useDispatch();
  const clients = useSelector(selectAllClients);
  const status = useSelector(selectClientsStatus);
  const error = useSelector(selectClientsError);
  const navigate = useNavigate();

  useEffect(() => {
    console.log('ClientSelector useEffect, status:', status);
    if (status === 'idle') {
      console.log('Dispatching fetchClients');
      dispatch(fetchClients());
    }
  }, [status, dispatch]);

  useEffect(() => {
    console.log('Clients updated:', clients);
  }, [clients]);

  useEffect(() => {
    console.log('Status updated:', status);
  }, [status]);

  useEffect(() => {
    console.log('Error updated:', error);
  }, [error]);

  const handleClientSelect = (clientId) => {
    dispatch(setCurrentClient(clientId));
    navigate('/projects');
  };

  if (status === 'loading') {
    return <LoadingSpinner />;
  }

  if (status === 'failed') {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <Card>
        <CardHeader>
          <CardTitle className="text-2xl font-bold">Select a Client</CardTitle>
        </CardHeader>
        <CardContent>
        {Array.isArray(clients) && clients.length === 0 ? (
          <p>No clients available.</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {clients.map((client) => (
              <Button
                key={client.id}
                onClick={() => handleClientSelect(client.id)}
                variant="outline"
                className="h-24 text-lg"
              >
                {client.name}
              </Button>
            ))}
          </div>
        )}
      </CardContent>
      </Card>
    </div>
  );
};

export default ClientSelector;