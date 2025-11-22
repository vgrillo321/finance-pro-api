from fastapi import FastAPI
from app.api.routes import router as api_router
# 👇 IMPORTANTE: esto carga todos los modelos, incluido Account
import app.db.models

app = FastAPI(title="FINANCIERO PRO API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")
