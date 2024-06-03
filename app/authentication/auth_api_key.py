import os
import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# A helper function that sets the api_key for any dependant call
def get_api_key():
    api_key = os.getenv('API_KEY')
    if not api_key:
        logger.info('API key not found')
        raise HTTPException(status_code=500, detail="API key not found")
    logger.info('API key retrieved')
    return api_key
