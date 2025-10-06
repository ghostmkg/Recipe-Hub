#!/usr/bin/env bash
# format backend and frontend code
set -e

echo "Formatting Python backend..."
cd apps/api
# install black if not installed
pip install black isort flake8 --quiet || true
# format Python files
black .
isort .
# optional linting
flake8 .

cd ../../

echo "Formatting frontend..."
cd apps/web
# install prettier if not installed
npm install --silent prettier eslint --save-dev || true
# format all JS/TS files
npx prettier --write "src/**/*.{js,ts,jsx,tsx}"
# optional eslint fix
npx eslint "src/**/*.{js,ts,jsx,tsx}" --fix

cd ../../
echo "Formatting completed."
