from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    # Dummy login endpoint
    return {"message": "Login endpoint placeholder"}
