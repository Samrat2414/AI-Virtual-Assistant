```python
import customtkinter as ctk
from assistant import Assistant


# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AIAssistantGUI:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title("AI Virtual Assistant")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)

        # Assistant controller
        self.assistant = Assistant()

        self.create_widgets()

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

        # Input box
        self.entry = ctk.CTkEntry(
            self.root,
            width=800,
            height=45,
            placeholder_text="Type your message..."
        )

        self.entry.pack(
            side="left",
            padx=(70, 10),
            pady=15
        )

        # Send button
        self.send_button = ctk.CTkButton(
            self.root,
            text="SEND",
            width=120,
            height=45,
            command=self.send_message
        )

        self.send_button.pack(
            side="left",
            pady=15
        )

        # Enter key
        self.entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    def send_message(self):

        message = self.entry.get().strip()

        if message == "":
            return

        # Show user message
        self.chat_box.insert(
            "end",
            f"You: {message}\n"
        )

        # Send to Assistant
        response = self.assistant.process_message(
            message
        )

        # Show AI response
        self.chat_box.insert(
            "end",
            f"AI: {response}\n\n"
        )

        # Clear input
        self.entry.delete(
            0,
            "end"
        )

        # Scroll down
        self.chat_box.see(
            "end"
        )

    def run(self):

        self.root.mainloop()
```
