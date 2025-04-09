import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice

def speak(words):
    engine.say(words)
    engine.runAndWait()

if __name__=="__main__" :
    speak('2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? 2? ')
