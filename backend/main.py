
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace '*' with your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/trip-assistant")
async def trip_assistant(request: Request):
    data = await request.json()
    # You can process the data here
    return {
        "status": "success",
        "received": data
    }

@app.get("/")
async def root():
    return {"message": "TaskMate backend is running"}
