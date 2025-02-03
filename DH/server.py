#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""DH kex server."""

import os
from socketserver import BaseRequestHandler, ThreadingTCPServer
import binascii


SECRET_MSG = b"I love you!"


def generate_random(N, bits=1536):
    """Generate a random number with bits=1536, then mod N."""
    byte = bits // 8
    rnd_num = os.urandom(byte)
    # ensure the number of bits is as high as 'bits'
    while rnd_num[0] < 128:
        rnd_num = os.urandom(byte)

    # convert from ascii to hex to a decimal integer
    rnd_num = int(''.join(format(i, 'x') for i in rnd_num), 16)
    return rnd_num % N


class DH_Alice(BaseRequestHandler):
    """Alice the DH server."""

    def send_int(self, num):
        """Send integer, 'num' is decimal number."""
        num_str = format(num, 'x').encode('utf8')
        self.request.sendall(num_str)

    def recv_int(self):
        """Receive and convert it to integer."""
        num_str = self.request.recv(8192).decode('utf8')
        return int(num_str, 16)

    def handle(self):
        """DH Alice handler."""
        p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff', 16)
        # the generator of the group (Z/pZ)*
        g = 2
        # shared secret
        self.shared = 'eitn41 <3'.encode('utf-8')

        # generate random exponent x1
        x1 = generate_random(p)
        # calc g^x1 & send (A -> B)
        g_x1 = pow(g, x1, p)
        self.send_int(g_x1)
        # receive g^x2
        g_x2 = self.recv_int()
        # Calc Alice's key (do not share)
        key = pow(g_x2, x1, p)
        # Encrypt the message
        m = binascii.hexlify(SECRET_MSG)
        m = int(m, 16)
        enc = m ^ key
        self.send_int(enc)


if __name__ == '__main__':
    try:
        dh = ThreadingTCPServer(("0.0.0.0", 6004), DH_Alice)
        print("Serving on 0.0.0.0 port 6004 ...")
        dh.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, exiting.")
        dh.socket.close()
