#!/usr/bin/env bash
# Build script for Render.com deployment

set -e  # Exit on error

echo "===== HireSight Build Script ====="

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
cd backend
pip install -r requirements.txt

# Create necessary directories
echo "Creating directories..."
mkdir -p data uploads

# Initialize database
echo "Initializing database..."
python -c "from app.core.database import init_db; init_db()"

# Seed database with company data
echo "Seeding database with companies..."
python data/seed_companies.py << EOF
no
EOF

echo "===== Build Complete ====="
