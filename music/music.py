import pyttsx3
import os

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def music():
    try:
        speak("Sure Sir! I play the music.")
        dir= 'C:\\Users\\shamaila saeed\\Music\\mp3\\'
        songs=os.listdir(dir)
        a=list()
        b=list()
        for i in songs:
            if i.endswith(".mp3"):
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
                if j.endswith(".mp3"):
                    a.append(j)
                else:
                    c.append(j)
        j=1
        for i in a:
            print(j,"-",i)
            j+=1
        speak("Please Enter the song")
        while True:
            n=input("Music >").lower()
            try:
                if (n in "quit") or (n in'exit'):
                    speak("Ok Sir, I quit the music. Any task for me Sir.")
                    break
                else:
                    n=int(n)-1
                    l=a[n].split(".mp3")
                    for i in l:
                        print(i)
                    speak(l)
                    if n>=0 and n<=13:
                        os.startfile(os.path.join(dir, a[n]))
                        print(dirlist[0])
                        print(a[n])
                    if n>13 and n<=22:
                        os.startfile(os.path.join(dirlist[0], a[n]))

                    if n>22 and n<=74:
                        os.startfile(os.path.join(dirlist[1], a[n]))
                    if n>74:
                        os.startfile(os.path.join(dirlist[2], a[n]))
            except:
                speak("Please enter the correct song, Sir")
    except:
        print("xyz")
#music()