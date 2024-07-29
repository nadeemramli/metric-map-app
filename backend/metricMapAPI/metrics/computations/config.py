# config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    # Global logging level
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Maximum number of retries for database operations
    MAX_DB_RETRIES = int(os.getenv('MAX_DB_RETRIES', 3))
    
    # Timeout for long-running computations (in seconds)
    COMPUTATION_TIMEOUT = int(os.getenv('COMPUTATION_TIMEOUT', 300))

config = Config()