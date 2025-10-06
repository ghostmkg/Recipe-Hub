#!/usr/bin/env bash
# unified dev script: seed DB, format code (optional), start backend & frontend
set -e

echo "Step 1: Seeding database..."
cd apps/api
pip install -r requirements.txt || true
python scripts/seed_db.py
cd ../../

# Optional formatting step
echo "Step 2: Formatting code (optional)..."
./format.sh || true

# Step 3: Start backend and frontend
echo "Step 3: Starting backend (uvicorn) & frontend (npm run dev)..."
cd apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
cd ../web
npm install || true
npm run dev
