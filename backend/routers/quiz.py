from fastapi import APIRouter
from services.ai_generator import generate_quiz
from services.adaptive_engine import calculate_next_difficulty

router = APIRouter(prefix="/quiz")

@router.post("/generate")
def generate_quiz_api(data: dict):
    return generate_quiz(
        topic=data.get("topic"),
        difficulty=data.get("difficulty", "easy"),
        num_questions=data.get("num_questions", 5),
        input_text=data.get("input_text", "")
    )

@router.post("/submit")
def submit_answers(data: dict):
    answers = data["answers"]
    correct = sum(1 for a in answers if a["user_answer"] == a["correct_answer"])
    score = correct / len(answers)

    next_difficulty = calculate_next_difficulty(score, data["difficulty"])
    
    return {
        "score": score,
        "correct": correct,
        "next_difficulty": next_difficulty
    }
