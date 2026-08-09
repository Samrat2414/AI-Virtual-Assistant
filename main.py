from login_gui import LoginGUI
from gui import AIAssistantGUI


def start_assistant():

    app = AIAssistantGUI()
    app.run()


def main():

    login = LoginGUI(
        on_success=start_assistant
    )

    login.run()


if __name__ == "__main__":
    main()