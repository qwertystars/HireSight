# Brainstorming Session Results

**Session Date:** 2025-10-24
**Facilitator:** Strategic Business Analyst Mary
**Participant:** Srijan

## Executive Summary

**Topic:** HireSight - Hackathon MVP focused on core features only (no authentication or auxiliary features)

**Session Goals:** Define the complete hackathon project scope - identify the absolute core features needed to demonstrate value, map out the minimal viable implementation, and create a clear execution plan for the hackathon timeframe

**Techniques Used:** First Principles Thinking, SCAMPER Method, Resource Constraints

**Total Ideas Generated:** 45+ (across immediate opportunities, future innovations, and moonshots)

### Key Themes Identified:

1. **Alignment Over Skills** - The fundamental reframe from "can you do this?" to "should you do this here?"
2. **Commitment Signals** - Tracking growth over time reveals authentic passion better than resumes
3. **Ethical Differentiation** - Refusing to nudge toward misalignment creates trust and moat
4. **Demo Smart, Build Core** - Show ambitious vision with hardcoded features, build only essentials
5. **Two-Tier Discovery** - Show all alignments, then provide conditional growth paths only for authentic matches

## Technique Sessions

### Session 1: First Principles Thinking (15 min)

**Fundamental Truths Identified:**

1. **Misalignment is the core problem** - Good people are selected but by the wrong companies, leading to eventual departure
2. **Passion vs. Paycheck** - People want to work for something they care about, not just what they learned to make money
3. **Discovery Gap** - Candidates need to know which companies align with their values/passions
4. **Company Clarity Gap** - Companies need to know who they truly want (beyond just skills)
5. **The real problem isn't skills matching - it's VALUES and PASSION alignment**

**Key Insight:** Traditional hiring focuses on "can you do the job?" but the first principle is "should you do THIS job at THIS company?" - alignment before capability.

**Minimal Solution - Three Core Elements:**

1. **Candidate Profile:** What the candidate knows/cares about
2. **Company Needs:** What the company needs (skills + values)
3. **Growth Guidance:** If there's a gap, what should candidates develop interest in?

**The Core Value Proposition:** Not just "here's a match" but "here's your path to alignment" - shows candidates which companies align NOW and what to learn/explore to align with dream companies LATER.

**First Principles Conclusion:** HireSight = Alignment Matcher + Growth Compass

**The "Wow Moment" - Core Demo Flow:**

**Primary View: Reverse Match (Company-First Perspective)**
- Companies enter values/mission → See candidates who CARE about this work
- Shows passion and exploration history, not just skills/resume
- "Sarah has been exploring climate solutions for 2 years" > "John has React skills"

**Secondary Flow: Alignment + Conditional Gap Bridge**
- IF: High alignment (shared values/passion) + Skill gap EXISTS
  - THEN: Show roadmap to bridge the gap
  - Message: "You care about the right things, here's how to build the skills"
- IF: High alignment + Skills match
  - THEN: Direct match, no roadmap needed
- IF: Low alignment (even with skills)
  - THEN: Don't show roadmap - no nudging toward misaligned work

**Ethical Principle:** Only help candidates grow toward what they ALREADY care about. Never push them toward companies that don't align with their values, regardless of money offered.

**Key Differentiator:** Protects candidate authenticity over company acquisition budgets.

### Session 2: SCAMPER Method - Feature Definition (20 min)

**S - SUBSTITUTE: Implementation Reality**

**What we keep from traditional hiring:**
- Resumes/CVs (familiar input for candidates)
- Job descriptions (familiar input for companies)
- GitHub profiles (optional enrichment)

**What we substitute in interpretation:**
- Traditional: Keyword matching for skills
- HireSight: Domain/values extraction for alignment

**Core User Flows Defined:**

**Company Flow:**
1. Upload job description (manual input)
2. Upload candidate resumes (batch or individual)
3. Get ranked candidates by alignment score
4. See WHY each candidate aligns (passion signals, not just skills)

**Candidate Flow:**
1. Upload resume
2. See companies ranked by alignment percentage
   - 90-100%: Strong alignment, apply now
   - 60-89%: Partial alignment, see gap bridge roadmap
   - <60%: Low alignment, don't show or show as "not recommended"
3. For partial matches: See what to learn/explore to increase alignment

**Critical Challenge Identified:**
System requires large company dataset to understand nuances and show meaningful alignment variations. Without sufficient company data, AI can't distinguish between "good fit" vs "totally different company."

**Hackathon Data Problem:** Need to solve the cold-start problem for demo.

**Solution: Seed with Real Companies**
- Pre-populate 20-30 real companies across domains (Climate, EdTech, FinTech, Healthcare, Social Impact, Big Tech)
- Scrape mission/values from About Us, Careers pages
- Makes demo tangible and relatable for judges

**C - COMBINE: Enhanced Candidate Recommendation System**

**Two-Tiered Recommendation for Candidates:**

**Tier 1: Alignment Score Display**
- Show all companies with alignment percentage
- Example: "Company X is 60% aligned with your goals and values"
- Clear visibility across ALL companies in database

**Tier 2: Skill Gap Analysis (On-Demand)**
- For ANY company in the list, candidate can click "Check Skill Gap"
- System shows: Current skills vs Required skills
- Gap identified with learning roadmap

**The Journey Tracking Feature (POWERFUL):**

When candidate chooses to pursue a company:
1. **Bookmark/Select:** Candidate indicates interest in Company X
2. **Track Progress:** System saves baseline snapshot
   - Alignment score: 60%
   - Skill gap: [Python, ML, Domain Knowledge]
3. **Candidate Goes Away:** Learns, builds projects, gains experience
4. **Return to HireSight:** Re-upload resume or connect GitHub
5. **System Detects Growth:**
   - Alignment: 60% → 75%
   - Skills: Gap closed (new projects show Python/ML work)
   - Bonus signals: New GitHub projects in relevant domain
6. **Auto-Notification to Company:**
   "Candidate [Name] showed interest in your role 3 months ago.
   Progress update:
   - Alignment: ↑ 15%
   - Skills acquired: Python, ML fundamentals
   - New projects: [Climate dashboard project]
   - Demonstrated commitment to your mission"

**Value Proposition:**
- **For Candidates:** Clear growth path + proof of effort
- **For Companies:** See candidates who CARE enough to grow toward alignment
- **Unique Moat:** You're not just matching, you're tracking COMMITMENT over time

**E - ELIMINATE: Hackathon Scope - What to Cut**

**What we're NOT building for hackathon:**
- ❌ Real authentication system
- ❌ Full journey tracking backend
- ❌ Actual re-upload detection logic
- ❌ Real-time GitHub integration
- ❌ Email notification system

**What we're DEMONSTRATING with clever shortcuts:**
- ✅ Core matching engine (real)
- ✅ Skill gap analysis (real)
- ✅ Bookmark feature (real, simple state)
- ✅ Growth notification (DEMO BUTTON)
  - Hardcoded notification banner
  - "Show Example" button → displays pre-written notification
  - Shows candidate from list who "returned" with growth
  - Demonstrates the concept without building full tracking

**Demo Strategy:** Build real value (matching), fake the complex parts (notifications) to show vision.

**M - MODIFY: Feature Priorities for Hackathon**

**MUST BUILD (Core MVP):**
1. Resume upload & parsing
2. Alignment score calculation & display
3. Company list with percentages
4. "Check Skill Gap" button → shows gap analysis
5. "Track Interest" bookmark button
6. Company view: See ranked candidates

**DEMO/MOCKUP (Show concept):**
7. "Demo Growth Notification" button (hardcoded banner)
8. Before/After comparison (static mockup)

**FUTURE FEATURES (Mention in pitch):**
9. Real journey tracking over time
10. Automated company notifications
11. GitHub auto-sync
12. Learning resource recommendations

### Session 3: Resource Constraints - 24-Hour Hackathon Plan (15 min)

**Hackathon Context:**
- **Duration:** 24 hours
- **Team:** 4 people (2 Frontend, 1 Backend, 1 ML/Scoring)
- **Tech Stack:**
  - Frontend: HTML, CSS, JS
  - Backend: Python, FastAPI, .db files (SQLite)
  - ML: Dynamic weighted scoring algorithm
- **Pre-Work Completed:**
  - Phase 1 (Analysis) + Phase 2 (Planning) done via BMAD
  - Resume parsing understood (AI can implement)
  - GitHub repo integration done (analysis logic needed)
- **Goal:** Everything works for demo

**Constraint-Based Feature Prioritization:**

**TIER 1 - Hour 0-12 (MUST WORK for demo):**
1. **Database schema** (.db file with tables visible)
   - Companies table (name, mission, values, skills_required)
   - Candidates table (name, resume_text, skills, interests)
   - Interests table (track bookmarks)
2. **Backend APIs** (FastAPI)
   - POST /upload-resume (parse + store)
   - GET /companies (return all with alignment scores)
   - POST /check-gap (calculate skill gap for company)
   - POST /track-interest (bookmark company)
   - GET /candidates (company view)
3. **ML Scoring Algorithm**
   - Extract skills + domain keywords from resume
   - Calculate alignment score (weighted: 60% domain match, 40% values)
   - Skill gap calculation
4. **Seed Data**
   - 20 real companies pre-populated

**TIER 2 - Hour 12-20 (Core UX):**
5. **Candidate Frontend**
   - Upload resume page
   - Company list with alignment percentages
   - "Check Gap" modal/popup
   - "Track Interest" button
6. **Company Frontend**
   - View ranked candidates
   - See alignment reasoning

**TIER 3 - Hour 20-24 (Demo Polish):**
7. **Demo Button** (hardcoded notification)
8. **Styling/UX polish**
9. **Pitch deck preparation**
10. **Demo script walkthrough**

**What to Build vs What to Fake:**
- ✅ Build: All TIER 1 + most of TIER 2
- 🎭 Fake: Growth tracking (demo button)
- ⏭️ Skip: Auth, real GitHub analysis (mention as future)

**DETAILED 24-HOUR EXECUTION PLAN:**

**Phase 1: Foundation (Hours 0-6)**

**Hour 0-2: Setup & Architecture**
- ALL: Project setup, repo structure, dependencies
- Backend: Database schema design + seed data script
- ML: Research resume parsing libraries (spaCy/NLTK)
- Frontend: Wireframe screens, component structure

**Hour 2-4: Core Backend**
- Backend: Implement database models, seed 20 companies
- ML: Build resume parser (extract skills, keywords, domains)
- Frontend: Build upload UI + basic layout

**Hour 4-6: Scoring Algorithm**
- ML: Implement alignment scoring algorithm
- Backend: API endpoint for /upload-resume
- Frontend: Company list display (hardcoded data first)

**MILESTONE 1:** Resume uploads to DB, scoring algo works on test data

**Phase 2: Integration (Hours 6-12)**

**Hour 6-8: Core APIs**
- Backend: GET /companies with dynamic alignment scores
- Backend: POST /check-gap endpoint
- ML: Skill gap calculation logic
- Frontend: Connect upload to backend

**Hour 8-10: Candidate Flow**
- Frontend: Display company list with real alignment scores
- Frontend: "Check Gap" button + modal
- Backend: POST /track-interest endpoint
- Frontend: Bookmark functionality

**Hour 10-12: Company View**
- Backend: GET /candidates endpoint (ranked by alignment)
- Frontend: Company dashboard showing ranked candidates
- Frontend: Show WHY candidates align (domain matches)

**MILESTONE 2:** End-to-end candidate flow works, company view shows ranked list

**Phase 3: Polish & Demo (Hours 12-24)**

**Hour 12-16: UX Enhancement**
- Frontend: Styling, responsive design
- Frontend: "Demo Notification" button (hardcoded)
- Frontend: Better visualizations (progress bars, score indicators)
- Backend: API error handling, validation

**Hour 16-18: Demo Scenarios**
- ALL: Create 3-5 test resumes with different profiles
- ALL: Verify all flows work end-to-end
- Frontend: Polish the notification mockup

**Hour 18-20: Buffer & Bug Fixes**
- ALL: Test everything, fix bugs
- ALL: Ensure demo can run smoothly
- Backend: Verify .db file is visible/queryable

**Hour 20-22: Pitch Preparation**
- ALL: Create pitch deck
- ALL: Practice demo script
- ALL: Prepare talking points about future features

**Hour 22-24: Final Polish & Sleep**
- Minor tweaks only
- Final walkthrough
- Get some rest before presentation!

**Critical Success Factors:**
1. ✅ Resume upload → See aligned companies (MUST WORK)
2. ✅ Check gap → See roadmap (MUST WORK)
3. ✅ Company view → See ranked candidates (MUST WORK)
4. ✅ Demo button → Show growth notification (MUST IMPRESS)
5. ✅ .db file visible → Proves data persistence

## Idea Categorization

### Immediate Opportunities

_Ideas ready to implement now for hackathon_

1. **Resume-based alignment matching** - Use existing resume format, reinterpret through values/domain lens
2. **Two-tier recommendation system** - Show all companies with alignment %, then on-demand gap analysis
3. **Seed with real companies** - 20-30 pre-populated companies across domains (Climate, EdTech, FinTech, Healthcare, Social Impact)
4. **Simple bookmark tracking** - Let candidates mark interest in companies
5. **Demo button for growth notification** - Hardcoded banner showing the vision without building full tracking
6. **SQLite database** - Visible .db file proves data persistence for judges
7. **Reverse match view** - Company dashboard showing candidates ranked by alignment

### Future Innovations

_Ideas requiring development/research (mention in pitch)_

1. **Full journey tracking** - Actually track candidate growth over weeks/months
2. **Automated company notifications** - Real-time alerts when tracked candidates improve alignment
3. **GitHub auto-sync** - Pull commits, projects, contributions automatically to detect skill growth
4. **Learning resource recommendations** - Suggest courses, projects, readings to close gaps
5. **Commitment scoring** - Weight candidates who demonstrate consistent interest over time
6. **Multi-dimensional alignment** - Beyond values: culture fit, work style, team dynamics
7. **Company culture profiles** - Rich profiles beyond job descriptions (mission, impact stories, team values)

### Moonshots

_Ambitious, transformative concepts_

1. **HireSight as a career GPS** - Not just matching, but lifelong guidance toward aligned work
2. **Reverse the power dynamic** - Candidates choose companies, not the other way around
3. **End resume fraud** - GitHub/project history provides authentic proof of skills and interests
4. **Kill the cover letter** - Alignment scores replace persuasive writing with authentic signals
5. **Ethical hiring marketplace** - Companies compete on values/mission, not just compensation
6. **Passion-first economy** - Help people find work they love, reducing burnout and turnover globally

### Insights and Learnings

_Key realizations from the session_

1. **The real hiring problem is misalignment, not skills gaps** - People leave jobs not because they can't do them, but because they don't care about them
2. **Commitment is the ultimate signal** - A candidate who spends 3 months learning to align with your company is more valuable than a perfect-skill candidate with no passion
3. **Demo the vision, build the core** - For hackathons, show the ambitious future with smart shortcuts while building only essential features
4. **Ethical moat is defensible** - Refusing to nudge candidates toward misaligned work (even for money) creates trust and differentiation
5. **Alignment before capability** - The first question isn't "can you do this?" but "should you do this at this company?"
6. **Journey tracking > snapshot matching** - Tracking growth over time reveals commitment better than any resume snapshot

## Action Planning

### Top 3 Priority Ideas

#### #1 Priority: Build Core Alignment Matching Engine

- **Rationale:** This is the foundational value proposition. Without accurate alignment scoring, everything else falls apart. Must work perfectly for demo credibility.

- **Next steps:**
  1. Backend dev: Design database schema (Companies, Candidates, Interests tables)
  2. ML dev: Implement resume parsing (extract skills, domains, keywords)
  3. ML dev: Build weighted alignment algorithm (60% domain match, 40% values alignment)
  4. Backend dev: Create seed data script with 20 real companies
  5. Test with diverse resume profiles to verify scoring makes sense

- **Resources needed:**
  - Python libraries: spaCy/NLTK for NLP, SQLite for database
  - Real company data: scrape mission/values from company websites
  - Test resumes: 5-10 diverse profiles across domains

- **Timeline:** Hours 0-6 (first 25% of hackathon)

#### #2 Priority: Two-Tier Recommendation System with Gap Analysis

- **Rationale:** This is the unique differentiator - not just showing matches, but showing growth paths. The "wow factor" that makes judges lean forward.

- **Next steps:**
  1. Frontend: Build company list UI with alignment percentages
  2. Backend: GET /companies endpoint with sorting by alignment
  3. Frontend: "Check Gap" button for each company
  4. Backend: POST /check-gap endpoint (skill gap calculation)
  5. Frontend: Modal/popup showing gap + roadmap suggestions
  6. Frontend: "Track Interest" bookmark button
  7. Backend: POST /track-interest endpoint

- **Resources needed:**
  - Frontend framework/vanilla JS for interactive UI
  - API design for clean request/response flow
  - Clear UX design for gap display

- **Timeline:** Hours 6-12 (second 25% of hackathon)

#### #3 Priority: Demo-Ready Polish with Growth Notification Mockup

- **Rationale:** Judges see dozens of demos. Polish separates winners from participants. The hardcoded notification demonstrates vision without overbuilding.

- **Next steps:**
  1. Frontend: Style everything professionally (clean, modern design)
  2. Frontend: Build "Demo Growth Notification" button
  3. Frontend: Create hardcoded notification banner with realistic data
  4. Backend: Company view with ranked candidates
  5. ALL: Create 3-5 test scenarios covering different alignment profiles
  6. ALL: Practice demo script and timing
  7. ALL: Prepare pitch deck with problem/solution/impact

- **Resources needed:**
  - CSS framework or custom styling
  - Realistic mock data for notification
  - Pitch deck template
  - Team coordination for smooth demo delivery

- **Timeline:** Hours 12-24 (final 50% of hackathon)

## Reflection and Follow-up

### What Worked Well

1. **First Principles Thinking unlocked the core insight** - Starting from fundamental truths revealed that the problem isn't skills matching, but alignment matching. This reframing shaped everything that followed.

2. **Practical constraints drove focus** - The 24-hour hackathon timeline forced ruthless prioritization, separating "must build" from "can fake" clearly.

3. **Ethical stance emerged naturally** - The principle of "only guide toward authentic passion" wasn't forced - it emerged from understanding the problem deeply.

4. **Team structure maps perfectly to execution plan** - 2 frontend, 1 backend, 1 ML matches the workload distribution naturally.

### Areas for Further Exploration

1. **Scoring algorithm refinement** - What exact weights? How to measure "domain alignment" vs "values alignment"?

2. **Resume parsing accuracy** - Which NLP library works best? How to handle non-standard resume formats?

3. **Company data collection** - Most efficient way to scrape/structure company mission/values data?

4. **Gap bridge recommendations** - How specific should learning roadmaps be? Link to actual courses?

5. **Demo scenarios** - Which 3-5 candidate profiles best demonstrate the system's range?

6. **Pitch narrative** - How to tell the story in 3 minutes? Start with problem or solution?

### Recommended Follow-up Techniques

1. **Mind Mapping** - Visualize the complete system architecture and data flows
2. **Six Thinking Hats** - Evaluate the scoring algorithm from multiple perspectives (facts, risks, benefits)
3. **Question Storming** - Generate all possible judge questions to prepare responses
4. **SCAMPER on scoring algorithm** - Systematically refine the alignment calculation approach

### Questions That Emerged

1. How do we handle candidates with no clear domain focus (generalists)?
2. What if a company's stated values don't match their actual culture?
3. Should we weight recent projects/experience more than older ones?
4. How do we prevent gaming the system (keyword stuffing resumes)?
5. What's the minimum viable seed data to make alignment scores feel accurate?
6. Should we show alignment reasoning to candidates (transparency vs complexity)?
7. How do we handle edge cases (career changers, students, international candidates)?

### Next Session Planning

- **Suggested topics:**
  - PRD creation (move to Phase 2 - Planning with PM agent)
  - Technical architecture deep-dive
  - API contract definition
  - Database schema finalization
  - Pitch deck creation session

- **Recommended timeframe:** Within next 24-48 hours (before hackathon starts)

- **Preparation needed:**
  - Gather sample resumes for testing
  - Research company data sources
  - Set up development environment
  - Create shared repo and project board
  - Align team on tech stack specifics

---

_Session facilitated using the BMAD CIS brainstorming framework_
