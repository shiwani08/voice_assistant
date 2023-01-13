import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#to change the voice of assitant
engine.setProperty('voice', voices[1].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()   

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("suprabhat")
    elif hour>=12 and hour<=16:
        speak("good afternoon")
    
    elif hour>=16 and hour<=22:
        speak("good evening")
    
    else: 
        speak("shubh ratri")

    speak("hello im friday, how can i help you")

def takeCommand():
    #takes mic input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please repeat that again...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #for tasks
        if 'wikipedia' in query:
            speak('just a min sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Wiki's words not mine")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open neal.fun' in query:
            webbrowser.open("neal.fun")

        elif 'search it on stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    