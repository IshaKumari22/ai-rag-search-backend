from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base, engine
from app.models import story


Base.metadata.create_all(bind=engine)
app=FastAPI(title="AI-Ready Search Backend (RAG)")


app.include_router(router)
@app.get("/")
def health_check():
    return {"status":"Backend running successfully"}

