from src.agent.agent import Agent

from src.connection.connection import (connection, ConnectionType)

from pydantic import Field

ID_DATABASE = 1

class DatabaseAgent(Agent):
    """
    Retrieves information within a database
    """

    query: str = Field(..., title='natural language query', description='natural language query, which will be used to describe what the user wants to get back from the database')

    def execute(self, *args, **kwargs):
        response = connection(connection_type=ConnectionType.POST, url=f"http://localhost:9876/generate/sql/{ID_DATABASE}/", **self.model_dump(), only_sql=False, **kwargs)
        return response.json()
