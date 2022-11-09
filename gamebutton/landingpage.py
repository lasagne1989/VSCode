#libraries
from tkinter import *

root = Tk()

class landingPage:
    def __init__(self, master, time_limit: int = 5, players: list = ["Gordon","Claire","Izzie"]):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        #root.geometry("320x240")
        root.attributes('-fullscreen', True)
        root['bg']='grey9'
        
        #Create UI
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 24), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor=S)
        
        self.display1['text'] = 'Awaiting Phone Connection'