# import fitz

# def extract_text_from_pdf(file_path:str):
#     document=fitz.open(file_path)
#     text=""
#     for page in document:
#         text+=page.get_text()

#     document.close()
#     return text


# # similarity score generation using nlp and cosine similarity
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

# model = SentenceTransformer("all-MiniLM-L6-v2")

# def calculate_similarity(text1:str,text2:str):
#     embeddings=model.encode([text1,text2])
#     similarity=cosine_similarity(
#         [embeddings[0]],
#         [embeddings[1]]
#     )[0][0]
#     return round(similarity*100,2)



# def extract_skills(text:str):
#     text=text.lower()
#     skills=[
#         "python","java","c++","sql","postgresql",
#         "mysql","fastapi","django","flask",
#         "react","javascript","html","css",
#         "docker","git","machine learning",
#         "deep learning","tensorflow","pytorch",
#         "pandas","numpy"
#     ]
#     found=[]
#     for skill in skills:
#         if skill in text:
#             found.append(skill)

#     return list(set(found))



# def calculate_ats_score(resume_skills:str,jd_skills:str):

#     resume_set=set(skill.strip().lower() for skill in resume_skills.split(","))

#     jd_set=set(skill.strip().lower() for skill in jd_skills.split(","))

#     if len(jd_set)==0:
#         return 0

#     matched=len(resume_set.intersection(jd_set))

#     return round((matched/len(jd_set))*100,2)