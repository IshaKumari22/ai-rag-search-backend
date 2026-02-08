from pydantic import BaseModel

class StoryCreate(BaseModel):
    title: str
    description: str
    genre: str
    duration_minutes: int
    transcript: str
