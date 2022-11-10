#!/usr/bin/env python

import websockets
import asyncio
from myIP import IPAddr

msg = ""
connected = False

def sockSVR(self):
    async def handler(websocket):
        msg = await websocket.recv()
        connected = True
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    start_server= websockets.serve(handler, "%s"%IPAddr, 8765)
    loop.run_until_complete(start_server)
    loop.run_forever()