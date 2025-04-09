import pyttsx3
import speech_recognition as sr
import webbrowser
import os

# https://medium.com/analytics-vidhya/a-guide-to-your-own-a-i-voice-assistant-using-python-17f79c94704

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
            except Exception as e:
                print("Nothing said.")
                continue
            return query

def speak(words):
    engine.say(words)
    engine.runAndWait()

# Returns all chars in the haystack that appear after
# the needle substring.
def cut_off_at(needle, haystack):
    needle_len = len(needle)
    needle_loc = haystack.find(needle)
    return haystack[needle_loc + needle_len + 1:]

if __name__=="__main__" :
    while True:
        query = takeCommand().lower()
        print(f"User said: {query}\n")  #User query will be printed.

        if "computer" not in query:
            continue
        
        # User has issued a command.

        if "repeat" in query:
            speak(cut_off_at("repeat", query))

        if "open youtube" in query:
            webbrowser.open("https://youtube.com")

        if "open twitter" in query:
            webbrowser.open("https://twitter.com/eskayOW")

        if "open github" in query:
            webbrowser.open("https://github.com")

        if "play animal collective" in query:
            codePath = "D:\music\Animal Collective\Meeting Of The Waters\\02 - Animal Collective - Man Of Oil.mp3"
            os.startfile(codePath)
