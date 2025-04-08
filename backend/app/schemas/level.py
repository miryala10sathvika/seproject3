from pydantic import BaseModel

class LevelBase(BaseModel):
    name: str
    description: str

class LevelResponse(LevelBase):
    id: int

    class Config:
        orm_mode = True
