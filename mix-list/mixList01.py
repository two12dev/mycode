#!/usr/bin/env python3

# List containing 3 items
my_list = ["192.168.0.5", 5060, "UP"]

#Prints out the first item in the list
print(f"The first item in the list (IP): {my_list[0]}")

#Prints out the second item in the list
print(f"The second item in the list (port): {my_list[1]}")

#Prints out the last item in the list
print(f"The last item in the list (state): {my_list[2]}")

#challenge - print only the ips from list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#my solution
print(f"The IPs from this list are: {iplist[3]} and {iplist[4]}")
