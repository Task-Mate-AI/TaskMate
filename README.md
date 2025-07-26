# TaskMate

TaskMate is your AI-powered personal assistant to simplify daily tasks like summarizing emails and planning trips.

## 🚀 How to Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 🌐 Deployment

- **Frontend**: Deploy via [Vercel](https://vercel.com/)
- **Backend**: Deploy via [Railway](https://railway.app/) or [Render](https://render.com/)

## 📦 API Routes

- `POST /api/email-helper` — summarizes an email and drafts a reply
- `POST /api/trip-assistant` — builds a trip plan from user preferences