#!/usr/bin/python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect('www.py4inf.xom', 80)
