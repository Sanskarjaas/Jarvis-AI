import webbrowser
import speech_recognition as sr
import os
import pyttsx3
import datetime

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error Occured From Jarvis Sorry  I Failed This time :"



if __name__ == '__main__':
    while True:
        print("Listening.....")
        query=takeCommand()
        sites=[
            ["youtube","https://youtube.com"],
            ["wikipedia","https://wikipedia.com"],
            ["google","https://google.com"],
            ["facebook","https://facebook.com"],
            ["instagram","https://instagram.com"],
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir ......")
                webbrowser.open(site[1])

            if "open music" in query:
                musicPath="/Users"
                os.system(f"open{musicPath}")


            if "the time" in query:
                strfTime=datetime.datetime.now().strftime("%H:%M:%S")
                say(f"sir the time is{strfTime}")


            if "open facetime".lower() in query.lower():
                os.system(f"/Users/ACER/AppData/Local/Microsoft/WindowsApps/Skype.exe")

