#!/usr/bin/env python3

#open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    dnslist = dnsfile.readlines()
    for svr in dnslist:
        print(svr, end="")
# no need to close file will be closed automatically      
