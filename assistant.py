from ai_chat import AIChat
from commands import CommandManager


class Assistant:

    def __init__(self):
        self.ai = AIChat()
        self.commands = CommandManager()

    def process_message(self, message):

        # Check for computer commands
        command_response = self.commands.execute(message)

        if command_response:
            return command_response

        # Otherwise use AI chat
        return self.ai.get_response(message)
