import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text: str):
    print("talk")
    engine.say(text)
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()


def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as src:
        listener.adjust_for_ambient_noise(src, duration=1)
        pc = listener.listen(src)

    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("No entiendo lo que me dices")
    except sr.RequestError as e:
        print(f"Could not request resutls from Google speech rec: {e} ")
    return rec
