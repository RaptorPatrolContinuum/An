from math import *
print("START")

#input("Write a command here.")
#FML I am not going to do a set implementation in C just yet
#f = open('INP.txt', 'r')
#print(f.read())
#f.seek(0)
#construct basis:

def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

def Address(string, file):
    #make charbasis
    charbasis = []
    file.seek(0)
    for c in file.read():
        if c not in charbasis:
            charbasis.append(c)
    #check charbasis:
    #make Xn
    Xn = []
    n = 1
    for x in range(getSize(file)):
         Xn.append(n)
         n += 1
    basis = charbasis + Xn
    i = 1
    partialbinary= []
    for c in string:
        '''
        #(i,c) is the function we see
        # now we need to map it into EXtension(function)
        
        x = basis.index(i)+1
        y = basis.index(c)+1
        L = x + y - 1
        TOP = (((L-1)**2)+(L-1))/2
        if x % 2 == 0:
            MIDDLE = x
        else:
            MIDDLE = y
        partialbinary.append(TOP+MIDDLE-1)
        #-1 since binary starts with 0 and the count I have starts at 1
        #so partial binary is the values at which 2^[partialbinary]^[control] and control = 1
        #then the actual address is enuming through partial binary then summing 2^[partial.item(0)]+2^[partial.item(1)], etc...
        print("wtf is happenning", i,c,x,y,L,TOP,MIDDLE,TOP+MIDDLE-1)
        '''
        #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
        #(x,y)= (1/2)(x+y)(x+y+1)+y
        x = basis.index(i)+1
        y = basis.index(c)+1
        appendthis = (1/2)*(x+y)*(x+y+1)+y
        partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
        i += 1
    return [basis,1,partialbinary]

def Vision(Addresslist):
    #Addresslist = [basis,1,partialbinary]
    function = []
    representation = []
    for pair in Addresslist[2]:
        z = pair
        w = floor((sqrt(8*z+1)-1)/2)
        t = (w*w+w)/2
        y = z - t
        x = w - y
        function.append([x,y])
        representation.append([Addresslist[0][int(x)-1],Addresslist[0][int(y)-1]])
    return representation

def Stringify(representation):
    #representation = list of pairs
    #takes function representation and just shows the y values in a list (AKA the string value since pairs are implicit in the representation)
    show = []
    for pair in representation:
        show.append(str(pair[1]))
    return "".join(show)

def Cheat(string):
    #take a string and return a list of strings that represent the important morphemes:
    #punctuation:
    #.?!,;:-—)}]'"...
    #line break
    #paragraph break(?)
    Morphemes = []
    delimiters = [" ", "."] #...
    #FML I NEED A BREAK
    SentenceStartPos = 0
    for x in string:
        if x == ".":
            #know the last .?! , (if any) then cut between first and last .?!
            print(".")
            Morphemes.append()
            SentenceStartPos = string.index(x)
        elif x == "?":
            print("?")
            SentenceStartPos = string.index(x)
        elif x == "!":
            print("!")
            SentenceStartPos = string.index(x)

        elif x == ",":
            #split between beginning of sentence and rest of sentence [did I word it right]
            print(",")
        elif x == ";":
            #split between beginning of sentence and rest of sentence [did I word it right]
            print(";")
        elif x == ":":
            #split between beginning of sentence and rest of sentence [did I word it right]
            print(":")
        elif x == "-":
            #split between beginning of sentence and rest of sentence [did I word it right]
            print("-")
        elif x == "—":
            #split between beginning of sentence and rest of sentence [did I word it right]
            print("—")
        elif x == "(" or ")":
            #make pair
            print(")")
        elif x == "{" or "}":
            #make pair
            print("}")
        elif x == "[" or"]":
            #make pair
            print("]")
        elif x == "'":
            #make pair
            print("'")
        elif x == "\"":
            #make pair
            print("\"")
        
    return Morphemes
    

'''
TODO
be able to write to text file
be able to run text files and test them out
"see itself" by running address func on the text files
be able to eval a text file by running it and putting that in the vision
have a persistent basis
figure out how to curry or just use address func
magic is when it attempts to simulate actors and gets y/n then uses that info to make future  decisions
'''

file = open('INP.txt', 'r')
print("checking address return:", Address("don't", file))
print("checking vision return:", Vision(Address("don't", file)))
print("checking stringify return:", Stringify(Vision(Address("don't", file))))
#print("cheating by preprogramming stuff", Cheat(".?!,;:-—)}]'\""))


N = []






print("END")
