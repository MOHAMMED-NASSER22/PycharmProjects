import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")


def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as M:

        print("speak anything")

        audio = r.listen(M)

    data = r.recognize_google(audio)

    try:

        print("You said " + r.recognize_google(audio))

    except:

        print("sorry")

    return data


def jarvis(data):
    if "what time is it" in data:
        speak(ctime())


time.sleep(2)
speak("hopalala")
data = recordAudio()
jarvis(data)