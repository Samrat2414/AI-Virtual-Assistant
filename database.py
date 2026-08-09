import sqlite3


class DatabaseManager:

    def __init__(self, database_name="assistant.db"):

        self.database_name = database_name

        self.connection = sqlite3.connect(
            self.database_name
        )

        self.create_tables()

    # =========================
    # CREATE TABLES
    # =========================

    def create_tables(self):

        cursor = self.connection.cursor()

        # Notes table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                note TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Chat history table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Reminders table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                seconds INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

    # =========================
    # SAVE NOTE
    # =========================

    def save_note(self, note):

        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO notes (note) VALUES (?)",
            (note,)
        )

        self.connection.commit()

    # =========================
    # GET NOTES
    # =========================

    def get_notes(self):

        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT note, created_at FROM notes ORDER BY id DESC"
        )

        return cursor.fetchall()

    # =========================
    # SAVE CHAT
    # =========================

    def save_chat(self, user_message, ai_response):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO chat_history
            (user_message, ai_response)
            VALUES (?, ?)
            """,
            (
                user_message,
                ai_response
            )
        )

        self.connection.commit()

    # =========================
    # GET CHAT HISTORY
    # =========================

    def get_chat_history(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT user_message, ai_response, created_at
            FROM chat_history
            ORDER BY id ASC
            """
        )

        return cursor.fetchall()

    # =========================
    # CLOSE DATABASE
    # =========================

    def close(self):

        self.connection.close()
```
