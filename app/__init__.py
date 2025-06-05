from fastapi import FastAPI
from app.router import router as whatsapp_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WhatsApp CRM",
              version="1.0")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["GET", "POST"],
                   allow_headers=["*"])

app.include_router(whatsapp_router, prefix="/api", tags=["Whatsapp CRM Manager"])
