import React, { useState } from "react";

function App() {
  // Stores what the user types
  const [message, setMessage] = useState("");

  // Stores the AI response
  const [response, setResponse] = useState("");

  // Shows loading while waiting for API
  const [loading, setLoading] = useState(false);

  // Function to send message to backend
  const sendMessage = async () => {
    // Don't send empty messages
    if (!message.trim()) return;

    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
        }),
      });

      const data = await res.json();

      // Display full response
      setResponse(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error(error);
      setResponse("Error connecting to backend.");
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h1>🔍 Research Agent (Groq + LangGraph)</h1>

      <textarea
        rows="5"
        cols="70"
        placeholder="Ask something..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          width: "100%",
          padding: "10px",
          fontSize: "16px",
        }}
      />

      <br />
      <br />

      <button
        onClick={sendMessage}
        style={{
          padding: "10px 20px",
          cursor: "pointer",
        }}
      >
        Send
      </button>

      <br />
      <br />

      {loading && <h3>Thinking...</h3>}

      {!loading && response && (
        <>
          <h2>Response</h2>

          <pre
            style={{
              background: "#f4f4f4",
              padding: "15px",
              borderRadius: "8px",
              whiteSpace: "pre-wrap",
            }}
          >
            {response}
          </pre>
        </>
      )}
    </div>
  );
}

export default App;