# utils.py

import logging
from functools import wraps
from typing import Any, Callable

logger = logging.getLogger(__name__)

def log_exceptions(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Exception in {func.__name__}: {str(e)}")
            raise
    return wrapper

def validate_metadata(metadata: dict, required_fields: list) -> bool:
    """
    Validate that all required fields are present in the metadata.
    """
    missing_fields = [field for field in required_fields if field not in metadata]
    if missing_fields:
        logger.error(f"Missing metadata fields: {', '.join(missing_fields)}")
        return False
    return True

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Safely perform division, returning a default value if the denominator is zero.
    """
    return numerator / denominator if denominator != 0 else default

# Add more utility functions as needed