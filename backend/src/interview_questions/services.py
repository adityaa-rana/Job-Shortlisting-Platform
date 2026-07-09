from google import genai

from src.utils.settings import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

MODEL_NAME = "gemini-3.1-flash-lite"


def generate_interview_questions(
    skills: str
):

    prompt = f"""
    You are an interview preparation assistant.

    Generate interview questions for these skills:

    {skills}

    Return ONLY in the following format:

    BEGINNER

    1.
    2.
    3.
    4.
    5.

    INTERMEDIATE

    1.
    2.
    3.
    4.
    5.

    ADVANCED

    1.
    2.
    3.
    4.
    5.

    Do not add introductions, explanations, markdown, notes, or extra text.
    Keep only 5 questions for each section.
    """

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        return "Unable to generate interview questions at the moment."