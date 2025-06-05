from fastapi import FastAPI
from app.main import router as whatsapp_router

app = FastAPI(title="WhatsApp CRM")

app.include_router(whatsapp_router, prefix="api/", tags=["Whatsapp CRM Manager"])
