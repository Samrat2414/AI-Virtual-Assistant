import datetime
from automation import AutomationManager
from notes import NotesManager


class CommandManager:

    def __init__(self):
        self.automation = AutomationManager()
        self.notes = NotesManager()

    def execute(self, message):

        command = message.lower().strip()

        # =========================
        # AUTOMATION COMMANDS
        # =========================

        if "open chrome" in command:
            return self.automation.open_chrome()

        if "open youtube" in command:
            return self.automation.open_youtube()

        if "open notepad" in command:
            return self.automation.open_notepad()

        if "open calculator" in command:
            return self.automation.open_calculator()

        if "open file explorer" in command:
            return self.automation.open_file_explorer()

        # =========================
        # GOOGLE SEARCH
        # =========================

        if command.startswith("search google for "):

            query = command.replace(
                "search google for ",
                "",
                1
            ).strip()

            if query:
                return self.automation.google_search(query)

        # =========================
        # TIME
        # =========================

        if "what time" in command or "current time" in command:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            return f"The current time is {current_time}."

        # =========================
        # ADD NOTE
        # =========================

        if command.startswith("add note "):

            note = message[len("add note "):].strip()

            if note:
                return self.notes.add_note(note)

            return "Please tell me what note you want to save."

        # =========================
        # SHOW NOTES
        # =========================

        if command == "show notes" or command == "show my notes":

            return self.notes.get_notes()

        # =========================
        # CLEAR NOTES
        # =========================

        if command == "clear notes" or command == "delete notes":

            return self.notes.clear_notes()

        # =========================
        # NO COMMAND
        # =========================

        return None
