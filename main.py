import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice

def takeCommand():
    #It takes microphone input from the user and returns string output    
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")  #User query will be printed.
            except Exception as e:
                print("Nothing said.")
                continue
            return query

def speak(words):
    engine.say(words)
    engine.runAndWait()

if __name__=="__main__" :
    while True:
        query = takeCommand().lower()
        speak(query)
