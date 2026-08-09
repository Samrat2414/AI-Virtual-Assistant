import customtkinter as ctk

from assistant import Assistant
from speech import SpeechManager
from settings import SettingsManager


class AIAssistantGUI:

    def __init__(self):

        self.settings = SettingsManager()

        # Appearance
        ctk.set_appearance_mode(
            self.settings.get("appearance")
        )
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title(
            self.settings.get("assistant_name")
        )

        self.root.geometry("1100x700")
        self.root.resizable(False, False)

        self.assistant = Assistant()
        self.speech = SpeechManager()

        self.create_widgets()

    def create_widgets(self):

        # =========================
        # TITLE
        # =========================

        self.title_label = ctk.CTkLabel(
            self.root,
            text="🤖 AI Virtual Assistant",
            font=("Arial", 28, "bold")
        )

        self.title_label.pack(
            pady=25
        )

        # =========================
        # CHAT BOX
        # =========================

        self.chat_box = ctk.CTkTextbox(
            self.root,
            width=950,
            height=500,
            font=("Arial", 16)
        )

        self.chat_box.pack(
            pady=10
        )

        self.chat_box.insert(
            "end",
            "AI: Hello! I am your AI Virtual Assistant.\n"
            "AI: How can I help you today?\n\n"
        )

        # =========================
        # INPUT
        # =========================

        self.entry = ctk.CTkEntry(
            self.root,
            width=600,
            height=45,
            placeholder_text="Type your message..."
        )

        self.entry.pack(
            side="left",
            padx=(50, 10),
            pady=15
        )

        # =========================
        # SEND
        # =========================

        self.send_button = ctk.CTkButton(
            self.root,
            text="SEND",
            width=120,
            height=45,
            command=self.send_message
        )

        self.send_button.pack(
            side="left",
            padx=5,
            pady=15
        )

        # =========================
        # VOICE
        # =========================

        self.voice_button = ctk.CTkButton(
            self.root,
            text="🎤 VOICE",
            width=120,
            height=45,
            command=self.voice_message
        )

        self.voice_button.pack(
            side="left",
            padx=5,
            pady=15
        )

        # Enter key
        self.entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    # =========================
    # SEND MESSAGE
    # =========================

    def send_message(self):

        message = self.entry.get().strip()

        if not message:
            return

        self.chat_box.insert(
            "end",
            f"You: {message}\n"
        )

        response = self.assistant.process_message(
            message
        )

        self.chat_box.insert(
            "end",
            f"AI: {response}\n\n"
        )

        if self.settings.get("voice_enabled"):
            self.speech.speak(response)

        self.entry.delete(
            0,
            "end"
        )

        self.chat_box.see(
            "end"
        )

    # =========================
    # VOICE MESSAGE
    # =========================

    def voice_message(self):

        self.chat_box.insert(
            "end",
            "System: Listening... 🎤\n"
        )

        self.root.update()

        message = self.speech.listen()

        if message:

            self.chat_box.insert(
                "end",
                f"You: {message}\n"
            )

            response = self.assistant.process_message(
                message
            )

            self.chat_box.insert(
                "end",
                f"AI: {response}\n\n"
            )

            if self.settings.get("voice_enabled"):
                self.speech.speak(response)

        else:

            self.chat_box.insert(
                "end",
                "System: Sorry, I couldn't understand you.\n\n"
            )

        self.chat_box.see(
            "end"
        )

    # =========================
    # RUN
    # =========================

    def run(self):

        self.root.mainloop()
