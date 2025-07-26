from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow CORS so frontend (Vercel) can talk to backend (Railway)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your Vercel frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 Route to summarize emails
@app.post("/api/email-summarizer")
async def summarize_email(request: Request):
    data = await request.json()
    email_text = data.get("emailText", "")
    tone = data.get("tone", "Neutral")
    summary_type = data.get("summaryType", "Summary")

    # Stub response – replace with real AI logic later
    return {
        "summary": f"Summarized email with tone '{tone}' and type '{summary_type}': {email_text[:60]}..."
    }

# ✈️ Route to assist with trip planning
@app.post("/api/trip-assistant")
async def plan_trip(request: Request):
    data = await request.json()
    destination = data.get("destination")
    duration = data.get("duration")
    budget = data.get("budget")
    preferences = data.get("preferences", "")

    # Stub response – replace with real planning logic later
    return {
        "plan": f"Trip planned to {destination} for {duration} days within ${budget}, preferences: {preferences}"
    }

# 🩺 Health check (optional)
@app.get("/")
def root():
    return {"status": "Backend is alive"}
