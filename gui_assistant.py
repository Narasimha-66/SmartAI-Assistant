import tkinter as tk
from tkinter import scrolledtext
import threading
from core import speak, listen
import datetime
from utils import parse_time_input
from reminder_manager import add_reminder
from reminder_manager import check_reminders  

threading.Thread(target=check_reminders, daemon=True).start()

# Placeholder for processing commands 
def process_command(command):
    response_box.insert(tk.END, f"You: {command}\n")

    if 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {now}"
        speak(response)

    elif 'joke' in command:
        import pyjokes
        joke = pyjokes.get_joke()
        speak(joke)
        response = joke
        
    elif 'who is' in command or 'tell me about' in command:
        import wikipedia
        topic = command.replace('who is', '').replace('tell me about', '').strip()
        if topic:
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia...")
                speak(summary)
                response = summary
            except wikipedia.exceptions.DisambiguationError as e:
                response = "That topic is too broad. Please be more specific."
                speak(response)
            except wikipedia.exceptions.PageError:
                response = "Sorry, I couldn’t find anything on that topic."
                speak(response)
            except:
                response = "Something went wrong while searching Wikipedia."
                speak(response)
        else:
            response = "Please say the topic you want me to search."
            speak(response)


    elif 'weather' in command and 'in' in command:
        from weather import get_weather
        words = command.split()
        city = None
        for i in range(len(words)):
            if words[i] == 'in' and i + 1 < len(words):
                city = " ".join(words[i + 1:])
                break
        if city:
            response = get_weather(city)
            speak(response)
        else:
            response = "Please mention a city after saying weather."
    
    elif 'set alarm' in command:
        speak("Please say the time like 12 41 or 18 30 or 12:41.")
        time_input = listen()
        from alarm_features import set_alarm
        
        alarm_time = parse_time_input(time_input)
        if alarm_time:
            set_alarm(alarm_time)
        else:
            speak("Sorry, I couldn't understand the time.")

    elif 'set timer' in command:
        speak("How many seconds should I set the timer for?")
        seconds = listen()
        from alarm_features import set_timer
        try:
            set_timer(int(seconds))
        except:
            speak("Sorry, I couldn't understand the timer duration.")

    elif 'remind me to' in command:
        from reminder_manager import add_reminder
       
        if 'at' in command:
            parts = command.rsplit('at', 1)
            task = parts[0].replace('remind me to', '').strip()
            time_input = parts[1].strip()
            time_str = parse_time_input(time_input)
            if time_str:
                add_reminder(task, time_str)
                speak(f"Reminder set to {task} at {time_str}")
            else:
                speak("Sorry, I couldn’t understand the time.")
        else:
            speak("Please specify time like 'remind me to drink water at 14 30'")


    elif 'exit' in command or 'stop' in command:
        speak("Goodbye Simha!")
        app.quit()
        return
    
    else:
      
        response = f"I heard you say: {command}"
        speak(response)
        response_box.insert(tk.END, f"Assistant: {response}\n\n")

# Background listener

def start_listening():
    def listen_loop():
        speak("I'm listening, Simha...")
        command = listen()
        if command:
            process_command(command)
    threading.Thread(target=listen_loop).start()


# GUI setup
app = tk.Tk()
app.title("Smart Assistant - Spark")
app.geometry("500x400")

response_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=15)
response_box.pack(padx=10, pady=10)

listen_button = tk.Button(app, text="🎤 Start Listening", command=start_listening)
listen_button.pack(pady=5)

exit_button = tk.Button(app, text="⛔ Exit", command=app.destroy)
exit_button.pack(pady=5)

app.mainloop()
