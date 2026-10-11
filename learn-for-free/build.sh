#!/usr/bin/env bash
# build.sh - build one volume or all volumes (git-bash / WSL / macOS / Linux)
# Usage: ./build.sh 01-html | ./build.sh --all
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python}"
if command -v python >/dev/null 2>&1; then PY=python; elif command -v python3 >/dev/null 2>&1; then PY=python3; fi
exec "$PY" build.py "$@"
