#!/usr/bin/env python

import os
import websockets
import asyncio
from tkinter import *
from tools.myIP import IPAddr

fullscreen = False

root = Tk()


class landingPage:
    def __init__(self, master):
        self.master = master
        # Set up screen
        root.config(cursor="none")
        if fullscreen == False:
            root.geometry("320x240")
        else:
            root.attributes('-fullscreen', True)
        root['bg']='grey9'
        self.display1 = Label(master, fg='white', bg='grey9', font=("Ariel", 30), wraplength=318)
        self.display1.place(relx=.5, rely=.5, anchor=S)
        self.display1['text'] = 'Awaiting Phone Connection'
        # Start Websocket
        self.msg = ""
        self.sockSVR()

    def sockSVR(self):
        async def handler(websocket):
            self.msg = await websocket.recv()
            start = f"start"
            await websocket.send(start)
            os.startfile("main.py")
            app.quit()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        start_server= websockets.serve(handler, "%s"%IPAddr, 8765)
        loop.run_until_complete(start_server)
        loop.run_forever()

if __name__ == "__main__":
    app = landingPage()
    app.mainloop()