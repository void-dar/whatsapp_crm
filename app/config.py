from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Settings(BaseSettings):
    APP_SECRET_KEY: str

    # Twilio
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_WHATSAPP_NUMBER: str

    # Google Sheets
    GOOGLE_SERVICE_ACCOUNT_FILE: Path
    GOOGLE_SHEET_ID: str

    # Airtable (optional)
    AIRTABLE_API_KEY: str | None = None
    AIRTABLE_BASE_ID: str | None = None
    AIRTABLE_TABLE_NAME: str | None = None

    # Notion (optional)
    NOTION_INTEGRATION_TOKEN: str | None = None
    NOTION_DATABASE_ID: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()


