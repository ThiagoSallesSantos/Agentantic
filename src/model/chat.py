import ollama
from ollama import ChatResponse, Options

from typing import List, Dict, Optional

def chat(message: List[Dict], prompt: List[Dict], chat_history: List[Dict], tools: Optional[List[Dict]] = None) -> ChatResponse:
    
    messages = prompt + chat_history + message

    return ollama.chat(
        model='llama3.2',
        messages=messages,
        tools=tools,
        options=Options(
            temperature=0.0,
            num_ctx=8192,
        ),
        keep_alive=0,
    )
