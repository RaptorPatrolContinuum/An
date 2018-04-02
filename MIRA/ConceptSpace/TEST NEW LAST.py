#!/usr/bin/env python
import sys
sys.path.insert(0, 'C:\An\MIRA')
from MiraExternals import *
from linecache import *

testfile = "SIDATA BEFORE DEATH.txt"
#getmaxlines of a file
maxlinenumber = mapcountLINES([testfile])
#get the last line of that file
#FILEindexread([name, index])


print("maxline attempt", maxlinenumber)
#try linecache
lastline = getline(testfile,maxlinenumber)
#print("what is lastline attempt", rchop(lastline, '\n'))
print("Macky Gee - MAKE ME FEEL BY XQC", FILEindexread([testfile,maxlinenumber]))
