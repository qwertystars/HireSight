# HireSight - System Architecture Document

**Project:** hiresight
**Author:** Srijan (Architect: Winston)
**Date:** 2025-10-24
**Version:** 1.0
**Project Level:** 2 (Medium - Multiple epics, 10+ stories)

---

## Executive Summary

HireSight is a hackathon MVP demonstrating alignment-first hiring through AI-powered candidate-company matching. The architecture uses a **lightweight FastAPI backend with SQLite** for rapid development, supporting 14 user stories across 2 epics. The system prioritizes **demo reliability** (zero crashes), **response speed** (<1s queries, <10s resume processing), and **AI agent consistency** through explicit implementation patterns.

**Key Architectural Decisions:**
- Manual lightweight setup (no template overhead) for 24-hour hackathon velocity
- Python 3.12 + FastAPI backend with layered structure for story organization
- SQLite database with file-based resume storage
- Human-implemented ML/NLP services (resume parsing, alignment scoring) with clear API contracts
- Human-implemented React frontend, backend provides RESTful JSON APIs
- Direct HTTP response format (no wrappers) for simplicity
- CORS-enabled local development (backend + frontend separate servers)

---

## Technology Stack

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **Language** | Python | 3.12 | Backend implementation |
| **Web Framework** | FastAPI | latest (0.1xx) | REST API server |
| **Database** | SQLite | 3.x (built-in) | Data persistence |
| **ORM** | SQLAlchemy | 2.x | Database abstraction, async support |
| **Validation** | Pydantic | v2 | Request/response schemas, settings |
| **File Handling** | python-multipart | latest | Resume file uploads |
| **Resume Parsing** | Custom (human) | N/A | PDF/DOCX text extraction |
| **NLP/ML** | Custom (human) | N/A | Skills extraction, alignment scoring |
| **Testing** | pytest | latest | Unit and integration tests |
| **Environment** | python-dotenv | latest | Configuration management |
| **Frontend** | React + Vite | Human-implemented | User interface (separate from backend) |

---

## Project Initialization

**Backend Setup (AI Agent Story 1.1):**

```bash
# Create project structure
mkdir -p hiresight/backend
cd hiresight/backend

# Initialize Python virtual environment
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Create requirements.txt
cat > requirements.txt << EOF
fastapi
uvicorn[standard]
sqlalchemy
pydantic
pydantic-settings
python-multipart
python-dotenv
pytest
httpx
EOF

# Install dependencies
pip install -r requirements.txt

# Create directory structure (see Project Structure section below)
mkdir -p app/{core,models,schemas,api/routes,services,utils}
mkdir -p uploads data tests/{test_api,test_services}
touch app/__init__.py app/main.py
```

**Frontend Setup (Human):**
```bash
# From project root
npm create vite@latest frontend -- --template react
cd frontend
npm install
# Add Tailwind, routing, HTTP client as needed
```

**Environment Configuration:**

Create `backend/.env`:
```env
DATABASE_URL=sqlite:///./data/hiresight.db
UPLOAD_DIR=./uploads
CORS_ORIGINS=http://localhost:5173
LOG_LEVEL=INFO
```

---

## Complete Project Structure

```
hiresight/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI app, CORS, startup/shutdown
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py              # Pydantic Settings (env vars)
│   │   │   └── database.py            # SQLAlchemy engine, Base, get_db()
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── candidate.py           # Candidate ORM model
│   │   │   ├── company.py             # Company ORM model
│   │   │   └── interest.py            # Interest tracking ORM model
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── candidate.py           # CandidateCreate, CandidateResponse
│   │   │   ├── company.py             # CompanyResponse, CompanyListResponse
│   │   │   ├── alignment.py           # AlignmentResult schema
│   │   │   └── skill_gap.py           # SkillGapResponse schema
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       ├── health.py          # GET /health (Story 1.1)
│   │   │       ├── candidates.py      # POST /api/upload-resume (Story 1.3)
│   │   │       ├── companies.py       # GET /api/companies, POST /api/candidates (Stories 1.5, 1.8)
│   │   │       ├── alignment.py       # POST /api/check-gap (Story 1.6)
│   │   │       └── interests.py       # POST /api/track-interest (Story 1.7)
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── resume_parser.py       # HUMAN: extract_text_from_resume()
│   │   │   ├── nlp_service.py         # HUMAN: extract_skills_and_domains()
│   │   │   ├── alignment_service.py   # HUMAN: calculate_alignment()
│   │   │   └── skill_gap_service.py   # calculate_skill_gap() - AI agent
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── file_storage.py        # save_uploaded_file() utility
│   ├── uploads/                        # Stored resume files (.gitignore)
│   ├── data/
│   │   ├── hiresight.db               # SQLite database (.gitignore)
│   │   └── seed_companies.py          # Company seeding script (Story 1.2)
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py                # pytest fixtures (test DB, client)
│   │   ├── test_api/
│   │   │   ├── test_health.py
│   │   │   ├── test_candidates.py
│   │   │   ├── test_companies.py
│   │   │   └── test_alignment.py
│   │   └── test_services/
│   │       └── test_skill_gap_service.py
│   ├── .env                            # Environment variables
│   ├── .env.example                    # Example env template
│   ├── requirements.txt                # Python dependencies
│   └── README.md                       # Backend setup instructions
│
├── frontend/                           # HUMAN IMPLEMENTED
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── pages/
│   │   │   ├── CandidateUpload.jsx    # Story 2.1
│   │   │   ├── CompanyList.jsx        # Story 2.2
│   │   │   └── CompanyDashboard.jsx   # Story 2.5
│   │   ├── components/
│   │   │   ├── SkillGapModal.jsx      # Story 2.3
│   │   │   ├── InterestTracker.jsx    # Story 2.4
│   │   │   └── GrowthNotificationDemo.jsx  # Story 2.6
│   │   └── services/
│   │       └── api.js                 # HTTP client (fetch/axios)
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
├── docs/
│   ├── PRD.md                          # Product Requirements Document
│   ├── epics.md                        # Epic breakdown with stories
│   ├── architecture.md                 # This document
│   └── bmm-workflow-status.md          # Workflow tracking
│
├── .gitignore
└── README.md                           # Project overview, quick start
```

---

## Epic to Architecture Mapping

### Epic 1: Foundation & Core Matching Engine → `backend/`

| Story | Primary Files | Description |
|-------|--------------|-------------|
| **1.1** | `core/database.py`, `models/*.py`, `main.py`, `routes/health.py` | Database schema, FastAPI app, health check |
| **1.2** | `data/seed_companies.py` | Populate 20 companies (climate, EdTech, health, social) |
| **1.3** | `routes/candidates.py`, `services/resume_parser.py` (HUMAN), `utils/file_storage.py` | Resume upload, parsing, storage |
| **1.4** | `services/alignment_service.py` (HUMAN), `services/nlp_service.py` (HUMAN) | Alignment scoring algorithm (60/40 domain/values) |
| **1.5** | `routes/companies.py`, `schemas/alignment.py` | Company list API with alignment ranking |
| **1.6** | `routes/alignment.py`, `services/skill_gap_service.py`, `schemas/skill_gap.py` | Skill gap analysis and recommendations |
| **1.7** | `routes/interests.py`, `models/interest.py` | Interest tracking (timestamp bookmarks) |
| **1.8** | `routes/companies.py` (POST /api/candidates), integration with 1.3+1.4 | Company dashboard: batch candidate ranking |

### Epic 2: User Experience & Demo Polish → `frontend/` (HUMAN)

| Story | Component | Description |
|-------|-----------|-------------|
| **2.1** | `CandidateUpload.jsx` | Drag-and-drop resume upload UI |
| **2.2** | `CompanyList.jsx` | Ranked companies with alignment scores |
| **2.3** | `SkillGapModal.jsx` | Skill gap analysis modal |
| **2.4** | `InterestTracker.jsx` | Track interest button/state |
| **2.5** | `CompanyDashboard.jsx` | Hiring manager view |
| **2.6** | `GrowthNotificationDemo.jsx` | Hardcoded demo notification |

---

## Data Architecture

### Database Schema (SQLite)

**Table: `candidates`**
```sql
CREATE TABLE candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resume_path TEXT NOT NULL,               -- "uploads/resume_123.pdf"
    extracted_text TEXT,                     -- Full resume text
    extracted_skills TEXT,                   -- JSON array: ["Python", "React"]
    extracted_domains TEXT,                  -- JSON array: ["climate tech"]
    values_signals TEXT,                     -- JSON array: ["sustainability"]
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Table: `companies`**
```sql
CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mission TEXT NOT NULL,                   -- Mission statement
    values TEXT NOT NULL,                    -- JSON array: ["impact", "innovation"]
    required_skills TEXT NOT NULL,           -- JSON array: ["Python", "AWS"]
    domain TEXT NOT NULL,                    -- "climate tech", "EdTech", etc.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Table: `interests`**
```sql
CREATE TABLE interests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    tracked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id),
    FOREIGN KEY (company_id) REFERENCES companies(id),
    UNIQUE(candidate_id, company_id)         -- Prevent duplicates
);
```

**Indexes:**
```sql
CREATE INDEX idx_candidate_id ON interests(candidate_id);
CREATE INDEX idx_company_id ON interests(company_id);
```

---

## API Contracts

### Endpoint Summary

| Method | Endpoint | Purpose | Story |
|--------|----------|---------|-------|
| GET | `/health` | Health check | 1.1 |
| POST | `/api/upload-resume` | Upload candidate resume | 1.3 |
| GET | `/api/companies?candidate_id={id}` | Get ranked companies for candidate | 1.5 |
| POST | `/api/check-gap` | Analyze skill gap | 1.6 |
| POST | `/api/track-interest` | Bookmark company | 1.7 |
| POST | `/api/candidates` | Batch rank candidates for company | 1.8 |

### Detailed API Specifications

**1. Health Check**
```http
GET /health
Response 200: {"status": "ok"}
```

**2. Upload Resume (Story 1.3)**
```http
POST /api/upload-resume
Content-Type: multipart/form-data
Body: file (PDF/DOCX)

Response 200:
{
  "candidate_id": 1,
  "message": "Resume processed successfully"
}

Response 400: {"detail": "Invalid file format. Only PDF and DOCX allowed."}
```

**3. Get Ranked Companies (Story 1.5)**
```http
GET /api/companies?candidate_id=1

Response 200:
[
  {
    "id": 5,
    "name": "ClimateAI Solutions",
    "alignment_percentage": 92.5,
    "reasoning": "Strong match: 2 years climate data projects"
  },
  {
    "id": 12,
    "name": "GreenTech Education",
    "alignment_percentage": 78.0,
    "reasoning": "Good fit: EdTech experience + sustainability values"
  }
]

Response 404: {"detail": "Candidate not found"}
```

**4. Check Skill Gap (Story 1.6)**
```http
POST /api/check-gap
Content-Type: application/json
Body: {"candidate_id": 1, "company_id": 5}

Response 200:
{
  "company_name": "ClimateAI Solutions",
  "current_alignment": 78.0,
  "missing_skills": ["Kubernetes", "Climate modeling"],
  "recommended_learning_path": [
    "Kubernetes fundamentals course",
    "Climate science basics",
    "ML for climate data"
  ]
}

Response 404: {"detail": "Candidate or company not found"}
```

**5. Track Interest (Story 1.7)**
```http
POST /api/track-interest
Content-Type: application/json
Body: {"candidate_id": 1, "company_id": 5}

Response 200:
{
  "message": "Interest tracked successfully",
  "company_name": "ClimateAI Solutions"
}

Response 400: {"detail": "Interest already tracked"}
Response 404: {"detail": "Candidate or company not found"}
```

**6. Batch Rank Candidates (Story 1.8)**
```http
POST /api/candidates
Content-Type: multipart/form-data
Body:
  - company_id: 5
  - files[]: resume1.pdf, resume2.pdf, ...
  - alignment_threshold (optional): 70

Response 200:
{
  "company_name": "ClimateAI Solutions",
  "total_candidates": 10,
  "candidates": [
    {
      "candidate_id": 15,
      "name": "Maria Chen",
      "alignment_percentage": 88.0,
      "reasoning": "Strong passion signals: 3 years building climate education tools"
    },
    {
      "candidate_id": 16,
      "name": "John Doe",
      "alignment_percentage": 72.0,
      "reasoning": "Moderate match: Some EdTech experience, general tech skills"
    }
  ]
}
```

---

## Integration Points

### Backend ↔ Frontend Communication

**Protocol:** HTTP REST API
**Format:** JSON
**Base URL:** `http://localhost:8000` (backend), `http://localhost:5173` (frontend)
**CORS:** Enabled for localhost:5173 in `main.py`

**Frontend HTTP Client Pattern:**
```javascript
// frontend/src/services/api.js
const API_BASE = 'http://localhost:8000';

export async function uploadResume(file) {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE}/api/upload-resume`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail);
  }

  return response.json();
}
```

### Backend ↔ Database

**Access Pattern:** SQLAlchemy ORM (async support)
**Session Management:** Dependency injection via `Depends(get_db)`
**Migrations:** Not required (SQLite, schema created on startup)

```python
# core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/hiresight.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Backend ↔ Human-Implemented Services

**Critical Contracts (AI agents call, humans implement):**

```python
# services/resume_parser.py (HUMAN IMPLEMENTED)
def extract_text_from_resume(file_path: str) -> str:
    """
    Extract plain text from PDF or DOCX resume.

    Args:
        file_path: Path to resume file (e.g., "uploads/resume_123.pdf")

    Returns:
        Extracted text as string

    Raises:
        ValueError: If file format unsupported or parsing fails
    """
    raise NotImplementedError("Human implementation required")


# services/nlp_service.py (HUMAN IMPLEMENTED)
def extract_skills_and_domains(text: str) -> dict:
    """
    Extract structured data from resume text using NLP/ML.

    Args:
        text: Resume text content

    Returns:
        {
            "skills": ["Python", "React", "Machine Learning"],
            "domains": ["climate tech", "education"],
            "values_signals": ["sustainability", "impact", "mission-driven"]
        }
    """
    raise NotImplementedError("Human implementation required")


# services/alignment_service.py (HUMAN IMPLEMENTED)
def calculate_alignment(candidate_id: int, company_id: int, db: Session) -> dict:
    """
    Calculate alignment score using weighted algorithm: 60% domain + 40% values.

    Args:
        candidate_id: Candidate database ID
        company_id: Company database ID
        db: SQLAlchemy session

    Returns:
        {
            "score": 92.5,  # float 0-100
            "reasoning": "Strong match: 2 years climate data projects, sustainability values align"
        }

    Raises:
        ValueError: If candidate or company not found
    """
    raise NotImplementedError("Human implementation required")
```

**AI Agent Responsibilities:**
- Create function signatures with docstrings
- Add `raise NotImplementedError("Human implementation required")`
- Call these functions from API routes
- Handle return values and exceptions properly

---

## Implementation Patterns (AI Agent Consistency Rules)

### NAMING CONVENTIONS

| Category | Convention | Example |
|----------|-----------|---------|
| **Database Tables** | snake_case, plural | `candidates`, `companies`, `interests` |
| **Database Columns** | snake_case | `candidate_id`, `created_at`, `extracted_skills` |
| **Foreign Keys** | `{table}_id` | `candidate_id`, `company_id` |
| **Python Files** | snake_case | `resume_parser.py`, `alignment_service.py` |
| **Python Classes** | PascalCase | `Candidate`, `Company`, `AlignmentResult` |
| **Python Functions** | snake_case | `calculate_alignment()`, `get_candidate_by_id()` |
| **API Endpoints** | kebab-case, plural | `/api/candidates`, `/api/track-interest` |
| **Pydantic Schemas** | PascalCase + suffix | `CandidateCreate`, `CompanyResponse` |

### CODE STRUCTURE PATTERNS

**SQLAlchemy Model Template:**
```python
# models/candidate.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    resume_path = Column(String, nullable=False)
    extracted_text = Column(Text)
    extracted_skills = Column(Text)  # JSON string
    extracted_domains = Column(Text)  # JSON string
    values_signals = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
```

**Pydantic Schema Template:**
```python
# schemas/candidate.py
from pydantic import BaseModel
from datetime import datetime

class CandidateCreate(BaseModel):
    """Request schema for creating candidate."""
    # Input fields only
    pass

class CandidateResponse(BaseModel):
    """Response schema for candidate data."""
    id: int
    resume_path: str
    extracted_skills: list[str] | None
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2 (was orm_mode)
```

**API Route Template:**
```python
# api/routes/candidates.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.candidate import CandidateResponse

router = APIRouter(prefix="/api", tags=["candidates"])

@router.post("/upload-resume", response_model=dict)
async def upload_resume(
    file: UploadFile,
    db: Session = Depends(get_db)
):
    """
    Upload and process candidate resume.

    - Validates file format (PDF/DOCX only)
    - Saves file to uploads/ directory
    - Extracts text and NLP data
    - Creates candidate record in database

    Returns candidate_id and success message.
    """
    # Validation
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Invalid file format. Only PDF and DOCX allowed.")

    # Implementation
    # ...

    return {"candidate_id": candidate.id, "message": "Resume processed successfully"}
```

**Service Function Template:**
```python
# services/skill_gap_service.py
from sqlalchemy.orm import Session
from app.models.candidate import Candidate
from app.models.company import Company
import json

def calculate_skill_gap(candidate_id: int, company_id: int, db: Session) -> dict:
    """
    Calculate skill gap between candidate and company requirements.

    Args:
        candidate_id: Candidate database ID
        company_id: Company database ID
        db: Database session

    Returns:
        {
            "missing_skills": ["Kubernetes", "Climate modeling"],
            "recommended_learning_path": ["Course 1", "Course 2"]
        }

    Raises:
        ValueError: If candidate or company not found
    """
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    company = db.query(Company).filter(Company.id == company_id).first()

    if not candidate or not company:
        raise ValueError("Candidate or company not found")

    candidate_skills = set(json.loads(candidate.extracted_skills or "[]"))
    required_skills = set(json.loads(company.required_skills))

    missing_skills = list(required_skills - candidate_skills)

    # Generate learning path (simple for MVP)
    learning_path = [f"{skill} fundamentals course" for skill in missing_skills]

    return {
        "missing_skills": missing_skills,
        "recommended_learning_path": learning_path
    }
```

### FORMAT PATTERNS

**API Success Response (200):**
```json
{
  "id": 1,
  "name": "ClimateAI Solutions",
  "alignment_percentage": 92.5,
  "reasoning": "Strong match: 2 years climate data projects"
}
```

**API Error Response (4xx/5xx):**
```json
{
  "detail": "Candidate not found"
}
```

**Timestamps:**
- **Storage:** Python `datetime` objects (UTC), SQLite `TIMESTAMP`
- **API Output:** ISO 8601 strings via Pydantic (`"2025-10-24T10:30:00Z"`)

**JSON Arrays in SQLite:**
- Store as TEXT column: `'["Python", "React", "ML"]'`
- Parse with `json.loads()` when reading
- Serialize with `json.dumps()` when writing

**File Paths:**
- **Database:** Relative paths (`"uploads/resume_123.pdf"`)
- **Code:** Resolve to absolute with `os.path.join(settings.UPLOAD_DIR, filename)`

### ERROR HANDLING PATTERNS

**In API Routes:**
```python
from fastapi import HTTPException

# Not found
if not candidate:
    raise HTTPException(status_code=404, detail="Candidate not found")

# Bad request
if invalid_format:
    raise HTTPException(status_code=400, detail="Invalid file format. Only PDF and DOCX allowed.")

# Server error
try:
    result = process_data()
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
```

**In Services:**
```python
# Return None for not found (let route decide response)
def get_candidate(candidate_id: int, db: Session):
    return db.query(Candidate).filter(Candidate.id == candidate_id).first()

# Raise ValueError for business logic errors
def calculate_alignment(candidate_id, company_id, db):
    if not validate_data():
        raise ValueError("Invalid candidate or company data")
```

### DATABASE ACCESS PATTERNS

**Always use dependency injection:**
```python
@router.get("/api/companies")
async def list_companies(db: Session = Depends(get_db)):
    companies = db.query(Company).all()
    return companies
```

**Query patterns:**
```python
# Single record
candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

# Multiple records
companies = db.query(Company).filter(Company.domain == "climate tech").all()

# Create
new_candidate = Candidate(resume_path="uploads/resume_1.pdf")
db.add(new_candidate)
db.commit()
db.refresh(new_candidate)  # Get auto-generated ID

# Update
candidate.extracted_skills = json.dumps(skills)
db.commit()

# Delete
db.delete(interest)
db.commit()
```

### IMPORT ORDER

**Standard structure (PEP 8):**
```python
# Standard library
import os
import json
from datetime import datetime
from typing import Optional

# Third-party packages
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Local application
from app.core.database import Base, get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateResponse
from app.services.alignment_service import calculate_alignment
```

### LOGGING PATTERN

```python
import logging

logger = logging.getLogger(__name__)

# Info level for normal operations
logger.info(f"Processing resume for candidate {candidate_id}")

# Error level for failures
logger.error(f"Failed to parse resume {file_path}: {error}")

# Debug level for detailed tracing
logger.debug(f"Extracted skills: {skills}")
```

### CONFIGURATION MANAGEMENT

**All configuration in `.env`:**
```env
DATABASE_URL=sqlite:///./data/hiresight.db
UPLOAD_DIR=./uploads
CORS_ORIGINS=http://localhost:5173
LOG_LEVEL=INFO
```

**Access via Pydantic Settings:**
```python
# core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    upload_dir: str
    cors_origins: str
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
```

**Usage:**
```python
from app.core.config import settings

# Use settings, never hardcode
db_path = settings.database_url
upload_path = settings.upload_dir
```

---

## Security Architecture

**Authentication:** None (hackathon MVP, demo-only)

**File Upload Security:**
- Validate file extensions: `.pdf`, `.docx` only
- Validate MIME types: `application/pdf`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- Save with generated filenames (e.g., `resume_{timestamp}_{uuid}.pdf`)
- Store outside web root (uploads/ directory, not served directly)

**CORS Configuration:**
```python
# main.py
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_origins],  # "http://localhost:5173"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**SQL Injection Prevention:**
- Use SQLAlchemy ORM exclusively
- Never construct raw SQL strings
- Parameterized queries via ORM methods

**Data Privacy:**
- No PII collection beyond resume content (MVP)
- No user accounts, no passwords
- Resume files stored locally, not cloud (demo scope)

---

## Performance Considerations

### Non-Functional Requirements (from PRD)

| NFR | Requirement | Architecture Support |
|-----|-------------|---------------------|
| **NFR001** | Resume processing <10 seconds | Async file I/O, optimized NLP (human implementation) |
| **NFR002** | Zero crashes during 5-min demo | Try-catch blocks, validation, test coverage |
| **NFR003** | Alignment queries <1 second | SQLite indexes on candidate_id/company_id, in-memory scoring |

### Performance Strategies

**Database:**
- SQLite WAL mode for better concurrency: `PRAGMA journal_mode=WAL;`
- Indexes on foreign keys (interests table)
- Denormalized JSON fields for speed (extract once, query fast)

**API Response Times:**
- `/health`: <10ms (no DB query)
- `/api/upload-resume`: <10s (file I/O + NLP bottleneck)
- `/api/companies?candidate_id=X`: <500ms (20 company calculations)
- `/api/check-gap`: <200ms (single calculation)
- `/api/track-interest`: <100ms (simple INSERT)

**Optimization Opportunities (if needed):**
- Cache alignment scores (calculated once, reuse)
- Pre-calculate all scores on resume upload (Story 1.3 → 1.4 integration)
- Batch company queries (single DB query for all 20 companies)

---

## Deployment Architecture (MVP Scope)

**Target:** Local development/demo only (no production deployment)

**Backend Execution:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend Execution:**
```bash
cd frontend
npm run dev  # Vite dev server on http://localhost:5173
```

**Demo Setup:**
1. Start backend server (terminal 1)
2. Start frontend dev server (terminal 2)
3. Seed database: `python data/seed_companies.py`
4. Open browser: `http://localhost:5173`

**Data Persistence:**
- SQLite database: `backend/data/hiresight.db`
- Uploaded resumes: `backend/uploads/`
- Both gitignored, create fresh for each demo

---

## Development Environment

**Prerequisites:**
- Python 3.12+
- Node.js 18+ (for frontend)
- Git

**Backend Setup:**
```bash
cd backend
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -c "from app.core.database import Base, engine; Base.metadata.create_all(bind=engine)"
python data/seed_companies.py
```

**Frontend Setup (Human):**
```bash
cd frontend
npm install
npm run dev
```

**Running Tests:**
```bash
cd backend
pytest tests/ -v
```

**Environment Variables:**
Copy `.env.example` to `.env` and configure paths.

---

## Architecture Decision Records (ADRs)

### ADR-001: Manual Lightweight Setup vs Full-Stack Template

**Decision:** Use manual lightweight FastAPI + React setup instead of official full-stack template.

**Context:** Hackathon MVP with 24-hour deadline, SQLite requirement, no authentication needed.

**Rationale:**
- Official template includes PostgreSQL (vs SQLite), Docker, auth scaffolding, CI/CD
- Stripping template overhead would take 2-4 hours
- Manual setup gives exact dependencies needed, faster initial velocity
- Expert user can structure project optimally for hackathon constraints

**Consequences:**
- No Docker containerization (acceptable for local demo)
- No pre-built auth (not needed for MVP)
- Manual directory structure setup (one-time cost: 15 minutes)

---

### ADR-002: Direct HTTP Response Format vs Wrapped

**Decision:** Use direct JSON responses with HTTP status codes, no wrapper objects.

**Context:** API response format standardization across all endpoints.

**Rationale:**
- RESTful standard: HTTP codes convey success/failure
- FastAPI default behavior (less code, fewer conversions)
- Cleaner frontend integration (no unwrapping needed)
- Hackathon velocity: simpler is faster

**Consequences:**
- Success responses are direct objects/arrays
- Error responses use FastAPI's `{"detail": "message"}` format
- Frontend checks `response.ok` instead of `response.success` field

---

### ADR-003: Store Resume Files on Disk vs Database Blobs

**Decision:** Store resume files on disk, save file paths in database.

**Context:** Resume file persistence strategy for PDF/DOCX uploads.

**Rationale:**
- Easier debugging (files visible in filesystem)
- Better performance (no blob serialization overhead)
- Simpler backup (files separate from database)
- Standard practice for file storage

**Consequences:**
- Must manage uploads/ directory (gitignore, cleanup)
- Database stores relative paths: `"uploads/resume_123.pdf"`
- File operations require path resolution at runtime

---

### ADR-004: Human Implementation of ML/NLP Services

**Decision:** Resume parsing, NLP extraction, and alignment scoring implemented by human, not AI agents.

**Context:** Core business logic for alignment matching requires domain expertise and algorithm tuning.

**Rationale:**
- 60/40 domain/values weighting requires careful calibration
- "Passion signal" detection needs nuanced NLP understanding
- Demo quality depends on accurate alignment scores
- Human can iterate on algorithm quality during hackathon

**Consequences:**
- AI agents create service stubs with `NotImplementedError`
- Clear API contracts defined for human implementation
- Backend structure ready, human fills critical logic
- Testing can proceed with mock implementations

---

### ADR-005: Python 3.12 Over 3.11

**Decision:** Use Python 3.12 for backend implementation.

**Context:** Choose Python version for FastAPI backend.

**Rationale:**
- User explicitly requested 3.12
- Improved performance over 3.11 (15-20% faster in benchmarks)
- Latest language features available
- All required libraries (FastAPI, SQLAlchemy) fully compatible

**Consequences:**
- Development machine must have Python 3.12 installed
- CI/CD (if added later) must use 3.12 images
- No compatibility concerns with chosen dependencies

---

### ADR-006: SQLite Over PostgreSQL

**Decision:** Use SQLite for data persistence instead of PostgreSQL.

**Context:** Database choice for hackathon MVP with ~20 companies, demo-scale data.

**Rationale:**
- Zero configuration (no server setup, no connection pooling)
- Built-in with Python (no external dependencies)
- Perfect for hackathon demo scale (<100 records)
- File-based (easy to reset, share, backup)
- PRD explicitly mentions SQLite for MVP

**Consequences:**
- No multi-user concurrency (acceptable for demo)
- No advanced features (full-text search, JSON operators)
- Migration to PostgreSQL post-MVP requires schema changes
- WAL mode sufficient for hackathon needs

---

## Validation Checklist

- [x] Decision table includes specific Python 3.12, FastAPI latest, SQLite 3.x
- [x] Every epic (1-2) mapped to architecture components
- [x] Source tree complete with all directories and key files
- [x] No placeholder text (all sections filled with specifics)
- [x] All FRs (FR001-FR014) have architectural support
- [x] All NFRs (NFR001-NFR003) addressed with strategies
- [x] Implementation patterns cover naming, structure, formats
- [x] Human-implemented services clearly documented with contracts
- [x] API contracts specify all 6 endpoints with request/response examples
- [x] Database schema includes all 3 tables with columns and indexes
- [x] Error handling patterns defined for routes and services
- [x] Cross-cutting concerns addressed (logging, config, CORS)
- [x] Project initialization commands documented
- [x] Integration points explained (backend/frontend, backend/DB, backend/human services)

---

## Next Steps

1. **Review this architecture document** - Ensure all decisions align with your vision
2. **Proceed to Story 1.1** - AI dev agent creates project structure and database schema
3. **Implement human services** - Fill in `resume_parser.py`, `nlp_service.py`, `alignment_service.py` during/after AI agent work
4. **Build frontend** - Implement React UI consuming backend APIs (Epic 2)
5. **Demo preparation** - Test end-to-end flow, prepare 5-minute presentation

**This architecture ensures AI agents build consistent, hackathon-ready backend infrastructure while you focus on the ML/NLP brain and user experience.**

---

**Document Status:** ✅ Complete and validated
**Ready for Implementation:** Yes
**Next Workflow:** story-context (Scrum Master prepares Story 1.1)

