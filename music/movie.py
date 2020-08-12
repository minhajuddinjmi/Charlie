import pyttsx3
import os
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def movie():
    #speak("Ok sir, I play the movie. Please select the movie")
    data = os.walk("C:\\Movie\\")
    path= list()
    file= list()
    folder= list()
    for i in data:
        i = list(i)
        path.append(i[0])
        folder.append(i[1])
        file.append(i[2])
    for i in range(len(path)):
        print(path[i],":")
        x=1
        for j in file[i]:
            print(x, "-", j)
            x += 1
        print()
    p = [i.lower() for i in path]
    while True:
        speak("Please enter folder and movie name.")
        n = input("Movie >")
        try:
            if (n in "quit") or (n in 'exit'):
                speak("Ok Sir, I quit the music. Any task for me Sir.")
                break
            else:
                dir, m = str(), str()
                l = n.split(" ")
                print(l)
                for i in range(len(p)):
                    if l[0] in p[i]:
                        dir = path[i]
                        break
                for i in range(1,len(l)):
                    m+=" "+l[i]
                m= m.strip()


                print(dir)
                print(m)
                os.startfile(os.path.join(dir, m))
        except Exception as e:
            print(e)
            speak("Please enter the correct movie, Sir")
#movie()

'''def movie():
    try:
        speak("Sure Sir! I play the movie.")
        dir= 'C:\\Movie\\'
        movie=os.listdir(dir)
        a=list()
        b=list()
        for i in movie:
            if i.endswith(".mp4") or i.endswith(".mkv"):
                a.append(i)
            else:
                b.append(i)
        dirlist=list()
        c=list()
        for i in b:
            x=dir+i
            dirlist.append(x)
            s=os.listdir(x)
            for j in s:
                if j.endswith(".mp4") or i.endswith(".mkv"):
                    a.append(j)
                else:
                    c.append(j)
        j=1
        for i in a:
            print(j,"-",i)
            j+=1
        speak("Please Enter the movie")
        while True:
            n=input("Movie >").lower()
            try:
                if n=="quit":
                    speak("Ok Sir, I quit the movie. Any task for me Sir.")
                    break
                else:
                    n=int(n)-1
                    l=a[n].split(".mp4")
                    for i in l:
                        print(i)
                    speak(l)
                    if n>=0 and n<=13:
                        os.startfile(os.path.join(dir, a[n]))
                    if n>13 and n<=22:
                        os.startfile(os.path.join(dirlist[0], a[n]))
                    if n>22 and n<=74:
                        os.startfile(os.path.join(dirlist[1], a[n]))
                    if n>74:
                        os.startfile(os.path.join(dirlist[2], a[n]))
            except:
                speak("Please enter the correct movie, Sir")
    except:
        speak("Please enter the correct movie, Sir")'''