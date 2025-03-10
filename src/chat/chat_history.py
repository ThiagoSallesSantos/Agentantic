from typing import List, Dict

class ChatHistory:

    def __init__(self):
        self.messages: List[Dict] = []

    def add_message(self, message: List[Dict]) -> None:
        self.messages += message

    @property
    def get_messages(self) -> List[Dict]:
        return self.messages
