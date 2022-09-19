import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from datetime import date
import subprocess
import psutil
import pyjokes
import pyautogui
from tkinter import filedialog

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!, sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!, sir")   

    else:
        speak("Good Evening!, sir")  

    speak("I am Jarvis . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def joke():
    joke = pyjokes.get_joke('en', category= 'neutral')
    print(joke)
    speak(f"Ok, heres a joke {joke}")

def hi():
    print("Hello")
    speak("Hello")
    
def fine():
    print("I'am fine, what about you?")
    speak("I'am fine, what about you?")

def screenshot():
    
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension= '.png')
    myScreenshot.save(file_path)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'a joke' in query:
            joke() 
            
        elif 'hello' in query:
            print("Hello")
            speak("Hello")
            
        elif 'how are you' in query:
            fine()

        elif 'open youtube' in query:
                webbrowser.register('chrome', None)
                webbrowser.open("https://youtube.com")

        elif 'open google' in query:
                webbrowser.register('chrome', None)
                webbrowser.open ("https://google.com")

        elif 'open stackoverflow' in query:
                webbrowser.register('chrome', None)
                webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "G:\\Vedant Folder do not open\Vs code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'open weather' in query:
            print("Ok opening weather app")
            speak("Ok, opening weather app")
            codePath = "G:\\Projects\\Coding\\Python\\Folder files\\Macc-soft app\\weather.py"
            os.startfile(codePath)
            
        elif 'open system manager' in query:
            print("Ok, opening system manager app")
            speak("Ok, opening system manager app")
            codePath = "G:\\Projects\\Coding\\Python\\Folder files\\Macc-soft app\\mac-soft.py"
            os.startfile(codePath)
            
        elif 'screenshot' in query:
            screenshot()
            
            
        elif 'date' in query:
            today = date.today()
            current_date = today.strftime("%B %d %Y")
            print("Todays date is :- ", current_date)
            speak("today's date is") 
            speak(current_date)
            
        elif 'file explorer' in query:
            print ("Ok, opening file explorer")
            speak("Ok, opening file explorer")
            subprocess.Popen(r'explorer /select, "C:\path\of\folder\file"')
            
        elif 'battery' in query:
            def convertTime(seconds):
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                return "%d:%02d:%02d" % (hours, minutes, seconds)
            
            Battery = psutil.sensors_battery()
            percent = Battery.percent
            time = convertTime(Battery.secsleft)
            print("percent = ",percent,"time = ",time)
            speak(f"sir, you have {percent} percent battery and {time} time is left")
            
            
       

       
