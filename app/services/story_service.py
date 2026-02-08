from sqlalchemy.orm import Session
from app.models.story import Story
from app.services.embedding_service import generate_embedding
from app.services.vector_store import add_vector

def create_story(db: Session, story_data: dict):
    combined_text = f"{story_data['title']} {story_data['description']} {story_data.get('transcript', '')}"

    try:
        embedding = generate_embedding(combined_text)
    except Exception as e:
        print("Embedding failed:", e)
        embedding = None  # allow DB save

    story = Story(**story_data)
    db.add(story)
    db.commit()
    db.refresh(story)

    # vector store is optional for demo
    if embedding:
        try:
            from app.services.vector_store import add_vector
            add_vector(story.id, embedding)
        except Exception as e:
            print("Vector store failed:", e)

    return story



def get_all_stories(db: Session):
    return db.query(Story).all()

def filter_stories(db: Session, genre: str):
    return db.query(Story).filter(Story.genre == genre).all()
