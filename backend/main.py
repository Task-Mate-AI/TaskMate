from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS Fix: Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Optional: Replace * with your Vercel domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running!"}

# ✅ Fix for /api/trip-assistant (POST only)
@app.post("/api/trip-assistant")
async def trip_assistant(request: Request):
    body = await request.json()
    destination = body.get("destination")
    duration = body.get("duration")
    budget = body.get("budget")
    preferences = body.get("preferences")

    return {
        "plan": f"Trip to {destination} for {duration} days with ${budget} budget. Preferences: {preferences}"
    }

# ✅ Fix for /api/email-summarizer (POST only)
@app.post("/api/email-summarizer")
async def email_summarizer(request: Request):
    body = await request.json()
    email_text = body.get("emailText")
    tone = body.get("tone")
    summary_type = body.get("summaryType")

    return {
        "summary": f"Summary ({summary_type}, {tone}): {email_text[:50]}..."
    }
