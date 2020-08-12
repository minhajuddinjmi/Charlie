yotube='https://www.youtube.com/results?search_query='

input=input().lower().replace(" ","+")

s=yotube+input
print(s)


l=["a.mp3","c.mp3","d.mp3","b.mp3","2","3","4"]
a=[]
b=[]

for i in l:
    if i.endswith(".mp3"):
        b.append(i)
    else:
        a.append(i)
a=sorted(a)
print(a)
b=sorted(b)
print(b)