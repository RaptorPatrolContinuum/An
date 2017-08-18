from math import *
import ast

file = open('INP.txt', 'r')
basis = open('Basis.txt', 'r+')
memory = open('Memory.txt', 'r+')

def M_(thestr):
    ANS = []
    i = 0
    for x in thestr:
        ANS.append([str(i),x])
        i += 1
    return ANS

def CantorPair(x,y):
    return (1/2)*(x+y)*(x+y+1)+y

def CantorInv(z):
    w = floor((sqrt(8*z+1)-1)/2)
    t = (w*w+w)/2
    y = z - t
    x = w - y
    return [x,y]

def Address(basis,obj):
    '''
    assume:
    basis is a list
    obj is a list of pairs
    '''
    Interim = []
    for x in obj:
        print("Cantor Data", basis.index(x[0]),basis.index(x[1]))
        Interim.append(CantorPair(basis.index(x[0]),basis.index(x[1])))
    
    ANS="1".zfill(int(max(Interim))+1)
    print("need Interim Data", Interim)
    Interim = list(filter(lambda x: x != max(Interim), Interim))
    for x in Interim:
        ANS = ANS[:int(x)] + "1" + ANS[int(x)+1:]
    ANS = int(ANS[::-1], 2)
    return ANS

def AutoVision(number,Lval):
    #print("==========statspls", number,Lval)
    #print("plsonlyonce",Lval,Lval == 1)
    '''
    this is for 
    '''
    ANS = []
    binary = "{0:b}".format(number)[::-1]
    #print("number, binary", number, binary, Lval)
    #print("thebin",binary)
    #print("first index must match", str(binary).index('1'))
    #so we're going the right direction
    if Lval == 1:
        print("right choice!")
        indexer = 0
        for d in str(binary):
            if d == '1':
                print("what is index?", indexer, CantorInv(indexer))
            indexer += 1
        '''
        z = number
        w = floor((sqrt(8*z+1)-1)/2)
        t = (w*w+w)/2
        y = z - t
        x = w - y
        
        #print("number, append", number, [x,y])
        #print("how the fuck do you even get empty pair", number,[x,y])
        ANS.append([x,y])
        '''
    else:
        '''
        for each one, construct the part recursively:
	go down 1 Lval
	'''	
        i = 0
        for x in binary:
            if x == "1":
                '''
                what do we do?
                L-1
                because L == 1 we eval and append
                '''
                ANS.append(AutoVision(i,Lval-1))
            i += 1
        #FUCKING ZERO ALWAYS IS AN EXCEPTION THE DAMN BASTARD
        if number == 0:
            #ANS.append(AutoVision(0,Lval-1))
            ANS.append([[0.0, 0.0]])
    if ANS == []:
        #print("stats", number,Lval)
        print("ANS IS []!")
    return ANS

while True:
    inputtext = str(input("Exit or logout to leave \n"))
    if inputtext == "exit" or inputtext == "logout":
        break
    else:
        '''
        What's the plan?
        
        '''
        #init basis
        basis.seek(0)
        if len(basis.read()) == 0:
            basislist = ["True","False"]
            
        else:
            #get basistext as list:
            basis.seek(0)
            basislist = ast.literal_eval(basis.read())

        #init memory:
        memory.seek(0)
        if len(memory.read()) == 0:
            memorylist = []
        else:
            #get basistext as list:
            memory.seek(0)
            memorylist = ast.literal_eval(memory.read())

        for char in inputtext:
            #if stuff is not in the basis:
            if char in basislist:
                pass
            else:
                #append to basis
                basislist.append(char)
        
        if len(inputtext) in basislist:
            pass
        else:
            for k in range(len(inputtext)+1):
                if str(k) in basislist:
                    pass
                else:
                    basislist.append(str(k))
                    

        #print("basislist", basislist)
        #print("fml", Address(basislist,M_(inputtext)))
        print(AutoVision(Address(basislist,M_(inputtext)),1))
