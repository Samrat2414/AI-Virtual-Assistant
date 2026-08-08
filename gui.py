import customtkinter as ctk


class AIAssistantGUI:

    def __init__(self):
        # Main window
        self.root = ctk.CTk()
        self.root.title("AI Virtual Assistant")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)

        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_widgets()

    def create_widgets(self):

        # ==============================
        # TITLE
        # ==============================

        title = ctk.CTkLabel(
            self.root,
            text="🤖 AI Virtual Assistant",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(20, 5))

        # ==============================
        # STATUS
        # ==============================

        self.status_label = ctk.CTkLabel(
            self.root,
            text="🟢 Status: Ready",
            font=("Arial", 15)
        )
        self.status_label.pack(pady=5)

        # ==============================
        # CHAT BOX
        # ==============================

        self.chat_box = ctk.CTkTextbox(
            self.root,
            width=950,
            height=450,
            font=("Arial", 16),
            corner_radius=15
        )
        self.chat_box.pack(pady=15)

        self.chat_box.insert(
            "end",
            "🤖 AI Assistant: Hello! How can I help you today?\n\n"
        )

        # ==============================
        # INPUT FRAME
        # ==============================

        input_frame = ctk.CTkFrame(
            self.root,
            corner_radius=15
        )
        input_frame.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # ==============================
        # MESSAGE INPUT
        # ==============================

        self.message_entry = ctk.CTkEntry(
            input_frame,
            width=700,
            height=45,
            placeholder_text="Type your message...",
            font=("Arial", 15)
        )
        self.message_entry.pack(
            side="left",
            padx=15,
            pady=12
        )

        # ==============================
        # SEND BUTTON
        # ==============================

        send_button = ctk.CTkButton(
            input_frame,
            text="Send",
            width=90,
            height=45,
            command=self.send_message
        )
        send_button.pack(
            side="left",
            padx=5
        )

        # ==============================
        # MICROPHONE BUTTON
        # ==============================

        mic_button = ctk.CTkButton(
            input_frame,
            text="🎤",
            width=60,
            height=45,
            command=self.microphone_clicked
        )
        mic_button.pack(
            side="left",
            padx=5
        )

        # Press ENTER to send
        self.message_entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    # ==============================
    # SEND MESSAGE
    # ==============================

    def send_message(self):

        message = self.message_entry.get().strip()

        if message:

            self.chat_box.insert(
                "end",
                f"👤 You: {message}\n"
            )

            self.chat_box.insert(
                "end",
                "🤖 Assistant: I received your message. AI features coming soon!\n\n"
            )

            self.message_entry.delete(0, "end")

            self.chat_box.see("end")

    # ==============================
    # MICROPHONE
    # ==============================

    def microphone_clicked(self):

        self.status_label.configure(
            text="🎤 Status: Listening..."
        )

        self.chat_box.insert(
            "end",
            "🎤 Assistant: Voice recognition will be added in Step 4.\n\n"
        )

        self.chat_box.see("end")

    # ==============================
    # RUN APPLICATION
    # ==============================

    def run(self):
        self.root.mainloop()
