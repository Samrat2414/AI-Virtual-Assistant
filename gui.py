```python
import customtkinter as ctk
from assistant import Assistant
from speech import SpeechManager


# =========================
# APPEARANCE
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AIAssistantGUI:

    def __init__(self):

        # Main window
        self.root = ctk.CTk()

        self.root.title("AI Virtual Assistant")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)

        # Assistant
        self.assistant = Assistant()

        # Speech system
        self.speech = SpeechManager()

        # Create GUI
        self.create_widgets()

    # =========================
    # CREATE GUI
    # =========================

    def create_widgets(self):

        # Title
        self.title_label = ctk.CTkLabel(
            self.root,
            text="🤖 AI Virtual Assistant",
            font=("Arial", 28, "bold")
        )

        self.title_label.pack(
            pady=25
        )

        # Chat box
        self.chat_box = ctk.CTkTextbox(
            self.root,
            width=950,
            height=500,
            font=("Arial", 16)
        )

        self.chat_box.pack(
            pady=10
        )

        # Welcome message
        self.chat_box.insert(
            "end",
            "AI: Hello! I am your AI Virtual Assistant.\n"
            "AI: How can I help you today?\n\n"
        )

        # =========================
        # INPUT BOX
        # =========================

        self.entry = ctk.CTkEntry(
            self.root,
            width=620,
            height=45,
            placeholder_text="Type your message..."
        )

        self.entry.pack(
            side="left",
            padx=(50, 10),
            pady=15
        )

        # =========================
        # SEND BUTTON
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
        # VOICE BUTTON
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

        if message == "":
            return

        # Show user message
        self.chat_box.insert(
            "end",
            f"You: {message}\n"
        )

        # Get AI response
        response = self.assistant.process_message(
            message
        )

        # Show AI response
        self.chat_box.insert(
            "end",
            f"AI: {response}\n\n"
        )

        # Speak AI response
        self.speech.speak(
            response
        )

        # Clear input
        self.entry.delete(
            0,
            "end"
        )

        # Scroll to bottom
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

        # Listen
        message = self.speech.listen()

        if message:

            # Show recognized message
            self.chat_box.insert(
                "end",
                f"You: {message}\n"
            )

            # Get response
            response = self.assistant.process_message(
                message
            )

            # Show response
            self.chat_box.insert(
                "end",
                f"AI: {response}\n\n"
            )

            # Speak response
            self.speech.speak(
                response
            )

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
```
