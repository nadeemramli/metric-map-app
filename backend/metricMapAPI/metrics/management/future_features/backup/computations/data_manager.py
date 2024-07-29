# data_manager.py

import pandas as pd
import json
from typing import List, Dict, Union, Any
import io

class DataManagerResult:
    def __init__(self, manager_id: int, operation_type: str, result: Dict[str, Any]):
        self.manager_id = manager_id
        self.operation_type = operation_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'manager_id': self.manager_id,
            'operation_type': self.operation_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class DataManager:
    def __init__(self, manager_id: int):
        self.manager_id = manager_id

    def update_historical_data(self, historical_data: pd.DataFrame, new_data: pd.DataFrame) -> DataManagerResult:
        updated_data = pd.concat([historical_data, new_data], ignore_index=True)
        updated_data = updated_data.sort_values('date').reset_index(drop=True)
        return DataManagerResult(
            self.manager_id,
            'update_historical_data',
            {'updated_data': updated_data.to_dict(orient='records')}
        )

    def bulk_import(self, file_content: str, file_format: str) -> DataManagerResult:
        if file_format == 'csv':
            data = pd.read_csv(io.StringIO(file_content))
        elif file_format == 'json':
            data = pd.read_json(io.StringIO(file_content))
        elif file_format == 'excel':
            data = pd.read_excel(io.BytesIO(file_content.encode()))
        else:
            raise ValueError(f"Unsupported file format: {file_format}")
        
        # Here you would typically save this data to your database
        # For now, we'll just return it as part of the result
        return DataManagerResult(
            self.manager_id,
            'bulk_import',
            {'imported_data': data.to_dict(orient='records')}
        )

    def bulk_export(self, data: pd.DataFrame, file_format: str) -> DataManagerResult:
        if file_format == 'csv':
            export_content = data.to_csv(index=False)
        elif file_format == 'json':
            export_content = data.to_json(orient='records')
        elif file_format == 'excel':
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                data.to_excel(writer, index=False)
            export_content = output.getvalue()
        else:
            raise ValueError(f"Unsupported file format: {file_format}")
        
        return DataManagerResult(
            self.manager_id,
            'bulk_export',
            {'exported_data': export_content}
        )

    @classmethod
    def run_operation(cls, manager_id: int, operation_type: str, **kwargs) -> DataManagerResult:
        manager = cls(manager_id)
        
        if operation_type == 'update_historical_data':
            return manager.update_historical_data(kwargs['historical_data'], kwargs['new_data'])
        elif operation_type == 'bulk_import':
            return manager.bulk_import(kwargs['file_content'], kwargs['file_format'])
        elif operation_type == 'bulk_export':
            return manager.bulk_export(kwargs['data'], kwargs['file_format'])
        else:
            raise ValueError(f"Unknown operation type: {operation_type}")

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)