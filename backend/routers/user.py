from fastapi import APIRouter
from models.user_model import User

# Create a router for user-related endpoints
# All routes will be prefixed with /user
router = APIRouter(prefix="/user", tags=["User"])

# Temporary in-memory database (for testing/demo purposes)
fake_db = []


@router.post("/create")
def create_user(user: User):
    """
    Create a new user.

    The user data is validated using the User Pydantic model
    and stored in a temporary in-memory list.
    """
    # Add the user to the fake database
    fake_db.append(user)

    # Return success message along with created user
    return {
        "message": "User created successfully",
        "user": user
    }


@router.get("/all")
def get_users():
    """
    Retrieve all users from the fake database.
    """
    return fake_db
