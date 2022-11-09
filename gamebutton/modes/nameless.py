#!/usr/bin/env python

#libraries
import random
from tkinter import *
#import RPi.GPIO as GPIO

from tools.press import Button
from main import fullscreen

#from GameButton import sounds

root = Tk()

class Nameless:
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
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 35), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor=S)
       
        # Press count variable
        self.press_count = 0
        
        # Pick first player and set up cycle
        self.setup()
    
    def setup(self):
        # Set up main button press
        reg_event = Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
        reg_event.setup()
        reg_event.event()
        # Pick first player and set up cycle
        player_count = len(self.players)
        player_num = random.randint(0, player_count - 1)
        self.display1['text'] = self.players[player_num] + ", You Go First!"
    
    def start(self, channel):
        # Show randomised First player on first press
        if self.press_count == 0:
            # Start the countdown for first player
            self.timer_text = DoubleVar()
            self.timer_text.set(self.time_limit + 1)
            self.display1['textvariable'] = self.timer_text
            self.increment_timer()
            self.press_count += 1
        # Restart the countdown and get the next player
        else:
            self.timer_text = DoubleVar()
            self.timer_text.set(self.time_limit)
            self.display1['textvariable'] = self.timer_text
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
            self.display1['text'] = 'You Dumb Bitch!'
            root.update()
            self.press_count = 0
            #sounds.gimmeSomeBanter()
            # wait for the button to be pressed again
            wait_event = Button(GPIO.IN, GPIO.PUD_DOWN, GPIO.FALLING, self.start)
            wait_event.wait()
