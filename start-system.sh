#!/bin/bash
cd backend && uvicorn run_backend:app --reload --port 8000
