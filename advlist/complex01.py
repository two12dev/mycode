#!/usr/bin/env python3
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
print(list1)
print(list1[1])

#creating second list and will combine them together
list2 = ["juniper"]

list1.extend(list2)
print(list1)

#creating a 3rd list to try append
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
list1.append(list3)
print(list1)

print(list1[4])

print(list1[4][0])
