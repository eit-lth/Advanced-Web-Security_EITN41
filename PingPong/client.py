#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Ping Pong client.

python client.py Ping asdf (some text)
python client.py PingPong 25 (a number)
"""

import socket
import sys


def Ping(a):
    """Play with Pong server."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("0.0.0.0", 6001))
    print("Ping:", a)
    client.sendall(a.encode('utf8'))
    a = client.recv(8192).decode('utf8')
    print(a)
    client.close()


def PingPong(a):
    """Play with PingPong server (demo of interaction play)."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("0.0.0.0", 6002))
    a = int(a)
    while a > 0:
        print("Ping:", a)
        client.sendall((format(a)).encode('utf8'))
        a = client.recv(8192).decode('utf8')
        print(a)
        a = int(a[6:]) - 1
    client.close()
    exit()


if __name__ == '__main__':
    if sys.argv[1] == 'Ping':
        Ping(sys.argv[2])
    if sys.argv[1] == 'PingPong':
        PingPong(sys.argv[2])
