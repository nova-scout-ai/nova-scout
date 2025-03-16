# Deployment Kit - Dropshipping AI System
# Created: 2025-03-16

# --- Folder Structure Setup ---
mkdir dropshipping-ai-system && cd dropshipping-ai-system

# Create project folders
echo "Setting up project folders..."
mkdir backend frontend data automation

# --- Backend Setup ---
echo "Creating FastAPI backend app..."
cd backend
cat <<EOF > requirements.txt
fastapi
uvicorn
pandas
textblob
scikit-learn
beautifulsoup4
requests
python-multipart
EOF

cat <<EOF > run_backend.py
from backend_api_service import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
EOF
cd ..

# --- Frontend Setup ---
echo "React frontend already prepared. Push /frontend to Vercel."

# --- Data Folder (Syncable with backend API) ---
touch data/niche_vault_latest.json
touch data/order_log_latest.json
touch data/financial_metrics_latest.json

# --- Automation Runner Script (Cron or manual) ---
cat <<EOF > automation/daily_runner.py
# Trigger core pipeline logic manually or via cron
import os
print("Running AI pipeline...")
os.system("python ../backend/ai_core_pipeline.py")
EOF

# --- Starter Script ---
cat <<EOF > start-system.sh
#!/bin/bash
echo "Starting Dropshipping AI Backend..."
cd backend && uvicorn run_backend:app --reload --port 8000
EOF
chmod +x start-system.sh

# --- Render/Deploy Notes ---
echo "Create a free Render backend service:
1. Push this backend folder to GitHub.
2. Connect to Render.
3. Add build command: pip install -r requirements.txt
4. Start command: python run_backend.py
"

echo "Deploy Frontend to Vercel:
1. Push /frontend folder to GitHub.
2. Connect to Vercel (vercel.com).
3. Deploy instantly.
"
