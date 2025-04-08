from sqlalchemy import Column, Integer, String, Text
from app.database.base import Base

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
