from ai_chat import AIChat
from commands import CommandManager
from database import DatabaseManager


class Assistant:

    def __init__(self):

        self.ai = AIChat()
        self.commands = CommandManager()
        self.database = DatabaseManager()

    def process_message(self, message):

        # Check computer commands
        command_response = self.commands.execute(message)

        if command_response:
            response = command_response

        else:
            # Normal AI response
            response = self.ai.get_response(message)

        # Save conversation
        self.database.save_chat(
            message,
            response
        )

        return response
