import datetime
import re

from automation import AutomationManager
from notes import NotesManager
from reminder import ReminderManager
from weather import WeatherManager


class CommandManager:

    def __init__(self):

        self.automation = AutomationManager()
        self.notes = NotesManager()
        self.reminders = ReminderManager()
        self.weather = WeatherManager()

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

            query = message[
                len("search google for "):
            ].strip()

            if query:
                return self.automation.google_search(query)

            return "Please tell me what you want to search."

        # =========================
        # TIME
        # =========================

        if (
            "what time" in command
            or "current time" in command
        ):

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            return f"The current time is {current_time}."

        # =========================
        # WEATHER
        # =========================

        if command.startswith("weather in "):

            city = message[
                len("weather in "):
            ].strip()

            if city:
                return self.weather.get_weather(city)

            return "Please tell me the city name."

        # =========================
        # ADD NOTE
        # =========================

        if command.startswith("add note "):

            note = message[
                len("add note "):
            ].strip()

            if note:
                return self.notes.add_note(note)

            return "Please tell me what note you want to save."

        # =========================
        # SHOW NOTES
        # =========================

        if command in [
            "show notes",
            "show my notes"
        ]:

            return self.notes.get_notes()

        # =========================
        # CLEAR NOTES
        # =========================

        if command in [
            "clear notes",
            "delete notes"
        ]:

            return self.notes.clear_notes()

        # =========================
        # ADD REMINDER
        # =========================

        reminder_match = re.search(
            r"remind me in (\d+)\s*"
            r"(second|seconds|minute|minutes)\s*(.*)",
            command
        )

        if reminder_match:

            amount = int(
                reminder_match.group(1)
            )

            unit = reminder_match.group(2)

            reminder_message = (
                reminder_match.group(3).strip()
            )

            if not reminder_message:
                reminder_message = "Your reminder."

            if "minute" in unit:
                seconds = amount * 60
            else:
                seconds = amount

            return self.reminders.add_reminder(
                reminder_message,
                seconds
            )

        # =========================
        # SHOW REMINDERS
        # =========================

        if command in [
            "show reminders",
            "show my reminders"
        ]:

            return self.reminders.get_reminders()

        # =========================
        # NO COMMAND FOUND
        # =========================

        return None