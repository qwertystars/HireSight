# Product Brief: HireSight

**Date:** 2025-10-24
**Author:** Srijan
**Status:** Draft for PM Review

---

## Executive Summary

**Product Concept:**
HireSight is an alignment-first hiring platform that matches mission-driven tech professionals with companies based on values and passion, not just skills. We reframe hiring from "can you do this job?" to "should you do this at THIS company?" - solving the root cause of turnover (misalignment) rather than symptoms (resume gaps).

**The Problem:**
70% of employees are disengaged at work, costing companies $1 trillion annually in misalignment-driven turnover. Traditional platforms (LinkedIn, Indeed) optimize for skills keyword matching, missing the critical question of whether candidates genuinely care about a company's mission. Professionals accept jobs at organizations whose values they don't share, leading to burnout and departure within 18-24 months.

**Our Solution:**
HireSight analyzes resumes and company missions to calculate 0-100% alignment scores based on domain/values matching. Candidates see companies ranked by alignment percentage and receive conditional growth roadmaps: "You align with Company X at 65% - here's what to learn to reach 85%." Companies see candidates ranked by passion signals ("2 years exploring climate tech") rather than resume keywords. Our unique moat: journey tracking over time, detecting when candidates demonstrate commitment by growing toward alignment and auto-notifying companies.

**Target Market:**
- **Primary:** Mission-driven tech professionals (ages 22-35) seeking purpose-driven careers
- **Secondary:** Climate/EdTech/HealthTech startups (10-500 employees) struggling with culture-fit hiring and 30-40% first-year turnover

**Business Model:**
Freemium - candidates free forever (network effects), companies pay $199-$499/month. Value prop: reducing 2 mis-hires/year saves $150K-400K in turnover costs, delivering 50-200x ROI on subscription.

**Hackathon MVP Scope (24 hours):**
Build core alignment matching engine with 20 pre-seeded companies, skill gap analysis, and bookmark tracking. Demo journey tracking concept with hardcoded notification (prove vision without overbuilding). Success criteria: working .db file, sub-second API responses, "wow moment" for judges.

**Post-MVP Vision:**
Phase 2 (3-6 months): Deploy full journey tracking with automated growth notifications. Long-term: Transform from matching platform to "career GPS" - lifelong alignment companion helping 1M+ people find work they love. Expansion opportunities: enterprise tier, recruiter partnerships, learning platform integrations, data licensing.

**Key Differentiators:**
1. **Alignment > Skills** - First-principles reframe of hiring problem
2. **Journey Tracking** - Commitment signals over time (defensible moat)
3. **Ethical Stance** - Only guide toward authentic passion, never nudge toward misalignment
4. **Growth Guidance** - Conditional roadmaps for aligned roles, not generic job spam

**Strategic Impact:**
Entering $200B global recruitment market with category-defining innovation. Projected $500K ARR at 12 months (200 paying companies). Break-even month 8-10. If successful, potential to reduce global employee burnout and transform hiring from transactional matching to values-driven career development.

---

## Problem Statement

### The Core Problem: Misalignment, Not Skills Gaps

Traditional hiring platforms focus on the wrong question: "Can you do this job?" instead of "Should you do this job at this company?" This fundamental misalignment leads to:

**For Candidates:**
- Good professionals accepting positions at companies whose missions they don't care about
- Working for a paycheck rather than passion, leading to burnout and disengagement
- Eventual departure once they realize the misalignment (avg. 18-24 months)
- Limited visibility into which companies truly align with their values and interests
- No clear path to bridge gaps toward roles they genuinely care about

**For Companies:**
- High turnover costs (estimated 50-200% of annual salary per departure)
- Hiring skilled candidates who lack genuine passion for the company's mission
- Inability to identify candidates who demonstrate authentic commitment signals
- Missing candidates who would be passionate fits but need minor skill development
- Resume keyword-matching that optimizes for skills over cultural/mission alignment

**Quantifiable Impact:**
- 70% of employees report feeling disengaged at work (Gallup)
- Misalignment-driven turnover costs US companies $1 trillion annually
- Average time-to-realize-misfit: 6-12 months, leading to lost productivity and recruitment restart

**Why Existing Solutions Fall Short:**
- LinkedIn/Indeed: Pure keyword matching, no values/mission alignment scoring
- Culture-fit assessments: Manual, post-interview, not integrated into discovery
- Traditional recruiters: Focus on filling roles quickly, not long-term alignment
- Job boards: No proactive guidance on how candidates can grow toward aligned opportunities

**Urgency:**
With remote work normalizing, candidates have global options. Companies that can't demonstrate values alignment and provide clear growth paths will lose top talent to mission-driven competitors. The shift from "job for life" to "mission for now" requires new matching paradigms.

---

## Proposed Solution

### HireSight: Alignment Matcher + Growth Compass

HireSight reframes hiring from "skills matching" to "alignment matching + growth guidance." We analyze resumes, GitHub profiles, and company missions to calculate values/passion alignment scores and provide conditional growth paths.

**Core Value Proposition:**
Not just "here's a match" but "here's your path to alignment" - showing candidates which companies align NOW and what to explore/learn to align with aspirational companies LATER.

**How It Works:**

**For Candidates:**
1. Upload resume (familiar format, reinterpreted through values lens)
2. See companies ranked by alignment percentage (90-100%: strong fit, 60-89%: partial fit with growth path, <60%: not recommended)
3. For any company, click "Check Skill Gap" to see:
   - Current skills vs required skills
   - Learning roadmap to close gaps
4. "Track Interest" in companies to bookmark growth journey
5. **Future:** Return later, re-upload resume → system detects growth and notifies companies of commitment signals

**For Companies:**
1. Upload job descriptions (traditional format)
2. Upload candidate resumes (batch processing)
3. See candidates ranked by alignment score with reasoning:
   - "Sarah has been exploring climate solutions for 2 years" > "John has React skills"
   - Shows passion signals from project history, not just keyword matches
4. **Future:** Receive notifications when tracked candidates grow toward alignment ("Candidate improved alignment from 60% → 85% over 3 months")

**Key Differentiators:**

| Traditional Platforms | HireSight |
|----------------------|-----------|
| Skills keyword matching | Domain/values alignment scoring |
| "Can you do this job?" | "Should you do this at THIS company?" |
| Static resume snapshot | Journey tracking & commitment signals |
| Push any job for revenue | Ethical: Only guide toward authentic passion |
| No growth guidance | Conditional roadmaps for aligned roles only |

**The Unique Moat - Journey Tracking Over Time:**
When candidates return after pursuing growth (learning new skills, building projects in aligned domains), HireSight detects progress and auto-notifies companies. This reveals **commitment** - the ultimate hiring signal that resumes can't capture.

**Why This Will Succeed:**
1. **Candidate Pull:** Professionals want meaningful work, not just employment
2. **Company Pull:** Reducing turnover by 20% saves millions; passionate employees outperform by 2-3x
3. **Ethical Moat:** Refusing to nudge candidates toward misaligned work (even for money) builds trust and differentiation
4. **First Principles Alignment:** Solves the actual problem (misalignment) rather than symptoms (resume gaps)

---

## Target Users

### Primary User Segment

**Mission-Driven Tech Professionals (Candidates)**

**Demographics:**
- Age: 22-35 years old
- Experience: Early-career to mid-level (0-7 years)
- Education: Bachelor's degree or higher, technical backgrounds (CS, Engineering, Data Science)
- Location: Global, with concentration in tech hubs (SF, NYC, Berlin, Bangalore, Remote-first)

**Current Behavior:**
- Actively browse job boards (LinkedIn, Indeed, AngelList) but feel overwhelmed by irrelevant matches
- Spend 3-5 hours/week researching companies manually to understand missions and values
- Read company "About Us" and "Careers" pages trying to gauge cultural fit
- Ask for informational interviews to understand if they'd actually care about the work
- Frequently change jobs (avg. tenure 2-3 years) searching for meaningful alignment

**Specific Pain Points:**
- "I can't tell from job descriptions if I'll actually care about this company's mission"
- "I have the skills but don't know which climate/social-impact companies are hiring"
- "I want to work in EdTech but lack domain experience - how do I break in?"
- "LinkedIn shows me 1000 jobs but none feel like the RIGHT fit for who I am"

**Goals:**
- Find roles at companies whose missions they genuinely care about
- Understand which skills to develop to access aspirational companies
- Avoid accepting offers they'll regret in 12 months
- Build careers around passion, not just compensation

**Motivation Drivers:**
- Purpose over paycheck (willing to accept 10-20% pay cut for mission alignment)
- Long-term career satisfaction and reduced burnout
- Desire to make tangible impact in domains they care about (climate, education, healthcare, etc.)

### Secondary User Segment

**Mission-Driven Companies & Startups (Employers)**

**Firmographics:**
- Company size: 10-500 employees (startups to growth-stage)
- Sectors: Climate tech, EdTech, HealthTech, Social Impact, Ethical AI, Sustainable businesses
- Stage: Seed to Series B
- Hiring frequency: 2-10 roles/quarter

**Current Behavior:**
- Post on LinkedIn/AngelList and get 200+ applications, 80% unaligned
- Spend 15-20 hours/week screening resumes manually
- Conduct phone screens to "feel out" cultural fit (inefficient)
- Lose great candidates who don't realize they'd be passionate about the mission
- Experience 30-40% first-year turnover from culture/mission mismatch

**Specific Pain Points:**
- "We hire skilled developers who don't care about our climate mission - they leave in 18 months"
- "Can't identify which candidates are genuinely passionate vs. just job hunting"
- "Miss candidates who'd be perfect fits but need 3-6 months of skill development"
- "Resume screening is a black hole - no signal for values/mission alignment"

**Goals:**
- Hire candidates who are genuinely passionate about the company's mission
- Reduce turnover by improving mission/culture fit
- Identify candidates who demonstrate commitment signals (not just credentials)
- Build teams of people who stay long-term and evangelize the mission

**Motivation Drivers:**
- Retention: Reducing turnover from 35% → 15% saves $500K-2M annually
- Performance: Passionate employees deliver 2-3x output vs. disengaged hires
- Culture: Maintaining strong mission-driven culture as they scale
- Speed: Faster time-to-hire with pre-qualified aligned candidates

---

## Goals and Success Metrics

### Business Objectives

**Hackathon MVP Goals (24 hours):**
1. **Demo Readiness:** Fully functional alignment matching engine with 20 pre-seeded companies
2. **Judge Impact:** "Wow moment" delivered through demo of growth notification concept
3. **Technical Proof:** Working .db file demonstrating data persistence and backend functionality
4. **Pitch Clarity:** Judges understand the problem, solution, and unique moat within 3-minute pitch

**Post-Hackathon Goals (0-6 months):**
1. **Candidate Acquisition:** Onboard 500 mission-driven tech professionals to platform
2. **Company Acquisition:** Partner with 50 mission-driven startups across climate/social-impact sectors
3. **Match Quality:** Achieve 75%+ alignment accuracy (validated through user feedback surveys)
4. **Revenue Model Validation:** Test freemium model (free for candidates, $199/month for companies)

**Long-term Goals (12-24 months):**
1. **Market Position:** Become the go-to platform for mission-driven tech hiring
2. **Journey Tracking Launch:** Deploy full commitment-tracking system with growth notifications
3. **Network Effects:** Reach critical mass where candidates come for company data, companies come for candidate pool
4. **Revenue Target:** $500K ARR with 250 paying companies

### User Success Metrics

**Candidate Success Metrics:**
1. **Discovery Efficiency:** Time to find 5 aligned companies < 10 minutes (vs 5+ hours manually)
2. **Match Relevance:** 80%+ of candidates rate top-3 recommended companies as "would consider applying"
3. **Growth Clarity:** 70%+ of users with gap analysis report "clear understanding of next learning steps"
4. **Return Rate:** 40%+ of candidates return within 3 months to update profiles/check new matches
5. **Application Conversion:** 50%+ of candidates apply to at least 1 aligned company within 2 weeks

**Company Success Metrics:**
1. **Screening Efficiency:** Reduce resume review time from 15 hours/week to 3 hours/week
2. **Match Quality:** 60%+ of top-10 recommended candidates invited to interviews
3. **Hiring Success:** Companies report 80%+ mission-fit satisfaction with HireSight hires at 6-month mark
4. **Retention Impact:** Track 20%+ reduction in first-year turnover for mission-aligned hires (12-month lag metric)
5. **Commitment Signals:** 30%+ of hires come from candidates who demonstrated growth journey tracking

### Key Performance Indicators (KPIs)

| KPI | Target (MVP) | Target (6mo) | Target (12mo) | Measurement |
|-----|-------------|--------------|---------------|-------------|
| **Platform Engagement** |
| Active Candidates | 50 (demo) | 500 | 2,500 | Monthly active uploads |
| Active Companies | 20 (seeded) | 50 | 200 | Monthly active job posts |
| Avg. Session Duration | N/A | 8 min | 12 min | Time on platform |
| **Match Quality** |
| Alignment Score Accuracy | N/A | 75% | 85% | User validation surveys |
| Application Rate | N/A | 15% | 25% | % candidates who apply |
| Interview Rate | N/A | 60% | 75% | % top-10 matches interviewed |
| **Growth & Retention** |
| Candidate Return Rate | N/A | 40% | 60% | Return within 90 days |
| Company Retention | N/A | 80% | 90% | Monthly subscription renewal |
| Journey Tracking Adoption | 0% (demo only) | 25% | 50% | % candidates who bookmark |
| **Revenue (Post-MVP)** |
| MRR | $0 | $10K | $50K | Monthly recurring revenue |
| CAC | N/A | <$50 | <$30 | Customer acquisition cost |
| LTV:CAC Ratio | N/A | 3:1 | 5:1 | Lifetime value ratio |

---

## Strategic Alignment and Financial Impact

### Financial Impact

**Development Investment (Hackathon MVP):**
- **Time Investment:** 24 hours × 4 team members = 96 person-hours
- **Cost:** $0 (hackathon project, no external costs)
- **Resources:** Laptops, GitHub, free-tier APIs (OpenAI/Claude for NLP), SQLite

**Post-Hackathon Investment (0-6 months):**
- **Development:** $40K-60K (2 engineers @ 3 months, part-time/contract)
- **Infrastructure:** $500-1K/month (hosting, APIs, database scaling)
- **Marketing/Sales:** $5K-10K (content, ads, partnerships with mission-driven communities)
- **Total Initial Investment:** ~$50K-75K

**Revenue Potential:**

**Freemium Model:**
- **Candidates:** Free forever (network effects, data generation)
- **Companies:** $199/month base tier, $499/month growth tier (journey tracking access)

**6-Month Revenue Projection:**
- 50 paying companies × $199/month × 50% avg. retention × 4 months avg. = $20K
- Potential range: $10K-30K depending on acquisition velocity

**12-Month Revenue Projection:**
- 200 paying companies × $299/month avg. (mix of tiers) × 80% retention = $500K ARR
- Break-even: Month 8-10

**Cost Savings for Customers:**
- **Per-company annual value:** Reducing 2 mis-hires/year saves $150K-400K in turnover costs
- **ROI for companies:** 50-200x on $2,400 annual subscription
- **Strong value prop justifies pricing and enables upsells**

**Long-term Revenue Opportunities:**
- Enterprise tier: $2K-5K/month for large companies (500+ employees)
- API access for recruiters/HR platforms: $1K-3K/month
- Learning platform partnerships (course commissions): 10-15% of referrals
- Data licensing (anonymized alignment insights): $50K-200K/year for EdTech/HR analytics companies

### Company Objectives Alignment

**[NEEDS CONFIRMATION - Assuming hackathon/personal project context]**

**If Hackathon Project:**
- **Goal:** Win hackathon, demonstrate technical + product thinking
- **Alignment:** Solves real-world problem with measurable impact, strong differentiation
- **Outcome:** Portfolio piece, potential startup foundation, team-building experience

**If Startup/Commercial Project:**
- **Mission:** Build ethical hiring tools that improve career satisfaction and reduce turnover
- **Vision:** Transform hiring from transactional matching to values-driven career development
- **Strategic Fit:** Addresses $200B+ global recruitment market with first-principles innovation

**If Within Existing Company:**
- **HR Tech Innovation:** Modernize internal hiring with alignment-first approach
- **Talent Retention:** Reduce turnover costs and improve employee satisfaction
- **Competitive Advantage:** Attract mission-driven talent in tight labor market

### Strategic Initiatives

**Phase 1: Validate (Hackathon + 0-3 months)**
1. **Win Hackathon:** Prove concept viability and generate initial traction
2. **User Interviews:** Conduct 20-30 interviews with mission-driven candidates and companies
3. **MVP Refinement:** Iterate on alignment scoring algorithm based on feedback
4. **Early Adopters:** Recruit 10 beta companies and 100 beta candidates

**Phase 2: Build (3-6 months)**
1. **Product Enhancement:** Polish UX, add real authentication, improve matching accuracy
2. **Content Strategy:** Build SEO presence around "mission-driven jobs" and "values-aligned careers"
3. **Community Building:** Engage with climate-tech, social-impact, EdTech communities
4. **Metrics Validation:** Prove 20%+ turnover reduction hypothesis with early customers

**Phase 3: Scale (6-12 months)**
1. **Journey Tracking Launch:** Deploy full commitment-tracking system (the unique moat)
2. **Enterprise Tier:** Add advanced features for larger companies (ATS integration, team analytics)
3. **Geographic Expansion:** Expand beyond US to EU and Asia tech hubs
4. **Fundraising (Optional):** If scaling beyond bootstrapped growth, raise $500K-1M seed round

**Phase 4: Dominate (12-24 months)**
1. **Category Leadership:** Own "mission-driven tech hiring" category
2. **Network Effects:** Reach critical mass where platform becomes industry standard
3. **Platform Expansion:** Add learning integrations, mentorship matching, career pathing tools
4. **Strategic Partnerships:** Integrate with LinkedIn, GitHub, job boards as "alignment layer"

---

## MVP Scope

### Core Features (Must Have)

**TIER 1: Core Matching Engine (Hours 0-12) - Critical for Demo**

1. **Database Schema & Seeding**
   - Companies table: name, mission, values, required_skills, domain
   - Candidates table: name, resume_text, extracted_skills, interests, domains
   - Interests table: candidate_id, company_id, timestamp (bookmark tracking)
   - **20 pre-seeded real companies** across Climate, EdTech, FinTech, Healthcare, Social Impact

2. **Resume Upload & Parsing**
   - POST /upload-resume endpoint
   - NLP extraction: skills, domain keywords, values signals
   - Store parsed data in candidates table
   - Return candidate_id for frontend

3. **Alignment Scoring Algorithm**
   - Weighted calculation: 60% domain/mission match + 40% values alignment
   - Compare candidate domains/interests with company mission/values
   - Generate 0-100% alignment score for each company
   - Skill gap calculation: required_skills - candidate_skills

4. **Company List API**
   - GET /companies?candidate_id=X
   - Return all companies sorted by alignment score
   - Include: company_name, alignment_percentage, brief_reason
   - Response time: <500ms

5. **Skill Gap Analysis**
   - POST /check-gap with candidate_id + company_id
   - Calculate skill difference
   - Return: missing_skills, recommended_learning_path
   - Display in modal/popup on frontend

6. **Track Interest Bookmark**
   - POST /track-interest with candidate_id + company_id
   - Store in interests table with timestamp
   - Return success confirmation
   - Frontend shows "Tracking" badge

**TIER 2: User Interface (Hours 12-20) - Demo Polish**

7. **Candidate Frontend**
   - Resume upload page with drag-and-drop
   - Company list display with alignment percentages (visual progress bars)
   - "Check Skill Gap" button per company → modal with gap analysis
   - "Track Interest" bookmark button per company
   - Clean, professional styling (no authentication UI)

8. **Company Dashboard (Reverse Match)**
   - View candidates ranked by alignment score
   - Show "why this candidate aligns" reasoning
   - Display passion signals: "2 years exploring climate tech" vs "has React"
   - Filter/sort by alignment threshold

**TIER 3: Demo Magic (Hours 20-24) - The Wow Factor**

9. **Growth Notification Demo Button**
   - Hardcoded "Demo Growth Tracking" button on company dashboard
   - Clicking shows pre-written notification banner:
     - "Candidate [Name] tracked interest 3 months ago"
     - "Progress: Alignment 65% → 82%"
     - "New skills: Python, ML fundamentals"
     - "New projects: Climate dashboard project"
   - Demonstrates vision without building full tracking backend

10. **Demo Scenarios & Data**
    - 5-7 test candidate profiles with varied alignment patterns
    - 3 demo flows: perfect match, partial match with gap, no alignment
    - Visible .db file for judges to inspect

### Out of Scope for MVP

**Explicitly NOT Building for Hackathon:**

1. ❌ **Real Authentication System**
   - No user accounts, passwords, login flows
   - Demo uses single-session state only
   - Post-MVP: Auth0 or Firebase Auth

2. ❌ **Full Journey Tracking Backend**
   - No actual re-upload detection logic
   - No historical comparison engine
   - No automated notifications
   - Post-MVP: Build tracking service with database history

3. ❌ **Real-time GitHub Integration**
   - No live repo analysis or commit tracking
   - Mention in pitch as "future capability"
   - Post-MVP: GitHub API integration, project classification

4. ❌ **Email/Push Notifications**
   - No email service setup
   - No notification queue system
   - Post-MVP: SendGrid/Twilio integration

5. ❌ **Payment/Subscription System**
   - No Stripe integration
   - No billing logic
   - Post-MVP: Freemium model with payment gateway

6. ❌ **Advanced NLP Features**
   - No sentiment analysis or deep resume understanding
   - Basic keyword extraction only
   - Post-MVP: Fine-tuned models for better accuracy

7. ❌ **Mobile App**
   - Web-only for demo
   - Responsive design sufficient
   - Post-MVP: React Native or PWA

8. ❌ **ATS Integration**
   - No Greenhouse/Lever/Workday connections
   - Post-MVP: API partnerships

9. ❌ **Learning Resource Recommendations**
   - Skill gap shows gaps but not specific courses/links
   - Post-MVP: Partner with Coursera, Udemy, etc.

10. ❌ **Multi-language Support**
    - English only for hackathon
    - Post-MVP: i18n for global markets

### MVP Success Criteria

**Technical Success (Must All Pass):**
- ✅ Resume upload processes and stores data in .db file
- ✅ Alignment scoring algorithm returns scores 0-100% for all companies
- ✅ Skill gap analysis identifies missing skills accurately
- ✅ Company dashboard ranks candidates by alignment
- ✅ All APIs respond in <1 second with test data
- ✅ .db file is visible and queryable by judges
- ✅ Zero crashes or errors during 5-minute demo

**Demo Success (Judge Evaluation):**
- ✅ Problem clearly explained in <60 seconds
- ✅ "Wow moment" achieved during growth notification demo
- ✅ 3 different candidate scenarios demonstrated successfully
- ✅ Judges understand the unique moat (commitment tracking over time)
- ✅ Technical questions answered confidently (how scoring works, data model)

**User Experience Success:**
- ✅ Upload → Results in <10 seconds (perceived speed)
- ✅ Alignment scores feel intuitive and reasonable
- ✅ Skill gap recommendations are specific and actionable
- ✅ UI is polished enough to be "real product" believable
- ✅ Demo flows smoothly without manual intervention/resets

**Strategic Success (Pitch Impact):**
- ✅ Judges understand "alignment > skills" first principle
- ✅ Ethical stance resonates (anti-nudging misalignment)
- ✅ Future vision is credible and exciting
- ✅ Market opportunity is clear ($200B recruitment market)
- ✅ Team demonstrates both technical and product thinking

---

## Post-MVP Vision

### Phase 2 Features

**Full Journey Tracking System (3-6 months post-MVP):**
1. **Profile History Engine**
   - Store resume/profile snapshots at each upload
   - Automatic comparison: skills gained, projects added, domain depth
   - Visual timeline showing candidate growth journey

2. **Automated Growth Notifications**
   - Real-time alerts to companies when tracked candidates improve alignment
   - Email/dashboard notifications: "Candidate X improved from 65% → 85% alignment"
   - Include evidence: new skills, relevant projects, commitment duration

3. **Commitment Scoring**
   - Weight candidates by demonstration of sustained interest over time
   - Algorithm: Time tracking (months) × Alignment improvement (%) × Project relevance
   - Surface "high-commitment" candidates to top of company dashboards

4. **GitHub Auto-Sync**
   - OAuth connection to GitHub accounts
   - Automatic project classification by domain (climate, education, health, etc.)
   - Contribution analysis: commit frequency, project complexity, collaboration signals

5. **Learning Roadmap Enhancements**
   - Link skill gaps to specific courses (Coursera, Udemy, freeCodeCamp)
   - Track completion of recommended resources
   - Show progress toward alignment milestones

6. **Multi-dimensional Alignment**
   - Beyond mission: work style, team culture, company stage preferences
   - Add culture-fit questions for candidates (async/sync, startup/corporate, etc.)
   - Refine matching with personality/work-style compatibility

**Enhanced Company Features:**
7. **Rich Company Profiles**
   - Beyond job descriptions: impact stories, team values, day-in-the-life content
   - Video content from team members explaining mission
   - Metrics dashboard: employee retention, diversity stats, growth trajectory

8. **ATS Integration**
   - Two-way sync with Greenhouse, Lever, Workday
   - Push HireSight candidates directly to interview pipelines
   - Track which HireSight candidates get hired + retention data

9. **Team Analytics Dashboard**
   - Aggregate hiring metrics: avg. time-to-hire, alignment score → retention correlation
   - ROI tracking: turnover reduction savings vs subscription cost
   - Candidate funnel analysis: alignment thresholds → application → hire rates

### Long-term Vision

**Years 1-2: HireSight as Career GPS**

Transform from "matching platform" to "lifelong career alignment companion":

1. **Career Pathing Intelligence**
   - Not just "here's a job" but "here's your 5-year mission-aligned career trajectory"
   - Show progression paths: Junior Dev at Climate Startup → Lead Eng at Series B → CTO at Impact Unicorn
   - Model successful career transitions in database (anonymized patterns)

2. **Reverse the Power Dynamic**
   - Companies compete for mission-aligned candidates, not the other way around
   - Candidates set alignment standards, companies adjust missions/communication to attract talent
   - Platform becomes "candidate-first marketplace" (like how Airbnb empowered hosts)

3. **End Resume Fraud**
   - GitHub/project history as authentic proof of skills and interests
   - Automated verification: claimed skills → actual projects evidence
   - Reputation system: track long-term alignment accuracy (did they stay 2+ years?)

4. **Kill the Cover Letter**
   - Alignment scores replace persuasive writing
   - Objective signals (project history, commitment tracking) > subjective narratives
   - Democratize access: underrepresented candidates compete on passion, not polish

5. **Ethical Hiring Marketplace**
   - Companies differentiate on mission/values/impact, not just compensation
   - Transparent culture data: retention rates, promotion velocity, work-life balance metrics
   - Candidates choose employers based on alignment, creating market pressure for ethical practices

6. **Passion-First Economy**
   - Help 1M+ people find work they love, measurably reducing burnout
   - Track global impact: aggregate career satisfaction, turnover reduction, mission-fulfillment scores
   - Partnerships with mental health orgs to study impact of mission-aligned work

### Expansion Opportunities

**Adjacent Markets & Revenue Streams:**

1. **Enterprise Tier (Large Companies)**
   - Target: 500-10,000 employee companies (Google, Microsoft, etc.)
   - Features: Bulk hiring, internal mobility matching, retention prediction
   - Pricing: $2K-10K/month based on company size

2. **Recruiter/Agency Partnerships**
   - API access for third-party recruiters to leverage alignment data
   - White-label solution for boutique agencies specializing in mission-driven placements
   - Revenue share: 10-15% of placement fees

3. **Geographic Expansion**
   - Phase 1: US + Canada (English-only)
   - Phase 2: EU (multi-language support)
   - Phase 3: Asia-Pacific (India, Singapore, Australia)
   - Localization: cultural adaptation of alignment frameworks

4. **Non-Tech Verticals**
   - Start with tech (easier data, clearer signals)
   - Expand to: Healthcare professionals, educators, nonprofit sector, creative industries
   - Adapt scoring algorithms for domain-specific signals

5. **Learning Platform Partnerships**
   - Commission model: 10-20% of course sales from skill-gap recommendations
   - Co-create "Mission-to-Career" bootcamps with aligned domains
   - Certification tracking: candidates complete recommended learning → auto-update profiles

6. **Data Licensing**
   - Anonymized insights on alignment trends, skill demands, career transitions
   - Sell to: EdTech companies (curriculum planning), HR analytics platforms, workforce research orgs
   - Estimated value: $50K-500K/year depending on dataset scope

7. **B2B2C Through Universities**
   - Partner with university career centers
   - Help graduates find mission-aligned first jobs (reduce post-grad existential crisis)
   - Institutional pricing: $10K-50K/year per university

8. **Mentorship Matching**
   - Connect candidates pursuing growth paths with mentors in aligned companies
   - Paid tier for companies: access to "future aligned talent" early
   - Community revenue: $29/month for premium mentorship access

9. **Impact Measurement Tools**
   - Help companies track and communicate their social/environmental impact
   - Bundle with recruitment: "Hire aligned talent AND prove your impact"
   - Separate product line: $500-2K/month for impact dashboard

10. **Acquisition Targets**
    - Natural acquirers: LinkedIn (alignment layer), Indeed (modernization), ATS platforms (differentiation)
    - Strategic value: $50M-500M depending on traction and network effects
    - Alternative: Stay independent, become category-defining platform

---

## Technical Considerations

### Platform Requirements

**Hackathon MVP Platform:**
- **Primary Platform:** Web application (desktop + mobile responsive)
- **Browser Support:** Chrome, Firefox, Safari (latest versions only)
- **Deployment:** Local demo (no cloud hosting for hackathon)
- **Database:** SQLite (.db file, visible for judges)
- **Performance:** Sub-second API responses for demo data (20 companies, 10 test candidates)

**Post-MVP Platform:**
- **Platform Evolution:** Progressive Web App (PWA) for mobile-friendly experience
- **Browser Support:** All modern browsers + IE11 fallback (if enterprise customers require)
- **Mobile:** Responsive web first, native app consideration at 10K+ users
- **Accessibility:** WCAG 2.1 AA compliance (screen readers, keyboard navigation, color contrast)
- **Performance Requirements:**
  - API response time: <200ms for 95th percentile
  - Page load time: <2 seconds on 4G connection
  - Database queries: <50ms for alignment calculations
  - Support 1,000+ concurrent users

**Infrastructure Scaling:**
- **0-500 users:** Single server, SQLite → PostgreSQL migration
- **500-5,000 users:** Load balancer, separate API/DB servers, Redis caching
- **5,000+ users:** Microservices architecture, CDN for static assets, read replicas for DB

### Technology Preferences

**Hackathon MVP Stack (Confirmed):**

**Frontend:**
- **Framework:** Vanilla HTML/CSS/JavaScript (no framework overhead for 24-hour build)
- **Styling:** Custom CSS or lightweight Tailwind CDN for rapid prototyping
- **State Management:** Simple localStorage for session persistence
- **Rationale:** Maximum velocity, minimal setup time, easy debugging under time pressure

**Backend:**
- **Framework:** Python FastAPI (async support, automatic API docs, fast development)
- **Database:** SQLite with visible .db file (demo requirement)
- **ORM:** SQLAlchemy or raw SQL (keep it simple)
- **Rationale:** Team expertise in Python, FastAPI is lightweight and well-documented

**ML/NLP:**
- **Library:** spaCy or NLTK for resume parsing (keyword extraction, entity recognition)
- **Scoring:** Custom algorithm (weighted calculations, no ML model training needed)
- **APIs:** OpenAI/Claude API for resume summarization (free tier acceptable)
- **Rationale:** Pre-trained models avoid training time, focus on business logic

**Deployment:**
- **Hackathon:** Local Flask/FastAPI server (localhost demo)
- **Version Control:** GitHub (visible commit history shows work)
- **Demo Environment:** Run on presentation laptop with pre-loaded data

**Post-MVP Technology Evolution:**

**Frontend (Production):**
- **Framework:** React or Vue.js for richer interactivity
- **State Management:** Redux/Vuex or React Context
- **Build Tools:** Vite or Webpack
- **Design System:** Tailwind + custom component library
- **Testing:** Jest + React Testing Library

**Backend (Production):**
- **Keep:** FastAPI (proven during MVP)
- **Database:** PostgreSQL (production-grade, JSONB for flexible schemas)
- **Caching:** Redis for session management and frequent queries
- **Queue:** Celery for async tasks (resume parsing, notifications)
- **Testing:** pytest + coverage reporting

**Infrastructure (Production):**
- **Hosting:** AWS or GCP (t3.medium instances to start)
- **CDN:** CloudFlare for static assets and DDoS protection
- **Monitoring:** Sentry (error tracking), Mixpanel (user analytics), DataDog (infrastructure)
- **CI/CD:** GitHub Actions for automated testing and deployment
- **Backup:** Automated daily DB backups to S3

**Security Considerations:**
- **Authentication:** Auth0 or Firebase Auth (OAuth, SSO for enterprise)
- **API Security:** Rate limiting, JWT tokens, CORS policies
- **Data Privacy:** GDPR compliance, encrypted data at rest (sensitive resume data)
- **PII Handling:** Anonymization for analytics, user data deletion on request

### Architecture Considerations

**Hackathon MVP Architecture (Monolithic):**

```
┌─────────────────────────────────────────────────┐
│              Frontend (HTML/CSS/JS)             │
│  - Upload UI                                    │
│  - Company List Display                         │
│  - Gap Analysis Modal                           │
└────────────────┬────────────────────────────────┘
                 │ HTTP REST
┌────────────────▼────────────────────────────────┐
│           Backend (FastAPI)                     │
│  - /upload-resume (parse, store)                │
│  - /companies (calculate alignment)             │
│  - /check-gap (skill analysis)                  │
│  - /track-interest (bookmark)                   │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────┐
│          SQLite Database (.db)                  │
│  - Companies (seeded with 20 real orgs)         │
│  - Candidates (uploaded resumes)                │
│  - Interests (bookmarks)                        │
└─────────────────────────────────────────────────┘
```

**Alignment Scoring Algorithm (Core Logic):**
```python
def calculate_alignment(candidate, company):
    # Domain matching (60% weight)
    domain_score = cosine_similarity(
        candidate.domains,
        company.mission_keywords
    )

    # Values matching (40% weight)
    values_score = keyword_overlap(
        candidate.interests,
        company.values
    )

    # Weighted final score
    alignment = (domain_score * 0.6) + (values_score * 0.4)
    return round(alignment * 100)  # 0-100%

def calculate_skill_gap(candidate, company):
    required = set(company.required_skills)
    has = set(candidate.skills)
    gap = required - has
    return list(gap)
```

**Post-MVP Architecture (Microservices - Future):**

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Frontend   │    │  Mobile App  │    │  API Gateway │
│   (React)    │───▶│   (Future)   │───▶│  (Kong/AWS)  │
└──────────────┘    └──────────────┘    └──────┬───────┘
                                                │
                    ┌───────────────────────────┴───────────────┐
                    │                                           │
         ┌──────────▼──────────┐                  ┌────────────▼──────────┐
         │  Matching Service   │                  │  Profile Service      │
         │  - Alignment calc   │                  │  - Resume parsing     │
         │  - Company ranking  │                  │  - Data storage       │
         └──────────┬──────────┘                  └────────────┬──────────┘
                    │                                           │
         ┌──────────▼──────────┐                  ┌────────────▼──────────┐
         │  Tracking Service   │                  │  Notification Service │
         │  - Journey history  │                  │  - Email/push alerts  │
         │  - Growth detection │                  │  - Company updates    │
         └─────────────────────┘                  └───────────────────────┘
                    │
         ┌──────────▼──────────────────────────────────┐
         │          PostgreSQL + Redis                 │
         │  - Candidates, Companies, Tracking History  │
         └─────────────────────────────────────────────┘
```

**Key Architectural Decisions:**

1. **Monolith → Microservices:** Start simple, split when scaling demands it (5K+ users)
2. **Database Evolution:** SQLite → PostgreSQL at 500 users (before foreign key complexity explodes)
3. **Async Processing:** Resume parsing and alignment calculations move to queue (Celery) when response times degrade
4. **Caching Strategy:** Redis for frequently accessed data (company list, candidate profiles)
5. **API Versioning:** /v1/ endpoints from day 1 to allow backward-compatible iterations

**Integration Points (Post-MVP):**
- **GitHub API:** OAuth for repo access, GraphQL for project analysis
- **Learning Platforms:** Coursera/Udemy APIs for course recommendations
- **ATS Systems:** Webhooks + REST APIs for candidate syncing
- **Email Service:** SendGrid or AWS SES for transactional emails
- **Analytics:** Segment for event tracking, feeds to Mixpanel/Amplitude

**Data Model (Core Entities):**
- **Candidates:** id, resume_text, parsed_skills[], domains[], interests[], github_url
- **Companies:** id, name, mission, values[], required_skills[], domain, industry
- **Interests:** candidate_id, company_id, timestamp, alignment_snapshot
- **Tracking:** candidate_id, profile_snapshots[], growth_events[], notifications_sent[]

---

## Constraints and Assumptions

### Constraints

**Hackathon Constraints:**
1. **Time:** 24 hours total development time - forces ruthless feature prioritization
2. **Team Size:** 4 people (2 frontend, 1 backend, 1 ML) - no room for scope creep
3. **Budget:** $0 budget - must use free tiers, open-source tools, local hosting
4. **No Authentication:** Security not feasible in 24 hours - demo-only single-user experience
5. **Seed Data Required:** Cold-start problem - must pre-populate 20 companies manually

**Post-MVP Constraints:**
1. **Initial Funding:** Bootstrapped or small angel round ($50K-100K) - limits hiring and marketing spend
2. **Two-Sided Marketplace:** Need both candidates AND companies - chicken-and-egg problem
3. **Data Quality:** Alignment accuracy depends on resume/company data quality - garbage in, garbage out
4. **Regulatory:** GDPR/CCPA compliance required before scaling to EU - legal complexity and cost
5. **Competition:** LinkedIn, Indeed have massive network effects - need clear differentiation to gain traction

**Technical Constraints:**
1. **NLP Accuracy:** Resume parsing won't be perfect - manual review needed for edge cases
2. **Scoring Subjectivity:** "Alignment" is inherently subjective - algorithm refinement requires user feedback
3. **Scaling Costs:** NLP APIs (OpenAI/Claude) expensive at scale - may need self-hosted models post-1K users
4. **GitHub Dependency:** Journey tracking requires GitHub integration - limits to candidates with active repos

**Resource Constraints:**
1. **Engineering:** Limited to 1-2 engineers initially - must prioritize ruthlessly
2. **Sales/Marketing:** No dedicated BD initially - founder-led sales to beta customers
3. **Customer Support:** Manual onboarding for early customers - won't scale beyond 50 companies

### Key Assumptions

**User Behavior Assumptions:**
1. **Candidates care about mission alignment enough to use a new platform** - Need to validate willingness to leave LinkedIn
2. **Companies will pay $200-500/month for better alignment matching** - Assumes turnover reduction ROI is clear
3. **Resumes contain sufficient signal about passions/values** - May need to add questionnaires if not
4. **Candidates will return to update profiles** - Journey tracking depends on re-engagement
5. **Mission-driven companies exist in sufficient numbers** - Targeting climate/EdTech/social-impact companies

**Technical Assumptions:**
1. **NLP can extract domain/values from resumes with 70%+ accuracy** - Off-the-shelf models sufficient
2. **Alignment scoring correlates with actual job satisfaction** - Need longitudinal study to validate
3. **20 seeded companies sufficient for compelling demo** - Enough variety to show differentiation
4. **GitHub projects reliably indicate domain interest** - Climate projects = climate passion
5. **Weighted algorithm (60/40) is reasonable starting point** - Will iterate based on feedback

**Market Assumptions:**
1. **Mission-driven hiring is a growing trend** - Gen Z/Millennials prioritize purpose over pay
2. **Turnover is expensive enough to justify prevention spend** - Companies care about retention ROI
3. **Alignment-first approach is differentiated enough** - LinkedIn won't copy feature quickly
4. **$200B recruitment market has room for niche player** - Can capture 0.1% = $200M opportunity
5. **Hackathon judges value mission-driven solutions** - Aligns with typical hackathon themes

**Business Model Assumptions:**
1. **Freemium works for two-sided marketplace** - Candidates free, companies pay
2. **Companies will adopt without full journey tracking** - MVP value (alignment scores) sufficient initially
3. **Churn will be low (<20%) if product delivers ROI** - Retention key to profitability
4. **Word-of-mouth in mission-driven communities drives growth** - Low CAC assumption
5. **Can reach profitability within 12-18 months** - Break-even at 200 paying companies

**Validation Required:**
- ✅ **Assumption #1 (Candidate demand):** Test with 100 beta users - track engagement and NPS
- ✅ **Assumption #2 (Willingness to pay):** Interview 20 companies - validate pricing and ROI expectations
- ✅ **Assumption #3 (Technical feasibility):** Prototype alignment scoring with 50 real resumes
- ✅ **Assumption #7 (Judge appeal):** Align pitch with hackathon themes and judging criteria

---

## Risks and Open Questions

### Key Risks

**High Priority Risks (Could Kill Project):**

1. **Cold Start Problem (Likelihood: High, Impact: High)**
   - **Risk:** Neither candidates nor companies join without the other side present
   - **Mitigation:** Seed 20 companies for demo, target climate-tech community first (tight-knit, mission-aligned)
   - **Fallback:** Pivot to B2B-only (companies upload candidates, we rank them)

2. **Alignment Scoring Inaccuracy (Likelihood: Medium, Impact: High)**
   - **Risk:** Algorithm produces nonsensical matches, users lose trust immediately
   - **Mitigation:** Manual validation of scoring on 50 test cases before launch
   - **Fallback:** Add "Report inaccurate match" feedback loop, iterate algorithm weekly

3. **LinkedIn Network Effects (Likelihood: High, Impact: Medium)**
   - **Risk:** Users won't leave LinkedIn for a new platform without strong differentiation
   - **Mitigation:** Position as "complement, not replacement" - LinkedIn for network, HireSight for alignment
   - **Fallback:** Build browser extension that adds alignment scores TO LinkedIn profiles

4. **Resume Parsing Failures (Likelihood: Medium, Impact: Medium)**
   - **Risk:** Non-standard resume formats break NLP parsing
   - **Mitigation:** Support manual profile creation as backup, iterate on parsing accuracy
   - **Fallback:** Human-in-the-loop review for failed parses

**Medium Priority Risks:**

5. **Insufficient Company Data (Likelihood: Medium, Impact: Medium)**
   - **Risk:** Can't scrape enough mission/values data to differentiate companies accurately
   - **Mitigation:** Require companies to self-report mission during onboarding
   - **Impact:** Delays scaling but improves data quality

6. **Regulatory Compliance Costs (Likelihood: Low, Impact: High)**
   - **Risk:** GDPR/CCPA compliance expensive, delays EU launch
   - **Mitigation:** US-only initially, budget $10K-20K for legal review before international expansion
   - **Timing:** Not relevant until 1K+ users

7. **Competition Copies Feature (Likelihood: Medium, Impact: Medium)**
   - **Risk:** LinkedIn adds "mission alignment score" feature
   - **Mitigation:** Journey tracking moat takes time to replicate (6-12 months data)
   - **Positioning:** We're specialized, they're generalist

**Low Priority Risks:**

8. **Ethical Concerns About Algorithmic Bias (Likelihood: Low, Impact: Medium)**
   - **Risk:** Alignment algorithm discriminates against certain demographics
   - **Mitigation:** Regular bias audits, transparency about scoring methodology
   - **Monitoring:** Track demographic data (opt-in) to detect disparities

9. **API Cost Explosion (Likelihood: Medium, Impact: Low)**
   - **Risk:** OpenAI/Claude API costs grow faster than revenue
   - **Mitigation:** Switch to self-hosted models (Llama, etc.) at 1K users
   - **Timing:** Not urgent until post-MVP scaling

### Open Questions

**Product Questions:**
1. **How do we handle generalist candidates with no clear domain focus?**
   - Should they see all companies equally? Or prompt them to define interests?
2. **What if a company's stated values don't match actual culture?**
   - Do we add employee reviews/ratings? Partner with Glassdoor?
3. **Should we weight recent experience more than older projects?**
   - Recency might indicate current passion vs past exploration
4. **How specific should learning roadmaps be?**
   - Generic ("Learn Python") vs specific ("Take Harvard CS50, build climate dashboard")
5. **Do we show alignment reasoning to candidates?**
   - Transparency builds trust but adds UI complexity

**Technical Questions:**
6. **Which NLP library performs best for resume parsing?**
   - spaCy vs NLTK vs Hugging Face transformers - need benchmarking
7. **What's the optimal weight ratio for domain vs values?**
   - 60/40 is hypothesis, needs A/B testing
8. **How do we prevent keyword stuffing (gaming the system)?**
   - Cross-reference resume claims with GitHub projects? Manual review?
9. **Should we use cosine similarity or different distance metric for alignment?**
   - Test alternatives: Jaccard, embeddings-based similarity

**Business Questions:**
10. **What pricing tier structure maximizes revenue?**
    - Base ($199), Growth ($499), Enterprise ($2K+) - validate with customer interviews
11. **Should we charge candidates for premium features?**
    - Goes against freemium model but unlocks revenue
12. **Do we build in-house ATS or integrate with existing?**
    - Build = differentiation, Integrate = faster go-to-market
13. **What's the minimum viable seed data for accurate alignment?**
    - 20 companies? 50? 100? Test with judges/users

**Go-to-Market Questions:**
14. **Should we launch at hackathon or wait for post-MVP polish?**
    - Hackathon = visibility, Post-MVP = better first impression
15. **Which vertical to target first?**
    - Climate tech (passionate, tight-knit) vs EdTech (larger market) vs Social Impact (broad)
16. **Do we need investor funding or bootstrap?**
    - Depends on growth goals - $500K ARR achievable bootstrapped?

### Areas Needing Further Research

**User Research (Pre-Launch):**
1. **Candidate Interviews (n=30):**
   - Pain points in current job search beyond "too many irrelevant jobs"
   - Willingness to use platform without existing network effects
   - Perception of alignment scores - do they trust algorithmic matching?
   - Would they pay for premium features? (Career coaching, direct intros)

2. **Company Interviews (n=20):**
   - Current screening process costs (time/money)
   - Evidence that misalignment causes turnover (validate hypothesis)
   - Willingness to pay $200-500/month - what ROI do they expect?
   - What data would prove HireSight candidates have better retention?

**Technical Research:**
3. **NLP Benchmarking:**
   - Test spaCy, NLTK, Hugging Face on 50 real resumes
   - Measure accuracy: skills extraction, domain classification, values inference
   - Determine if OpenAI API needed or open-source models sufficient

4. **Algorithm Validation:**
   - Manual scoring of 100 candidate-company pairs by domain experts
   - Compare algorithm output to human judgment
   - Identify patterns where algorithm fails (edge cases)

**Competitive Research:**
5. **Feature Comparison:**
   - LinkedIn, Indeed, AngelList, Hired - what's missing in their matching?
   - Niche players: Climatebase (climate jobs), Idealist (nonprofit) - how do they differentiate?
   - Identify white space: what do NONE of them do well?

6. **Market Sizing:**
   - How many mission-driven companies exist? (Climate, EdTech, Social Impact, Ethical AI)
   - What's their hiring frequency? (TAM calculation)
   - Interview 5-10 to validate demand

**Business Model Research:**
7. **Pricing Studies:**
   - Van Westendorp analysis: survey 50+ companies on willingness to pay
   - Competitive pricing: what do ATS platforms charge? Recruiting agencies?
   - Value-based pricing: calculate turnover cost savings per hire

8. **Unit Economics:**
   - CAC modeling: what's cost to acquire 1 candidate? 1 company?
   - LTV calculation: avg. subscription length, upsell potential
   - Payback period: how many months to recover CAC?

---

## Appendices

### A. Research Summary

**Source: Brainstorming Session (2025-10-24)**

**Key Findings:**

1. **Core Insight - Alignment Over Skills:**
   - Traditional hiring focuses on "can you do this job?" when the real question is "should you do this at THIS company?"
   - Misalignment causes 70% of turnover, not skill gaps
   - First principles thinking revealed values/passion matching as the fundamental problem

2. **Unique Moat Identified - Journey Tracking:**
   - Static resume snapshots miss the most important signal: commitment over time
   - Candidates who spend 3+ months learning toward alignment demonstrate authentic passion
   - Tracking growth and auto-notifying companies creates defensible differentiation

3. **Ethical Positioning:**
   - "Only guide toward authentic passion" - never nudge candidates toward misaligned work for revenue
   - This ethical stance builds trust and creates moat against incumbents focused on placement volume
   - Candidates protected from short-term misaligned decisions

4. **Hackathon Strategy:**
   - Build core matching engine (real value), demo advanced features with shortcuts
   - 24-hour execution plan validated: Tier 1 (hours 0-12), Tier 2 (12-20), Tier 3 (20-24)
   - Pre-seed 20 real companies to solve cold-start problem for demo

5. **Technical Approach:**
   - Weighted scoring: 60% domain/mission match + 40% values alignment
   - FastAPI + SQLite + vanilla JS for maximum velocity
   - NLP extraction (spaCy/NLTK) for resume parsing

6. **Market Validation Needs:**
   - Test alignment scoring accuracy with 50 real resumes
   - Interview 20 companies to validate willingness to pay $200-500/month
   - Validate that turnover reduction ROI justifies subscription cost

### B. Stakeholder Input

**Primary Stakeholder: Srijan (Product Owner/Technical Lead)**

**Vision:**
- Create alignment-first hiring platform that reduces burnout and increases career satisfaction
- Prioritize hackathon MVP success while maintaining long-term product vision
- Balance ethical principles (anti-nudging) with business viability

**Constraints Emphasized:**
- 24-hour hackathon timeline requires ruthless prioritization
- 4-person team structure: 2 frontend, 1 backend, 1 ML
- No authentication for MVP - demo-only experience
- Pre-work completed: Phase 1 (Analysis) done via BMAD framework

**Key Decisions Made:**
- YOLO mode for Product Brief generation (speed over iteration)
- HireSight as final product name
- Hackathon-first approach with post-MVP commercialization path
- Tech stack confirmed: FastAPI, SQLite, vanilla JS, spaCy/NLTK

**Open Items for Stakeholder Review:**
- [NEEDS CONFIRMATION] Company objectives alignment section - hackathon vs startup context
- Pricing validation ($199-$499/month) - interview target companies
- Geographic launch priority - US vs EU vs global
- Fundraising approach - bootstrap vs seed round

### C. References

**Source Documents:**
1. **Brainstorming Session Results (2025-10-24)**
   - Location: `/docs/brainstorming-session-results-2025-10-24.md`
   - 45+ ideas generated across immediate opportunities, future innovations, and moonshots
   - Techniques used: First Principles Thinking, SCAMPER, Resource Constraints

2. **BMM Workflow Status (2025-10-24)**
   - Location: `/docs/bmm-workflow-status.md`
   - Project: HireSight, Level 2, Greenfield software project
   - Current phase: Phase 1 - Analysis (brainstorm complete, product brief in progress)
   - Next recommended step: Move to Phase 2 - Planning (PRD creation)

**Market Research (To Be Conducted):**
3. **Turnover Cost Studies:**
   - Industry standard: 50-200% of annual salary per departure
   - Source: [To be researched] SHRM, Gallup workplace studies

4. **Mission-Driven Hiring Trends:**
   - Gen Z/Millennial preference for purpose-driven work
   - Source: [To be researched] Deloitte Millennial Survey, LinkedIn Workforce Reports

5. **Competitive Analysis:**
   - LinkedIn, Indeed, AngelList, Hired - feature gaps analysis
   - Niche players: Climatebase, Idealist, Escape the City
   - Source: [To be conducted] Direct platform testing + user interviews

**Technical References:**
6. **NLP Libraries:**
   - spaCy: https://spacy.io/ (production-ready NLP)
   - NLTK: https://www.nltk.org/ (research/prototyping)
   - Hugging Face: https://huggingface.co/ (transformer models)

7. **Tech Stack Documentation:**
   - FastAPI: https://fastapi.tiangolo.com/
   - SQLite: https://www.sqlite.org/
   - GitHub API: https://docs.github.com/en/rest

**Frameworks & Methodologies:**
8. **Product Development:**
   - BMAD (Business Model Analysis & Design) framework
   - First Principles Thinking for problem decomposition
   - SCAMPER for feature ideation

9. **Validation Approaches:**
   - Jobs-to-be-Done framework for user research
   - Van Westendorp pricing analysis for willingness-to-pay
   - Lean Startup methodology for MVP iteration

---

_This Product Brief serves as the foundational input for Product Requirements Document (PRD) creation._

_Next Steps: Handoff to Product Manager for PRD development using the `workflow prd` command._
