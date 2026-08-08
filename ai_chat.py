class AIChat:

    def __init__(self):
        self.name = "AI Virtual Assistant"

    def get_response(self, message):

        message = message.lower().strip()

        if "hello" in message or "hi" in message:
            return "Hello Guru! How can I help you?"

        elif "your name" in message:
            return "I am your AI Virtual Assistant."

        elif "python" in message:
            return "Python is a powerful programming language."

        elif "github" in message:
            return "GitHub is useful for storing and sharing your projects."

        elif "thank" in message:
            return "You're welcome, Guru!"

        elif "bye" in message:
            return "Goodbye Guru! See you again."

        else:
            return "I received your message. I am ready to learn more."
