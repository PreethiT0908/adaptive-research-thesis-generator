# 🎓 Adaptive Thesis Generator - Frontend & Backend Integration

## Quick Start

### Option 1: Automated Startup (Easiest)

**Windows Command Prompt:**
```bash
start-dev.bat
```

**Windows PowerShell:**
```powershell
.\start-dev.ps1
```

This will automatically start:
- Backend API on `http://localhost:8001`
- Frontend on `http://localhost:5173`

### Option 2: Manual Startup

**Terminal 1 - Backend:**
```bash
cd app
python api.py
```

**Terminal 2 - Frontend:**
```bash
cd thesis-frontend
npm run dev
```

---

## 📋 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│              React Frontend (Port 5173)                  │
│                                                         │
│  - User Interface (Generate.jsx)                        │
│  - Form Input Handling                                  │
│  - Result Display                                       │
└──────────────────┬──────────────────────────────────────┘
                   │
         Vite Dev Server Proxy
         (/api → localhost:8001)
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│          FastAPI Backend (Port 8001)                     │
│                                                         │
│  - Profile Agent (User data processing)                │
│  - Blueprint Agent (Thesis structure generation)        │
│  - Search Agent (Find research papers)                  │
│  - RAG Agent (Knowledge base creation)                  │
│  - Additional agents (validation, ethics, revision)     │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 What's Connected

### Frontend Files Modified/Created:
- **Generate.jsx** - Improved form with API integration
- **Generate.css** - Enhanced styling and UX
- **.env.local** - Environment configuration
- **vite.config.js** - API proxy configuration

### Backend Files Modified:
- **api.py** - Added uvicorn startup code

### Helper Scripts:
- **start-dev.bat** - Batch file for Windows CMD
- **start-dev.ps1** - PowerShell script for Windows
- **FRONTEND_BACKEND_CONNECTION.md** - Technical documentation

---

## 🔌 API Integration Details

### Endpoint: `POST /api/generate`

**Request Format:**
```javascript
{
  "degree": "PhD",              // "UG", "Master", or "PhD"
  "university": "MIT",           // University name
  "discipline": "Computer Science", // Field of study
  "topic": "Machine Learning",   // Research topic
  "target_journal": "IEEE"       // (Optional) Target publication
}
```

**Response Format:**
```javascript
{
  "policy": {
    // Research policy details from Profile Agent
  },
  "blueprint": {
    // Thesis structure from Blueprint Agent
  },
  "papers": [
    // Array of papers found by Search Agent
  ]
}
```

---

## ✅ Verification Checklist

After starting both servers, verify:

- [ ] **Backend is running:**
  - Visit http://localhost:8001
  - Should show: `{"message": "Adaptive Thesis Generator API Running"}`

- [ ] **API documentation available:**
  - Visit http://localhost:8001/docs
  - Should show Swagger UI with `/generate` endpoint

- [ ] **Frontend is running:**
  - Visit http://localhost:5173
  - Should show the thesis generator form

- [ ] **Frontend can communicate with backend:**
  - Fill in the form and click "Generate Thesis"
  - Check browser console (F12) for any errors
  - Results should appear below the form

---

## 🐛 Troubleshooting

### Backend not starting

**Error: "Port 8001 already in use"**
- Kill the process using port 8001:
  ```bash
  netstat -ano | findstr :8001
  taskkill /PID <PID> /F
  ```
- Or change the port in `app/api.py` line with `uvicorn.run()`

**Error: "Module not found (fastapi, uvicorn)"**
- Install dependencies:
  ```bash
  cd app
  pip install fastapi uvicorn
  ```

### Frontend not starting

**Error: "npm not found"**
- Install Node.js from https://nodejs.org

**Error: "Module not found"**
- Install dependencies:
  ```bash
  cd thesis-frontend
  npm install
  ```

### API requests failing

**Error: CORS issues**
- Backend is configured to accept requests from `localhost:5173`
- Check that backend is actually running on port 8001

**Error: 404 on /api/generate**
- The Vite proxy might not be working
- Verify vite.config.js has the proxy configuration
- Restart the frontend server

**Error: Connection refused**
- Ensure backend started first (takes 1-2 seconds)
- Verify port 8001 is accessible
- Check firewall settings

---

## 🛠️ Development Workflow

1. **Make changes to frontend:**
   - Edit files in `thesis-frontend/src/`
   - Vite will hot-reload automatically

2. **Make changes to backend:**
   - Edit files in `app/`
   - Restart the backend server (Ctrl+C, then run again)

3. **Test API changes:**
   - Use Swagger UI at http://localhost:8001/docs
   - Or use curl:
   ```bash
   curl -X POST http://localhost:8001/generate \
     -H "Content-Type: application/json" \
     -d '{
       "degree": "PhD",
       "university": "MIT",
       "discipline": "AI",
       "topic": "Neural Networks"
     }'
   ```

---

## 📦 Dependencies

### Backend Requirements
```
fastapi
uvicorn
pydantic
```

### Frontend Requirements
```
react
react-dom
axios
react-router-dom
```

See `thesis-frontend/package.json` for complete frontend dependencies.

---

## 🌐 Ports and Services

| Service | Port | URL |
|---------|------|-----|
| Backend API | 8001 | http://localhost:8001 |
| API Documentation | 8001 | http://localhost:8001/docs |
| Frontend Dev | 5173 | http://localhost:5173 |
| Alternative Frontend | 3000 | http://localhost:3000 (if using CRA) |

---

## 📝 Environment Configuration

**Frontend (.env.local):**
```
VITE_API_URL=http://localhost:8001
```

**Backend (app/api.py):**
```python
uvicorn.run(app, host="0.0.0.0", port=8001)
```

---

## 🎯 Next Steps

1. ✅ Start both servers using provided scripts
2. ✅ Open http://localhost:5173 in your browser
3. ✅ Fill in the thesis generation form
4. ✅ Click "Generate Thesis"
5. ✅ View results in the UI
6. 🔄 Implement additional agents (Drafting, Validation, Ethics, Revision, Output)

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vite.dev/)
- [Axios Documentation](https://axios-http.com/)

---

## ❓ Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review browser console (F12) for frontend errors
3. Check terminal output for backend errors
4. Verify both services are running on correct ports
5. Ensure firewall isn't blocking connections
