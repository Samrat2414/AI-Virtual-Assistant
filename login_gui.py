import customtkinter as ctk
from login import LoginManager


class LoginGUI:

    def __init__(self, on_success):

        self.on_success = on_success
        self.login_manager = LoginManager()

        self.root = ctk.CTk()
        self.root.title("AI Virtual Assistant - Login")
        self.root.geometry("450x500")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self.root,
            text="🤖 AI Virtual Assistant",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(40, 10))

        subtitle = ctk.CTkLabel(
            self.root,
            text="Login or create a new account",
            font=("Arial", 14)
        )
        subtitle.pack(pady=5)

        self.username_entry = ctk.CTkEntry(
            self.root,
            width=300,
            height=45,
            placeholder_text="Username"
        )
        self.username_entry.pack(pady=(35, 10))

        self.password_entry = ctk.CTkEntry(
            self.root,
            width=300,
            height=45,
            placeholder_text="Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(
            self.root,
            text="LOGIN",
            width=300,
            height=45,
            command=self.login
        )
        self.login_button.pack(pady=(25, 10))

        self.register_button = ctk.CTkButton(
            self.root,
            text="REGISTER",
            width=300,
            height=45,
            command=self.register
        )
        self.register_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.root,
            text="",
            font=("Arial", 13)
        )
        self.status_label.pack(pady=20)

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        success, message = self.login_manager.login(
            username,
            password
        )

        self.status_label.configure(
            text=message
        )

        if success:

            self.login_manager.close()
            self.root.destroy()

            self.on_success()

    def register(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        success, message = self.login_manager.register(
            username,
            password
        )

        self.status_label.configure(
            text=message
        )

    def run(self):

        self.root.mainloop()