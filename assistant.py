from ai_chat import AIChat


class Assistant:

    def __init__(self):
        self.ai = AIChat()

    def process_message(self, message):
        return self.ai.get_response(message)
