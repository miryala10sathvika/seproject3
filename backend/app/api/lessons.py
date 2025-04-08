from fastapi import APIRouter
from app.services.lesson_service import get_all_lessons

router = APIRouter()

@router.get("/")
def get_lessons():
    lessons = get_all_lessons()
    return {"lessons": lessons}
