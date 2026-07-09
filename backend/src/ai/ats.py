def calculate_ats_score(matches, total_jd_skills):
    """
    Calculates ATS score from semantic matches.
    """

    if total_jd_skills == 0:
        return 0

    total_similarity = sum(
        match["similarity"]
        for match in matches
    )

    ats_score = (total_similarity / total_jd_skills) * 100

    return round(ats_score, 2)


