#!/bin/bash
# run_all.sh
# This script sets up and runs the full prototype on new systems.

set -e

# --- Check for required commands ---
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 is required but it's not installed. Please install Python3."; exit 1; }
command -v pip3 >/dev/null 2>&1 || { echo >&2 "pip3 is required but it's not installed. Please install pip3."; exit 1; }
command -v node >/dev/null 2>&1 || { echo >&2 "Node.js is required but it's not installed. Please install Node.js."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo >&2 "npm is required but it's not installed. Please install npm."; exit 1; }

# --- Database configuration ---
# Using SQLite by default, no need to check for DATABASE_URL
# You can still override with your own DATABASE_URL if needed

# --- Create and activate Python virtual environment ---
if [ ! -d "venv" ]; then
  echo "Creating Python virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# --- Install backend dependencies ---
echo "Installing backend dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt

# --- Initialize the database ---

echo "Initializing the SQLite database..."
PYTHONPATH=./backend python -c "from app.database.session import init_db; init_db()"

# --- Install frontend dependencies ---
echo "Installing frontend dependencies..."
(cd frontend && npm install)

# --- Start backend and frontend servers ---
echo "Starting backend server..."
uvicorn app.main:app --reload --host 0.0.0.0 &
BACKEND_PID=$!

echo "Starting frontend server..."
(cd frontend && npm run dev) &
FRONTEND_PID=$!

echo "Servers are running. Press Ctrl+C to stop both servers."

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
