import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as M:
    print("speak anything")
    audio = r.listen(M)

    try:
        print("You said " + r.recognize_google(audio))
    except:
        print("sorry")