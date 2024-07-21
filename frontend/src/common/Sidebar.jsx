import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { logout} from '@/store/slices/userSlice';
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
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
  LogOut 
} from 'lucide-react';

const sidebarItems = [
  { icon: LayoutDashboard, label: 'Dashboard', path: '/dashboard' },
  { icon: BarChart2, label: 'Metrics', path: '/metrics' },
  { icon: LineChart, label: 'Strategy', path: '/strategy' },
  { icon: ClipboardList, label: 'Execution', path: '/execution' },
  { icon: GitBranch, label: 'Relationships', path: '/relationships' },
];

const SidebarButton = ({ icon: Icon, label, path, isActive }) => (
  <TooltipProvider>
    <Tooltip>
      <TooltipTrigger asChild>
        <Link to={path}>
          <Button
            variant="ghost"
            size="icon"
            className={cn(
              "w-full h-12 p-3 justify-center",
              isActive ? "bg-gray-800 text-white" : "text-gray-400 hover:text-white hover:bg-gray-800"
            )}
          >
            <Icon className="h-5 w-5" />
          </Button>
        </Link>
      </TooltipTrigger>
      <TooltipContent side="right">
        <p>{label}</p>
      </TooltipContent>
    </Tooltip>
  </TooltipProvider>
);

const Sidebar = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleLogout = async () => {
    try {
      await dispatch(logout()).unwrap();
      navigate('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <aside className="bg-gray-900 h-screen w-16 flex flex-col items-center py-4">
      <div className="mb-8 flex items-center justify-center w-full h-12">
        <Target className="h-6 w-6 text-white" />
      </div>
      <nav className="flex-1 flex flex-col items-center space-y-2 w-full">
        {sidebarItems.map((item) => (
          <SidebarButton
            key={item.path}
            icon={item.icon}
            label={item.label}
            path={item.path}
            isActive={location.pathname === item.path}
          />
        ))}
      </nav>
      <div className="mt-auto space-y-2 w-full">
        <SidebarButton icon={Cog} label="Settings" path="/settings" isActive={location.pathname === '/settings'} />
        <TooltipProvider>
          <Tooltip>
            <TooltipTrigger asChild>
              <Button
                variant="ghost"
                size="icon"
                className="w-full h-12 p-3 justify-center text-gray-400 hover:text-white hover:bg-gray-800"
                onClick={handleLogout}
              >
                <LogOut className="h-5 w-5" />
              </Button>
            </TooltipTrigger>
            <TooltipContent side="right">
              <p>Logout</p>
            </TooltipContent>
          </Tooltip>
        </TooltipProvider>
      </div>
    </aside>
  );
};

export default Sidebar;