import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import random
from pathlib import Path

# https://medium.com/analytics-vidhya/a-guide-to-your-own-a-i-voice-assistant-using-python-17f79c94704

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice

# Listen for voice activity. Return spoken words as a string.
def take_command():
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
                print("Nothing said. Trying again.")
                continue

            return query

# The text-to-speech speaks some words.
def speak(words):
    engine.say(words)
    engine.runAndWait()

# Returns all chars in the haystack that appear after
# the needle substring.
def cut_off_at(needle, haystack):
    needle_len = len(needle)
    needle_loc = haystack.find(needle)
    return haystack[needle_loc + needle_len + 1:]

# Plays a random song by an artist.
def play_artist(artist):
    music_dir = Path("D:\music")
    artist_dir = music_dir / artist

    # Compile list of albums.
    albums = [x for x in artist_dir.iterdir()]
    
    # Compile list of songs.
    songs = []
    for album in albums:
        for f in album.iterdir():
            if str(f).endswith(".mp3"):
                songs.append(f)
    
    # Select a random song.
    choice = random.choice(songs)

    # Play the song.
    os.startfile(choice)


if __name__=="__main__" :
    while True:
        query = take_command().lower()
        print(f"User said: {query}\n")  #User query will be printed.

        if "computer" not in query:
            continue
        
        # User has issued a command.

        if "repeat" in query:
            speak(cut_off_at("repeat", query))

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open twitter" in query:
            webbrowser.open("https://twitter.com/eskayOW")

        elif "open github" in query:
            webbrowser.open("https://github.com")

        elif "play" in query:
            play_artist(cut_off_at("play", query))
