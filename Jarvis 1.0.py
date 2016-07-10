from Tkinter import *
import os
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 150)

master = Tk()

e = Entry(master, width=50)
e.pack()

e.focus_set()

def callback(event=None):
    print e.get()
    r = e.get()
    if (r == ""):
        engine.say("You have to type something you idiot.")
        engine.runAndWait()
        e.delete(0, 'end')
    elif (r == "open chrome"):
        os.system("start chrome.exe")
        engine.say("Opened Chrome Master Colby")
        engine.runAndWait()
        e.delete(0, 'end')
    elif (r == "close chrome"):
        os.system("TASKKILL /F /IM chrome.exe")
        engine.say("Closed Chrome Master Colby")
        engine.runAndWait()
        e.delete(0, 'end')
    elif (r == "open itunes"):
        os.system("start itunes.exe")
        engine.say("Opened iTunes Master Colby")
        engine.runAndWait()
        e.delete(0, 'end')       
    elif (r == "close itunes"):
        os.system("TASKKILL /F /IM itunes.exe")
        engine.say("Closed iTunes Master Colby")
        engine.runAndWait()
        e.delete(0, 'end')
    elif (r == "go to sleep"):
        engine.say("Goodnight Colby.  Sweet dreams.")
        engine.runAndWait()
        os.system("rundll32.exe PowrProf.dll,SetSuspendState")
        e.delete(0, 'end')
    elif (r == "lock"):
        engine.say("Locking your computer.")
        engine.runAndWait()
        os.system("Rundll32.exe User32.dll,LockWorkStation")
        e.delete(0, 'end')
    else:
        engine.say("I don't understand you.")
        engine.runAndWait()
        e.delete(0, 'end')

master.bind('<Return>', callback)
master.title("Jarvis 1.0")
master.geometry("250x25")

mainloop()
text = e.get()

