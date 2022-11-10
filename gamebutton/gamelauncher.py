#!/usr/bin/env python

#files
from modes.standard import Standard
from modes.nameless import Nameless
from data import Config

def main():
    if Config.mode == "standard":
        app = Standard()
    if Config.mode == "nameless":
        app = Nameless()
    #if Config.mode == "chess":
    #    app = Chess(Config.time_limit, Config.players)
    app.mainloop()

if __name__ == "__main__":
    main()

