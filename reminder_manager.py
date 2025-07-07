import json
import datetime
import time
from core import speak

REMINDER_FILE = "reminders.json"

def load_reminders():
    try:
        with open(REMINDER_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_reminders(reminders):
    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file)

def add_reminder(task, time_str):
    reminders = load_reminders()
    reminders.append({"task": task, "time": time_str})
    save_reminders(reminders)
    speak(f"Reminder added for {task} at {time_str}")

def check_reminders():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        reminders = load_reminders()
        updated_reminders = []

        for reminder in reminders:
            if reminder["time"] == now:
                speak(f"Reminder: {reminder['task']}")
            else:
                updated_reminders.append(reminder)

        save_reminders(updated_reminders)
        time.sleep(60)
