from fastapi import APIRouter, HTTPException

from src.routes.schemas.input import ChatInput

from src.chat import (ChatHistory, formatter_content)

from src.model.chat import chat

from src.agent import (get_agents, execute_tools_calls)
from src.agent.agents import DatabaseAgent

from src.prompt.prompt import get_prompt_agent, get_prompt_chat

from ollama import ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def chat_llm(
    input: ChatInput
):
    try:
        message = formatter_content(input.query, role="user")

        prompt_agent = get_prompt_agent()
        prompt_agent = formatter_content(prompt_agent, role="system")

        chat_history = ChatHistory()

        response = chat(
            message=message,
            prompt=prompt_agent,
            chat_history=chat_history.get_messages,
            tools=get_agents(list_agents=[DatabaseAgent])
        )

        list_response_tool_calls = execute_tools_calls(list_tools_calls=response.message.tool_calls)
        list_tools = formatter_content(list_response_tool_calls, role="tool")

        message += list_tools

        prompt_chat = get_prompt_chat()
        prompt_chat = formatter_content(prompt_chat, role="system")

        response = chat(
            message=message,
            prompt=prompt_chat,
            chat_history=chat_history.get_messages,
        )

        return response

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
