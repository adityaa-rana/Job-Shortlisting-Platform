from typing import List


NORMALIZATION_MAP = {

    # Languages
    "cpp": "C++",
    "c plus plus": "C++",
    "cplusplus": "C++",

    "js": "JavaScript",
    "ts": "TypeScript",

    # Frontend
    "reactjs": "React",
    "react.js": "React",

    "vuejs": "Vue.js",

    "nextjs": "Next.js",

    "node": "Node.js",
    "nodejs": "Node.js",

    # Database
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",

    "mongo": "MongoDB",

    # AI
    "ml": "Machine Learning",

    "dl": "Deep Learning",

    "tf": "TensorFlow",

    "hf": "Hugging Face",

    # Cloud
    "amazon web services": "AWS",

    # General
    "rest": "REST API",
    "restful api": "REST API"
}


def normalize_skills(skills: List[str]) -> List[str]:

    normalized = set()

    for skill in skills:

        key = skill.strip().lower()

        if key in NORMALIZATION_MAP:

            normalized.add(
                NORMALIZATION_MAP[key]
            )

        else:

            normalized.add(
                skill.strip()
            )

    return sorted(normalized)