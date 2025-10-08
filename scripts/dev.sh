#!/bin/bash

# Script to run backend and frontend in development mode

echo "🚀 Starting development servers..."

# Start FastAPI backend

cd ../apps/servers || exit
uvicorn app.services.main:app --reload --host 0.0.0.0 --port 8000 &
BACK_PID=$!

# Start React frontend

cd ../../web || exit
npm run dev &

# Wait for backend

wait $BACK_PID
