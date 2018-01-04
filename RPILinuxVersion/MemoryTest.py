#!/usr/bin/env python
from MiraExternals import *


AddressX = AutoAddressFunc([['0', '0'], ['1', '0'], ['2', '0'], ['0', '2'], ['1', '2']])
AddressY = AutoAddressFunc([['0', '0'], ['0', '1'], ['0', '2'], ['2', '1']])

print("nani",AddressX,AddressY)
#print("testing memory to see if per line trick works",ShittySI([[299,165],"Auto"]))
print("testing memory to see if per line trick works",ShittySI([[AddressX,AddressY],"Auto"]))
