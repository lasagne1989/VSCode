#!/usr/bin/env python

import socket

def getIP():
    hostname = socket.gethostname()
    hnlocal = f"{hostname}.local"
    IPAddr = socket.gethostbyname(hnlocal)
    return IPAddr
    
if __name__ == "__main__":
    getIP()