#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Ping Pong server: python server.py."""

from socketserver import ThreadingTCPServer, BaseRequestHandler
import threading


class Pong(BaseRequestHandler):
    """Play with Ping client."""

    def handle(self):
        """Pong handler."""
        while True:
            s = self.request.recv(8192).decode('utf8')
            if not s:
                print("Client disconnected")
                break
            self.request.sendall(('Pong: '+s).encode('utf8'))


class PingPong(BaseRequestHandler):
    """Ping Pong server."""

    def handle(self):
        """Ping Pong handler."""
        while True:
            a = self.request.recv(8192).decode('utf8')
            if not a:
                print("Client disconnected")
                break
            a = int(a) - 1
            self.request.sendall(('Pong: '+format(a)).encode('utf8'))


if __name__ == '__main__':
    try:
        # Use thread to let multiple port run.
        pong = ThreadingTCPServer(("0.0.0.0", 6001), Pong)
        print("Serving on 0.0.0.0 port 6001 ...")
        pingpong = ThreadingTCPServer(("0.0.0.0", 6002), PingPong)
        print("Serving on 0.0.0.0 port 6002 ...")
        t1 = threading.Thread(target=pong.serve_forever, daemon=True)
        t2 = threading.Thread(target=pingpong.serve_forever, daemon=True)
        # start threads
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, exiting.")
        pong.socket.close()
        pingpong.socket.close()
