import threading
import time


class ReminderManager:

    def __init__(self):
        self.reminders = []

    def add_reminder(self, message, seconds):

        reminder = {
            "message": message,
            "seconds": seconds
        }

        self.reminders.append(reminder)

        thread = threading.Thread(
            target=self._wait_and_notify,
            args=(reminder,),
            daemon=True
        )

        thread.start()

        return f"Reminder set for {seconds} seconds."

    def _wait_and_notify(self, reminder):

        time.sleep(reminder["seconds"])

        print(
            f"\n🔔 REMINDER: {reminder['message']}\n"
        )

        self.reminders.remove(reminder)

    def get_reminders(self):

        if not self.reminders:
            return "You don't have any active reminders."

        result = "Active reminders:\n"

        for index, reminder in enumerate(
            self.reminders,
            start=1
        ):
            result += (
                f"{index}. "
                f"{reminder['message']} "
                f"({reminder['seconds']} seconds)\n"
            )

        return result
