from fastapi import HTTPException, Query
from .config import settings

def verify_access_key(access_key: str = Query(...)):
    
    if access_key != settings.ACCESS_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing access key")
