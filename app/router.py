from fastapi import APIRouter, Request, HTTPException, Query, Depends, status, Form
from app.storage.sheet_utils import append_to_sheet
from app.storage.airtable import append_to_airtable
from app.storage.notion import append_to_notion
from datetime import datetime
from .security import verify_access_key

router = APIRouter()

@router.post("/webhook", status_code=status.HTTP_202_ACCEPTED)
async def whatsapp_webhook(request: Request, From = Form(...), Body = Form(...) , type: str = Query(default="sheet"), _: None = Depends(verify_access_key)):
    form = await request.form()
    sender = From
    body = Body
    date = datetime.now().isoformat()

    if not sender or not body:
        print(f"{sender} and {body}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid message")

    if type == "sheet":
        append_to_sheet([sender, body, date])

    if type == "airtable":
        append_to_airtable({"Sender": sender, "Message": body, "Date": date})

    if type == "notion":
        append_to_notion(body, sender, date)

    return {"Event": "Message received"}

@router.get("/", status_code=status.HTTP_202_ACCEPTED)
async def test_connection():
    return status.HTTP_200_OK