#!/usr/bin/env bash
# Push Forge to GitHub. Secrets are gitignored (.env, .venv, renders/, broll).
# Prereq: authenticate first — either `gh auth login`, or create a repo and add
# a remote with a Personal Access Token.
set -euo pipefail

REPO_NAME="forge"
cd "$(dirname "$0")/.."

if command -v gh >/dev/null 2>&1; then
  # Easiest path: GitHub CLI creates the repo and pushes in one shot.
  gh repo create "$REPO_NAME" --private --source=. --remote=origin --push
  echo "✅ Pushed to GitHub via gh."
else
  cat <<'EOF'
gh (GitHub CLI) not found. Manual push:

  1) Create an empty repo at https://github.com/new  (name: forge)
  2) Then run:
       git remote add origin https://github.com/<YOUR_USER>/forge.git
       git branch -M main
       git push -u origin main
     (When prompted for password, paste a GitHub Personal Access Token.)
EOF
fi
