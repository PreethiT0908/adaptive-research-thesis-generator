# Frontend and Backend Connection Setup

## Architecture

```
Frontend (React + Vite)
    │ http://localhost:5173
    │
    ├─→ Vite Dev Server Proxy
    │   │ /api/* → http://localhost:8001/*
    │
    └─→ Backend API (FastAPI + Uvicorn)
        └─ http://localhost:8001
```

## Setup Instructions

### 1. Install Backend Dependencies
```bash
cd app
pip install fastapi uvicorn
```

### 2. Install Frontend Dependencies
```bash
cd thesis-frontend
npm install
```

### 3. Run Both Servers

#### Option A: Automated (Windows)
Run the batch file from project root:
```bash
start-dev.bat
```

#### Option B: Manual - Two Terminal Windows
Terminal 1 (Backend):
```bash
cd app
python api.py
```

Terminal 2 (Frontend):
```bash
cd thesis-frontend
npm run dev
```

## Access Points

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8001
- **API Docs**: http://localhost:8001/docs (Swagger UI)

## API Endpoints

### POST /generate
Generates a thesis with the provided parameters.

**Request Body:**
```json
{
  "degree": "PhD",
  "university": "MIT",
  "discipline": "Computer Science",
  "topic": "Machine Learning Applications",
  "target_journal": "IEEE"
}
```

**Response:**
```json
{
  "policy": { ... },
  "blueprint": { ... },
  "papers": [ ... ]
}
```

## CORS Configuration

The backend allows requests from:
- `http://localhost:5173` (Frontend dev server)
- `http://localhost:3000` (Alternative CRA port)
- `http://localhost:8001` (API server itself)

## Debugging

1. **Check backend is running**: Visit http://localhost:8001 - should see a message
2. **Check API docs**: Visit http://localhost:8001/docs
3. **Check browser console**: Press F12 in frontend to see API request details
4. **Check network tab**: Monitor POST /api/generate request

## Environment Variables

Backend port: Hardcoded to 8001 in api.py
Frontend proxy: Configured in vite.config.js

To change ports, update:
- `app/api.py` line: `uvicorn.run(app, host="0.0.0.0", port=8001)`
- `thesis-frontend/vite.config.js` proxy configuration
