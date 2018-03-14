import mmap
import os

def tail(filename, n):
    """Returns last n lines from the filename. No exception handling"""
    size = os.path.getsize(filename)
    with open(filename, "rb") as f:
        # for Windows the mmap parameters are different
        #fm = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
        fm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        try:
            for i in range(size - 1, -1, -1):
                if fm[i] == '\n':
                    n -= 1
                    if n == -1:
                        break
            return fm[i + 1 if i else 0:].splitlines()
        finally:
            fm.close()


GIGANTOR = "SIData9.txt"



def tailSHIT(f, n, offset=0):
    """
    HINT!!!!!
    THIS RETURNS A LIST SO YOU HAVE TO INDEX[0] TO GET ACTUAL OBJECT!!!!


    Reads a n lines from f with an offset of offset lines.
    HINT: this is used in ConstructPNXNLines
    file is in the form of open(filename,...)


    this works for constructlines
    """
    avg_line_length = 74
    to_read = n + offset
    while 1:
        try:
            f.seek(-(avg_line_length * to_read), 2)
        except IOError:
            # woops.  apparently file is smaller than what we want
            # to step back, go to the beginning instead
            f.seek(0)
        pos = f.tell()
        lines = f.read().splitlines()
        if len(lines) >= to_read or pos == 0:
            return lines[-to_read:offset and -offset or None]
        avg_line_length *= 1.3
#GIGANTOROPEN = open(GIGANTOR,'r+')
#print("tail pls2",tailSHIT(GIGANTOROPEN, 1))
#GIGANTOROPEN.close()
#print("tail pls",tail(GIGANTOR, 1))

print("tail pls",tailSHIT(open('EMPTY.txt','r+'), 1))
