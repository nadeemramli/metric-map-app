from .utils import cache_result, get_dataframe_from_historical_data
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.conf import settings
import io

@cache_result()
def bulk_export_data(metric_id, start_date=None, end_date=None, data_type='raw'):
    df = get_dataframe_from_historical_data(metric_id)
    
    if start_date:
        df = df[df['date'] >= start_date]
    if end_date:
        df = df[df['date'] <= end_date]
    
    if data_type == 'raw':
        return df.to_dict('records')
    elif data_type == 'daily':
        return df.resample('D', on='date').mean().reset_index().to_dict('records')
    elif data_type == 'weekly':
        return df.resample('W', on='date').mean().reset_index().to_dict('records')
    elif data_type == 'monthly':
        return df.resample('M', on='date').mean().reset_index().to_dict('records')
    else:
        raise ValueError(f"Unknown data type: {data_type}")

def process_google_sheet_for_import(sheet_url):
    # Extract the sheet ID from the URL
    sheet_id = sheet_url.split('/')[5]

    # Set up the Google Sheets API client
    creds = Credentials.from_authorized_user_file(settings.GOOGLE_SHEETS_CREDENTIALS_FILE)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API to get the data
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range='A:Z').execute()
    values = result.get('values', [])

    if not values:
        raise ValueError('No data found in the Google Sheet')

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(values[1:], columns=values[0])

    # Perform any necessary data cleaning or formatting
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    # You might want to add more data validation or cleaning steps here

    return df.to_dict('records')

@cache_result(timeout=60)  # Cache for 1 minute, adjust as needed
def prepare_data_for_bulk_import(sheet_url):
    try:
        processed_data = process_google_sheet_for_import(sheet_url)
        return {
            'status': 'success',
            'data': processed_data,
            'message': f'Successfully processed {len(processed_data)} rows of data'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Error processing Google Sheet: {str(e)}'
        }