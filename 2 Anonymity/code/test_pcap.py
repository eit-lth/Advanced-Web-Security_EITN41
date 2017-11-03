#!/usr/bin/python3

from scapy.all import *

pkts = rdpcap('test.pcap')

print ('timestamp\tEth src\t\t\tEth dst\t\t\tIP src\t\tIP dst')
for pkt in pkts:
    print ('{}\t\t{}\t{}\t{}\t{}'.format(pkt.time, pkt.getlayer(Ether).src, pkt.getlayer(Ether).dst, 
        pkt.getlayer(IP).src, pkt.getlayer(IP).dst))
