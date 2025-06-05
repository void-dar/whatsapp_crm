from google.oauth2 import service_account
from googleapiclient.discovery import build
from app.config import settings
import json

service_acc_info = settings.GOOGLE_SERVICE_ACCOUNT_KEY
service_acc_info = json.loads(service_acc_info)

def append_to_sheet(data: list[str]):
    creds = service_account.Credentials.from_service_account_info(service_acc_info)
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    sheet.values().append(
        spreadsheetId=settings.GOOGLE_SHEET_ID,
        range="Sheet1!A1",
        valueInputOption="USER_ENTERED",
        body={"values": [data]},
    ).execute()