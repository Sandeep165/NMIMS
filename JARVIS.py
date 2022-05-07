from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hr = int(datetime.datetime.now().hour)

    if hr>=0 and hr<=12:
        speak("Good morning")
    elif hr >=12 and hr<=18:
        speak("Good Afternoon ")
    else:
        speak("Good evening")

    speak("Hello Sir I am you personal assistant Please tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :- {query}\n")

    except Exception as e:
        # print(e)
        print("Please can you repeat the part agin.....")
        return None
    return query


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()


        if "wikipedia" in query:
            speak("Searching in wikipedia.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to the wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play the song" in query:
            m_dir  = "D:\\Songs"
            songs = os.listdir(m_dir)
            print(songs)
            os.startfile(os.path.join(m_dir,songs[1]))

        elif "the time" in query:
            mytime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(mytime)

        elif "open code" in query:
            loc = "C:\\Users\\sande\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(loc)

