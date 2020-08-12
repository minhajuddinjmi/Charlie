import pyttsx3
import datetime
import os
import speech_recognition as sr
from music import music
from music import movie
#from music import camera
import wikipedia as w
import webbrowser as web

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 0.5
        audio = r.listen(source)
    query = r.recognize_google(audio, language='en-in')
    print(query)
    return query

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour<=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Charli... Please tell me how can I help you, Minhaj")

wishme()
while True:
    '''try:
        query= take_command()
        query = query.lower()
    except Exception as e:
        pass
        query = ''
        '''

    query =input(">").lower()

    #query='dkljflaskjdlfaksjf'
#-------------------Shutdown computer-------------
    if 'shutdown' in query or 'shutdown options' in query:
        speak("Are you sure shutdown the computer? Please confirm yes or no")
        shut=input("options >").lower()
        if "yes" in shut:
            print("1. Shutdown the system\n2. Restart the system\n3. log off the system")
            speak("You have three options -")
            speak("First is shutdown the system.")
            speak("Secound is restart the system")
            speak("And thrid is log off the system")
            while True:
                speak("Please enter your choice, Minhaj")
                option = input("choice >")
                if "1"== option:
                    speak("I am shutting down the system.")
                    os.startfile("shut.bat")
                    quit()
                elif "2"==option:
                    speak("I am shutting down the system.")
                    os.startfile("retstart.bat")
                    quit()
                elif "3"==option:
                    speak("I am shutting down the system.")
                    os.startfile("logoff.bat")
                    quit()
                else:
                    speak("I don't understand, what are you saying?")
        elif "no" in shut:
            speak("Any task for me. I am waiting for you.")
#--------------------Music------------------------
    if 'music' in query:
        music.music()
#--------------------Time----------------------------
    if 'time' in query:
        time= datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'The time is {time}')
#------------------------Movie------------------------
    if 'movie' in query:
        movie.movie()
#------------------------Open Folder--------------------
    if 'folder' in query:
        speak("Please enter the folder name:")
        while True:
            folder = input("Folder name >").lower()
            try:
                if "quit"in folder:
                    speak("Ok Sir, I quit the folder. Any task for me Sir.")
                    break
                elif 'minhaj' in folder:
                    path = 'C:\\important files\\Minhaj Uddin'
                    os.startfile(path)
                    break
                elif 'misbah'in folder:
                    path = 'C:\\important files\\Misbah'
                    os.startfile(path)
                    break
                elif 'movie'in folder:
                    path = 'C:\\Movie'
                    os.startfile(path)
                    break
                else:
                    speak("Please enter the correct folder, Minhaj")
            except:
                speak("Please enter the correct folder, Minhaj")
#-------------------------Pycharm---------------------------
    if 'code' in query:
        speak("Sure Minhaj, I am opening the pycharm")
        path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.3\\bin\\pycharm64.exe"
        os.startfile(path)
#------------------------Wikipedia------------------------------------
    if 'wikipedia' in query:
        speak("Please enter the which you want to search.")
        while True:
            s = input("Wikipedia >").lower()
            try:
                if "quit" in s:
                    speak("Ok Minhaj, I quit the wikipediar. Any task for me Minhaj.")
                    break
                else:
                    print("Searching...")
                    speak("Searching in Wikipedia...")
                    result=w.summary(s,sentences=2)
                    print(result)
                    speak("According to wikipedia,")
                    speak(result)
                    break
            except:
                speak("Please check your internet connection, Minhaj")
#--------------------------youtube------------------------------------
    if 'youtube' in query:
        youtube='https://www.youtube.com/results?search_query='
        speak("Do you want to search on youtube?")
        while True:
            try:
                answer= input("Youtube >").lower()
                if 'yes'in answer:
                    speak("Enter your search query...")
                    s=input("searching... >").lower().replace(' ','+')
                    search=youtube+s
                    web.open_new_tab(search)
                    break
                elif 'no'in answer:
                    web.open_new_tab(youtube)
                    break
                elif 'quit'in answer:
                    speak("Okay Minhaj, I quit the youtube.")
                    break
                else:
                    speak("Please clear your answer")
            except Exception as e:
                speak("I don't understand, what you want to me?")
#---------------------Gooogle---------------------------
    if 'google' in query:
        web.open_new_tab('google.com')
# ---------------------Gooogle---------------------------
    if 'facebook' in query:
        web.open_new_tab('www.facebook.com')
#---------------------Command Prompt--------------------
    if 'cmd' in query or 'command prompt' in query:
        speak("Sure Minhaj,I am opening command prompt")
        os.startfile(r"C:\Windows\System32\cmd.exe")
        speak("Command prompt has oppend, you can use it.")
#--------------------Python-------------------------------
    if 'python' in query:
        speak("Sure Minhaj,I am opening Python")
        os.startfile(r"C:\Windows\System32\cmd.exe")
        speak("Python has oppend, you can use it.")
#------------------Open Camera--------------------------
    if 'camera' in query:
        speak("Sure Minhaj, I am opening the camera.")
        os.startfile("music\\Camera.py")
        speak("Camera has oppend, you can use it.")
#--------------------------Quit the program---------------------------
    if 'quit' in query or 'exit' in query:
        speak('Thank you Minhaj')
        quit()