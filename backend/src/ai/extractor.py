import json
from pathlib import Path

import spacy
from spacy.matcher import PhraseMatcher

# Path to skills database
BASE_DIR = Path(__file__).parent
SKILLS_PATH = BASE_DIR / "data" / "skills.json"

# Load spaCy model only once when server starts
nlp = spacy.load("en_core_web_sm")

# Load skills database
with open(SKILLS_PATH, "r", encoding="utf-8") as file:
    skills = json.load(file)

# Create PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Create patterns
patterns = [nlp.make_doc(skill) for skill in skills]

matcher.add("SKILLS", patterns)


def extract_skills(text: str) -> list[str]:
    """
    Extract skills from text using spaCy PhraseMatcher.
    """

    doc = nlp(text)

    matches = matcher(doc)

    found_skills = set()

    for _, start, end in matches:
        found_skills.add(doc[start:end].text)

    return sorted(found_skills)