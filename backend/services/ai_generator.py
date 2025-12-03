import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_quiz(topic, difficulty, num_questions, input_text=""):
    prompt = f"""
    You are SmartQuizzer, an adaptive quiz generator.

    Topic/Text: {topic or input_text}
    Difficulty: {difficulty}
    Number of questions: {num_questions}

    Generate multiple-choice questions with 4 options.
    Provide: question, options, correct_answer, explanation, difficulty.
    Output must be valid JSON ONLY.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
