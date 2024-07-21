// src/components/common/Toast.jsx
import React from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export const showToast = (message, type = 'info') => {
  toast[type](message);
};

const Toast = () => {
  return <ToastContainer position="top-right" autoClose={3000} />;
};

export default Toast;