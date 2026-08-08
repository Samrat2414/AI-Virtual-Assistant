import subprocess
import datetime
import webbrowser


class CommandManager:

    def execute(self, message):

        command = message.lower().strip()

        # Open Chrome
        if "open chrome" in command:
            webbrowser.open("https://www.google.com")
            return "Opening Chrome."

        # Open YouTube
        if "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube."

        # Open Notepad
        if "open notepad" in command:
            subprocess.Popen("notepad.exe")
            return "Opening Notepad."

        # Open Calculator
        if "open calculator" in command:
            subprocess.Popen("calc.exe")
            return "Opening Calculator."

        # Open File Explorer
        if "open file explorer" in command:
            subprocess.Popen("explorer.exe")
            return "Opening File Explorer."

        # Current time
        if "what time" in command or "current time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."

        # No command found
        return None
