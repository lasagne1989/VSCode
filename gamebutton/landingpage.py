#libraries
from tkinter import *
from main import fullscreen

root = Tk()

class landingPage:
    def __init__(self, master, time_limit: int = 5, players: list = ["Gordon","Claire","Izzie"]):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        if fullscreen == False:
            root.geometry("320x240")
        else:
            root.attributes('-fullscreen', True)
        root['bg']='grey9'
        
        #Create UI
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 24), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor=S)
        
        self.display1['text'] = 'Awaiting Phone Connection'