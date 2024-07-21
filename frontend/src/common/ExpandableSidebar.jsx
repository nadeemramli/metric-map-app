import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { 
    LayoutDashboard,
    BarChart2,
    GitBranch,
    Cog, 
    ListChecks, 
    LineChart, 
    ClipboardList,
    Target, 
    Network, 
    Settings, 
    LogOut,
    ChevronRight, ChevronLeft 
  } from 'lucide-react';
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

const sidebarItems = [
    { icon: LayoutDashboard, label: 'Dashboard', path: '/dashboard' },
    { icon: BarChart2, label: 'Metrics', path: '/metrics' },
    { icon: LineChart, label: 'Strategy', path: '/strategy' },
    { icon: ClipboardList, label: 'Execution', path: '/execution' },
    { icon: GitBranch, label: 'Relationships', path: '/relationships' },
  ];

const SidebarButton = ({ icon: Icon, label, path, isActive, expanded }) => (
  <Link to={path} className="w-full">
    <Button
      variant="ghost"
      size="icon"
      className={cn(
        "w-full h-12 p-3 justify-start transition-all duration-300 ease-in-out",
        isActive ? 'bg-secondary' : '',
        expanded ? 'pl-4' : ''
      )}
    >
      <Icon className="h-5 w-5 shrink-0" />
      {expanded && <span className="ml-3">{label}</span>}
      {!expanded && <span className="sr-only">{label}</span>}
    </Button>
  </Link>
);

const ExpandableSidebar = () => {
  const [expanded, setExpanded] = useState(false);
  const location = useLocation();

  return (
    <aside 
      className={cn(
        "fixed inset-y-0 left-0 z-10 flex flex-col bg-background transition-all duration-300 ease-in-out",
        expanded ? "w-64" : "w-16"
      )}
    >
      <div className="flex items-center justify-between p-4">
        <Link to="/dashboard" className={cn(
          "flex items-center justify-center rounded-lg bg-primary text-primary-foreground",
          expanded ? "h-8 w-8" : "h-8 w-8"
        )}>
          <LayoutDashboard className="h-5 w-5" />
        </Link>
        <Button
          variant="ghost"
          size="icon"
          onClick={() => setExpanded(!expanded)}
          className={cn("absolute right-0 top-4 transition-all duration-300 ease-in-out", 
            expanded ? "-right-4 bg-background" : ""
          )}
        >
          {expanded ? <ChevronLeft className="h-4 w-4" /> : <ChevronRight className="h-4 w-4" />}
        </Button>
      </div>
      <nav className="flex flex-col items-center gap-2 p-2">
        {sidebarItems.map((item) => (
          <SidebarButton
            key={item.path}
            icon={item.icon}
            label={item.label}
            path={item.path}
            isActive={location.pathname.startsWith(item.path)}
            expanded={expanded}
          />
        ))}
      </nav>
    </aside>
  );
};

export default ExpandableSidebar;