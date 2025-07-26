#!/bin/bash

# Fail if any command fails
set -e

# Ask for GitHub repo URL if not set
if [ -z "$1" ]; then
  echo "Usage: ./push.sh <your-github-repo-url>"
  exit 1
fi

REPO_URL=$1

# Initialize git and push
echo "Initializing Git repo..."
git init
git remote add origin "$REPO_URL"
git add .
git commit -m "Initial TaskMate MVP"
git branch -M main
git push -u origin main

echo "✅ Successfully pushed to $REPO_URL"