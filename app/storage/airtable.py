from pyairtable import Table
from app.config import settings

def append_to_airtable(data: dict):
    if not all([settings.AIRTABLE_API_KEY, settings.AIRTABLE_BASE_ID, settings.AIRTABLE_TABLE_NAME]):
        return

    table = Table(settings.AIRTABLE_API_KEY, settings.AIRTABLE_BASE_ID, settings.AIRTABLE_TABLE_NAME)
    table.create(data)
