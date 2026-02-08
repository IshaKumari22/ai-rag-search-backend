from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.story_service import create_story, filter_stories
from app.services.search_service import semantic_search, rag_search
from app.api.schemas.story_schema import StoryCreate
from app.core.logging import logger

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- STORIES --------

@router.post("/stories")
def add_story(story: StoryCreate, db: Session = Depends(get_db)):
    return create_story(db, story.dict())

@router.get("/stories/filter")
def filter_by_genre(genre: str, db: Session = Depends(get_db)):
    return filter_stories(db, genre)

# -------- SEARCH --------

@router.get("/search")
def search(query: str, db: Session = Depends(get_db)):
    return semantic_search(db, query)

# -------- RAG SEARCH --------

@router.get("/rag-search")
def rag_search_api(query: str, db: Session = Depends(get_db)):
    logger.info(f"RAG search requested: {query}")
    return {"response": rag_search(db, query)}
