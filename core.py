import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass  # run loop already started



def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition.")
            return ""
