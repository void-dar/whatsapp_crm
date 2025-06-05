from google.oauth2 import service_account
from googleapiclient.discovery import build
from app.config import settings

def append_to_sheet(data: list[str]):
    creds = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_SERVICE_ACCOUNT_KEY
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    sheet.values().append(
        spreadsheetId=settings.GOOGLE_SHEET_ID,
        range="Sheet1!A1",
        valueInputOption="USER_ENTERED",
        body={"values": [data]},
    ).execute()