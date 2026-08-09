import hashlib
import sqlite3


class LoginManager:

    def __init__(self, database_name="assistant.db"):

        self.database_name = database_name

        self.connection = sqlite3.connect(
            self.database_name
        )

        self.create_table()

    # =========================
    # CREATE USERS TABLE
    # =========================

    def create_table(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        self.connection.commit()

    # =========================
    # PASSWORD HASH
    # =========================

    def hash_password(self, password):

        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    # =========================
    # REGISTER
    # =========================

    def register(self, username, password):

        username = username.strip()

        if not username or not password:
            return False, "Username and password are required."

        password_hash = self.hash_password(
            password
        )

        try:

            cursor = self.connection.cursor()

            cursor.execute(
                """
                INSERT INTO users
                (username, password)
                VALUES (?, ?)
                """,
                (
                    username,
                    password_hash
                )
            )

            self.connection.commit()

            return True, "Registration successful."

        except sqlite3.IntegrityError:

            return False, "Username already exists."

    # =========================
    # LOGIN
    # =========================

    def login(self, username, password):

        password_hash = self.hash_password(
            password
        )

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE username = ?
            AND password = ?
            """,
            (
                username.strip(),
                password_hash
            )
        )

        user = cursor.fetchone()

        if user:
            return True, "Login successful."

        return False, "Invalid username or password."

    # =========================
    # CLOSE
    # =========================

    def close(self):

        self.connection.close()