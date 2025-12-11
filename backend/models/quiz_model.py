from pydantic import BaseModel
from typing import List

class QuizRequest(BaseModel):
    topic: str | None = None
    input_text: str | None = None
    difficulty: str = "easy"
    num_questions: int = 5

class AnswerItem(BaseModel):
    question: str
    correct_answer: str
    user_answer: str

class SubmitQuizRequest(BaseModel):
    difficulty: str
    answers: List[AnswerItem]
