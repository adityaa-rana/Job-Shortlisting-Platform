# def calculate_missing_skills(
#     resume_skills: str,
#     jd_skills: str
# ):

#     resume_set = set(
#         skill.strip().lower()
#         for skill in resume_skills.split(",")
#         if skill.strip()
#     )

#     jd_set = set(
#         skill.strip().lower()
#         for skill in jd_skills.split(",")
#         if skill.strip()
#     )

#     missing = list(
#         jd_set - resume_set
#     )

#     return ",".join(missing)