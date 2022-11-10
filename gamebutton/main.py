#!/usr/bin/env python

#files
from modes.standard import Standard
from modes.nameless import Nameless
from landingpage import landingPage
from IPandWebsockets.opensocket import connected
from data import Config

fullscreen = False

def main():
    while connected == True:
        landingpage.quit
        if Config.mode == "standard":
            app = Standard()
        if Config.mode == "nameless":
            app = Nameless()
        #if Config.mode == "chess":
        #    app = Chess(Config.time_limit, Config.players)
        app.mainloop()

if __name__ == "__main__":
    landingpage = landingPage()
    landingpage.mainloop()
    main()

