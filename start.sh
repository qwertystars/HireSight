#!/usr/bin/env bash
# Start script for Render.com deployment

set -e  # Exit on error

echo "===== Starting HireSight API ====="

cd backend

# Use gunicorn with uvicorn workers for production
exec gunicorn app.main:app \
    --worker-class uvicorn.workers.UvicornWorker \
    --workers 2 \
    --bind 0.0.0.0:${PORT:-10000} \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    --graceful-timeout 30 \
    --keep-alive 5
