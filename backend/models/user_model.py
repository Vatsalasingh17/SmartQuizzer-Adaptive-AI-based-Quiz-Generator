from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    preferred_difficulty: str = "medium"
