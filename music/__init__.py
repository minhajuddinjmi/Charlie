import pyttsx3
import os

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''print(os.getcwd())
os.chdir('c:\\Movie')
print(os.getcwd())


f=nt.scandir('c:\\Movie')
for i in f:
    print(i)
#Folder Create
try:
    f=os.makedirs('C:\\Minhaj')
except:
    print('minhaj')

#os.renames('c:\\Minhaj','c:\\Misbah')

fi=os.walk('c:\\Movie')
for i in fi:
    for j in i:
        print(j)
'''#remove folder
#os.removedirs('c:\\Minhaj')