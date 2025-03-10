from abc import ABC, abstractmethod

from pydantic import BaseModel

from typing import Any

class Agent(ABC, BaseModel):

    @classmethod
    def model_json_schema(cls, *args, **kwargs):
        json_schema = super().model_json_schema(*args, **kwargs)

        return {
            "type": "function",
            "function": {
                "name": cls.__name__,
                "description": json_schema["description"],
                "parameters": {
                    "type": json_schema["type"],
                    "required": json_schema["required"],
                    "properties": json_schema["properties"]
                }
            }
        }

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass

    def __call__(self, *args, **kwargs) -> Any:
        return self.execute(*args, **kwargs)
