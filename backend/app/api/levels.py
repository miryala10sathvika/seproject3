from fastapi import APIRouter
from app.services.level_service import get_all_levels

router = APIRouter()

@router.get("/")
def get_levels():
    levels = get_all_levels()
    return {"levels": levels}
