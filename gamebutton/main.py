#!/usr/bin/env python

#libraries
import json
from dataclasses import dataclass
#files
from modes.standard import Standard
from modes.nameless import Nameless
from landingpage import landingPage
from IPandWebsockets.opensocket import msg, connected

if msg != "next":
    dict = json.loads(msg)

@dataclass
class Config:
    mode: str = dict['mode']
    time_limit: int = dict['time_limit']
    players: list = dict['players']
    dob: list = dict['dob']

def main():
    
    while connected == True:
        landingpage.quit
        if Config.mode == "standard":
            app = Standard(Config.time_limit, Config.players)
        if Config.mode == "nameless":
            app = Nameless(Config.time_limit, Config.players)
        #if Config.mode == "chess":
        #    app = Chess(Config.time_limit, Config.players)
        app.mainloop()

if __name__ == "__main__":
    landingpage = landingPage()
    landingpage.mainloop()
    main()

