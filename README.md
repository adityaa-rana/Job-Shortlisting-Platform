
# HireWise AI : JOB APPLICATION AND RECRUITMENT PLATFORM  
An AI-powered Applicant Tracking System (ATS) that streamlines the recruitment process by enabling recruiters to create job postings, manage applications, and rank candidates using semantic resume analysis and AI-driven ATS scoring. Candidates can upload resumes, explore job opportunities, apply for suitable positions, and receive personalized AI-generated learning roadmaps for missing skills.

The platform combines **FastAPI**, **React**, **PostgreSQL**, **spaCy**, **Sentence Transformers**, and **Google Gemini** to automate resume screening, semantic skill matching, and candidate ranking.

---

# Why this Project?

Traditional recruitment often involves manually reviewing hundreds of resumes, making the hiring process time-consuming and prone to human bias. Conventional ATS systems rely heavily on exact keyword matching, causing highly qualified candidates to be overlooked when different terminologies or synonymous skills are used.

This project addresses these limitations by leveraging Natural Language Processing (NLP) and Semantic Similarity techniques to intelligently compare candidate resumes with job descriptions. Instead of relying solely on exact keyword matches, the platform understands contextual relationships between skills, resulting in more accurate ATS scores and candidate rankings.

Additionally, the system identifies missing skills and utilizes Google's Gemini API to generate personalized learning roadmaps, helping candidates improve their qualifications.

---

# Table of Contents

- Features
- Demo
- Tech Stack
- Project Workflow
- AI Pipeline
- AI Modules
- System Architecture
- Project Structure
- Database Schema
- Authentication Flow
- ATS Score Calculation
- API Endpoints
- Installation
- Challenges Faced
- Future Scope
- Project Outcome
- License

---

# Demo
## Login Page
<img width="953" height="551" alt="image" src="https://github.com/user-attachments/assets/f1ec4915-4ce6-432c-adf0-daa58135e63d" />

## Registration Page
<img width="767" height="572" alt="image" src="https://github.com/user-attachments/assets/cbafe7eb-e234-4e03-b4e7-ed55b5a40bbe" />


## Candidate Dashboard
<img width="1915" height="696" alt="Screenshot 2026-07-10 003230" src="https://github.com/user-attachments/assets/fe04a2e8-ce84-4ab6-b3d8-dfecc10d232f" />

## Candidate Resumes
<img width="1918" height="981" alt="Screenshot 2026-07-10 012140" src="https://github.com/user-attachments/assets/bcba90a9-379f-444c-a037-f7e3bc6e2c90" />

## Available Jobs
<img width="1918" height="797" alt="Screenshot 2026-07-10 012126" src="https://github.com/user-attachments/assets/8df0cf1d-cc04-4fea-88fa-773df1226cad" />

## Candidate Applications
<img width="1345" height="772" alt="image" src="https://github.com/user-attachments/assets/72b3e2a3-109a-4644-b00f-b21efab37ac2" />


### Missing Skills + Learning Roadmap
<img width="1323" height="700" alt="image" src="https://github.com/user-attachments/assets/dcbe8d5b-ee80-4ca0-8337-06828aabc992" />


### To-do checklist
<img width="1350" height="778" alt="image" src="https://github.com/user-attachments/assets/636f49f5-04b2-40b2-bbec-b5ca8ea0c56e" />



### Generate JD specific interview questions
<img width="1327" height="685" alt="image" src="https://github.com/user-attachments/assets/a8ed7e90-e242-4b19-a6c0-b7853c2a5bd8" />

## Recruiter Dashboard
<img width="1918" height="567" alt="image" src="https://github.com/user-attachments/assets/e9a4352f-5ac1-4e31-9ce4-c91c32a75eb1" />

## Create New Job(Recruiter)
<img width="1918" height="836" alt="Screenshot 2026-07-10 012106" src="https://github.com/user-attachments/assets/7b82f35e-8e89-414c-987b-a2b411da9f38" />

## Uploaded Jobs (Recruiter)
<img width="1918" height="847" alt="Screenshot 2026-07-10 012115" src="https://github.com/user-attachments/assets/b88d60ed-1f3b-4d01-abd2-f55f09ff1e5e" />

## Applicants Page (Recruiter)
<img width="1918" height="848" alt="Screenshot 2026-07-10 012320" src="https://github.com/user-attachments/assets/d2c41fa1-5228-47c3-bafd-bbf1ef5e88f5" />

---

# Features

## Candidate Features

- User Registration & Login (JWT Authentication)
- Upload Resume (PDF)
- Resume Parsing & Text Extraction
- Automatic Skill Extraction
- Browse Available Jobs
- Apply to Jobs
- View Applied Jobs
- Track Application Status
- View Resume Analysis
- ATS Score Generation
- AI Generated Learning Roadmap for Missing Skills

---

## Recruiter Features

- Recruiter Registration & Login
- Create Job Postings
- Upload Job Description PDFs
- Automatic JD Skill Extraction
- View Applicants
- Rank Candidates using ATS Score
- Semantic Resume-JD Matching
- View Top Candidates
- Manage Job Applications
- View Jobs Created by Recruiter

---

## AI/NLP Features

- Resume PDF Parsing
- Job Description Parsing
- Text Preprocessing
- Skill Extraction using spaCy PhraseMatcher
- Skill Normalization
- Semantic Skill Matching using Sentence Transformers
- ATS Score Calculation
- Missing Skill Identification
- AI Generated Learning Roadmap using Google Gemini

---

# Tech Stack

| Category | Technologies |
|------------|-------------------------------|
| Frontend | React.js, React Router, Axios |
| Backend | FastAPI, Python |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Validation | Pydantic |
| AI/NLP | spaCy, PhraseMatcher |
| Embedding Model | all-MiniLM-L6-v2 |
| LLM | Google Gemini |
| PDF Parsing | PyMuPDF |
| Deployment Ready | Uvicorn |

---

# Project Workflow

```
                   Candidate
                       │
                       ▼
               Upload Resume (PDF)
                       │
                       ▼
             Resume Text Extraction
                       │
                       ▼
             Resume Skill Extraction
                       │
                       ▼
             Resume Skill Normalization
                       │
                       │
                       ▼

Recruiter ─────► Upload Job Description (PDF)
                       │
                       ▼
              JD Text Extraction
                       │
                       ▼
              JD Skill Extraction
                       │
                       ▼
             JD Skill Normalization
                       │
                       ▼
             Semantic Skill Matching
                       │
                       ▼
               ATS Score Generation
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
     Candidate Ranking      Missing Skills
                                     │
                                     ▼
                       Gemini Learning Roadmap
```

---

# Evolution of the AI Pipeline

## Previous Architecture

Initially, the ATS engine relied entirely on exact keyword matching.

```
Resume PDF
      │
      ▼
Extract Text
      │
      ▼
Hardcoded Skill Extraction
      │
      ▼
Resume Skills

Job Description PDF
      │
      ▼
Extract Text
      │
      ▼
Hardcoded Skill Extraction
      │
      ▼
JD Skills

Resume Skills
      │
      ▼
Exact String Matching
      │
      ▼
ATS Score

Missing Skills
      │
      ▼
Gemini Learning Roadmap
```

### Limitations

### 1. Hardcoded Skills

Skills were maintained manually.

```python
skills = [
    "python",
    "java",
    "c++"
]
```

Problems:

- Limited vocabulary
- Difficult to maintain
- Required source code modifications for new skills

---

### 2. Exact Matching

Example

Resume

```
FastAPI
```

Job Description

```
REST API
```

Old ATS

```
No Match
```

because

```
FastAPI ≠ REST API
```

---

### 3. Poor Scalability

Adding new technologies required manually editing the Python source code.

---

### 4. Domain Dependency

The hardcoded approach worked reasonably well only for software engineering resumes and struggled to generalize across other domains.

---

# New AI Pipeline

The ATS engine has been redesigned to support semantic understanding of skills.

```
                     Resume PDF
                          │
                          ▼
                 parser.py
                          │
                          ▼
              preprocessing.py
                          │
                          ▼
                extractor.py
                          │
                          ▼
              normalizer.py
                          │
                          ▼
                 Resume Skills

----------------------------------------------------

                  Job Description
                          │
                          ▼
                 parser.py
                          │
                          ▼
               preprocessing.py
                          │
                          ▼
                 extractor.py
                          │
                          ▼
               normalizer.py
                          │
                          ▼
                 JD Skills

----------------------------------------------------

Resume Skills
        │
        │
        ▼

Sentence Transformer Matcher

        ▲
        │

JD Skills
        │
        ▼

Semantic Skill Matches
        │
 ┌──────┴──────────┐
 ▼                 ▼

ATS Score     Missing Skills
                    │
                    ▼

       Gemini Learning Roadmap
```

---

# AI Modules

## parser.py

### Purpose

Extract textual content from uploaded PDF resumes and job descriptions.

**Input**

- Resume.pdf
- JobDescription.pdf

**Output**

- Raw Text

**Library Used**

- PyMuPDF

---

## preprocessing.py

### Purpose

Clean and normalize extracted text before NLP processing.

Operations include

- Remove extra whitespace
- Remove unnecessary symbols
- Normalize formatting
- Reduce textual noise

Example

Before

```
Python!!!

TensorFlow      SQL
```

After

```
Python TensorFlow SQL
```

---

## extractor.py

This module is the core of the skill extraction pipeline.

Instead of relying on manually coded keyword checks,

```python
if "python" in text
```

the system uses

- spaCy
- PhraseMatcher
- Custom Skills Database

Pipeline

```
Text

↓

spaCy NLP

↓

PhraseMatcher

↓

skills.json

↓

Detected Skills
```

The skills database contains more than **15,000+** technical skills collected from:

- ESCO Skills Database
- Custom Technical Skills Repository

Supported categories include

- Programming Languages
- Frameworks
- Libraries
- Cloud Platforms
- Databases
- DevOps
- Artificial Intelligence
- Machine Learning
- Data Science
- Networking
- Cybersecurity
- Blockchain
- IoT
- Robotics
- Game Development
## normalizer.py

### Purpose

Different resumes often use different names for the same technology. The normalization module converts these aliases into a single canonical representation before comparison.

Without normalization, semantically identical skills may be treated as different.

Example

```
CPP
        ↓
C++
```

```
ReactJS
        ↓
React
```

```
NodeJS
        ↓
Node.js
```

```
JS
        ↓
JavaScript
```

### Why is Normalization Important?

Without normalization

Resume

```
CPP
```

Database

```
C++
```

Result

```
No Match
```

With normalization

```
CPP
      ↓
C++
      ↓
Match
```

This significantly improves both ATS scoring accuracy and semantic matching.

---

## matcher.py

The semantic matching engine is the core AI component responsible for intelligently comparing candidate skills with job requirements.

Instead of relying solely on exact keyword matching, it converts extracted skills into dense vector embeddings and compares them using cosine similarity.

### Model Used

```
Sentence Transformers

↓

all-MiniLM-L6-v2
```

### Semantic Matching Pipeline

```
Resume Skills
        │
        ▼
Generate Embeddings
        │
        ▼
JD Skill Embeddings
        │
        ▼
Cosine Similarity
        │
        ▼
Best Semantic Match
```

### Example

Resume

```
FastAPI
```

Job Description

```
REST API
```

Embedding Space

```
FastAPI ≈ REST API
```

Similarity Score

```
0.91
```

Result

```
Matched
```

Although the wording differs, both represent closely related backend API technologies.

---

# ATS Score Calculation

## Previous Approach

The previous ATS scoring mechanism relied on exact keyword matching.

```
Resume Skills

∩

JD Skills

↓

Matched Skills

↓

ATS Score
```

Formula

```python
matched_skills = resume_skills ∩ jd_skills

ATS Score = (matched_skills / total_jd_skills) × 100
```

### Limitations

- Exact keyword matching only
- Failed to recognize synonymous technologies
- Missed contextually similar skills
- Lower accuracy

---

## Current Semantic ATS Engine

The updated ATS engine performs semantic comparison before calculating the score.

```
Resume Skills

↓

Semantic Matching

↓

Matched JD Skills

↓

ATS Score
```

Instead of checking whether two skills have identical names, the system checks whether they represent similar concepts in embedding space.

This results in significantly more accurate resume evaluation.

---

## Missing Skills Detection

Instead of simply computing

```
JD Skills

-

Resume Skills
```

the system computes

```
JD Skills

-

Semantically Matched Skills
```

This prevents skills that are already represented using different terminology from being incorrectly classified as missing.

Example

Resume

```
TensorFlow
```

Job Description

```
Deep Learning
```

The semantic matcher recognizes the relationship between the two concepts, preventing TensorFlow from being unnecessarily flagged as a missing skill when similarity exceeds the configured threshold.

---

## AI Learning Roadmap

Google Gemini is responsible only for generating personalized learning recommendations.

```
Missing Skills
        │
        ▼
Google Gemini
        │
        ▼
4 Week Personalized Learning Roadmap
```

Separating ATS scoring from roadmap generation provides a cleaner system architecture and better modularity.

---

# Overall AI Pipeline

```
Resume PDF
        │
        ▼
PDF Parsing
        │
        ▼
Text Preprocessing
        │
        ▼
Skill Extraction
        │
        ▼
Skill Normalization
        │
        ▼
Resume Skill List
                │
                │
                ▼
         Semantic Matcher
                ▲
                │
JD Skill List ──┘
        │
        ▼
Matched Skills
        │
 ┌──────┴─────────┐
 ▼                ▼

ATS Score   Missing Skills
                    │
                    ▼

      Gemini Learning Roadmap
```

---

# System Architecture

```
                        React Frontend
                               │
                               ▼
                     FastAPI REST API Server
                               │
        ┌──────────────────────┼────────────────────────┐
        │                      │                        │
        ▼                      ▼                        ▼

 JWT Authentication     Resume Processing        Job Processing
        │                      │                        │
        ▼                      ▼                        ▼

 PostgreSQL          AI Processing Pipeline      Application Engine
 Database                   │
                             ▼

         parser.py → preprocessing.py → extractor.py
                             │
                             ▼

                      normalizer.py
                             │
                             ▼

                  Sentence Transformer
                             │
                             ▼

                     ATS Score Engine
                             │
                             ▼

                 Google Gemini Roadmap
```

---

# Project Structure

```text
ATS/
│
├── backend/
│   │
│   ├── src/
│   │   │
│   │   ├── ai/
│   │   │   ├── parser.py
│   │   │   ├── preprocessing.py
│   │   │   ├── extractor.py
│   │   │   ├── matcher.py
│   │   │   ├── normalizer.py
│   │   │   ├── skills.json
│   │   │   └── data/
│   │   │
│   │   ├── users/
│   │   ├── jobs/
│   │   ├── resumes/
│   │   ├── applications/
│   │   ├── roadmap_tasks/
│   │   ├── interview_questions/
│   │   ├── utils/
│   │   │
│   │   ├── main.py
│   │   └── uploads/
│   │
│   ├── requirements.txt
│   ├── .env
│   └── alembic/
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# Database Schema

## Users

| Field | Type |
|---------|---------|
| id | Integer |
| name | String |
| email | String |
| password | String |
| role | String |

---

## Jobs

| Field | Type |
|---------|---------|
| id | Integer |
| title | String |
| description | Text |
| experience_level | String |
| recruiter_id | Integer |
| jd_text | Text |
| jd_skills | Text |

---

## Resumes

| Field | Type |
|---------|---------|
| id | Integer |
| candidate_id | Integer |
| file_path | String |
| extracted_text | Text |
| extracted_skills | Text |
| ats_score | Integer |

---

## Applications

| Field | Type |
|---------|---------|
| id | Integer |
| candidate_id | Integer |
| job_id | Integer |
| resume_id | Integer |
| similarity_score | Integer |
| status | String |
| recruiter_message | String |

---

## Authentication

The platform uses JWT (JSON Web Token) based authentication to secure protected routes.

### Authentication Flow

```
User Login
      │
      ▼
Verify Credentials
      │
      ▼
Generate JWT Token
      │
      ▼
Store Token (Frontend)
      │
      ▼
Authorization Header

Bearer <JWT_TOKEN>

      │
      ▼

Protected API Access
```

Every protected endpoint validates the JWT before processing requests.
# API Endpoints

---

## Authentication & Users

Base URL

```
/users
```

| Method | Endpoint | Description | Authentication |
|----------|-----------|-------------|----------------|
| POST | `/register` | Register a new user | ❌ |
| POST | `/login` | User login | ❌ |
| GET | `/getuser` | Get current logged-in user | ✅ |
| PUT | `/update` | Update user profile | ✅ |
| DELETE | `/delete` | Delete user account | ✅ |

---

## Jobs

Base URL

```
/jobs
```

| Method | Endpoint | Description | Authentication |
|----------|-----------|-------------|----------------|
| POST | `/create` | Create Job Posting | ✅ Recruiter |
| GET | `/getall` | Get All Jobs | ❌ |
| GET | `/get/{job_id}` | Get Job Details | ❌ |
| PUT | `/update/{job_id}` | Update Job | ✅ Recruiter |
| DELETE | `/delete/{job_id}` | Delete Job | ✅ Recruiter |
| GET | `/{job_id}/applications` | View Applicants for Job | ✅ Recruiter |
| GET | `/top_candidates/{job_id}` | Rank Applicants using ATS Score | ✅ Recruiter |
| GET | `/my-jobs` | View Recruiter's Jobs | ✅ Recruiter |

---

## Resume

Base URL

```
/resumes
```

| Method | Endpoint | Description | Authentication |
|----------|-----------|-------------|----------------|
| POST | `/upload` | Upload Resume PDF | ✅ Candidate |
| GET | `/getall` | View Uploaded Resumes | ✅ Candidate |
| GET | `/get/{resume_id}` | Get Resume Details | ✅ Candidate |
| DELETE | `/delete/{resume_id}` | Delete Resume | ✅ Candidate |
| GET | `/analyze/{resume_id}` | Analyze Resume & Generate ATS Score | ✅ Candidate |

---

## Applications

Base URL

```
/applications
```

| Method | Endpoint | Description | Authentication |
|----------|-----------|-------------|----------------|
| POST | `/apply` | Apply for Job | ✅ Candidate |
| GET | `/my-applications` | View Applied Jobs | ✅ Candidate |
| GET | `/{application_id}` | Get Application Details | ✅ Candidate |
| PUT | `/{application_id}` | Update Application | ✅ Candidate |
| DELETE | `/delete/{application_id}` | Withdraw Application | ✅ Candidate |
| GET | `/{application_id}/resume` | View Resume Used in Application | ✅ |

---

## Interview Questions

Base URL

```
/questions
```

| Method | Endpoint | Description |
|----------|-----------|-------------|
| GET | `/{job_id}` | Generate AI Interview Questions for a Job |

---

## Learning Roadmap

Base URL

```
/tasks
```

| Method | Endpoint | Description |
|----------|-----------|-------------|
| GET | `/{application_id}` | Get Personalized Learning Roadmap |
| PUT | `/{task_id}` | Update Learning Task Status |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ats-system.git

cd ats-system
```

---

# Backend Setup

Navigate to the backend folder

```bash
cd backend
```

Create a virtual environment

```bash
python -m venv myenv
```

Activate the virtual environment

### Windows

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
source myenv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the backend directory.

```env
DB_CONNECTION=postgresql://postgres:password@localhost:5432/atsdb

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_TIME=30

GEMINI_API_KEY=your_google_gemini_api_key
```

---

# Database Setup

Create a PostgreSQL database.

Example

```
Database Name

atsdb
```

Run Alembic migrations

```bash
alembic upgrade head
```

If migrations are not being used, the database tables will be created automatically on application startup using SQLAlchemy metadata.

---

# Running the Backend

From the backend directory

```bash
uvicorn src.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Frontend Setup

Navigate to frontend

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run development server

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# How to Use

## Candidate Workflow

```
Register
     │
     ▼
Login
     │
     ▼
Upload Resume
     │
     ▼
Resume Analysis
     │
     ▼
Browse Jobs
     │
     ▼
Apply to Job
     │
     ▼
ATS Score Generated
     │
     ▼
Missing Skills Identified
     │
     ▼
AI Learning Roadmap Generated
```

---

## Recruiter Workflow

```
Register
      │
      ▼
Login
      │
      ▼
Create Job
      │
      ▼
Upload Job Description
      │
      ▼
Automatic Skill Extraction
      │
      ▼
Candidates Apply
      │
      ▼
Semantic Resume Matching
      │
      ▼
ATS Score Calculation
      │
      ▼
Top Candidates Ranked
      │
      ▼
View AI Generated Interview Questions
```

---

# AI Technologies Used

| Technology | Purpose |
|-------------|----------|
| PyMuPDF | PDF Text Extraction |
| spaCy | NLP Pipeline |
| PhraseMatcher | Skill Detection |
| Skills Database | Technical Skill Recognition |
| Sentence Transformers | Semantic Skill Matching |
| Cosine Similarity | ATS Matching |
| Google Gemini | Personalized Learning Roadmap |
| PostgreSQL | Data Storage |
| SQLAlchemy | ORM |
| FastAPI | REST Backend |
| React | Frontend |
# Challenges Faced

Developing an AI-powered Applicant Tracking System involved solving several technical and architectural challenges across web development, NLP, and AI integration.

## 1. Resume Parsing

Resumes come in a wide variety of formats and layouts, making text extraction inconsistent. Extracting meaningful information while handling formatting issues required implementing a robust PDF parsing pipeline using **PyMuPDF**.

---

## 2. Skill Extraction from Unstructured Text

Identifying technical skills from free-form resume text was challenging due to variations in wording, abbreviations, and formatting.

To address this, the system uses **spaCy PhraseMatcher** along with a custom skills database containing **15,000+ technical skills** collected from ESCO and other curated sources.

---

## 3. Skill Normalization

The same technology can appear under different names.

Examples:

```
CPP
C++
```

```
ReactJS
React
```

```
NodeJS
Node.js
```

A normalization layer was introduced to convert aliases into a canonical representation before matching.

---

## 4. Improving ATS Accuracy

Traditional ATS systems rely on exact keyword matching, causing semantically similar skills to be treated as different.

To improve accuracy, the project integrates **Sentence Transformers (all-MiniLM-L6-v2)** and computes semantic similarity using cosine similarity, enabling intelligent skill matching.

---

## 5. Role-Based Authentication

The application supports both Candidates and Recruiters with different permissions.

JWT authentication combined with role-based authorization ensures secure access to protected APIs.

---

## 6. AI Integration

Integrating Google Gemini required careful separation of responsibilities.

Instead of involving Gemini in ATS score computation, it is used exclusively for generating personalized learning roadmaps based on identified missing skills.

This modular architecture keeps ATS scoring deterministic while leveraging LLM capabilities for personalized recommendations.

---

# Future Scope

The current system provides an end-to-end AI-powered recruitment platform, but several enhancements can further improve its capabilities.

## Planned Improvements

- AI-powered resume rewriting and optimization
- Multi-language resume parsing
- Resume version management
- Recruiter analytics dashboard
- Candidate recommendation engine
- AI-powered interview feedback
- Resume ranking using larger embedding models
- Email notifications for application updates
- Interview scheduling module
- Calendar integration
- Docker containerization
- Cloud deployment on AWS or GCP
- Redis caching for improved performance

---

# Project Highlights

- AI-powered Applicant Tracking System
- Semantic Resume–Job Description Matching
- ATS Score Generation using Sentence Transformers
- Skill Extraction with spaCy PhraseMatcher
- 15,000+ Technical Skills Database
- Personalized Learning Roadmaps using Google Gemini
- Secure JWT Authentication
- FastAPI REST Backend
- React Frontend
- PostgreSQL Database
- Modular AI Pipeline
- RESTful API Architecture

---

# Learning Outcomes

This project provided practical experience in several domains of software engineering and artificial intelligence, including:

- Building scalable REST APIs with FastAPI
- Designing relational databases using PostgreSQL
- Authentication using JWT
- ORM development with SQLAlchemy
- Resume parsing from PDF documents
- Natural Language Processing using spaCy
- Semantic Similarity using Sentence Transformers
- Prompt Engineering with Google Gemini
- Frontend development using React
- End-to-end integration of AI with modern web technologies

---

# Acknowledgements

The following technologies and open-source libraries made this project possible:

- FastAPI
- React.js
- PostgreSQL
- SQLAlchemy
- spaCy
- Sentence Transformers
- Hugging Face
- PyMuPDF
- Google Gemini API
- ESCO Skills Database
- Uvicorn
- Pydantic

---


# Author

**Aditya Rana**

B.Tech Computer Science and Engineering (Data Science)

Vellore Institute of Technology, Chennai

---

# Contact

Feel free to connect for collaborations, suggestions, or discussions.

- **GitHub:** https://github.com/adityaa-rana
- **Email:** adityaranaaa3113@gmail.com

---


# Thank You

Thank you for taking the time to explore this project.

If you found this repository useful, consider giving it a ⭐ on GitHub. Feedback, suggestions, and contributions are always welcome!
