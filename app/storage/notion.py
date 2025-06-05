from notion_client import Client
from app.config import settings

def append_to_notion(message: str, sender: str, date: str):
    if not all([settings.NOTION_INTEGRATION_TOKEN, settings.NOTION_DATABASE_ID]):
        return

    notion = Client(auth=settings.NOTION_INTEGRATION_TOKEN)
    notion.pages.create(
        parent={"database_id": settings.NOTION_DATABASE_ID},
        properties={
            "Message": {"title": [{"text": {"content": message}}]},
            "Sender": {"rich_text": [{"text": {"content": sender}}]},
            "Date": {"rich_text": [{"text": {"content": date}}]}
        }
    )