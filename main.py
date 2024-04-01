import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from conv import random_text
from random import choice

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

USER = config('USER')
HOSTNAME = config('BOT')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Доброе утро {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Добрый день {USER}")
    elif (hour > 16) and (hour < 22):
        speak(f"Добрый вечер {USER}")
    else:
        speak(f"Доброй ночи {USER}")
    speak(f"Я {HOSTNAME}. Чем я могу вам помочь?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Распознаю...")
        queri = r.recognize_google(audio, language='ru')
        print(queri)
        if not 'стоп' in queri or 'выйти' in queri:
            speak(choice(random_text))
        else:
            speak("Удачного дня")
            exit()
    except Exception:
        speak("Извините, Я не понимаю. Можете повторить пожалуйста запрос")
        queri = 'None'
    return queri


if __name__ == '__main__':
    greet_me()
    while True:
        queri = take_command().lower()
        if 'как ты' in queri or 'как дела' in queri:
            speak('Я в порядке, Сэр. Как у вас дела?')
