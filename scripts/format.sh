#!/bin/bash

# Script to format backend and frontend code

echo "✨ Formatting backend with black + isort..."
cd ../apps/servers || exit
black . && isort .

echo "🧼 Formatting frontend with prettier..."
cd ../../web || exit
npx prettier --write "src/**/*.{ts,tsx,js,jsx,json,css}"
