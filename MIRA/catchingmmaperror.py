#!/usr/bin/python3.6.3
from MiraExternals import *

'''
mapcountLINES(['Memory.txt'])
try:
    mapcountLINES(['Memory.txt'])
except ValueError:
    arg2maxlines = 0
except Exception as e:
    print("ERROR IN lexicoSort",e)
'''
try:
    testy = mapcountLINES(['Memory.txt'])
except ValueError:
    testy = 0
except Exception as e:
    print("ERROR IN lexicoSort",e)

print("testy",testy)
