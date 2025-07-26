from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class EmailInput(BaseModel):
    email_thread: str
    reply_tone: Optional[str] = "friendly"
    reply_intent: str

class EmailOutput(BaseModel):
    summary: str
    reply: str

@app.post("/api/email-helper", response_model=EmailOutput)
def email_helper(input: EmailInput):
    # Simulated logic
    summary = "Simulated summary of the email thread"
    reply = f"Drafted reply with a {input.reply_tone} tone and intent to {input.reply_intent}"
    return EmailOutput(summary=summary, reply=reply)

class TripInput(BaseModel):
    destination: str
    days: int
    budget: float
    preferences: List[str] = []

class Flight(BaseModel):
    airline: str
    price: float
    departure: str
    return_: str

class Hotel(BaseModel):
    name: str
    price_per_night: float
    location: str

class TripOutput(BaseModel):
    flights: Flight
    hotel: Hotel
    activities: List[str]
    total_cost_estimate: float

@app.post("/api/trip-assistant", response_model=TripOutput)
def trip_assistant(input: TripInput):
    flight = Flight(airline="United Airlines", price=210, departure="Friday 10AM", return_="Monday 5PM")
    hotel = Hotel(name="Hotel Versey", price_per_night=150, location="Lincoln Park")
    activities = ["Day 1: Millennium Park", "Day 2: Art Institute + Pizza", "Day 3: Checkout & Souvenirs"]
    return TripOutput(flights=flight, hotel=hotel, activities=activities, total_cost_estimate=765)