import os
from fastapi import HTTPException


def get_api_key():
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise HTTPException(status_code=500, detail="API key not found")
    return api_key
