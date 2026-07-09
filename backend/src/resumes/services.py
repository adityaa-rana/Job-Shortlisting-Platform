# import fitz
# def extract_text_from_pdf(file_path:str):
#     document=fitz.open(file_path)

#     text=""

#     for page in document:
#         text+=page.get_text()
    
#     document.close()
#     return text


# def extract_skills(text:str):

#     text=text.lower()

#     skills=[
#         "python",
#         "java",
#         "c++",
#         "sql",
#         "mysql",
#         "postgresql",
#         "fastapi",
#         "django",
#         "flask",
#         "react",
#         "javascript",
#         "html",
#         "css",
#         "docker",
#         "git",
#         "machine learning",
#         "deep learning",
#         "tensorflow",
#         "pytorch",
#         "pandas",
#         "numpy"
#     ]

#     found_skills=[]

#     for skill in skills:
#         if skill in text:
#             found_skills.append(skill)

#     return list(set(found_skills))