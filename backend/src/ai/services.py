from google import genai

from src.utils.settings import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

MODEL_NAME = "gemini-3.1-flash-lite"


def generate_learning_roadmap(
    missing_skills: str
):

    prompt = f"""
    You are an interview preparation assistant and learning roadmap generation expert.

    Create a 4-week learning roadmap to learn and strengthen these skills:

    {missing_skills}

    Return ONLY in this format:

    WEEK 1
    - task
    - task
    - task

    WEEK 2
    - task
    - task
    - task

    WEEK 3
    - task
    - task
    - task

    WEEK 4
    - task
    - task
    - task

    Rules:
    - Do not repeat the skill names as a separate section.
    - Do not explain why the skills are important.
    - Do not add introductions or conclusions.
    - Output only the roadmap.
    - Keep tasks practical and actionable.
    - Keep each task description small in one line.
    """

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        return "Unable to generate learning roadmap at the moment."

def calculate_missing_skills(
    matches,
    jd_skills
):
    """
    Returns JD skills that did not get matched.
    """

    matched = {
        match["jd_skill"]
        for match in matches
    }

    missing = [
        skill
        for skill in jd_skills
        if skill not in matched
    ]

    return missing