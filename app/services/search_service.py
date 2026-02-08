from sqlalchemy.orm import Session
from app.services.embedding_service import generate_embedding
from app.services.vector_store import search_vectors
from app.models.story import Story
from app.services.generation_service import generate_response
from app.core.cache import redis_client


def semantic_search(db: Session, query: str):
    query_embedding = generate_embedding(query)
    story_ids = search_vectors(query_embedding)

    print("Vector search returned IDs:", story_ids)

    return db.query(Story).filter(Story.id.in_(story_ids)).all()

def rag_search(db: Session, query: str):
    if not query.strip():
        return "Query cannot be empty."

    results = semantic_search(db, query)
    if not results:
        return "No relevant data found."

    return generate_response(query, results)
