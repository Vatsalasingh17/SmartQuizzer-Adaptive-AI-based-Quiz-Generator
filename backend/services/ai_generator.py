import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file (including the API key)
load_dotenv()

# Initialize OpenAI client using API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_quiz(topic, difficulty, num_questions, input_text=""):
    """
    Generates a multiple-choice quiz in JSON format using the OpenAI API.

    Args:
        topic (str): The subject or theme of the quiz.
        difficulty (str): Difficulty level (e.g., easy, medium, hard).
        num_questions (int): Number of questions to generate.
        input_text (str): Optional text to base questions on.

    Returns:
        str: The model's JSON-formatted quiz output.
    """

    # Construct the prompt given to the model
    prompt = f"""
    You are SmartQuizzer, an adaptive quiz generator.

    Topic/Text: {topic or input_text}
    Difficulty: {difficulty}
    Number of questions: {num_questions}

    Generate multiple-choice questions with 4 options.
    Provide: question, options, correct_answer, explanation, difficulty.
    Output must be valid JSON ONLY.
    """

    # Send the prompt to OpenAI's chat completion endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract and return the model's reply (JSON string)
    return response.choices[0].message.content
