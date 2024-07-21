// src/utils/exportData.js
import { saveAs } from 'file-saver';
import * as XLSX from 'xlsx';

export const exportToCSV = (data, fileName) => {
  const blob = new Blob([data], { type: 'text/csv;charset=utf-8;' });
  saveAs(blob, fileName);
};

export const exportToExcel = (data, fileName) => {
  const ws = XLSX.utils.json_to_sheet(data);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "Sheet1");
  const excelBuffer = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });
  const blob = new Blob([excelBuffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8' });
  saveAs(blob, fileName);
};

// src/components/ExportButton.jsx
import React from 'react';
import { exportToCSV, exportToExcel } from './exportData';

const ExportButton = ({ data, fileName }) => {
  const handleExport = (format) => {
    if (format === 'csv') {
      exportToCSV(data, `${fileName}.csv`);
    } else if (format === 'excel') {
      exportToExcel(data, `${fileName}.xlsx`);
    }
  };

  return (
    <div>
      <button onClick={() => handleExport('csv')}>Export to CSV</button>
      <button onClick={() => handleExport('excel')}>Export to Excel</button>
    </div>
  );
};

export default ExportButton;