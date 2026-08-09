import json
import os


class SettingsManager:

    def __init__(self):

        self.file_name = "settings.json"

        self.default_settings = {
            "assistant_name": "AI Virtual Assistant",
            "voice_enabled": True,
            "appearance": "dark"
        }

        self.settings = self.load_settings()

    def load_settings(self):

        if not os.path.exists(self.file_name):

            self.save_settings(
                self.default_settings
            )

            return self.default_settings.copy()

        try:

            with open(
                self.file_name,
                "r",
                encoding="utf-8"
            ) as file:

                settings = json.load(file)

            return {
                **self.default_settings,
                **settings
            }

        except (json.JSONDecodeError, OSError):

            return self.default_settings.copy()

    def save_settings(self, settings=None):

        if settings is not None:
            self.settings = settings

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.settings,
                file,
                indent=4
            )

    def get(self, key):

        return self.settings.get(key)

    def set(self, key, value):

        self.settings[key] = value

        self.save_settings()

        return f"{key} updated successfully."

    def get_all(self):

        return self.settings.copy()

    def reset(self):

        self.settings = self.default_settings.copy()

        self.save_settings()

        return "Settings reset successfully."
