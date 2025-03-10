from src.agent.agent import Agent
from src.agent.agents import *

from ollama import Message

from typing import List, Dict, Any

def get_agents(list_agents: List[Agent]) -> List[Dict]:
    return [agent.model_json_schema() for agent in list_agents]

def execute_tools_calls(list_tools_calls: List[Message.ToolCall]) -> List[Any]:
    list_result_tools_calls: List[Any] = []

    for tool_call in list_tools_calls:
        agent: Agent = eval(tool_call.function.name)(**tool_call.function.arguments)
        list_result_tools_calls.append(agent())

    return list_result_tools_calls