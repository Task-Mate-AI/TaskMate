import React, { useState } from 'react';
import axios from 'axios';

function EmailHelper() {
  const [emailThread, setEmailThread] = useState('');
  const [intent, setIntent] = useState('confirm');
  const [tone, setTone] = useState('friendly');
  const [summary, setSummary] = useState('');
  const [reply, setReply] = useState('');

  const handleSubmit = async () => {
    const response = await axios.post('/api/email-helper', {
      email_thread: emailThread,
      reply_intent: intent,
      reply_tone: tone
    });
    setSummary(response.data.summary);
    setReply(response.data.reply);
  };

  return (
    <div>
      <h2>Summarize an Email Thread</h2>
      <textarea value={emailThread} onChange={e => setEmailThread(e.target.value)} placeholder="Paste email thread here" />
      <select value={intent} onChange={e => setIntent(e.target.value)}>
        <option value="confirm">Confirm</option>
        <option value="decline">Decline</option>
        <option value="reschedule">Reschedule</option>
      </select>
      <select value={tone} onChange={e => setTone(e.target.value)}>
        <option value="friendly">Friendly</option>
        <option value="formal">Formal</option>
        <option value="neutral">Neutral</option>
      </select>
      <button onClick={handleSubmit}>Submit</button>

      {summary && <div><h3>Summary</h3><p>{summary}</p></div>}
      {reply && <div><h3>Reply Draft</h3><p>{reply}</p></div>}
    </div>
  );
}

export default EmailHelper;