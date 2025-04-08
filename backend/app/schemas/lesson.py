from pydantic import BaseModel

class LessonBase(BaseModel):
    title: str
    content: str

class LessonResponse(LessonBase):
    id: int

    class Config:
        orm_mode = True
