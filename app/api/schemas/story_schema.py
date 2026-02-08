from pydantic import BaseModel

class StoryCreate(BaseModel):
    title: str
    genre: str
    transcript: str
