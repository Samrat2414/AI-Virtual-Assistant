import os


class NotesManager:

    def __init__(self):

        self.file_name = "notes.txt"

    def add_note(self, note):

        with open(
            self.file_name,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(note + "\n")

        return "Note saved successfully."

    def get_notes(self):

        if not os.path.exists(self.file_name):
            return "You don't have any notes yet."

        with open(
            self.file_name,
            "r",
            encoding="utf-8"
        ) as file:

            notes = file.read().strip()

        if not notes:
            return "You don't have any notes yet."

        return "Your notes:\n" + notes

    def clear_notes(self):

        if os.path.exists(self.file_name):

            open(
                self.file_name,
                "w",
                encoding="utf-8"
            ).close()

        return "All notes have been cleared."