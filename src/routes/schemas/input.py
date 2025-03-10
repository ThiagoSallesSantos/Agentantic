## Description: Input schemas for the API
from pydantic import BaseModel, Field

class ChatInput(BaseModel):
    query: str = Field(description="User message", alias="message")
