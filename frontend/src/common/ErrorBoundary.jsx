import React from 'react';
import { toast } from 'react-toastify';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({ error, errorInfo });
    
    // Log the error
    console.error("Uncaught error:", error, errorInfo);

    // Log additional information about the error
    console.log("Error occurred in component:", errorInfo.componentStack);
    console.log("Error message:", error.message);
    console.log("Error stack:", error.stack);

    // Show a toast notification
    toast.error("An unexpected error occurred. Our team has been notified.");

    // Here you could send the error to an error tracking service
    // For example, if using Sentry:
    // Sentry.captureException(error);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div className="error-boundary p-4 bg-red-100 border border-red-400 text-red-700 rounded">
          <h1 className="text-xl font-bold mb-2">Oops! Something went wrong.</h1>
          <p className="mb-4">We're sorry for the inconvenience. Please try refreshing the page or contact support if the problem persists.</p>
          {this.props.showDetails && (
            <details className="mt-4">
              <summary className="cursor-pointer">Error Details</summary>
              <pre className="mt-2 p-2 bg-red-50 rounded overflow-auto">
                {this.state.error && this.state.error.toString()}
                <br />
                {this.state.errorInfo && this.state.errorInfo.componentStack}
              </pre>
            </details>
          )}
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;