from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_skill_matching(
    resume_skills: list[str],
    jd_skills: list[str],
    threshold: float = 0.75
):
    """
    Match every JD skill with the most similar Resume skill.
    """

    if not resume_skills or not jd_skills:
        return []

    # Encode both lists only once
    resume_embeddings = model.encode(
        resume_skills,
        convert_to_numpy=True
    )

    jd_embeddings = model.encode(
        jd_skills,
        convert_to_numpy=True
    )

    similarity_matrix = cosine_similarity(
        jd_embeddings,
        resume_embeddings
    )

    matches = []

    for jd_index, jd_skill in enumerate(jd_skills):

        similarities = similarity_matrix[jd_index]

        best_resume_index = np.argmax(similarities)

        best_similarity = float(
            similarities[best_resume_index]
        )

        if best_similarity >= threshold:

            matches.append({

                "jd_skill": jd_skill,

                "matched_skill":
                    resume_skills[best_resume_index],

                "similarity":
                    round(best_similarity, 3)

            })

    return matches