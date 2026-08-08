import customtkinter as ctk
from ai_chat import AIChat

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AIAssistantGUI:

    def __init__(self):
        self.root = ctk.CTk()
        self.ai = AIChat()

        self.root.title("AI Virtual Assistant")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        self.title_label = ctk.CTkLabel(
            self.root,
            text="AI Virtual Assistant",
            font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=25)

        self.chat_box = ctk.CTkTextbox(
            self.root,
            width=950,
            height=500,
            font=("Arial", 16)
        )
        self.chat_box.pack(pady=10)

        self.chat_box.insert(
            "end",
            "AI: Hello! I am your AI Virtual Assistant.\n\n"
        )

        self.entry = ctk.CTkEntry(
            self.root,
            width=800,
            height=45,
            placeholder_text="Type your message..."
        )
        self.entry.pack(side="left", padx=(70, 10), pady=15)

        self.send_button = ctk.CTkButton(
            self.root,
            text="SEND",
            width=120,
            height=45,
            command=self.send_message
        )
        self.send_button.pack(side="left", pady=15)

        self.entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    def send_message(self):

        message = self.entry.get().strip()

        if message == "":
            return

        self.chat_box.insert(
            "end",
            f"You: {message}\n"
        )

        response = self.ai.get_response(message)

        self.chat_box.insert(
            "end",
            f"AI: {response}\n\n"
        )

        self.entry.delete(0, "end")
        self.chat_box.see("end")

    def get_response(self, message):

        message = message.lower()

        if "hello" in message or "hi" in message:
            return "Hello Guru! How can I help you?"

        if "python" in message:
            return "Python is a powerful programming language."

        if "name" in message:
            return "I am your AI Virtual Assistant."

        if "bye" in message:
            return "Goodbye Guru!"

        return "I received your message. More AI features can be added later."

    def run(self):
        self.root.mainloop()
