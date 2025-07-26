from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS from your Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your exact Vercel domain for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "TaskMate backend is running!"}

@app.post("/api/trip-assistant")
async def trip_assistant(request: Request):
    data = await request.json()
    destination = data.get("destination", "Unknown")
    duration = data.get("duration", 0)
    budget = data.get("budget", 0)
    preferences = data.get("preferences", "")

    return {
        "message": f"Planning a trip to {destination} for {duration} days with a budget of ${budget}. Preferences: {preferences}"
    }

@app.post("/api/email-summarizer")
async def email_summarizer(request: Request):
    data = await request.json()
    email_text = data.get("emailText", "")
    tone = data.get("tone", "Neutral")
    summary_type = data.get("summaryType", "Brief")

    return {
        "summary": f"[{summary_type}] ({tone}): This is a summary of your email: {email_text[:60]}..."
    }
