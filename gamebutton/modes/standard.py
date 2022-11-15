#!/usr/bin/env python

#libraries
import itertools
from tkinter import *
from tools.firstplayer import firstPlayer
import RPi.GPIO as GPIO
from tools.fullscreen import fullscreen
from tools.press import Button
from data import Data

#from GameButton import sounds

root = Tk()

class Standard:
    def __init__(self, master):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        if fullscreen == False:
            root.geometry("320x240")
        else:
            root.attributes('-fullscreen', True)
        root['bg']='grey9'
        self.time_limit = Data.Config.time_limit

        #Create UI
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 24), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor=S)
        self.display2 = Label(master, fg='white', bg='grey9', font=("Ariel", 35))
        self.display2.place(relx=.5, rely=.5, anchor=N)
       
        # Press count variable
        self.press_count = 0
        
        # Pick first player and set up cycle
        self.setup()
    
    def setup(self):
        self.display1['text'] = 'Press the button to choose first player'
        # Set up main button press
        reg_event = Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
        reg_event.setup()
        reg_event.event()
        # Pick first player and set up cycle
        self.next_players = itertools.cycle(firstPlayer.player_cycle)    
    
    def start(self, channel):
        # Show randomised First player on first press
        if self.press_count == 0:
            self.player = next(self.next_players)
            self.display1['text'] = self.player + ", You Go First!"
            self.press_count += 1
        elif self.press_count == 1:
            # Start the countdown for first player
            self.timer_text = DoubleVar()
            self.timer_text.set(self.time_limit + 1)
            self.display1['text'] = self.player
            self.display2['textvariable'] = self.timer_text
            self.increment_timer()
            self.press_count += 1
        # Restart the countdown and get the next player
        else:
            self.player = next(self.next_players)
            self.timer_text = DoubleVar()
            self.timer_text.set(self.time_limit)
            self.display1['text'] = self.player
            self.display2['textvariable'] = self.timer_text
            self.press_count += 1

    def increment_timer(self):
        self.ctr = int(self.timer_text.get())
        # countdown -1 second every second until we hit zero
        if self.ctr > 0:
            self.timer_text.set(self.ctr - 1)
            self.master.update()
            self.master.after(1000, self.increment_timer)
        # on zero give shit to the loser
        else:
            self.display1['text'] = self.player + ', You Dumb Bitch!'
            root.update()
            self.press_count = 1
            #sounds.gimmeSomeBanter()
            # wait for the button to be pressed again
            wait_event = Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
            wait_event.wait()
            # sends us back to the middle condition on start and progresses us to the next player
            #Move these above wait?
            self.player = next(self.next_players)
            self.press_count = 1

if __name__ == "__main__":
        Standard()