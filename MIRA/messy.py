import mmap
import os


def tail(f, n, offset=0):
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

def tailTEST(argList):
    #[fname, lines, _buffer=4098]
    f = open(argList[0],'r+')
    lines = argList[1]
    _buffer = 4098
    
    """Tail a file and get X lines from the end"""
    # place holder for the lines found
    lines_found = []

    # block counter will be multiplied by buffer
    # to get the block size from the end
    block_counter = -1

    # loop until we find X lines
    while len(lines_found) < lines:
        try:
            f.seek(block_counter * _buffer, os.SEEK_END)
        except IOError:  # either file is too small, or too many lines requested
            f.seek(0)
            lines_found = f.readlines()
            break

        lines_found = f.readlines()

        # we found enough lines, get out
        # Removed this line because it was redundant the while will catch
        # it, I left it for history
        # if len(lines_found) > lines:
        #    break

        # decrement the block counter to get the
        # next X bytes
        block_counter -= 1

    f.close()
    return lines_found[-lines:]
#GIGANTOROPEN = open(GIGANTOR,'r+')
#print("tail pls2",tailSHIT(GIGANTOROPEN, 1))
#GIGANTOROPEN.close()
#print("tail pls",tail(GIGANTOR, 1))

#print("tail pls",tailSHIT(open('MemoryUNORDERED.txt','r+'), 1))
#print("tail pls",tailTEST(['MemoryUNORDERED.txt',1]))
#openguy = open('MemoryUNORDERED.txt', 'r+')
#print("tail pls OG",tail(openguy,1))
#openguy.close()

def seqstring(argList):
    '''
    arg1 = string
    EX:
    STRING
    STRIN
    STRI
    STR
    ST
    S
    +
    TRING
    TRIN
    TRI
    TR
    T
    + .......











    HINT:
    use like 3 counters to simulate the edge indices
    then just go through it using a modified maximum that goes it once














    '''
    #arg1 should be a string
    arg1 = argList[0]
    ANS = []
    maxlength = len(arg1)
    print("wtfstats", arg1, maxlength)
    
    for y in range(0,maxlength):
        for x in range(0,maxlength+y):
            if x == 0:
                thingy = arg1[y:]
            else:
                thingy = arg1[y:-x]
            if len(thingy) > 0:
                print(thingy, y, x)
                ANS.append(thingy)
    '''
    y = 0
    for x in range(0,maxlength+y):
        if x == 0:
            thingy = arg1[y:]
        else:
            thingy = arg1[y:-x]
        if len(thingy) > 0:
            print(thingy, y, x)
            ANS.append(thingy)
        #y += 1
    return ANS
    '''
#print(seqstring(["damnwhatwasthat"]))
for x in range(0,15*15):
    print(x)

