#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""DH kex client."""

import os
import socket
import binascii


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


def send_int(num):
    """Send integer, 'num' is decimal number."""
    num_str = format(num, 'x').encode('utf8')
    client.sendall(num_str)


def recv_int():
    """Receive and convert it to integer."""
    num_str = client.recv(8192).decode('utf8')
    return int(num_str, 16)


if __name__ == '__main__':
    """python client.py"""
    p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff', 16)
    # the generator of the group (Z/pZ)*
    g = 2
    # connect
    host = "0.0.0.0"
    host = "igor.eit.lth.se"
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 6004))
    # Add your own code for DH kex
