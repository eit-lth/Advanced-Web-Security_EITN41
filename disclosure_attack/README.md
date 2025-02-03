# Implementation Details

The attack consists of two steps:

1. Learning phase: Loop until we have m disjoint sets (m is #comm. partners)
2. Excluding phase: Loop until the cardinality of each set is 1

The first several lines of the example file is

```
timestamp	eth src			eth dst			IP src		IP dst
1738540301		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	30.161.201.161	148.4.53.119
1738540309		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	44.247.155.107	148.4.53.119
1738540313		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	144.113.26.248	148.4.53.119
1738540314		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	249.113.158.97	148.4.53.119
1738540316		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	191.19.244.108	148.4.53.119
1738540322		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	232.115.219.123	148.4.53.119
1738540331		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	147.9.13.37	148.4.53.119
1738540337		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	105.224.98.224	148.4.53.119
1738540345		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	50.146.147.252	148.4.53.119
1738540351		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	159.134.46.222	148.4.53.119
1738540361		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	54.253.25.176	148.4.53.119
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	214.205.125.36
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	84.20.64.244
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	249.113.158.97
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	50.146.147.252
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	128.130.233.68
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	30.161.201.161
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	144.113.26.248
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	179.118.109.85
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	170.93.35.117
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	207.49.243.90
1738541496		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	198.109.205.23
1738541505		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	159.134.46.222	148.4.53.119
1738541508		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	54.69.153.94	148.4.53.119
1738541514		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	165.232.151.148	148.4.53.119
1738541517		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	128.130.233.68	148.4.53.119
1738541519		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	63.175.71.37	148.4.53.119
1738541524		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	147.9.13.37	148.4.53.119
1738541534		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	30.161.201.161	148.4.53.119
1738541540		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	197.221.252.62	148.4.53.119
1738541544		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	128.130.233.68	148.4.53.119
1738541545		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	214.205.125.36	148.4.53.119
1738541547		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	29.247.199.198	148.4.53.119
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	123.198.89.84
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	249.113.158.97
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	129.237.115.88
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	84.20.64.244
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	211.15.90.66
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	207.49.243.90
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	249.113.158.97
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	111.249.107.115
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	139.150.90.138
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	105.224.98.224
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	148.4.53.119	249.113.158.97
1738542696		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	54.253.25.176	148.4.53.119
1738542699		e4:70:b8:21:01:97	ff:ff:ff:ff:ff:ff	128.130.233.68	148.4.53.119
```

It's clear that the batch size is 11.

Nazir's IP is in the 1st batch (timestamp `1738540331`), this implies that Nazir sends data in the next batch, thus implies that one of his partners' IP is in 2nd batch, so collect the IP in 2nd batch.

Similarly, Nazir's IP is also in the 3rd batch (timestamp `1738541524`), so Nazir also sends data in the next batch, thus implies that one of his partners' IP is in 4th batch, so collect the IP in 4th batch.

Loop the above procedure. B.c. Nazir sends many times, it's likely that he send data to the same partner in the subsequent batch so should skip them to guarantee that the newly added sets has no overlap with the previous ones.

When you get a learning set of length 3, you are at the 2376 entry of the file (the file has 2992 entries in total), and your learning set is
```
[{'128.130.233.68', '214.205.125.36', '50.146.147.252', '84.20.64.244', '30.161.201.161', '144.113.26.248', '249.113.158.97', '179.118.109.85', '207.49.243.90', '198.109.205.23', '170.93.35.117'}, {'25.114.43.252', '82.63.21.68', '211.15.90.66', '151.123.22.177', '50.161.192.73', '42.9.134.126', '139.185.94.206', '43.126.173.119', '221.191.193.178', '197.252.247.28', '155.91.98.108'}, {'186.67.230.202', '17.168.150.84', '118.221.112.199', '217.188.215.79', '58.249.106.62', '159.9.176.51', '211.72.168.208', '167.134.233.134', '211.45.200.46', '44.247.155.107', '120.178.76.130'}]
```
That's finish the 1st stage.

There are 3 subsets in the learning set, each of length 11 (cardinality 11). Proceed to read the file (from 2377 to 2992) and utilize the rest information to reduce the size of each subset. Finally you shall get
```
[{'84.20.64.244'}, {'42.9.134.126'}, {'211.72.168.208'}]
```
And the rest is to sum the IP.
