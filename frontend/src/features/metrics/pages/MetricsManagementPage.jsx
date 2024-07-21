import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Search, ListFilter, FileDown, Plus, MoreHorizontal, Loader2 } from 'lucide-react';
import { 
  fetchMetrics, 
  selectAllMetrics,
  deleteMetric
} from '@/store/slices/metricsSlice';
import { selectAllTags, fetchTags } from '@/store/slices/tagsSlice';
import { selectAllConnections, fetchConnections } from '@/store/slices/connectionsSlice';
import { selectAllExperiments, fetchExperiments } from '@/store/slices/actionRemarksSlice';
import { toast } from 'react-toastify';

const MetricsManagementPage = () => {
  const dispatch = useDispatch();
  const metrics = useSelector(selectAllMetrics);
  const tags = useSelector(selectAllTags);
  const connections = useSelector(selectAllConnections);
  const experiments = useSelector(selectAllExperiments);
  const metricStatus = useSelector(state => state.metrics.status);
  const metricError = useSelector(state => state.metrics.error);

  const [searchTerm, setSearchTerm] = useState('');
  const [activeTab, setActiveTab] = useState('all');
  const [visibleColumns, setVisibleColumns] = useState(['name', 'type', 'category', 'tags']);

  useEffect(() => {
    if (metricStatus === 'idle') {
      dispatch(fetchMetrics());
    }
    dispatch(fetchTags());
    dispatch(fetchConnections());
    dispatch(fetchExperiments());
  }, [dispatch, metricStatus]);

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleDelete = async (metricId) => {
    if (window.confirm('Are you sure you want to delete this metric?')) {
      try {
        await dispatch(deleteMetric({ metricId })).unwrap();
        toast.success('Metric deleted successfully');
      } catch (error) {
        toast.error(`Failed to delete metric: ${error.message}`);
      }
    }
  };

  const handleExport = () => {
    // Implement CSV export logic here
    console.log('Exporting metrics...');
  };

  const filteredMetrics = metrics.filter(metric =>
    metric.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    metric.type.toLowerCase().includes(searchTerm.toLowerCase()) ||
    metric.category.toLowerCase().includes(searchTerm.toLowerCase()) ||
    metric.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  const getDisplayData = () => {
    switch (activeTab) {
      case 'metrics':
        return filteredMetrics;
      case 'connections':
        return connections;
      case 'experiments':
        return experiments;
      default:
        return filteredMetrics;
    }
  };

  const displayData = getDisplayData();

  if (metricStatus === 'loading') {
    return <div className="flex justify-center items-center h-screen"><Loader2 className="h-8 w-8 animate-spin" /></div>;
  }

  if (metricError) {
    return <div>Error: {metricError}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Metrics Management</h1>
        <div className="flex items-center space-x-2">
          <div className="relative">
            <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
            <Input
              placeholder="Search metrics..."
              value={searchTerm}
              onChange={handleSearch}
              className="pl-8"
            />
          </div>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline" size="sm" className="h-8 gap-1">
                <ListFilter className="h-4 w-4" />
                Filter
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              {['name', 'type', 'category', 'tags', 'value', 'rhythm', 'confidence'].map((column) => (
                <DropdownMenuCheckboxItem
                  key={column}
                  checked={visibleColumns.includes(column)}
                  onCheckedChange={(checked) => {
                    if (checked) {
                      setVisibleColumns([...visibleColumns, column]);
                    } else {
                      setVisibleColumns(visibleColumns.filter((col) => col !== column));
                    }
                  }}
                >
                  {column.charAt(0).toUpperCase() + column.slice(1)}
                </DropdownMenuCheckboxItem>
              ))}
            </DropdownMenuContent>
          </DropdownMenu>
          <Button size="sm" onClick={handleExport}>
            <FileDown className="h-4 w-4 mr-2" />
            Export
          </Button>
          <Link to="/metrics/new">
            <Button size="sm">
              <Plus className="h-4 w-4 mr-2" />
              Add Metric
            </Button>
          </Link>
        </div>
      </div>

      <Tabs defaultValue="all" className="w-full" onValueChange={setActiveTab}>
        <TabsList>
          <TabsTrigger value="all">All</TabsTrigger>
          <TabsTrigger value="metrics">Metrics</TabsTrigger>
          <TabsTrigger value="connections">Connections</TabsTrigger>
          <TabsTrigger value="experiments">Experiments</TabsTrigger>
        </TabsList>

        <TabsContent value="all">
          <Card>
            <CardHeader>
              <CardTitle>All Metrics</CardTitle>
            </CardHeader>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    {visibleColumns.map((column) => (
                      <TableHead key={column}>{column.charAt(0).toUpperCase() + column.slice(1)}</TableHead>
                    ))}
                    <TableHead>Actions</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {displayData.map((item) => (
                    <TableRow key={item.id}>
                      {visibleColumns.map((column) => (
                        <TableCell key={`${item.id}-${column}`}>
                          {column === 'tags' 
                            ? item[column].map(tag => (
                                <Badge key={tag} variant="secondary" className="mr-1">
                                  {tag}
                                </Badge>
                              ))
                            : item[column]}
                        </TableCell>
                      ))}
                      <TableCell>
                        <DropdownMenu>
                          <DropdownMenuTrigger asChild>
                            <Button variant="ghost" size="sm">
                              <MoreHorizontal className="h-4 w-4" />
                            </Button>
                          </DropdownMenuTrigger>
                          <DropdownMenuContent align="end">
                            <Link to={`/metrics/${item.id}`}>
                              <DropdownMenuCheckboxItem>View/Edit</DropdownMenuCheckboxItem>
                            </Link>
                            <DropdownMenuCheckboxItem onSelect={() => handleDelete(item.id)}>
                              Delete
                            </DropdownMenuCheckboxItem>
                          </DropdownMenuContent>
                        </DropdownMenu>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Implement similar TabsContent for 'metrics', 'connections', and 'experiments' */}
      </Tabs>
    </div>
  );
};

export default MetricsManagementPage;