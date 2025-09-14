import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);

  const askQuestion = async () => {
    setAnswer("Thinking... 🧠");
    const resp = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });
    const data = await resp.json();
    setAnswer(data.answer);
    setSources(data.sources);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>🤖 Minimal RAG Chatbot</h1>
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask me anything..."
        rows="4"
        cols="50"
      />
      <br />
      <button onClick={askQuestion}>Ask</button>
      <div style={{ marginTop: "2rem" }}>
        <h3>🧠 Answer:</h3>
        <p>{answer}</p>
        <h3>📄 Sources:</h3>
        <p>{sources.join(", ")}</p>
      </div>
    </div>
  );
}

export default App;
