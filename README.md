# HireSight

> Alignment-first hiring platform connecting mission-driven companies with passionate candidates.

HireSight is a web application that matches candidates with companies based on **values alignment** and **mission fit**, not just skills. Built for the modern hiring landscape where purpose matters as much as proficiency.

## 🌟 Features

- **Resume Upload & Analysis**: Upload PDF/DOCX resumes for automatic skill and values extraction
- **Alignment Scoring**: AI-powered matching algorithm (60% domain + 40% values)
- **Skill Gap Analysis**: Get personalized learning recommendations
- **Interest Tracking**: Track candidates' journey over time
- **Company Dashboard**: Batch candidate ranking for hiring managers

## 🏗️ Architecture

- **Backend**: Python 3.12 + FastAPI
- **Database**: SQLite with WAL mode (optimized for production)
- **Validation**: Pydantic v2
- **Deployment**: Render.com ready
- **Frontend**: React (to be implemented)

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- pip

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/HireSight.git
   cd HireSight
   ```

2. **Set up backend**
   ```bash
   cd backend
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env if needed
   ```

4. **Initialize database**
   ```bash
   python -c "from app.core.database import init_db; init_db()"
   ```

5. **Seed company data**
   ```bash
   python data/seed_companies.py
   ```

6. **Run the server**
   ```bash
   # Development mode (with auto-reload)
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

   # Or using the main.py directly
   python app/main.py
   ```

7. **Access the API**
   - API: http://localhost:8000
   - Health Check: http://localhost:8000/health
   - Interactive Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 📚 API Endpoints

### Health & Info

- `GET /` - API information
- `GET /health` - Health check with database status

### Candidates

- `POST /api/upload-resume` - Upload and process candidate resume
  - **Body**: `multipart/form-data` with `file` field
  - **Returns**: `{candidate_id, message}`

### Companies

- `GET /api/companies?candidate_id={id}` - Get ranked companies for candidate
  - **Query Params**:
    - `candidate_id` (required): Candidate ID
    - `threshold` (optional): Minimum alignment threshold (0-100)
  - **Returns**: Array of companies with alignment scores

### Alignment

- `POST /api/check-gap` - Analyze skill gap
  - **Body**: `{candidate_id, company_id}`
  - **Returns**: Missing skills and learning recommendations

### Interest Tracking

- `POST /api/track-interest` - Track candidate interest
  - **Body**: `{candidate_id, company_id}`
  - **Returns**: Success confirmation

- `DELETE /api/track-interest` - Untrack interest
  - **Body**: `{candidate_id, company_id}`
  - **Returns**: Success confirmation

## 🚢 Deployment to Render

### Automatic Deployment (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml` and deploy

3. **Configure Environment Variables** (if needed)
   - Navigate to your service in Render
   - Go to "Environment"
   - Add/update variables:
     - `CORS_ORIGINS`: Your frontend URL
     - `LOG_LEVEL`: INFO or DEBUG
     - Other variables are set in `render.yaml`

### Manual Deployment

1. **Create Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your repository

2. **Configure Service**
   - **Name**: hiresight-api
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `./start.sh`
   - **Plan**: Free (or higher)

3. **Add Environment Variables**
   ```
   PYTHON_VERSION=3.12.0
   ENVIRONMENT=production
   DATABASE_URL=sqlite:///./data/hiresight.db
   LOG_LEVEL=INFO
   LOG_FORMAT=json
   PORT=10000
   HOST=0.0.0.0
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Access your API at the provided URL

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_NAME` | Application name | HireSight |
| `APP_VERSION` | Application version | 1.0.0 |
| `DEBUG` | Debug mode | False |
| `ENVIRONMENT` | Environment (development/production) | development |
| `DATABASE_URL` | Database connection URL | sqlite:///./data/hiresight.db |
| `UPLOAD_DIR` | Upload directory path | ./uploads |
| `MAX_UPLOAD_SIZE` | Max upload size in bytes | 10000000 (10MB) |
| `CORS_ORIGINS` | Comma-separated CORS origins | http://localhost:5173 |
| `LOG_LEVEL` | Logging level | INFO |
| `LOG_FORMAT` | Log format (json/text) | json |
| `HOST` | Server host | 0.0.0.0 |
| `PORT` | Server port | 8000 |

### Database Optimizations

The application uses SQLite with the following optimizations enabled:

- **WAL mode**: Better concurrency
- **Increased cache size**: 64MB for faster queries
- **Foreign keys**: Enforced relationships
- **Memory-mapped I/O**: 256MB for performance
- **Connection pooling**: Automatic reconnection

## 📊 Database Schema

### Tables

**candidates**
- `id`: Integer (Primary Key)
- `resume_path`: String - Path to resume file
- `extracted_text`: Text - Full resume text
- `extracted_skills`: JSON - Array of skills
- `extracted_domains`: JSON - Array of domains
- `values_signals`: JSON - Array of values
- `created_at`: DateTime

**companies**
- `id`: Integer (Primary Key)
- `name`: String (Unique)
- `mission`: Text
- `values`: JSON - Array of values
- `required_skills`: JSON - Array of required skills
- `domain`: String
- `created_at`: DateTime

**interests**
- `id`: Integer (Primary Key)
- `candidate_id`: Integer (Foreign Key)
- `company_id`: Integer (Foreign Key)
- `tracked_at`: DateTime
- Unique constraint on (candidate_id, company_id)

## 🧪 Testing

```bash
cd backend
pytest tests/ -v
```

## 🔨 Development

### Project Structure

```
HireSight/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/        # API endpoints
│   │   ├── core/              # Config, database, logging
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   └── utils/             # Utilities
│   ├── data/
│   │   └── seed_companies.py  # Database seeding
│   ├── uploads/               # Uploaded resumes
│   ├── tests/                 # Test suite
│   ├── .env                   # Environment config
│   └── requirements.txt       # Dependencies
├── docs/                      # Documentation
├── build.sh                   # Build script (Render)
├── start.sh                   # Start script (Render)
└── render.yaml                # Render configuration
```

### Human-Implemented Services

The following services require human implementation:

1. **`services/resume_parser.py`**
   - `extract_text_from_resume()`: PDF/DOCX parsing
   - Suggested libraries: PyPDF2, pdfplumber, python-docx

2. **`services/nlp_service.py`**
   - `extract_skills_and_domains()`: NLP extraction
   - Suggested libraries: spaCy, NLTK, transformers

3. **`services/alignment_service.py`**
   - `calculate_alignment()`: Sophisticated matching algorithm
   - Current implementation: Basic keyword matching
   - Suggested improvements: Embeddings, semantic similarity

## 🎯 Roadmap

- [ ] Implement advanced NLP for resume parsing
- [ ] Add semantic similarity for alignment scoring
- [ ] Build React frontend
- [ ] Add authentication/authorization
- [ ] Implement real-time notifications
- [ ] Add PostgreSQL support for production scale
- [ ] Build candidate journey tracking
- [ ] Add company admin dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with FastAPI, SQLAlchemy, and Pydantic
- Inspired by the need for values-driven hiring
- Designed for mission-driven organizations

## 📧 Contact

For questions or support, please open an issue or contact [your-email@example.com]

---

**Made with ❤️ for mission-driven hiring**
