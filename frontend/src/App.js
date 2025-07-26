import React from 'react';
import EmailHelper from './components/EmailHelper';
import TripPlanner from './components/TripPlanner';

function App() {
  return (
    <div>
      <h1>TaskMate Assistant</h1>
      <EmailHelper />
      <TripPlanner />
    </div>
  );
}

export default App;