import React, { useState } from 'react';
import axios from 'axios';

function TripPlanner() {
  const [destination, setDestination] = useState('');
  const [days, setDays] = useState(3);
  const [budget, setBudget] = useState(800);
  const [preferences, setPreferences] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const response = await axios.post(`${process.env.REACT_APP_API_URL}/api/trip-assistant`, {
      destination,
      days: parseInt(days),
      budget: parseFloat(budget),
      preferences: preferences.split(',').map(p => p.trim())
    });
    setResult(response.data);
  };

  return (
    <div>
      <h2>Plan a Trip</h2>
      <input value={destination} onChange={e => setDestination(e.target.value)} placeholder="Destination" />
      <input type="number" value={days} onChange={e => setDays(e.target.value)} placeholder="Days" />
      <input type="number" value={budget} onChange={e => setBudget(e.target.value)} placeholder="Budget" />
      <input value={preferences} onChange={e => setPreferences(e.target.value)} placeholder="Preferences (comma-separated)" />
      <button onClick={handleSubmit}>Submit</button>

      {result && (
        <div>
          <h3>Trip Plan</h3>
          <p><strong>Flights:</strong> {result.flights.airline} - ${result.flights.price}</p>
          <p><strong>Hotel:</strong> {result.hotel.name} in {result.hotel.location}</p>
          <p><strong>Activities:</strong></p>
          <ul>{result.activities.map((item, index) => <li key={index}>{item}</li>)}</ul>
          <p><strong>Total Estimate:</strong> ${result.total_cost_estimate}</p>
        </div>
      )}
    </div>
  );
}

export default TripPlanner;