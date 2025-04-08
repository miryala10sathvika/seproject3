from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    # Dummy user list endpoint
    return {"message": "User list placeholder"}
