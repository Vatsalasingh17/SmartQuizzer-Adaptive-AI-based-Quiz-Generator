from fastapi import APIRouter
from models.user_model import User

router = APIRouter(prefix="/user", tags=["User"])

fake_db = []

@router.post("/create")
def create_user(user: User):
    fake_db.append(user)
    return {"message": "User created successfully", "user": user}

@router.get("/all")
def get_users():
    return fake_db
