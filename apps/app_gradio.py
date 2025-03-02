import gradio as gr
import ollama

model = 'gemma2:2b'

def chat_with_model(prompt):
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

iface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Chat with Gemma",
    description="Enter a message and get a response from the Gemma2 2B model.",
)

iface.launch()
