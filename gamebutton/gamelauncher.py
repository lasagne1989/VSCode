#!/usr/bin/env python

#files
import modes.standard
import modes.nameless
from data import Config

def Launch():
    if Config.mode == "standard":
        app = modes.standard.Standard()
    if Config.mode == "nameless":
        app = modes.nameless.Nameless()
    #if Config.mode == "chess":
    #    app = Chess(Config.time_limit, Config.players)
    app.mainloop()

if __name__ == "__main__":
    Launch()

