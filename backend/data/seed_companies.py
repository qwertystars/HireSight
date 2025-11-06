"""Seed script to populate companies table with mission-driven companies."""
import sys
import os
import json
import logging

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, init_db
from app.models.company import Company

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Company data: 20 mission-driven companies across different sectors
COMPANIES_DATA = [
    # Climate Tech (8 companies)
    {
        "name": "ClimateAI Solutions",
        "mission": "Leveraging AI to predict and mitigate climate change impacts on agriculture and supply chains",
        "values": ["sustainability", "data-driven impact", "innovation", "global collaboration"],
        "required_skills": ["Python", "Machine Learning", "Climate modeling", "Data Science", "AWS"],
        "domain": "climate tech"
    },
    {
        "name": "GreenEnergy Analytics",
        "mission": "Building software tools to optimize renewable energy production and distribution",
        "values": ["clean energy", "environmental stewardship", "technical excellence"],
        "required_skills": ["Python", "React", "IoT systems", "Data visualization", "Energy systems"],
        "domain": "climate tech"
    },
    {
        "name": "CarbonTrack",
        "mission": "Helping companies measure, report, and reduce their carbon footprint through automated tracking",
        "values": ["transparency", "accountability", "climate action", "innovation"],
        "required_skills": ["JavaScript", "React", "Node.js", "PostgreSQL", "APIs"],
        "domain": "climate tech"
    },
    {
        "name": "OceanGuard Technologies",
        "mission": "Protecting marine ecosystems through AI-powered monitoring and conservation tools",
        "values": ["ocean conservation", "biodiversity", "scientific rigor", "impact"],
        "required_skills": ["Python", "Computer Vision", "ML", "GIS", "Marine science"],
        "domain": "climate tech"
    },
    {
        "name": "SolarScale",
        "mission": "Making solar energy accessible and affordable for underserved communities worldwide",
        "values": ["energy justice", "accessibility", "community empowerment", "innovation"],
        "required_skills": ["Python", "React", "Mobile development", "Payment systems", "Energy modeling"],
        "domain": "climate tech"
    },
    {
        "name": "EcoSupply Chain",
        "mission": "Transforming supply chains to be carbon-neutral through optimization and transparency software",
        "values": ["sustainability", "efficiency", "transparency", "global impact"],
        "required_skills": ["Python", "Supply chain management", "Optimization algorithms", "Cloud platforms"],
        "domain": "climate tech"
    },
    {
        "name": "ForestAI",
        "mission": "Using satellite imagery and AI to prevent deforestation and support reforestation efforts",
        "values": ["conservation", "innovation", "data for good", "environmental protection"],
        "required_skills": ["Python", "Machine Learning", "Computer Vision", "GIS", "Satellite imagery"],
        "domain": "climate tech"
    },
    {
        "name": "CleanAir Insights",
        "mission": "Monitoring and improving air quality in urban areas through IoT sensors and data analytics",
        "values": ["public health", "environmental justice", "data transparency", "community focus"],
        "required_skills": ["Python", "IoT", "Data Science", "React", "Public health systems"],
        "domain": "climate tech"
    },

    # EdTech (6 companies)
    {
        "name": "LearnForAll",
        "mission": "Providing free, personalized education to students in under-resourced communities",
        "values": ["educational equity", "accessibility", "empowerment", "lifelong learning"],
        "required_skills": ["React", "Python", "Educational technology", "Mobile development", "UX design"],
        "domain": "EdTech"
    },
    {
        "name": "SkillBridge",
        "mission": "Connecting career changers with mentorship and skills training for high-growth industries",
        "values": ["career mobility", "inclusion", "mentorship", "skills development"],
        "required_skills": ["JavaScript", "React", "Node.js", "Recommendation systems", "Video platforms"],
        "domain": "EdTech"
    },
    {
        "name": "CodeForKids",
        "mission": "Teaching programming and computational thinking to K-12 students through interactive games",
        "values": ["early education", "creativity", "problem-solving", "inclusive learning"],
        "required_skills": ["JavaScript", "Game development", "Educational design", "React", "Python"],
        "domain": "EdTech"
    },
    {
        "name": "GlobalClassroom",
        "mission": "Breaking down language barriers in education with real-time translation and localized content",
        "values": ["global access", "cultural inclusivity", "language justice", "collaboration"],
        "required_skills": ["Python", "NLP", "Machine Translation", "React", "Internationalization"],
        "domain": "EdTech"
    },
    {
        "name": "STEMPath",
        "mission": "Increasing STEM participation among underrepresented groups through mentorship platforms",
        "values": ["diversity", "representation", "STEM access", "community building"],
        "required_skills": ["React", "Python", "Community platforms", "Data analytics", "Mobile"],
        "domain": "EdTech"
    },
    {
        "name": "LiteracyNow",
        "mission": "Combating adult illiteracy through AI-powered personalized reading programs",
        "values": ["literacy", "empowerment", "accessibility", "dignity"],
        "required_skills": ["Python", "NLP", "Mobile development", "Adaptive learning", "UX"],
        "domain": "EdTech"
    },

    # HealthTech (4 companies)
    {
        "name": "HealthAccess",
        "mission": "Bringing affordable telemedicine to rural and underserved urban communities",
        "values": ["health equity", "accessibility", "community health", "compassion"],
        "required_skills": ["React", "Python", "Healthcare systems", "Video conferencing", "HIPAA compliance"],
        "domain": "HealthTech"
    },
    {
        "name": "MentalWellAI",
        "mission": "Making mental health support accessible through AI-powered therapy assistants and community",
        "values": ["mental health awareness", "stigma reduction", "accessibility", "evidence-based care"],
        "required_skills": ["Python", "NLP", "React", "ML", "Healthcare privacy"],
        "domain": "HealthTech"
    },
    {
        "name": "MedEquity",
        "mission": "Reducing healthcare disparities by connecting patients with culturally competent providers",
        "values": ["health justice", "cultural competency", "patient-centered care", "equity"],
        "required_skills": ["Python", "React", "Healthcare systems", "Matching algorithms", "Data security"],
        "domain": "HealthTech"
    },
    {
        "name": "PreventiveCare AI",
        "mission": "Using predictive analytics to identify at-risk patients and prevent chronic diseases",
        "values": ["preventive health", "data-driven care", "cost reduction", "patient outcomes"],
        "required_skills": ["Python", "Machine Learning", "Healthcare data", "Statistics", "Predictive modeling"],
        "domain": "HealthTech"
    },

    # Social Impact (2 companies)
    {
        "name": "RefugeeConnect",
        "mission": "Helping refugees integrate through job matching, language learning, and community support",
        "values": ["human rights", "integration", "compassion", "empowerment"],
        "required_skills": ["React", "Python", "NLP", "Mobile development", "Community platforms"],
        "domain": "social impact"
    },
    {
        "name": "FoodRescue Tech",
        "mission": "Reducing food waste and hunger by connecting surplus food with people in need",
        "values": ["food security", "sustainability", "community impact", "efficiency"],
        "required_skills": ["React", "Python", "Logistics optimization", "Mobile", "Real-time systems"],
        "domain": "social impact"
    }
]


def seed_companies(db: Session) -> None:
    """Seed the database with company data."""
    logger.info("Starting company data seeding...")

    # Check if companies already exist
    existing_count = db.query(Company).count()
    if existing_count > 0:
        logger.info(f"Database already contains {existing_count} companies")
        response = input("Do you want to clear existing data and reseed? (yes/no): ")
        if response.lower() != "yes":
            logger.info("Seeding cancelled")
            return

        # Clear existing companies
        db.query(Company).delete()
        db.commit()
        logger.info("Existing companies cleared")

    # Insert companies
    for company_data in COMPANIES_DATA:
        company = Company(
            name=company_data["name"],
            mission=company_data["mission"],
            values=json.dumps(company_data["values"]),
            required_skills=json.dumps(company_data["required_skills"]),
            domain=company_data["domain"]
        )
        db.add(company)

    db.commit()
    logger.info(f"Successfully seeded {len(COMPANIES_DATA)} companies")

    # Display summary
    domains = {}
    for company_data in COMPANIES_DATA:
        domain = company_data["domain"]
        domains[domain] = domains.get(domain, 0) + 1

    logger.info("\nSeeding summary:")
    for domain, count in domains.items():
        logger.info(f"  {domain}: {count} companies")


def main():
    """Main function to run seeding."""
    try:
        # Initialize database
        logger.info("Initializing database...")
        init_db()

        # Create session
        db = SessionLocal()

        try:
            # Seed companies
            seed_companies(db)
            logger.info("\nSeeding completed successfully!")

        finally:
            db.close()

    except Exception as e:
        logger.error(f"Seeding failed: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
