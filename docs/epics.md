# hiresight - Epic Breakdown

**Author:** Srijan
**Date:** 2025-10-24
**Project Level:** 2
**Target Scale:** Medium project - multiple epics, 10+ stories

---

## Overview

This document provides the detailed epic breakdown for hiresight, expanding on the high-level epic list in the [PRD](./PRD.md).

Each epic includes:

- Expanded goal and value proposition
- Complete story breakdown with user stories
- Acceptance criteria for each story
- Story sequencing and dependencies

**Epic Sequencing Principles:**

- Epic 1 establishes foundational infrastructure and initial functionality
- Subsequent epics build progressively, each delivering significant end-to-end value
- Stories within epics are vertically sliced and sequentially ordered
- No forward dependencies - each story builds only on previous work

---

## Epic 1: Foundation & Core Matching Engine

**Expanded Goal:**

Establish the technical foundation for HireSight by creating the project infrastructure, database schema, and core alignment matching algorithm. This epic delivers a working backend API that can accept resume uploads, calculate alignment scores against seeded company data, and provide skill gap analysis. The deliverable is a fully functional matching engine that can be tested via API calls, setting the stage for UI development in Epic 2.

**Value Delivery:**

By the end of this epic, the core business logic (alignment calculation algorithm) will be proven and functional. The database will be seeded with 20 real mission-driven companies across climate tech, EdTech, and healthcare sectors, enabling immediate demo readiness. All APIs will respond in <1 second, validating technical feasibility for the hackathon presentation.

---

### Story Breakdown

**Story 1.1: Project Setup & Database Schema**

As a developer,
I want to set up the project structure and create the database schema,
So that I have a foundation to build the matching engine.

**Acceptance Criteria:**
1. FastAPI project initialized with proper directory structure (routes, models, services)
2. SQLite database created with tables: companies, candidates, interests
3. Companies table includes: id, name, mission, values, required_skills, domain
4. Candidates table includes: id, resume_text, extracted_skills, interests, domains
5. Interests table includes: candidate_id, company_id, timestamp
6. Database connection configured and tested
7. Basic health check endpoint (GET /health) returns 200 OK

**Prerequisites:** None (first story)

---

**Story 1.2: Seed Company Data**

As a developer,
I want to populate the database with 20 real mission-driven companies,
So that candidates have meaningful companies to match against during the demo.

**Acceptance Criteria:**
1. 20 companies researched and data collected (name, mission, values, required skills, domain)
2. Companies span multiple sectors: Climate tech (8), EdTech (6), HealthTech (4), Social Impact (2)
3. Each company has complete data: mission statement, 3-5 values, 5-10 required skills, domain classification
4. Database seeding script created to populate companies table
5. Script is idempotent (can run multiple times without duplicates)
6. Verification: Query returns all 20 companies with complete data

**Prerequisites:** Story 1.1 (database schema must exist)

---

**Story 1.3: Resume Upload & NLP Parsing**

As a candidate,
I want to upload my resume and have it parsed automatically,
So that my skills and interests are extracted without manual entry.

**Acceptance Criteria:**
1. POST /upload-resume endpoint accepts PDF/DOCX file uploads
2. NLP library (spaCy or NLTK) integrated and configured
3. Resume parsing extracts: skills (technical keywords), domain keywords, values signals
4. Extracted data stored in candidates table
5. Endpoint returns candidate_id and confirmation message
6. Error handling: Invalid file format returns 400 with clear message
7. Processing completes within 5 seconds for typical resume

**Prerequisites:** Story 1.1 (database schema must exist)

---

**Story 1.4: Alignment Scoring Algorithm**

As a developer,
I want to implement the core alignment scoring algorithm,
So that candidates can be matched with companies based on domain/values alignment.

**Acceptance Criteria:**
1. Alignment calculation function implements weighted algorithm: 60% domain match + 40% values alignment
2. Domain matching uses cosine similarity or keyword overlap between candidate domains and company mission
3. Values matching compares candidate interests with company values
4. Function returns alignment score (0-100%) for any candidate-company pair
5. Reasoning string generated explaining why score was calculated (e.g., "2 years climate projects")
6. Unit tests validate scoring logic with sample data
7. Edge cases handled: missing data, empty fields, no overlap

**Prerequisites:** Story 1.2 (company data), Story 1.3 (candidate data)

---

**Story 1.5: Company List API with Ranking**

As a candidate,
I want to retrieve a ranked list of companies based on my alignment scores,
So that I can discover which companies match my values and interests.

**Acceptance Criteria:**
1. GET /companies?candidate_id=X endpoint created
2. Endpoint calculates alignment scores for all 20 companies for given candidate
3. Companies sorted by alignment score (highest first)
4. Response includes: company_name, alignment_percentage, brief_reason
5. API responds in <500ms for full company list
6. Returns 404 if candidate_id doesn't exist
7. Response format is clean JSON suitable for frontend consumption

**Prerequisites:** Story 1.4 (alignment algorithm must exist)

---

**Story 1.6: Skill Gap Analysis API**

As a candidate,
I want to check my skill gaps for specific companies,
So that I know what to learn to improve my alignment.

**Acceptance Criteria:**
1. POST /check-gap endpoint accepts candidate_id + company_id
2. Calculates skill difference: required_skills - candidate_skills
3. Returns missing_skills list
4. Generates recommended_learning_path (simple list of skill names to learn)
5. Returns 404 if candidate or company doesn't exist
6. Edge case: If no skill gap, returns empty list with success message
7. Response time <200ms

**Prerequisites:** Story 1.5 (candidate and company data must be queryable)

---

**Story 1.7: Interest Tracking API**

As a candidate,
I want to bookmark companies I'm interested in,
So that the system tracks my journey and can notify companies when I grow.

**Acceptance Criteria:**
1. POST /track-interest endpoint accepts candidate_id + company_id
2. Stores interest record in interests table with current timestamp
3. Returns success confirmation message
4. Prevents duplicate entries (same candidate + company)
5. Returns 404 if candidate or company doesn't exist
6. Interest records are queryable for future journey tracking features

**Prerequisites:** Story 1.5 (candidate and company data must exist)

---

**Story 1.8: Company Candidate Ranking API**

As a hiring manager,
I want to view candidates ranked by alignment score for my company,
So that I can identify candidates who genuinely care about our mission.

**Acceptance Criteria:**
1. POST /candidates endpoint accepts company_id and list of candidate resumes
2. Batch processes uploaded candidate resumes (uses Story 1.3 parsing logic)
3. Calculates alignment scores for all candidates against specified company
4. Returns candidates sorted by alignment score with reasoning
5. Reasoning highlights passion signals (e.g., "3 years building climate tools") over keywords
6. Supports filtering by alignment threshold (e.g., show only >70%)
7. Response time <2 seconds for batch of 10 candidates

**Prerequisites:** Story 1.4 (alignment algorithm), Story 1.3 (resume parsing)

---

## Epic 2: User Experience & Demo Polish

**Expanded Goal:**

Build the complete user-facing experience for both candidates and companies, transforming the backend APIs from Epic 1 into an intuitive, demo-ready web application. This epic delivers polished UI screens for resume upload, company discovery with alignment scores, skill gap analysis, and interest tracking. The final story adds demo-specific features (growth notification mockup) that showcase the long-term vision to hackathon judges without requiring full implementation of journey tracking.

**Value Delivery:**

By the end of this epic, HireSight will be a complete, presentable web application ready for the 5-minute hackathon demo. Judges will experience the "wow moment" when they see alignment scores with transparent reasoning, understand skill gaps instantly, and witness the growth notification demo that illustrates the platform's unique moat. The UI will be clean, professional, and believable as a real product despite being built in 24 hours.

---

### Story Breakdown

**Story 2.1: Candidate Resume Upload UI**

As a candidate,
I want a clean, intuitive interface to upload my resume,
So that I can quickly get started discovering aligned companies.

**Acceptance Criteria:**
1. Landing page created with welcoming design and clear value proposition
2. Drag-and-drop resume upload component implemented
3. File type validation (PDF/DOCX only) with user-friendly error messages
4. Upload progress indicator displays while processing
5. Success confirmation shows: "Resume processed! Analyzing your alignment..."
6. Auto-redirect to company list view after successful upload
7. Responsive design works on desktop and tablet
8. Page loads in <2 seconds

**Prerequisites:** Story 1.3 (resume upload API must exist)

---

**Story 2.2: Company List View with Alignment Scores**

As a candidate,
I want to see all companies ranked by alignment score with visual indicators,
So that I can quickly identify which companies match my values.

**Acceptance Criteria:**
1. Company list page displays all 20 companies sorted by alignment percentage
2. Each company card shows: name, alignment score, brief reasoning
3. Visual progress bars color-coded: green (>80%), yellow (60-79%), gray (<60%)
4. Reasoning text displays passion signals (e.g., "Strong match: 2 years climate data projects")
5. "Check Skill Gap" and "Track Interest" buttons on each card
6. Page is responsive and scrollable
7. Loading state handled gracefully if API call takes >1 second
8. Data fetched from GET /companies API (Story 1.5)

**Prerequisites:** Story 1.5 (company list API), Story 2.1 (candidate upload flow)

---

**Story 2.3: Skill Gap Analysis Modal**

As a candidate,
I want to click "Check Skill Gap" and see what I need to learn,
So that I understand how to improve my alignment with aspirational companies.

**Acceptance Criteria:**
1. Clicking "Check Skill Gap" button opens modal overlay
2. Modal displays company name and current alignment score
3. Missing skills listed clearly (e.g., "Kubernetes, Climate modeling")
4. Recommended learning path shown as simple list
5. "Close" button dismisses modal and returns to company list
6. Modal design is clean and doesn't feel overwhelming
7. Data fetched from POST /check-gap API (Story 1.6)
8. Loading spinner shows while fetching gap analysis

**Prerequisites:** Story 1.6 (skill gap API), Story 2.2 (company list UI)

---

**Story 2.4: Interest Tracking Feature**

As a candidate,
I want to bookmark companies I'm interested in,
So that the system tracks my journey for future growth notifications.

**Acceptance Criteria:**
1. "Track Interest" button on each company card
2. Clicking button shows confirmation toast: "Tracking your interest in [Company]"
3. Button changes to "Tracking" with visual indicator (checkmark or star icon)
4. Tracked companies visually distinguished in list (border highlight or badge)
5. Interest stored via POST /track-interest API (Story 1.7)
6. User can toggle tracking on/off
7. Toast auto-dismisses after 3 seconds

**Prerequisites:** Story 1.7 (interest tracking API), Story 2.2 (company list UI)

---

**Story 2.5: Company Dashboard for Hiring Managers**

As a hiring manager,
I want to upload candidate resumes and see them ranked by alignment,
So that I can identify candidates who genuinely care about our mission.

**Acceptance Criteria:**
1. Company dashboard page created (separate from candidate view)
2. Job description upload form with company selection dropdown
3. Batch resume upload interface (drag-and-drop multiple files)
4. Processing indicator: "Analyzing 10 candidates..."
5. Results display: candidates ranked by alignment score
6. Each candidate shows: name, alignment %, reasoning with passion signals
7. Reasoning highlights authentic signals (e.g., "3 years building climate education tools")
8. Filter option: show only candidates above threshold (e.g., >70%)
9. Data fetched from POST /candidates API (Story 1.8)

**Prerequisites:** Story 1.8 (company candidate ranking API), Story 2.1 (upload UI patterns)

---

**Story 2.6: Growth Notification Demo Feature**

As a judge,
I want to see how journey tracking would work in the future,
So that I understand HireSight's unique moat and long-term vision.

**Acceptance Criteria:**
1. "Demo Growth Tracking" button added to company dashboard (Story 2.5)
2. Clicking button displays hardcoded notification banner/modal
3. Notification shows example: "Candidate Sarah Chen tracked interest 3 months ago"
4. Progress display: "Alignment improved: 65% → 82%"
5. Skills gained shown: "Learned: Python, ML fundamentals"
6. Projects added shown: "Built: Climate data dashboard"
7. Call-to-action: "Contact Candidate" button (non-functional, visual only)
8. Banner design is polished and conveys "future feature" clearly
9. Judges understand this demonstrates commitment signal tracking over time

**Prerequisites:** Story 2.5 (company dashboard must exist)

---

---

## Story Guidelines Reference

**Story Format:**

```
**Story [EPIC.N]: [Story Title]**

As a [user type],
I want [goal/desire],
So that [benefit/value].

**Acceptance Criteria:**
1. [Specific testable criterion]
2. [Another specific criterion]
3. [etc.]

**Prerequisites:** [Dependencies on previous stories, if any]
```

**Story Requirements:**

- **Vertical slices** - Complete, testable functionality delivery
- **Sequential ordering** - Logical progression within epic
- **No forward dependencies** - Only depend on previous work
- **AI-agent sized** - Completable in 2-4 hour focused session
- **Value-focused** - Integrate technical enablers into value-delivering stories

---

**For implementation:** Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown.
