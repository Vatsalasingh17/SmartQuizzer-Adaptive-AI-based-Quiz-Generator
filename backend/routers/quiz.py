from fastapi import APIRouter
from services.ai_generator import generate_quiz
from services.adaptive_engine import calculate_next_difficulty

# Create a router for quiz-related endpoints
# All routes will be prefixed with /quiz
router = APIRouter(prefix="/quiz")


@router.post("/generate")
def generate_quiz_api(data: dict):
    """
    Generate a quiz based on topic, difficulty, and other parameters.
    
    Expected input (JSON):
    {
        "topic": "Math",
        "difficulty": "easy",
        "num_questions": 5,
        "input_text": "Optional reference text"
    }
    """
    return generate_quiz(
        # Topic of the quiz (e.g., Math, Science)
        topic=data.get("topic"),

        # Difficulty level, defaults to "easy" if not provided
        difficulty=data.get("difficulty", "easy"),

        # Number of questions, defaults to 5
        num_questions=data.get("num_questions", 5),

        # Optional input text for context-based quiz generation
        input_text=data.get("input_text", "")
    )


@router.post("/submit")
def submit_answers(data: dict):
    """
    Submit quiz answers and calculate score and next difficulty level.

    Expected input (JSON):
    {
        "answers": [
            {
                "user_answer": "A",
                "correct_answer": "A"
            }
        ],
        "difficulty": "easy"
    }
    """

    # Extract submitted answers
    answers = data["answers"]

    # Count how many answers are correct
    correct = sum(
        1 for a in answers
        if a["user_answer"] == a["correct_answer"]
    )

    # Calculate score as a fraction (0.0 - 1.0)
    score = correct / len(answers)

    # Determine next difficulty based on performance
    next_difficulty = calculate_next_difficulty(
        score,
        data["difficulty"]
    )

    # Return quiz results and adaptive difficulty
    return {
        "score": score,
        "correct": correct,
        "next_difficulty": next_difficulty
    }
