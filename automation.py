import subprocess
import webbrowser
from urllib.parse import quote_plus


class AutomationManager:

    def open_chrome(self):
        webbrowser.open("https://www.google.com")
        return "Opening Google in your browser."

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    def open_notepad(self):
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    def open_calculator(self):
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    def open_file_explorer(self):
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer."

    def google_search(self, query):
        search_url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        webbrowser.open(search_url)

        return f"Searching Google for {query}."