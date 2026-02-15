#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${REPO_ROOT}"

if [[ ! -d ".venv" ]]; then
    python -m venv .venv
fi

source .venv/bin/activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r .devcontainer/requirements-week11.txt

python -m ipykernel install --user --name "vvp-venv" --display-name "Python (vvp .venv)"

echo "Virtual environment is ready at ${REPO_ROOT}/.venv"
