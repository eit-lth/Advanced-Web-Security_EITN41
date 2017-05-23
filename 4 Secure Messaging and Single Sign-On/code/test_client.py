#!/usr/bin/python3

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
soc.connect(("eitn41.eit.lth.se", 1337))

# the p shall be the one given in the manual
p = int('1234567890abcdef', 16)
g = 2

##########################
#### D-H Key Exchange ####
##########################

## receive g**x1
# receive the hex-string, decode, and remove trailing '\n'
g_x1 = soc.recv(4096).decode('utf8').strip()
print ('g**x1:', g_x1)
# interpret as a number
g_x1 = int(g_x1, 16)

# generate g**x2, x2 shall be a random number
x2 = 0
# calculate g**x2 mod p
g_x2 = pow(g, x2, p)
# convert to hex-string
g_x2_str = format(g_x2, 'x')
# send it
soc.send(g_x2_str.encode('utf8'))
# read the ack/nak. This should yield a nak due to x2 being 0
print ('\nsent g_x2:', soc.recv(4096).decode('utf8').strip())
