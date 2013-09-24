                            ## code_reaper ##
   
import urllib.request
from tkinter import *
from tkinter import filedialog
from re import *
import os
def rateme(name):
    response = urllib.request.urlopen('http://www.omdbapi.com/?t=%s'%(name))#fetch rating
    html = str(response.read())
    x=compile('"imdbRating":"(.*?)",')
    y=x.search(html)
    return(y.group(1))
root = Tk()
root.title("Flick-Sort beta")
f=Frame(root,width=600,height=400)
f.pack()
global l
l=Text(f,wrap=WORD)
def add(y):
        l.insert(INSERT,y)
        z=rateme(y)
        l.insert(INSERT,' ==> ')
        l.insert(INSERT,z)
        l.insert(INSERT,'\n')
        l.pack()

dirname =filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
if len(dirname ) > 0:
    print("You chose %s"% dirname) 
dirList=os.listdir(dirname)
for fname in dirList:
    a=fname.split(".")
    if a[-1] in ['mkv','wmv','mp4','avi']:
        x=a[0]
        if '[' in fname:
            x=fname.split("[")
            add(x[0])
        elif '(' in fname:
            x=fname.split("(")
            add(x[0])
        else:
            add(x)
    else:
        l.insert(INSERT,'Refine your Movie directory ')#if unhandled case <file - name> found  
        l.insert(INSERT,'\n')
        
        
root.mainloop()


    
