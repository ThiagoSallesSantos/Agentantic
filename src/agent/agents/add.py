from src.agent.agent import Agent

from pydantic import Field, PositiveInt

class AddTwoNumbers(Agent):
    """
    Add two numbers
    """

    a: PositiveInt = Field(..., title='First number')
    b: PositiveInt = Field(..., title='Second number')

    def execute(self, *args, **kwargs):
        return self.a - self.b
