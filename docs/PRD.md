# hiresight Product Requirements Document (PRD)

**Author:** Srijan
**Date:** 2025-10-24
**Project Level:** 2
**Target Scale:** Medium project - multiple epics, 10+ stories

---

## Goals and Background Context

### Goals

1. **Reduce misalignment-driven turnover** - Help mission-driven companies hire candidates who genuinely care about their mission, reducing first-year turnover from 30-40% to <20%

2. **Enable passion-driven career discovery** - Allow tech professionals to find roles at companies whose missions align with their values, reducing time-to-find-aligned-opportunity from 5+ hours to <10 minutes

3. **Prove alignment matching viability** - Demonstrate through hackathon MVP that alignment-first matching (domain/values over skills keywords) produces better hiring outcomes than traditional platforms

### Background Context

Traditional hiring platforms (LinkedIn, Indeed) optimize for skills keyword matching, asking "Can you do this job?" while missing the critical question: "Should you do this job at THIS company?" This fundamental misalignment leads to 70% employee disengagement and costs US companies $1 trillion annually in turnover. Professionals accept positions at organizations whose missions they don't share, leading to burnout and departure within 18-24 months.

HireSight reframes hiring from skills matching to alignment matching. By analyzing resumes and company missions to calculate 0-100% alignment scores based on domain/values matching, we help candidates discover companies they'll genuinely care about while enabling mission-driven startups (climate tech, EdTech, healthtech) to identify candidates who demonstrate authentic commitment signals. Our unique moat—journey tracking over time—detects when candidates grow toward alignment and auto-notifies companies, revealing commitment that resumes can't capture.

---

## Requirements

### Functional Requirements

**Core Matching Engine:**
- FR001: System shall accept resume uploads (PDF/DOCX format) and extract candidate data including skills, domain keywords, and values signals using NLP
- FR002: System shall store and manage company profiles including mission statements, required skills, values, and domain classifications
- FR003: System shall calculate 0-100% alignment scores for candidate-company pairs using weighted algorithm (60% domain/mission match + 40% values alignment)
- FR004: System shall rank and display companies for candidates sorted by alignment percentage with visual indicators

**Skill Gap Analysis:**
- FR005: System shall identify skill gaps between candidate profiles and company requirements
- FR006: System shall generate recommended learning paths showing which skills candidates need to develop for specific companies

**Interest Tracking:**
- FR007: System shall allow candidates to bookmark companies and track interest with timestamps
- FR008: System shall store interest tracking data for future journey tracking capabilities

**Company Features:**
- FR009: System shall allow companies to view candidates ranked by alignment scores
- FR010: System shall display alignment reasoning showing passion signals (e.g., "2 years exploring climate tech") rather than just keyword matches
- FR011: System shall enable companies to upload job descriptions and candidate resumes for batch processing

**Data Persistence:**
- FR012: System shall persist all candidate, company, and interest tracking data in a queryable database
- FR013: System shall respond to alignment score queries in <1 second for MVP dataset (20 companies, demo candidates)

**Demo Capability:**
- FR014: System shall provide a demo "growth notification" feature showing how journey tracking would work (hardcoded for hackathon MVP)

### Non-Functional Requirements

- NFR001: **Performance** - System shall process resume uploads and return alignment scores within 10 seconds for the candidate-facing experience
- NFR002: **Reliability** - System shall maintain zero crashes or errors during 5-minute demo presentation
- NFR003: **Usability** - UI shall be intuitive enough that judges can understand alignment scores and skill gaps without explanation

---

## User Journeys

### Primary User Journey: Candidate Discovers Aligned Companies

**Actor:** Sarah, mission-driven software engineer looking for climate tech roles

**Journey Steps:**

1. **Upload Resume**
   - Sarah visits HireSight and uploads her resume (PDF)
   - System extracts her skills (Python, React, ML) and domain interests (sustainability projects, climate data)
   - Confirmation: "Resume processed successfully"

2. **View Alignment Results**
   - Sarah sees list of 20 companies ranked by alignment score
   - Top match: "ClimateAI Solutions - 92% alignment"
   - Visual progress bars and brief reasoning: "Strong match: 2 years experience in climate data projects"

3. **Check Skill Gap**
   - Sarah clicks "Check Skill Gap" for a 78% aligned company
   - Modal shows: Missing skills: "Kubernetes, Climate modeling"
   - Learning path displayed: "Recommended: Cloud Native Computing course, Climate Science fundamentals"

4. **Track Interest**
   - Sarah clicks "Track Interest" on 3 companies she wants to pursue
   - System confirms: "Tracking your interest in [Company]. We'll notify them when you grow your skills."
   - Bookmarks visible on company cards

5. **Outcome**
   - Sarah has clear understanding of which companies align with her values
   - Knows exactly what to learn to improve alignment for aspirational roles
   - Journey tracked for future growth notifications (post-MVP feature)

### Secondary User Journey: Company Finds Aligned Candidates

**Actor:** Alex, hiring manager at GreenTech Startup (climate-focused EdTech company)

**Journey Steps:**

1. **Upload Job Requirements**
   - Alex uploads job description for Senior Software Engineer role
   - System extracts required skills (Python, AWS, education domain experience) and mission keywords (climate education, sustainability)
   - Confirmation: "Job profile created successfully"

2. **Upload Candidate Resumes**
   - Alex uploads 50 candidate resumes received from traditional job boards (batch processing)
   - System processes all resumes and calculates alignment scores
   - Progress indicator: "Processing 50 candidates... Complete"

3. **View Ranked Candidates**
   - Alex sees candidates ranked by alignment score
   - Top match: "Maria Chen - 88% alignment"
   - Reasoning displayed: "Strong passion signals: 3 years building climate education tools, contributed to open-source sustainability projects"
   - Can filter by alignment threshold (e.g., show only >70%)

4. **Compare Candidates**
   - Alex compares top 3 candidates
   - Traditional resume screening would prioritize John (most keywords)
   - HireSight highlights Maria (genuine climate-ed passion) over John (generic experience)
   - Decision: Invite Maria to interview based on authentic alignment signals

5. **View Growth Notification (Demo)**
   - Alex clicks "Demo Growth Tracking" button
   - Sees mockup notification: "Candidate tracked interest 3 months ago, improved alignment 65% → 82%, learned Python + ML fundamentals"
   - Understands future value: candidates who demonstrate commitment over time

6. **Outcome**
   - Alex identifies candidates who genuinely care about climate education mission
   - Reduces resume screening time from 15 hours to 2 hours
   - Confident that selected candidates will stay long-term (aligned with mission)

---

## UX Design Principles

1. **Clarity over complexity** - Alignment scores and reasoning must be immediately understandable without explanation (critical for 5-minute demo)

2. **Speed and responsiveness** - Candidate should see results within 10 seconds of upload; no loading states that break demo flow

3. **Trust through transparency** - Show WHY alignment scores are calculated (e.g., "2 years climate projects" not just "88%")

4. **Simplicity for hackathon scope** - Clean, professional interface without authentication complexity or advanced features

---

## User Interface Design Goals

**Platform & Screens:**

- **Target Platform:** Web application (desktop-first, mobile-responsive)
- **Browser Support:** Chrome, Firefox, Safari (latest versions for demo)

**Core Screens:**

1. **Candidate Upload Page**
   - Drag-and-drop resume upload
   - Processing confirmation
   - Clean, welcoming design

2. **Company List View (Candidate)**
   - Ranked list with alignment percentages
   - Visual progress bars (color-coded: green >80%, yellow 60-79%, gray <60%)
   - "Check Skill Gap" and "Track Interest" buttons per company

3. **Skill Gap Modal**
   - Missing skills list
   - Recommended learning path
   - Clear call-to-action

4. **Company Dashboard**
   - Candidates ranked by alignment
   - Passion signals highlighted
   - Demo "Growth Notification" button

**Design Constraints:**

- No authentication UI (demo-only, single-session)
- Lightweight styling (custom CSS or Tailwind CDN)
- Focus on data presentation clarity
- Must be "real product" believable for judges

---

## Epic List

**Epic 1: Foundation & Core Matching Engine**
- **Goal:** Establish project infrastructure, database, and core alignment matching algorithm
- **Estimated Stories:** 6-8 stories
- **Deliverable:** Working backend with alignment scoring, seeded company data, and functional APIs

**Epic 2: User Experience & Demo Polish**
- **Goal:** Build candidate and company frontends, implement skill gap analysis, and create demo-ready presentation
- **Estimated Stories:** 4-6 stories
- **Deliverable:** Complete UI with resume upload, company rankings, skill gaps, and growth notification demo

> **Note:** Detailed epic breakdown with full story specifications is available in [epics.md](./epics.md)

---

## Out of Scope

**Authentication & User Management:**
- No user accounts, passwords, or login flows
- No session persistence across browser sessions
- No user profile management
- Post-MVP: Auth0 or Firebase authentication

**Advanced Journey Tracking:**
- No actual re-upload detection or historical comparison
- No automated growth notifications (demo only with hardcoded example)
- No profile history tracking over time
- Post-MVP: Full journey tracking backend with database history

**External Integrations:**
- No real-time GitHub integration or repository analysis
- No email/push notification services
- No payment/subscription system (Stripe)
- No ATS integration (Greenhouse, Lever, Workday)
- No learning platform partnerships (Coursera, Udemy)
- Post-MVP: Strategic integrations as platform scales

**Advanced Features:**
- No advanced NLP (sentiment analysis, deep resume understanding)
- No mobile native applications (web-responsive only)
- No multi-language support (English only)
- No AI-powered course recommendations (basic skill gap lists only)
- Post-MVP: Enhanced ML models and features

**Scale & Production Readiness:**
- No production deployment or cloud hosting (local demo only)
- No load testing or high-concurrency support
- No comprehensive error handling beyond demo scenarios
- No data backup or disaster recovery
- Post-MVP: Production infrastructure on AWS/GCP
