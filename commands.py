import datetime
from automation import AutomationManager


class CommandManager:

    def __init__(self):
        self.automation = AutomationManager()

    def execute(self, message):

        command = message.lower().strip()

        # Open Chrome / Google
        if "open chrome" in command:
            return self.automation.open_chrome()

        # Open YouTube
        if "open youtube" in command:
            return self.automation.open_youtube()

        # Open Notepad
        if "open notepad" in command:
            return self.automation.open_notepad()

        # Open Calculator
        if "open calculator" in command:
            return self.automation.open_calculator()

        # Open File Explorer
        if "open file explorer" in command:
            return self.automation.open_file_explorer()

        # Google search
        if command.startswith("search google for "):

            query = command.replace(
                "search google for ",
                "",
                1
            ).strip()

            if query:
                return self.automation.google_search(query)

        # Current time
        if "what time" in command or "current time" in command:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            return f"The current time is {current_time}."

        # No command found
        return None
