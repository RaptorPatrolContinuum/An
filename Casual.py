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
    print("charbasis is :", charbasis)
    #make Xn
    Xn = []
    n = 1
    for x in charbasis:
         Xn.append(n)
         n += 1
    print("Xn is :", Xn)
    basis = charbasis + Xn
    print(charbasis)
    print(Xn)
    print(basis)
    i = 1
    partialbinary= []
    for c in string:
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
        print("wtf is happenning", i,c,x,y,L,TOP,MIDDLE,TOP+MIDDLE)
        i += 1
    print("partialbin is: ", partialbinary)
    return [basis,1,partialbinary]



'''
TODO
VISION FUNC: (inverse of address func) AKA recover function from address
be able to write to text file
be able to run text files and test them out
"see itself" by running address func on the text files
figure out how to curry or just use address func
magic is when it attempts to simulate actors and gets y/n then uses that info to make future  decisions
'''




#file = open('INP.txt', 'rb')
file = open('INP.txt', 'r')
print(getSize(file))
#print("test address func")
#file.seek(0)
#print("test address func2: \n", file.read())

print("checking address return", Address("don't", file))

N = []
delimiters = [" ", "."]








print("END")
