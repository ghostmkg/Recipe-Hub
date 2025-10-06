#!/usr/bin/env bash
# run backend & frontend for development (local)
set -e
echo "Starting backend (uvicorn)..."
cd apps/api
pip install -r requirements.txt || true
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
cd ../web
npm install || true
npm run dev
