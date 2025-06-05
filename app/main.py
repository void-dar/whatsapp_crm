from fastapi import APIRouter, Request, HTTPException, Query
from app.storage.sheet_utils import append_to_sheet
from app.storage.airtable import append_to_airtable
from app.storage.notion import append_to_notion
from typing import Optional
from datetime import datetime

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request, type: Optional[str] = Query("sheet")):
    form = await request.form()
    sender = form.get("From")
    body = form.get("Body")
    date = datetime.now().isoformat()

    if not sender or not body:
        raise HTTPException(status_code=400, detail="Invalid message")

    if type == "sheet":
        append_to_sheet([sender, body, date])

    if type == "airtable":
        append_to_airtable({"Sender": sender, "Message": body, "Date": date})

    if type == "notion":
        append_to_notion(body, sender, date)

    return "Message received"