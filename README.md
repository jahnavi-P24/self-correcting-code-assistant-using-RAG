# Project Index and Overview

## Backend
- `backend/api/openfix_pro.py` — Main FastAPI app
- `backend/api/routes/` — API route definitions
- `backend/api/schemas/` — Pydantic models
- `backend/api/services/` — Business logic
- `backend/api/utils/` — Utilities
- `backend/api/checkpoint/` — Caching/checkpoint logic
- `backend/api/frontend/` — Static frontend serving (if used)
- `backend/tests/` — Backend tests
- `backend/fixes/` — Fix scripts
- `backend/results/` — Output/result images
- `backend/data/` — Datasets
- `backend/evaluation/` — Evaluation scripts/reports
- `backend/utils/` — General backend utilities

## Frontend
- `frontend-react/src/components/` — React components
- `frontend-react/src/hooks/` — Custom hooks
- `frontend-react/public/` — Static files
- `frontend-react/cypress/` — E2E tests
- `frontend-react/src/` — Main app, entry points, assets

## Checkpoints
- `checkpoints/v1.0/`, `v2.0/`, `v3.0/` — Project snapshots

## Project Graphs
- `project_graphs/` — Generated graphs for documentation

## Scripts & Results
- `generate_project_graphs.py` — Script to generate graphs
- `mbpp_results.json`, `bigcode_results.json` — Test results
- `test_mbpp_sample.py`, `test_bigcode_sample.py` — Test scripts

## How to Navigate
- Start with the README for an overview.
- Backend code is in `backend/`, frontend in `frontend-react/`.
- Checkpoints contain full project snapshots for each major version.
- Project graphs and results are in their respective folders for documentation and analysis.

---

*This index is auto-generated and should be updated as the project evolves.* 