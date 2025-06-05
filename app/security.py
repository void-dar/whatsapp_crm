from fastapi import HTTPException, Query

def verify_access_key(access_key: str = Query(...)):
    from config import settings
    if access_key != settings.ACCESS_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing access key")
