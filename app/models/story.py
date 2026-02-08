from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    genre = Column(String, index=True)
    duration_minutes = Column(Integer)
    transcript = Column(Text)
