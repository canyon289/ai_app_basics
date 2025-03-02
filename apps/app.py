import gradio as gr
import ollama
import sqlite3
import datetime

# SQLite Database Setup
DB_PATH = "chat_log.db"

def setup_database():
    """Create a simple SQLite table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

setup_database()  # Ensure the DB is set up before running the app

def chat_with_model(prompt):
    """Send user input to Ollama, get response, and log to SQLite."""
    response = ollama.chat(model="gemma2:2b", messages=[{"role": "user", "content": prompt}])["message"]["content"]
    
    # Log the interaction to SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (prompt, response) VALUES (?, ?)", (prompt, response))
    conn.commit()
    conn.close()

    return response

# Gradio UI
iface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Chat with Gemma",
    description="Enter a message and get a response from the Gemma2 2B model. Your chats are logged in SQLite.",
)

iface.launch()