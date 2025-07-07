from core import speak, listen
import datetime
import time
import pygame

# Play alarm and listen for "stop alarm"
def play_alarm_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play(-1)  # Loop the sound

    speak("Alarm is ringing. Say 'stop alarm' to stop it.")

    start_time = time.time()
    timeout = 30  # auto-stop after 30 seconds

    while True:
        command = listen().lower()
        print("You said:", command)

        if 'stop alarm' in command:
            pygame.mixer.music.stop()
            speak("Alarm stopped.")
            break

        if time.time() - start_time > timeout:
            pygame.mixer.music.stop()
            speak("Alarm stopped automatically after 30 seconds.")
            break

# Manual stop (via assistant or fallback)
def stop_alarm_sound():
    pygame.mixer.music.stop()
    speak("Alarm stopped.")

# Set an alarm at a specific time (HH:MM)
def set_alarm(alarm_time):
    speak(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            play_alarm_sound()
            break
        time.sleep(10)

#  Set a countdown timer
def set_timer(seconds):
    try:
        seconds = int(seconds)
        speak(f"Timer set for {seconds} seconds.")
        time.sleep(seconds)
        play_alarm_sound()
    except:
        speak("Sorry, I couldn't set the timer.")
