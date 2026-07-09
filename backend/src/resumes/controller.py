from src.resumes.models import resumeModel
from fastapi import UploadFile,HTTPException,status
from sqlalchemy.orm import Session
import os
from src.ai.parser import extract_text_from_pdf
from src.ai.preprocessing import clean_text
from src.ai.extractor import extract_skills
from src.ai.normalizer import normalize_skills


def upload_resume(file:UploadFile,current_user,db:Session):

    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidates can upload resume")

    upload_dir="uploads/resumes"

    os.makedirs(upload_dir,exist_ok=True)

    file_path=f"{upload_dir}/{file.filename}"

    with open(file_path,"wb") as f:
        f.write(file.file.read())

    
    text = extract_text_from_pdf(file_path)

    text = clean_text(text) 
    skills=extract_skills(text)
    normalized_skills = normalize_skills(skills)

    new_resume=resumeModel(
        candidate_id=current_user.id,
        file_path=file_path,
        extracted_text=text,
        extracted_skills=", ".join(normalized_skills)

    )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    return new_resume

def get_all_resumes(current_user,db:Session):

    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidate can see resume")

    resumes=db.query(resumeModel).filter(resumeModel.candidate_id==current_user.id).all()

    return resumes

def get_resume(resume_id:int,current_user,db:Session):

    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidate can see resume")

    resume=db.query(resumeModel).filter(resumeModel.id==resume_id).first()

    if not resume:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resume not found")

    if resume.candidate_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Access denied")

    return resume

def delete_resume(resume_id:int,current_user,db:Session):

    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidate can delete resume")

    resume=db.query(resumeModel).filter(resumeModel.id==resume_id).first()

    if not resume:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resume not found")

    if resume.candidate_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Access denied")

    if os.path.exists(resume.file_path):
        os.remove(resume.file_path)

    db.delete(resume)
    db.commit()

    return None


# not requiree
def analyze_resume(resume_id:int,current_user,db:Session):

    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidate can see resume")

    resume=db.query(resumeModel).filter(resumeModel.id==resume_id).first()

    if not resume:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resume not found")

    if resume.candidate_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Access denied")

    extracted_text=extract_text_from_pdf(resume.file_path)

    skills=extract_skills(extracted_text)

    resume.extracted_text=extracted_text
    resume.extracted_skills=", ".join(skills)


    db.commit()
    db.refresh(resume)

    return resume