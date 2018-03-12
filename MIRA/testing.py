from MiraExternals import *


'''
THIS DOESN'T WORK PROPERLY (something trailing at the end) but fuck it working with IRL rules right now

filename = open("Basis.txt",'r+')
filename.seek(0)
filelist = ast.literal_eval(filename.read())
newtext = ""
for x in filelist:
    print("what is x",x)
    newtext = newtext + x + "\n"

print("what is newtext?",newtext)
filename.seek(0)
filename.write(newtext)
filename.close()

'''

#GET BASIS INDEX (REMEMBER TO START FROM 0!!!!!!)
filename = open("Basis.txt",'r+')
filename.seek(0)

def fileindex(argList):
    '''
    arg1 = filestream
    arg2 = string to check index of
    this gets first index of string with respect to filestream
    RETURNS: None if fail or integer if there is index

    thinking about this
    I have a string that I have to read line by line ???

    #seek to end
    #arg1.seek(0, 2)
    #testing writing
    #arg1.write("I KNOW EVERYTHING, EVERY SINGLE PART OF YOU")

    '''
    arg1 = argList[0]
    arg2 = argList[1]

    
    #check if arg1 is a file
    #I don't think checking this is feasible? because I could feed a string OR I could feed a list???

    #check if arg2 is a string
    if type(argList[1]) is str:
        pass
    else:
        print("arg2 not string!")
        return None
    
    arg1.seek(0)
    '''
    problems: if there are multiple I might only get the first index
    hint: don't write shit code then
    '''
    i = 0
    for x in arg1:
        #print("check type")
        #print(type(arg2) is str)
        #print(type(x) is str)
        #print(arg2, str(x),arg2 + "\n" == str(x))
        #print("check type END")
        if arg2 + "\n" == str(x):
            return i
        i += 1
    #if we get here then we need to append to basis then return answer
    '''
    PROBLEM:
    modifying file from this function
    right now I have just the filestream but I don't want to open file here
    lemme test something real quick
    '''
    
    arg1.seek(0, 2)
    arg1.write(arg2 + "\n")
    
    return i + 1
print(fileindex([filename, "ZZ"]))
print(fileindex([filename, "False"]))
print(fileindex([filename, "Your"]))


def fileindexINV(argList):
    '''
    arg1 = filestream
    arg2 = INDEX NUMBER
    this gets first index of string with respect to filestream
    RETURNS: None if fail or integer if there is index
    HINT: FILEINDEXINV DOES NOT CLOSE THE FILE
    also this is just to make shit look good I should just be using the tail function but whatever
    '''
    return tail(arg1, arg2, 0)



filename.close()

print("can I open a file then copy+close to work on it still?")
filename = open("Basis.txt",'r+')
keep = filename.read()
filename.close()
#print("check filename", keep)

elements = ('foo', 'bar', 'baz')
for count, elem in enumerate(elements):
    print (count, elem)

#===============

'''
import fileinput

processing_foo1s = False

for line in fileinput.input('1.txt', inplace=1):
  if line.startswith('foo1'):
    processing_foo1s = True
  else:
    if processing_foo1s:
      print('foo bar')
    processing_foo1s = False
  print(line)
'''

import fileinput

def FILEinsertAtPERMERROR(ArgList):
    '''
    function to insert text at a specific line in file
    arg1 = filestream
    arg2 = string to insert
    needs 'import fileinput'
    '''
    arg1 = ArgList[0].name
    #have to close this for fileinput to work
    ArgList[0].close()
    arg2 = ArgList[1]
    i = 0
    for line in fileinput.input(arg1, inplace=1):
        if i == 3:
            print(arg2)
        i += 1
        print(line, end='')
FILEinsertAtPERMERROR([open('1.txt','r+'),"ok inserted at 3 (fixed)?"])



def newtail(f, n, offset=0):
    """
    Reads a n lines from f with an offset of offset lines.
    HINT: this is used in ConstructPNXNLines
    file is in the form of open(filename,...)

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
    """
    for i, line in enumerate(f):
        print("newtail stats", i, n, line, )
        if i == n:
            return line


#print("fuck I have to write my own tail now too",tail(open("1.txt","r+"), 0, 0))
#print("fuck I have to write my own tail now too",newtail(open("1.txt","r+"), 0, 0))
