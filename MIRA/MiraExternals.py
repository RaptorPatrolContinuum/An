#!/usr/bin/python3.6.3
from __future__ import division
from __future__ import with_statement
from math import *
from inspect import *
import ast
#import sys
from sys import *
import time
import mmap
import random
import os
import itertools
from shutil import *

from collections import defaultdict
from subprocess import *
#from linecache import *
import fileinput

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

#file = open('INP.txt', 'r')
#basis = open('Basis.txt', 'r+')
#memory = open('Memory.txt', 'r+')

def ARB(function, replacelist): 
    '''
    ANSWER:
    need to map everything to concept space
    then ARB is just a basis remapping


    god fucking damn it I hate writing one function I just want to abstract as fast as possible

    FML IF I HAD A CONVERTER TO CONCEPT SPACE STRUCTURE I COULD DO THIS ALMOST INSTANTLY

    example:
    for x in alg1:
        f1.append(x[1])

    use replacelist:
    alg1:alg2
    f1:f2

    then eval:
    for x in alg2:
        f2.append(x[1])
    problem:
         sometimes it replaces the wrong thing!

    EX:
    for r in alg1:
        g1.append(r[1])

    with:
    r:x
    g1:f1

    I would get:
    fox x in alf1:
        f1.append(x[1])

    idea:
         use syntax hax (I need to keep a fucking library god damn it)
         know what is a var and what isn't a var

    idea: use positionals (would be too complicated?)
    '''
    NEWEVAL = []
    return NEWEVAL

def SynSplit(string):
    '''
    function so I can make ABStractreplace better
    idea: feed lines in
    split each line:

    EX:
    for r in alg1:
        g1.append(r[1])

    with:
    r:x
    g1:f1

    try:
    for r in alg1:

    split into:
    [for| |r| |in| |alg1:]
         [g1|.append(| r | [|1|] |)]
    '''
    return

def ran(func):
    ANS = []
    for x in func:
        ANS.append(x[1])
    return ANS

def ranDict(obj):
    '''
    get all the keys 'in order' from a dictionary
    '''
    ANS = []
    for x in obj:
        ANS.append(x)
    return ANS

def dom(func):
    ANS = []
    for x in func:
        ANS.append(x[0])
    return ANS

def M_(thestr):
    ANS = []
    i = 0
    '''
    if empty string we send it to M_(" ") (algorithm of space)
    '''
    if len(thestr) == 0:
        return M_(" ")
    for x in thestr:
        ANS.append([str(i),x])
        i += 1
    return ANS

def Minv_(thestr):
    ANS = []
    i = 0
    for x in thestr:
        ANS.append([x,str(i)])
        i += 1
    return ANS

def Q_(unknown):
    return [[unknown,unknown]]

def CantorPair(x,y):
    return (1/2)*(x+y)*(x+y+1)+y

def CantorInv(z):
    w = floor((sqrt(8*z+1)-1)/2)
    t = (w*w+w)/2
    y = z - t
    x = w - y
    return [x,y]

def CantorInvSTR(z):
    w = floor((sqrt(8*z+1)-1)/2)
    t = (w*w+w)/2
    y = z - t
    x = w - y
    return [str(int(x)),str(int(y))]

def fCheck(fcandidate):
    ANS = True
    '''
    an object is not a function when:
    one element of the fcandidate is not a pair
    check if each element of fcandidate is of size 2
    '''
    if len(fcandidate) == 0:
        return False
    for obj in fcandidate:
        #print("what is obj?",obj)
        #print("len(obj)",len(obj))
        if len(obj) != 2:
            ANS = False
    return ANS

def toString(argList):
    '''
    HINT: might have to take dom or range for this func
    obj to make into string (assume it's a written 'function' to be safe)
    f = arg1
    arg2 is basistype which can be a file or naive or INTEGERS
    
    assume f is a finite function of the form for all x in f, x = [a,b]
    return a string that is the range of f "in order"
    basistype is a list where we assume order OR take a basis

    '''
    f = argList[0]
    basistype = argList[1]
    ANS = ""
    #print("IS TO STRING FUCKED=======================",argList)
    if basistype == "naive":
        #print("what is f",f)
        for x in f:
            #print("what is x",x,x[0])
            ANS = ANS + str(x[0])
        return ANS
    if fCheck(f) == False:
        print("f1 is function? toString", fCheck(f))
        return
    if basistype == "INTEGERS":
        #then the x coord is just a number, so we order the answer by the numbers in the x coordinates
        #what happens if there are multiple of the same integer??
        ##then that's just wrong input format so we append in the same order as we get it
        ANSPREP = []
        #if x coord isn't a number, just append at the end
        for x in f:
            #print("WHAT IS X",x)
            if ANSPREP == []:
                ANSPREP = [x]
                #print("init ansprep",ANSPREP)
            else:
                i = 0
                for y in ANSPREP:
                    #print("what is y", y)
                    #print("stats, ", x,y,int(x[0]) < int(y[0]))
                    #print("i index",i)
                    if int(x[0]) < int(y[0]):
                        #print("insert issue?", ANSPREP)
                        ANSPREP = InsertAt(ANSPREP,x,i)
                        #print("insert issue SHOULD BE INSERTED", ANSPREP)
                        break
                    if i == len(ANSPREP)-1:
                        ANSPREP = InsertAt(ANSPREP,x,-1)
                        break
                    i += 1
                #print("CHECKING INSERT",ANSPREP)
    for x in ran(ANSPREP):
        ANS = ANS + str(x)
    #for x in f:
    #    ANS = ANS + x[1]
    #print("hoping lists retain some kind of order",f,ANS)
    return ANS

def Beta_(E_G):
    '''
    given E_G for some graph G, we return Basis_G
    here we make the basis = \rchi_obj union obj
    '''
    '''
    i = 0
    for x in obj:
        ANS.append(x)
        ANS.append([x,i])
        i += 1
    for y in range(i):
        #oh shit this is crazy because by the Duality theorem + kuratowski pair lemma that means these are actual numbers
        ANS.append([y,y])
    '''
    ANS = []
    #check if obj is a function:
    if fCheck(E_G) == False:
        print("Beta says that obj isn't a function!", E_G)
        return

    #construct V_G
    V_G = []
    for x in E_G:
        if x[0] not in V_G:
            V_G.append(x[0])
        if x[1] not in V_G:
            V_G.append(x[1])

    ANS = V_G + E_G + rchi(E_G)
    return ANS

def rchi(obj):
    ANS = []
    i = 0
    for x in obj:
        ANS.append(str(i))
        i += 1
    return ANS

def rchiINT(NUM):
    ANS = []
    i = 0
    for x in range(0,int(NUM)+1):
        ANS.append(str(i))
        i += 1
    return ANS


def Address(basis,obj):
    '''
    assume:
    basis is a list
    obj is a list of pairs
    '''
    
    Interim = []
    for x in obj:
        #print("wat is x?", x, type(x), basis)
        #print("Cantor Data", basis.index(x[0]),basis.index(x[1]))
        Interim.append(CantorPair(basis.index(x[0]),basis.index(x[1])))

    ANS="1".zfill(int(max(Interim))+1)
    #print("need Interim Data", Interim)
    Interim = list(filter(lambda x: x != max(Interim), Interim))
    for x in Interim:
        ANS = ANS[:int(x)] + "1" + ANS[int(x)+1:]
    ANS = int(ANS[::-1], 2)
    return ANS

def AddressFILE(argList):
    '''
    assume:
    basisNAME
    obj is a list of pairs
    '''
    basisfile = argList[0]
    obj = argList[1]
    #print("check arglist",argList)
    #print("qhat is obj?",obj)
    #print("why does fcheck work on ''? ", fCheck(obj))
    '''
    if len(obj) == 0:
        obj = " "
    '''
    if fCheck(obj) == False:
        print("obj to address is function? ADDRESSFILE", fCheck(obj))
        return
    
    Interim = []
    for x in obj:
        #print("wat is x?", x, type(x), basisfile)
        #print("Cantor Data", fileindex([basisfile,x[0]]),fileindex([basisfile,x[1]]))
        Interim.append(CantorPair(fileindex([basisfile,x[0]]),fileindex([basisfile,x[1]])))

    ANS="1".zfill(int(max(Interim))+1)
    #print("need Interim Data", Interim)
    Interim = list(filter(lambda x: x != max(Interim), Interim))
    for x in Interim:
        ANS = ANS[:int(x)] + "1" + ANS[int(x)+1:]
    ANS = int(ANS[::-1], 2)
    return ANS


def AddressFunc(index,obj):
    '''
    index is a finitefunction going from objects -> rchi objects
    object is the finitefunction we are addressing
    

    takes a function and optionally an index
    returns the address
    NOTE: THIS FUNC TAKES THE ALGORITHM OF THE OBJECT

    option: algorithm before or after?

    let obj be an arbitrary object (string or list)
    let index be a written function of the form: func => \rchi+func
    '''
    if obj == []:
        return int(0)

    Interim = []
    
    #print("obj for reference!",obj)
    for x in obj:
        #print("LINE 274")
        #print("index stats",index)
        #print("other stats",obj,Interim)
        #print("stats",x,x[0],int(RelEval(index,x[0])[0]))
        #print("suspected wtf",index,x[1])

        #print("x obj", x)
        #print("index",index)
        #print("x[0]",x[0])
        #print("so weird I need to do this by hand maybe",RelEval(index,x[0]))
        #print("Cantor 1st coord",int(RelEval(index,x[0])[0]))
        #print("index ",index)
        #print("x[1]",x[1])
        #print("int(empty set) just dies",RelEval(index,x[1]))
        #print("Cantor 2nd coord",int(RelEval(index,x[1])[0]))
        #print("the pair",CantorPair(int(RelEval(index,x[0])[0]),int(RelEval(index,x[1])[0])))
        #print("LINE 274 END")
        Interim.append(CantorPair(int(RelEval(index,x[0])[0]),int(RelEval(index,x[1])[0])))
    
    #print("more stats",obj,Interim)
    ANS="1".zfill(int(max(Interim))+1)
    #print("need Interim Data", Interim)
    Interim = list(filter(lambda x: x != max(Interim), Interim))
    #print("Interim filtered?",Interim)
    for x in Interim:
        ANS = ANS[:int(x)] + "1" + ANS[int(x)+1:]
    #print("ANS bin",ANS)
    ANS = int(ANS[::-1], 2)
    #print("ANS INT",ANS)
    return ANS

def AutoAddressFunc(obj):
    '''
    THE DIFFERENCE IS THAT I JUST ASSUME THE OBJ IS NUMBERS SO I DON'T HAVE TO MAKE A DUMB BASIS THAT DOESN'T MESH WITH THE 'NATURAL BASIS'
    index is a finitefunction going from objects -> rchi objects
    object is the finitefunction we are addressing
    

    takes a function and optionally an index
    returns the address
    NOTE: THIS FUNC TAKES THE ALGORITHM OF THE OBJECT

    option: algorithm before or after?

    let obj be an arbitrary object (string or list)
    let index be a written function of the form: func => \rchi+func
    '''
    if obj == []:
        return int(0)

    Interim = []
    
    for x in obj:
        #print("index stats",index)
        #print("other stats",obj,Interim)
        #print("stats",x,x[0],int(RelEval(index,x[0])[0]))
        #print("suspected wtf",index,x[1])

        #print("x obj", x)
        #print("Cantor 1st coord",int(RelEval(index,x[0])[0]))
        #print("Cantor 2nd coord",int(RelEval(index,x[1])[0]))
        #print("the pair",CantorPair(int(RelEval(index,x[0])[0]),int(RelEval(index,x[1])[0])))
        Interim.append(CantorPair(int(x[0]),int(x[1])))
    
    #print("more stats",obj,Interim)
    ANS="1".zfill(int(max(Interim))+1)
    #print("need Interim Data", Interim)
    Interim = list(filter(lambda x: x != max(Interim), Interim))
    #print("Interim filtered?",Interim)
    for x in Interim:
        ANS = ANS[:int(x)] + "1" + ANS[int(x)+1:]
    #print("ANS bin",ANS)
    ANS = int(ANS[::-1], 2)
    #print("ANS INT",ANS)
    return ANS

def AutoVisionHAX(AVlist,replacementlist):
    '''
    some hax because I'm a dumbass
    '''
    ANS = []
    for x in AVlist:
        ANS.append([RelEval(replacementlist,[str(int(x[0]))])[0],RelEval(replacementlist,[str(int(x[1]))])[0]])
    return ANS

def AutoVisionString(number,Lval):
    '''
    idea:
    I need to feed in a list of strings into address in order to make address work
    since autovision feeds in ints for some reason
    '''
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
        #print("right choice!")
        indexer = 0
        for d in str(binary):
            if d == '1':
                #print("what is index?", indexer, CantorInv(indexer))
                ANS.append((CantorInvSTR(indexer)))
            indexer += 1
    else:
        '''
        for each one, construct the part recursively:
        go down 1 Lval
        '''     
        print("ABUSE THE COMPRESSION THEOREM!")
    #if ANS == [] and number == 0:
    #    ANS = [['0','0']]
    if ANS == []:
        #print("stats", number,Lval)
        print("ANS IS []???!?!?!?!?!")
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
        #print("right choice!")
        indexer = 0
        for d in str(binary):
            if d == '1':
                #print("what is index?", indexer, CantorInv(indexer))
                ANS.append(CantorInv(indexer))
            indexer += 1
    else:
        '''
        for each one, construct the part recursively:
        go down 1 Lval
        '''     
        print("ABUSE THE COMPRESSION THEOREM!")
    if ANS == []:
        #print("stats", number,Lval)
        print("ANS IS []???!?!?!?!?!")
    return ANS

def Compose(f1,f2):
    '''
    do f2 THEN f1 like the way it's written!
    '''
    #check if f1,f2 are functions:
    if fCheck(f1) == False or fCheck(f2) == False:
        print("f1 is function? COMPOSE", fCheck(f1), "f2 is function?", fCheck(f2))
        return
    ALG = []
    for x in f2:
        for y in f1:
            if x[1] == y[0]:
                ALG.append([x[0],y[1]])
    return ALG

def ComposeMETA(argList):
    f1 = argList[0]
    f2 = argList[1]
    '''
    do f2 THEN f1 like the way it's written!
    '''
    #check if f1,f2 are functions:
    if fCheck(f1) == False or fCheck(f2) == False:
        print("WTF ARE THESE f1", f1 ,type(f1))
        print("WTF ARE THESE f2", f2, type(f2))
        print("f1 is function? COMPOSEMETA", fCheck(f1), "f2 is function?", fCheck(f2))
        return
    ALG = []
    for y in f2:
        for x in f1:
            #which one is the first half of the function?
            '''
            for x in thingy:
            replace y[0] with x
            AND SOMETHING ABOUT ARGUMENT_# WHERE # INCREMENTS
            info I need:
            the whole thing
            parts
            maybe write a replacer function
            '''
            ComposeTest = ComposeReplace(x,y)
            if ComposeTest != None:
                ALG = ALG + ComposeTest
            #if eval(ComposeReplace(x,y)):
            #    ALG.append([x[0],y[1]])
    return ALG

def ComposeReplace(str1,str2):
    '''
    HINT: I WRITE str1,str2 BUT I EVAULATE IN TERMS OF str2 FIRST, THEN str1
    HINT: USE Q_() function to make things automatically functions

    PICTURE:
    FUNCTION1 COMPOSED FUNCTION2:
     ^ where y is from
                         ^ where x is from

    HINT: DO FUNCTION2 BEFORE FUNCTION1 LIKE IN MATH
    
    str1 is x which is a pair
    str2 is y which is a pair

    PICTURE:
        (Extra data from Compose:)
         STR2             STR1
    [y[0],y[1]] COMPOSE [x[0],x[1]]
    GOAL:
    eval y[0] using x[0] as argument list
    this function just replaces argument_X in y[0] with elements of x[0] OR TOTAL_ARGUMENT of x[0] (AKA the whole thing of x[0])


    TODO:
    check if string or list
        total: have to add quotes to before and after
        per item: ???
    adding quotes or not
        total: ???
        per item: might have to add quotes?
        what to do:
        for each item in y[1], we replace ARGUMENT_i (where is is incrementing number) in x[0]
        PROBLEMS:
            let's look at ARGUMENT_1== b
            then all it's looking at is if argument_1 == b but other objects with different tails can be included
            actually, this isn't a proble, that just means that my check needs to be better
            
    evaluating properly

    '''
    #print("test str1",str1)
    #print("test str2",str2)
    ANS = None
    if isinstance(str2[1], str):
        total = "'" + str2[1] + "'"
        #print("test TOTAL",total)
        #print("TRY REPLACEMENT NOW")
        #print(str1[0].replace("TOTAL_ARGUMENT", total))
        #print(eval(str1[0].replace("TOTAL_ARGUMENT", total)))
        if eval(str1[0].replace("TOTAL_ARGUMENT", total)):
            #print("got here???")
            #return [str2[0],str1[1]]
            if ANS == None:
                ANS = [[str2[0],str1[1]]]
            else:
                ANS = ANS + [str2[0],str1[1]]
    elif isinstance(str2[1], list):
        #print("REAPERREAPERTHAT'SWHAT PEOPLEdetected list!!", str(str2[1]))
        i = 1
        total = str(str2[1])
        #print("x,y stats",str1,str2)
        #print("what is being replaced",str1[0])
        teststring = str1[0].replace("TOTAL_ARGUMENT", total)
        #print("what is totalDARLINGINTHEFRANXX",total)
        #print("why didn't TESTSTRING UPDATE",teststring)

        #do total
            

        #do elements
        for z in str2[1]:
            #print("maybe z is checked twice because of input",z)
            #print("stats","argument_" + str(i),"'"+z+"'")
            #print("what is replace?",teststring.replace("argument_" + str(i), "'"+z+"'"))
            teststring =             teststring.replace("argument_" + str(i), "'"+z+"'")
            #print("what is teststring",teststring)
            i+=1
        try:
            #print("eval teststring",eval(teststring))
            if eval(teststring):
                #print("ANSBEFORE",ANS)
                #print("WHAT IS ADDED?",[str2[0],str1[1]])
                #return [str2[0],str1[1]]
                if ANS == None:
                    ANS = [[str2[0],str1[1]]]
                else:
                    ANS = ANS + [[str2[0],str1[1]]]
                #print("ANSAFTER",ANS)
        except:
            pass
    return ANS


def RelEval(f1,arglist):
    '''
    "RELationEval"
    evals f1 using arglist and returns list
    f1 is finite function
    arg is singleton

    question: "composing" using list vs 1 obj
    '''
    ANS = []
    for y in arglist:
        for x in Compose(f1,Q_(y)):
            ANS.append(x[1])
    return ANS

    #print(RelEval([[1,2],[2,2],[7,8]],[1,2,7]))

def M_Compose(alg1, alg2):
    '''
    do ALG2 THEN ALG1!!!!
    problem: what if alg2 or alg1 don't map to functions???
    say that alg1 or alg2 are not mapped to funcs
    alg1 and alg2 should be inspectors of functions....
    '''
    ALG = []
    f1 = []
    f2 = []
    #construct f1 and f2
    for x in alg1:
        f1.append(x[1])
    for x in alg2:
        f2.append(x[1])
    #check if they are functions
    if fCheck(f1) == False or fCheck(f2) == False:
        print("f1 is function? M_COMPOSE", fCheck(f1), "f2 is function?", fCheck(f2))
        return
    #compose them
    return Compose(f1,f2)

def PreImage(f1):
    ANS = []
    #check if f is a function:
    if fCheck(f1) == False:
        print("f1 is function? PREIMAGE", fCheck(f1))
        return
    #reverse pair ordering:
    for x in f1:
        ANS.append([x[1],x[0]])
    return ANS

def Inspector_M(y):
    '''
    Inspector (y) = M_(y) compose M_^(-1)(y)

    (here we assume that y is already M_y!!!!!)
    '''
    #check if y is a function:
    #if fCheck(y) == False:
    #    print("y is function? INSPECTOR", fCheck(y))
    #    return
    return Compose(M_(y),PreImage(M_(y)))

def Elem_My(x,y):
    '''
    this is the element relation
    [this function says if x in y or not]
    
    #1: why is this important?
    >>>ALL THE FUNCTIONS ARE IN THE CONCEPT SPACE


    this function says if x in y or not:
    idea:
    Q_(x) compose Inspector(y)
    Inspector (y) = M_(y) compose M_^(-1)(y)
    '''
    if len(Compose(Q_(x),Inspector_M(y))) > 0:
        return True
    else:
        return False

def VisionBasis(argList):
    basis = argList[0]
    vision = argList[1]
    ANS = []
    if fCheck(vision) == False:
        print("vision is function?", fCheck(vision))
        return
    for x in vision:
        ANS.append([basis[int(x[0])],basis[int(x[1])]])
    return ANS

def VisionBasisFILE(argList):
    '''
    basisfile takes the whole filename (incl extension) of the basis
    HINT: need AutoVision to go from address to vision
    '''
    basisfile = argList[0]
    vision = argList[1]
    ANS = []
    if fCheck(vision) == False:
        print("vision is function?", fCheck(vision))
        return
    for x in vision:
        ANS.append([fileindexINV([basisfile,int(x[0])]),fileindexINV([basisfile,int(x[1])])])
    return ANS

def EdgeSortbyLinks(E_G):
    Start = {}
    for x in E_G:
        if x[0] in Start:
            Start[x[0]].append(x[1])
        else:
            Start[x[0]] = [x[1]]
    Filter = {}
    for x in Start:
        if len(Start[x]) in Filter:
            Filter[len(Start[x])].append(x)
        else:
            Filter[len(Start[x])] = [x]
    return Filter

def LinkPoolGen(smallLinks,largeLinks):
    '''
    note: the Links are from EdgeSortbyLinks
    '''
    #print("================LINKSSTART",smallLinks,largeLinks)
    LinkPool = {}
    for x in smallLinks:
        for y in smallLinks[x]:
            #compare with largeLinks and check the index
            #print("where am I?",x,smallLinks[x],y)
            for a in largeLinks:
                #print("stats I can use?", a, largeLinks[a])
                #print(x, "<=", a, x <= a)
                if x <= a:
                    if y in LinkPool:
                        LinkPool[y] = LinkPool[y] + largeLinks[a]
                    else:
                        LinkPool[y] = largeLinks[a]
                #print("Linkpool and sets", LinkPool)
    #print("testing Linkpool", LinkPool)
    #print("================LINKEND")
    return LinkPool

#insert into a list at the right index
def InsertAt (List,obj,Index):
    '''
    Inserts obj at List[Index] and appends the rest of list after it
    -1 means add to end/append
    '''
    if Index == -1:
        VALUE = List
        VALUE.append(obj)
    else:
        VALUE = List[:Index]
        VALUE.append(obj)
        for x in range(0,len(List[Index:])):
            VALUE.append(List[Index + x])
    return VALUE

def PhiConstruct(IndexRan,LinkPool,AutoToggle):
    '''
    IndexRan is a function where node corresponds to a list of indices that correspond to a number in LinkPool
    EX: [['A',0],['B',1],['C',0]]
    THIS MEANS YOU HAVE TO CONSTRUCT THE RANGE OF INDEXRAN SEPARATELY AND USE THAT TO FUCKING TEST SI
    LinkPool is a dictionary that has nodes and possible node links
    EX: LinkPool = {'A': ['X', 'Z', 'Y'], 'B': ['X', 'Z', 'Y'], 'C': ['X', 'Z', 'Y', 'G', 'H', 'I']}

    REMEMBER: Each pick is mutually exclusive, so if you pick node X then you can't pick node X again but if node X has index Y index Y can appear again but it will NOT be node X
    RETURN: TheChoice: finite function phi that can be used to check SI
    '''
    TheChoice = []
    Exclusion = []
    #print("PHICONSTRUCT START")
    #print("what is IndexRan?",IndexRan)
    for x in IndexRan:
        #print("testing",x,LinkPool)
        #print("what's failing?",x,x[0],LinkPool,LinkPool[x[0]])
        #print("failing 2 probably",[y for y in LinkPool[x[0]] if y not in ran(Exclusion)])
        ThePick = [y for y in LinkPool[x[0]] if y not in ran(Exclusion)][x[1]]
        Exclusion.append([x[0],ThePick])
        if AutoToggle == True:
            TheChoice = TheChoice + [[x[0],ThePick]]
        else:
            TheChoice = TheChoice + [[ThePick,x[0]],[x[0],ThePick]]
        #print("check pick and exclusion/ran exclusion", ThePick, Exclusion, ran(Exclusion))
        #TheChoice = TheChoice + [[ThePick,x[0]],[x[0],ThePick]]
        #I think ^^ is not good (maybe only for auto) because you can get duplicates and dumb shit like [1,0],[1,2] if you map 0->1 and 1->2
        #TheChoice = TheChoice + [[x[0],ThePick]]
        #print("choice?",TheChoice)
    #print("PHICONSTRUCT END")
    return TheChoice

def IsAuto(E_G):
    '''
    checks if a graph is just on integers or not (so we can figure out to use auto functions or not)
    '''
    for x in Vertex_(E_G):
        #print("what is x?",x)
        try:
            int(x)
        except ValueError:
            return False
            break
    return True

def dictMerge(dicA,dicB):
    '''
    Aparently I have to do this manually
    '''
    ANS = {}
    if len(dicA) == 0:
        return dicB
    if len(dicB) == 0:
        return dicA     
    for x in dicA:
        ANS[x] = dicA[x]
    for x in dicB:
        ANS[x] = dicB[x] 
    return ANS

def LessThan_C(i,j):
    '''
    takes a number i j and asks if bin(i) is "less than" bin(j) componentwise
    AKA bin(i) is an initial portion of bin(j)
    '''
    '''
    print("i,j!",i,j)
    binary = "{0:b}".format(i)[::-1]
    bin2 = "{0:b}".format(j)[::-1]
    print("bin1/2",binary,bin2)
    print("the check",str(binary))
    print("check2",str(bin2[:len(binary)]))
    if str(binary) == str(bin2[:len(binary)]):
        return True
    else:
        return False
    '''
    #print("i,j!",i,j)
    ANS = True
    binary = "{0:b}".format(i)[::-1]
    bin2 = "{0:b}".format(j)[::-1]
    #print("bin1/2",binary,bin2)
    #print("the check",str(binary))
    i = 0
    for x in str(binary):
        #print("i", i)
        if x == '1':
            try:
                str(bin2)[i] != '1' 
            except IndexError:
                return False
            if str(bin2)[i] != '1':
                return False
        i += 1
    return ANS

def Vertex_(E_G):
    '''
    takes in an edgelist and returns the vertices of that graph
    '''
    ANS = []
    for x in E_G:
        if x[0] not in ANS:
            ANS.append(x[0])
        if x[1] not in ANS:
            ANS.append(x[1])
    return ANS

def ShittySI(ListItems):
    '''
    NOTE: THIS IS BIDIRECTIONAL ACTUALLY!! SO SAYS YES IF E_G SI E_H OR E_H SI E_G!
    input is a list of the form: [[E_G,E_H], "Auto"]
    says if E_G SI to some E_J in E_H
    '''
    E_G = ListItems[0][0]
    E_H = ListItems[0][1]
    #if they're exact same they're SI
    if E_G == E_H:
        return [True, "same" ]
    #else:
    if len(E_G) < len(E_H):
        WLOG = E_G
        Larger = E_H
    else:
        WLOG = E_H
        Larger = E_G

    #print("REMEMBER TO ADD ZEROLINKS TO EDGESORTbyLINKS")
    #print("sort by links START")
    #print(WLOG)
    #print(Larger)
    #print(EdgeSortbyLinks(WLOG))
    #print(EdgeSortbyLinks(Larger))
    #print(LinkPoolGen(EdgeSortbyLinks(WLOG),EdgeSortbyLinks(Larger)))
    #print("sort by links END")

    LinkPool = LinkPoolGen(EdgeSortbyLinks(WLOG),EdgeSortbyLinks(Larger))
    
    #add Zerolinks to LinkPoolGen
    #a zeronode is a node that doesn't actually link to anything (just recieves links in the graph)
    #just check LinkPool VS Vertex_(WLOG)
    #print("ran keys",ranDict(LinkPool)) 
    ZeroNodes = [x for x in Vertex_(WLOG) if x not in ranDict(LinkPool)]
    #print("Zeronodes?",ZeroNodes) 
    for x in ZeroNodes:
        LinkPool[x] = Vertex_(Larger)
    #print("LinkPool+Zeronodes?",LinkPool)

    #make sure LinkPool lists contain each other when you go down the list
    LinkPoolList = []
    #print("OK LINKPOOL BETTER NOT BE FUCKED",LinkPool)
    for x in LinkPool:
        #print("LPL START======",LinkPoolList)
        #print("what is X START",x)
        if len(LinkPoolList) == 0:
            LinkPoolList.append([x,LinkPool[x]])
            #print("WHEN DOES LPL CHANGE",LinkPoolList)
        else:
            for y in LinkPoolList:
                Linked = False
                #print("stats", LinkPoolList)
                #print("y",y)
                ##"new object length is smaller, you add it to keep connection lengths similar"
                #print("I don't understand <=", len(LinkPool[x]),len(y[1]))
                if len(LinkPool[x]) <= len(y[1]):
                    #print("GOT ADDED ALREADY WTF",LinkPoolList)
                    LinkPoolList = InsertAt(LinkPoolList,[x,LinkPool[x]],LinkPoolList.index(y)) 
                    #print("LPL Insert",LinkPoolList)
                    Linked = True
                    break
                #append at end if largest
                if Linked == False:
                    LinkPoolList = LinkPoolList + [[x,LinkPool[x]]]
                    #print("WHEN DOES LPL CHANGE2",LinkPoolList)
                    break
        #print("LPL END=======",LinkPoolList)
    #print("check LinkPoolList",LinkPoolList)

    LinkSize = []
    LinkList = []
    #LinkSize is the size of each list in LinkPool
    #need to subtract 1 each time we append to LinkSize because we are making a choice and excluding them from the rest
    #LinkPool is the corresponding list at the right index
    i = 0
    for x in LinkPoolList:
        LinkSize.append(len(x[1])-i)
        i += 1
        LinkList.append(x[1])
    #print("check linksize",LinkSize)
    #print("check linklist",LinkList)

    #print("DOUBLE CHECK LINKPOOL START")
    #print("smaller", WLOG)
    #print("larger", Larger)
    #print(LinkPool)
    #print("DOUBLE CHECK LINKPOOL END")

    AutoCheck = IsAuto(WLOG) and IsAuto(Larger)
    #print("what is LinkPoolList?",LinkPoolList)
    
    NumberIndex = []
    for G in LinkSize:
        if len(NumberIndex) > 0:
            NumberNew = []
            for H in range(0,G):
                for J in NumberIndex:
                    Appendage = J + [H]
                    NumberNew.append(Appendage)
                    if len(Appendage) == len(LinkPool):
                        Indexer = []
                        #Phiconstruct needs Indsx ran: [node,elem]
                        i = 0
                        for K in Appendage:
                            Indexer.append([LinkPoolList[i][0],Appendage[i]])
                            i += 1
                        #print("here we test SI iwth",Appendage)
                        #print("Indexer is", Indexer)
                        #print("PhiConstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                        #If |V_H| > |V_G|, then construct H* to use instead:
                        if len(Vertex_(Larger)) > len(Vertex_(WLOG)):
                            #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                            HStar = []
                            for L in Larger:
                                passA = True
                                passB = True
                                if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                    passA = False
                                if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                    passB = False
                                if passA == True and passB == True:
                                    HStar.append(L)
                            #print("ok check out H*!",HStar)
                        else:
                            HStar = Larger

                        tryit = True
                        try: 
                            ListItems[1]
                        except IndexError:
                            tryit = False
                        if tryit == True:
                            if ListItems[1] == "Auto":
                                Vertex_Max = '0'
                                #print("vertexmax lolwut",Vertex_(WLOG) + Vertex_(Larger))
                                for NUM in Vertex_(WLOG) + Vertex_(Larger):
                                    if int(NUM) > int(Vertex_Max):
                                        Vertex_Max = str(NUM)
                                #print("V_G",Vertex_(WLOG))
                                #print("V_H",Vertex_(Larger))
                                #print("TheMax",Vertex_Max)
                                #print("parts for AD1",WLOG)
                                #print("Larger",Larger)
                                #print("Indexer",Indexer)
                                #print("LinkPool",LinkPool)
                                #print("PhiConstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                                #print("need to pick right max",rchiINT(Vertex_Max))
                                #print("basis",Minv_(rchiINT(Vertex_Max)))
                                #print("compose",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))

                                if len(Vertex_(Larger)) >= len(Vertex_(WLOG)):
                                    #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                                    HStar = []
                                    for L in Larger:
                                        passA = True
                                        passB = True
                                        if len(RelEval(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                            passA = False
                                        if len(RelEval(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                            passB = False
                                        if passA == True and passB == True:
                                            HStar.append(L)
                                    #print("ok check out H*!",HStar)
                                else:
                                    HStar = Larger
                                #print("DATA =======")
                                #print("smaller", WLOG)
                                #print("Larger", Larger)
                                #print("Vertex_Max",Vertex_Max)
                                #print("rchiINT",rchiINT(Vertex_Max))
                                #print("Minv_",Minv_(rchiINT(Vertex_Max)))
                                #print("Indexer IS THE PROBLEM",Indexer)
                                #print("LinkPool",LinkPool)
                                #print("AutoCheck",AutoCheck)
                                #print("phi",PhiConstruct(Indexer,LinkPool,AutoCheck))
                                #print("Compose",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))
                                #print("DATA END =-=========")
                                #print("=======died at 100MB", Minv_(rchiINT(Vertex_Max)))
                                #print("more stats", PhiConstruct(Indexer,LinkPool,AutoCheck))
                                #print("ok?",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))

                                AD1 = AddressFunc(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                                AD2 = AddressFunc(Minv_(rchiINT(Vertex_Max)),HStar)
                                #print("stats")
                                #print(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                                #print(Minv_(rchiINT(Vertex_Max)),HStar)
                                #print("AD checks prior",AD1,AD2)
                                #print("======= DIED END")
                            else:
                                #time to check SI:
                                AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                                AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                        else:
                            #time to check SI:
                            AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                            AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                        #print("ADchecks",AD1,AD2)
                        #print("tobin AD1","{0:b}".format(AD1)[::-1])
                        #print("tobin AD2","{0:b}".format(AD2)[::-1])
                        #print("LessthanC",LessThan_C(AD1,AD2)) 
                        if LessThan_C(AD1,AD2):
                            return [True,PhiConstruct(Indexer,LinkPool,AutoCheck)]
            NumberIndex = NumberNew
        else:
            for H in range(0,G):
                NumberIndex.append([H])
                if len(LinkList) == 1:
                    #print("should test tiny SI with",NumberIndex)
                    Indexer = []
                    #Phiconstruct needs Indsx ran: [node,elem]
                    i = 0
                    for K in range(0,len(LinkList)):
                        Indexer.append([LinkPoolList[i][0],H])
                        i += 1
                    #print("Indexer is ", Indexer)
                    #print("Phiconstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                    #If |V_H| > |V_G|, then construct H* to use instead:
                    if len(Vertex_(Larger)) > len(Vertex_(WLOG)):
                        #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                        HStar = []
                        for L in Larger:
                            passA = True
                            passB = True
                            if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                passA = False
                            if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                passB = False
                            if passA == True and passB == True:
                                HStar.append(L)
                        #print("ok check out H*!",HStar)
                    else:
                        HStar = Larger
                    tryit = True
                    try: 
                        ListItems[1]
                    except IndexError:
                        tryit = False
                    if tryit == True:
                        if ListItems[1] == "Auto":
                            Vertex_Max = '0'
                            for NUM in Vertex_(WLOG) + Vertex_(Larger):
                                if int(NUM) > int(Vertex_Max):
                                    Vertex_Max = str(NUM)
                            #print("parts for AD1",WLOG)
                            #print("Larger",Larger)
                            #print("Indexer",Indexer)
                            #print("LinkPool",LinkPool)
                            #print("PhiConstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                            #print("basis",Minv_(rchiINT(Vertex_Max)))
                            #print("compose",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))
                            AD1 = AddressFunc(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                            AD2 = AddressFunc(Minv_(rchiINT(Vertex_Max)),HStar)
                        else:
                            #time to check SI:
                            AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                            AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                    else:
                        #time to check SI:
                        AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                        AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar) 
                    #print("ADchecks",AD1,AD2)
                    #print("tobin AD1","{0:b}".format(AD1)[::-1])
                    #print("tobin AD2","{0:b}".format(AD2)[::-1])
                    #print("LessthanC",LessThan_C(AD1,AD2))

                    if LessThan_C(AD1,AD2):
                        return [True,PhiConstruct(Indexer,LinkPool,AutoCheck)]
    return ["Assume False"]

def DEDAutoShittySI(E_G,E_H):
    '''
    don't use this function anymore because it's too hard to maintain two funcs
    Auto prefix means this just works on numbers only
    says if E_G SI to some E_J in E_H
    '''
    #if they're exact same they're SI
    if E_G == E_H:
        return [True, "same"]
    #else:
    if len(E_G) < len(E_H):
        WLOG = E_G
        Larger = E_H
    else:
        WLOG = E_H
        Larger = E_G

    #print("REMEMBER TO ADD ZEROLINKS TO EDGESORTbyLINKS")
    #print(WLOG)
    #print(Larger)
    #print(EdgeSortbyLinks(WLOG))
    #print(EdgeSortbyLinks(Larger))
    #print(LinkPoolGen(EdgeSortbyLinks(WLOG),EdgeSortbyLinks(Larger)))

    LinkPool = LinkPoolGen(EdgeSortbyLinks(WLOG),EdgeSortbyLinks(Larger))
    
    #add Zerolinks to LinkPoolGen
    #a zeronode is a node that doesn't actually link to anything (just recieves links in the graph)
    #just check LinkPool VS Vertex_(WLOG)
    #print("ran keys",ranDict(LinkPool)) 
    ZeroNodes = [x for x in Vertex_(WLOG) if x not in ranDict(LinkPool)]
    #print("Zeronodes?",ZeroNodes) 
    for x in ZeroNodes:
        LinkPool[x] = Vertex_(E_H)
    #print("LinkPool+Zeronodes?",LinkPool)

    #make sure LinkPool lists contain each other when you go down the list
    LinkPoolList = []
    for x in LinkPool:
        #print("LPL start",LinkPoolList)
        if len(LinkPoolList) == 0:
            LinkPoolList.append([x,LinkPool[x]])
        else:
            for y in LinkPoolList:
                Linked = False
                if len(LinkPool[x]) <= len(y[1]):
                    LinkPoolList = InsertAt(LinkPoolList,[x,LinkPool[x]],LinkPoolList.index(y)) 
                    #print("LPL Insert",LinkPoolList)
                    Linked = True
                    break
                #append at end if largest
                if Linked == False:
                    LinkPoolList = LinkPoolList + [[x,LinkPool[x]]]
        #print("LPL end",LinkPoolList)
    #print("check LinkPoolList",LinkPoolList)

    LinkSize = []
    LinkList = []
    #LinkSize is the size of each list in LinkPool
    #need to subtract 1 each time we append to LinkSize because we are making a choice and excluding them from the rest
    #LinkPool is the corresponding list at the right index
    i = 0
    for x in LinkPoolList:
        LinkSize.append(len(x[1])-i)
        i += 1
        LinkList.append(x[1])
    #print("check linksize",LinkSize)
    #print("check linklist",LinkList)

    NumberIndex = []
    for G in LinkSize:
        if len(NumberIndex) > 0:
            NumberNew = []
            for H in range(0,G):
                for J in NumberIndex:
                    Appendage = J + [H]
                    NumberNew.append(Appendage)
                    if len(Appendage) == len(LinkPool):
                        Indexer = []
                        #Phiconstruct needs Indsx ran: [node,elem]
                        i = 0
                        for K in Appendage:
                            Indexer.append([LinkPoolList[i][0],Appendage[i]])
                            i += 1
                        #print("here we test SI iwth",Appendage)
                        #print("Indexer is", Indexer)
                        #print("PhiConstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                        #If |V_H| > |V_G|, then construct H* to use instead:
                        if len(Vertex_(Larger)) > len(Vertex_(WLOG)):
                            #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                            HStar = []
                            for L in Larger:
                                passA = True
                                passB = True
                                if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                    passA = False
                                if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                    passB = False
                                if passA == True and passB == True:
                                    HStar.append(L)
                            #print("ok check out H*!",HStar)
                        else:
                            HStar = Larger
                        #time to check SI:
                        AD1 = AddressFunc(Compose(Minv_(rchi(Larger)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                        AD2 = AddressFunc(Compose(Minv_(rchi(Larger)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                        if LessThan_C(AD1,AD2):
                            return [True,PhiConstruct(Indexer,LinkPool,AutoCheck)]
            NumberIndex = NumberNew
        else:
            for H in range(0,G):
                NumberIndex.append([H])
                if len(LinkList) == 1:
                    #print("should test tiny SI with",NumberIndex)
                    Indexer = []
                    #Phiconstruct needs Indsx ran: [node,elem]
                    i = 0
                    for K in range(0,len(LinkList)):
                        Indexer.append([LinkPoolList[i][0],H])
                        i += 1
                    #print("Indexer is ", Indexer)
                    #print("Phiconstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                    #If |V_H| > |V_G|, then construct H* to use instead:
                    if len(Vertex_(Larger)) > len(Vertex_(WLOG)):
                        #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                        HStar = []
                        for L in Larger:
                            passA = True
                            passB = True
                            if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                passA = False
                            if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                passB = False
                            if passA == True and passB == True:
                                HStar.append(L)
                        #print("ok check out H*!",HStar)
                    else:
                        HStar = Larger
                    #time to check SI:
                    AD1 = AddressFunc(Compose(Minv_(rchi(Larger)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                    AD2 = AddressFunc(Compose(Minv_(rchi(Larger)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                    if LessThan_C(AD1,AD2):
                        return [True,PhiConstruct(Indexer,LinkPool,AutoCheck)]
    return [False, "no idea"]


def pairfinder(string,charpair):
    #delete pairs:
    thefuckinganswer = []
    i = 1
    #we start at 1 because we are already using for loop AKA for loop assumes we already have 1 level
    index = 0
    maxi = 0
    for x in string:
        if x == charpair[0]:
            thefuckinganswer.append([index,i])
            if i > maxi:
                maxi = i
            i+= 1
        if x == charpair[1]:
            i= i - 1
            thefuckinganswer.append([index,i])
        index += 1
    return [thefuckinganswer,maxi]

def pairfinderSTRING(finderlist,string):
    '''
    takes pairfinder and the original string and returns the right morphemes
    '''
    ANS = []
    Indexers = {}
    for y in range(1,finderlist[1]+1):
        Indexers[y] = []
    for x in finderlist[0]:
        #print("flist", finderlist)
        #print("cstats", x, Indexers[x[1]],x[0])
        '''
        why is Indexers[x[1]] have a keyerror wtf
        '''
        Indexers[x[1]].append(x[0])
    for y in range(1,finderlist[1]+1):
        for z in range(0,len(Indexers[y])):
            if z % 2 == 0:
                ANS.append(string[Indexers[y][z]:Indexers[y][z+1]+1])
    return ANS

def Cheat(string):
    #take a string and return a list of strings that represent the important morphemes:
    #punctuation:
    
    #line break
    #paragraph break(?)
    
    #FUCKING USE CASES FOR "'"
    Morphemes = []
    
    sentencedelimiters = [".", "?", "!"] #...
    SentenceStartPos = 0
    SentenceStartPosList = []
    #every even is start and odd is close for each pair
    pairdelimiters=["(", ")", "{", "}", "[", "]", "\"", "\"", " ", " "]
    pairdelimiterpos={}
    #EACH PAIR CHAR NEEDS ITS OWN START POS
    for pair in pairdelimiters:
        #use dictionaries
        pairdelimiterpos[pair + "On"]= 0
        pairdelimiterpos[pair + "Location"]= [-1]
        #starts at -1 so that it gets the first word even though there is no space[might be a problem]
        pairdelimiterpos[pair + "List"]= []

    pairdelimiterpos["AllList"] = [-1,-1]
    #starts at -1 so that it gets the first word even though there is no space[might be a problem]

    splicedelimiters=[",", ";", ":", "-", "\n"]
    SpliceStartPos = 0

    for g in range(0,len(pairdelimiters)):
        if g % 2 == 0 and pairdelimiters[g] != " ":
            toappend = pairfinderSTRING(pairfinder(string,[pairdelimiters[g],pairdelimiters[g+1]]),string)
            if len(toappend) != 0:
                Morphemes.append(toappend)

    
    i = 0
    for x in string:
        if i == len(string)-1:
            #check if last morpheme is already in the list:
            inside = 0
            try:
                Morphemes.index(string[pairdelimiterpos["AllList"][-1]+1:])
            except(ValueError,IndexError):
                #print("already inside!","\n",string[pairdelimiterpos["AllList"][-1]+1:],"\n", Morphemes)
                inside = 1
            if inside == 0:
                #get the last morpheme:
                Morphemes.append(string[pairdelimiterpos["AllList"][-1]+1:])
        #you need a hierarchy to get sentence start pos to ignore pairdelimiter rules
        if x in splicedelimiters:
            if max(SentenceStartPos,SpliceStartPos) in range(pairdelimiterpos["AllList"][-2],pairdelimiterpos["AllList"][-1]+1) and len(pairdelimiterpos["AllList"])>=4:
                #find one that isn't in most recent pair
                k = 1
                for y in SentenceStartPosList:
                    K = len(SentenceStartPosList)
                    if SentenceStartPosList[K-k] not in range(pairdelimiterpos["AllList"][-2],pairdelimiterpos["AllList"][-1]+1):
                        delimstart = SentenceStartPosList[K-k]
                    else:
                        delimstart = 0
                    k += 1
            else:
                delimstart = max(SentenceStartPos,SpliceStartPos)
            Morphemes.append(string[delimstart:i+1])
            #keep track of everything
            pairdelimiterpos["AllList"].append(i)
            SpliceStartPos = i
        if x in pairdelimiters:
            '''
            THEY ARE BEING TREATED AS A SINGLE INSTEAD OF AS A PAIR
            '''
            if x == " " or x == "\"":
                #append the slice from the last location to this location
                Morphemes.append(string[pairdelimiterpos[x + "Location"][-1]+1:i])
                #make note of the last location
                pairdelimiterpos[x + "Location"].append(i)
                #keep track of everything
                pairdelimiterpos["AllList"].append(i)
            else:
                #if it's on for this particular character, slice the string then turn off
                if pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "On"] == 1:
                    pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "On"] = 0
                    #slice the string and append to Morphemes
                    Morphemes.append(string[pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "Location"][-1]:i+1])
                    #add to both location lists
                    pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "Location"].append(i)
                    #keep track of everything
                    pairdelimiterpos["AllList"].append(i)
                else:
                    pairdelimiterpos[x + "Location"].append(i)
                #be smart about how to turn this on:
                if pairdelimiters.index(x)%2 == 0:
                    pairdelimiterpos[x + "On"] = 1
        if x in sentencedelimiters:
            #know the last .?! , (if any) then cut between first and last .?!
            #ignore pair delimiters
            if SentenceStartPos in range(pairdelimiterpos["AllList"][-2],pairdelimiterpos["AllList"][-1]+1) and len(pairdelimiterpos["AllList"])>=4:
                #find one that isn't in most recent pair
                k = 1
                for y in SentenceStartPosList:
                    K = len(SentenceStartPosList)
                    if SentenceStartPosList[K-k] not in range(pairdelimiterpos["AllList"][-2],pairdelimiterpos["AllList"][-1]+1):
                        delimstart = SentenceStartPosList[K-k]
                    else:
                        delimstart = 0
                    k += 1
            else:
                delimstart = SentenceStartPos
            Morphemes.append(string[delimstart:i+1])
            #keep track of everything
            pairdelimiterpos["AllList"].append(i)
            #NEW
            #adding this line since words "stuck" next to punctuation get lost:
            #Morphemes.append(string[pairdelimiterpos["AllList"][-1]:i+1])
            
            SentenceStartPos = i+1
            SentenceStartPosList.append(i+1)
        i += 1
    #Morphemes
    return Morphemes

'''
Gödel's incompleteness theorems are two theorems of mathematical logic that demonstrate the inherent limitations of every formal axiomatic system containing basic arithmetic. These results, published by Kurt Gödel in 1931, are important both in mathematical logic and in the philosophy of mathematics. The theorems are widely, but not universally, interpreted as showing that Hilbert's program to find a complete and consistent set of axioms for all mathematics is impossible.

The first incompleteness theorem states that no consistent system of axioms whose theorems can be listed by an effective procedure (i.e., an algorithm) is capable of proving all truths about the arithmetic of the natural numbers. For any such formal system, there will always be statements about the natural numbers that are true, but that are unprovable within the system. The second incompleteness theorem, an extension of the first, shows that the system cannot demonstrate its own consistency.

Employing a diagonal argument, Gödel's incompleteness theorems were the first of several closely related theorems on the limitations of formal systems. They were followed by Tarski's undefinability theorem on the formal undefinability of truth, Church's proof that Hilbert's Entscheidungsproblem is unsolvable, and Turing's theorem that there is no algorithm to solve the halting problem.
'''
#print("CHECKING CHEAT FUNC")
#print(Cheat("Gödel's incompleteness theorems are two theorems of mathematical logic that demonstrate the inherent limitations of every formal axiomatic system containing basic arithmetic. These results, published by Kurt Gödel in 1931, are important both in mathematical logic and in the philosophy of mathematics. The theorems are widely, but not universally, interpreted as showing that Hilbert's program to find a complete and consistent set of axioms for all mathematics is impossible."))
#print(Cheat("printpls('testthis')"))
'''
^^^ MORPHEME PICKING IS CURRENTLY A FUCKING PROBLEM ESP WITH printpls('testthis')
'''




'''
this function is already deprecated since we aren't using gigantic lists anymore
'''


def BasisFix(inp,basis):
    '''
    this fixes basis so I can call address whenever
    '''
    for char in inp:
        #if stuff is not in the basis:
        if char in basis:
            pass
        else:
            #append to basis
            basis.append(char)
    if len(inp) in basis:
        pass
    else:
        for k in range(len(inputtext)+1):
            if str(k) in basis:
                pass
            else:
                basis.append(str(k))
    return

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

def tailREADLINES(argList):
    '''
    HINT:
    I only look at last line anyways, so I can just use linecache module + maxlines to get last line
    
    I need to avoid this function because it uses readlines()
    ALSO: THIS USES FUCKING .readlines() for some fucking reason, so this is automatically fucking bad.
    '''
    
    #[fname, lines, _buffer=4098]
    f = open(argList[0],'r+')
    lines = argList[1]
    #_buffer = 4098
    #try smaller buffer
    _buffer = 128
    
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

        lines_found = rchop(f.readlines(), '\n')

        # we found enough lines, get out
        # Removed this line because it was redundant the while will catch
        # it, I left it for history
        # if len(lines_found) > lines:
        #    break

        # decrement the block counter to get the
        # next X bytes
        block_counter -= 1

    #close file
    f.close()
    return lines_found[-lines:]
    
    
def tailOpened(argList):
    '''
    THIS IS DEPRECATED USE tail instead

    
    this version is for Construct PNXN lines because I read that catching a failure with exception is expensive
    '''
    #[fname, lines, _buffer=4098]
    #f = open(argList[0],'r+')
    f = argList[0]
    lines = argList[1]
    _buffer = 4098
    #try smaller buffer
    #_buffer = 128
    
    """Tail a file and get X lines from the end"""
    # place holder for the lines found
    lines_found = []

    # block counter will be multiplied by buffer
    # to get the block size from the end
    block_counter = -1

    # loop until we find X lines
    while len(lines_found) < lines:
        try:
            print("io.UnsupportedOperation: can't do nonzero end-relative seeks",block_counter, _buffer,block_counter * _buffer, os.SEEK_END)
            f.seek(block_counter * _buffer, os.SEEK_END)
        except IOError:  # either file is too small, or too many lines requested
            f.seek(0)
            lines_found = f.readlines()
            print("fucking readlines I'm stupid", len(lines_found))
            break

        lines_found = rchop(f.readlines(), '\n')

        # we found enough lines, get out

        # decrement the block counter to get the
        # next X bytes
        block_counter -= 1

    #close file
    #f.close()
    return lines_found[-lines:]

def FILEindexread(argList):
    '''
    Arglist is:
    arg1 = fileNAME
    arg2 = line index to read (starts from 0)

    HINT: THIS REMOVES TRAILING NEWLINE

    #FILENAME
    arg1 = argList[0]
    #INDEX TO READ
    arg2 = int(float(argList[1]))    
    #print("what is getline and args", argList, isinstance(arg2, int), getline(arg1,arg2))
    #print("IM FUCKING PRINTING EVERYTHING")
    #wtf = open(arg1,"r+")
    #print(wtf.read())
    #wtf.close()
    #print("IM FUCKING PRINTING EVERYTHING/")
    ANS = rchop(getline(arg1,arg2), '\n')
    #print("IS ANSWER BUSTED?", ANS)
    return ANS

    #PROBLEMS: LINECACHE PUTS FILE IN CACHE SO IT DOESNT SEE CHANGES AND IT HITS MEMORY MAX TOO FAST
    HINT: I FOUND A FUCKING MODULE THAT DOES THIS: linecache
    '''
    f = open(argList[0],'r+')
    n = argList[1]
    f.seek(0)
    for i, line in enumerate(f):
        #print("newtail stats", i, n, line, )
        if i == n:
            f.close()
            #return line.strip()
            return rchop(line, "\n")
    
def fileindex(argList):
    '''
    arg1 = fileNAME
    arg2 = string to check index of
    this gets first index of string with respect to filestream
    RETURNS: None if fail or integer if there is index
    '''
    arg1 = open(argList[0],'r+')
    arg2 = argList[1]
    
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
        if arg2 + "\n" == str(x):
            return i
        i += 1
    #if we get here then we need to append to basis then return answer
    #print("why is basis appending twice? I should be closing the file and rereading wtf",argList)
    arg1.seek(0, 2)
    arg1.write(arg2 + "\n")
    
    arg1.close()
    return i + 1

def fileindexINV(argList):
    '''
    arg1 = filestream (don't want to fuck with this right now)
    arg2 = INDEX NUMBER
    this gets first index of string with respect to filestream
    RETURNS: None if fail or integer if there is index
    also this is just to make shit look good I should just be using the tail function but whatever
    '''
    arg1 = argList[0]
    arg2 = argList[1]
    #openedwhy = open(arg1,'r+')
    #ANS = tail(openedwhy, arg2, 0)
    #openedwhy.close()
    ANS = FILEindexread([arg1,arg2])
    return ANS

def rchop(thestring, ending):
    if thestring.endswith(ending):
        return thestring[:-len(ending)]
    return thestring

def lexicoSortHARD(argList):
    '''
    HINT: this function linearly orders a file that is a list of lines with respect to some basis
    
    since I am forced to order the unordered list the hard way I might as well write this func
    arg1 = basis file name (WITH EXTENSION)
    arg2 = UNORDERED memory file name (WITH EXTENSION)
    PLAN:
    rename arg2 then have an empty file
    for each line in the renamed arg2 file, use bisectioninsert into clean arg2 file
    '''
    #arg1 = basis file name
    arg1 = argList[0]
    #arg2 = UNORDERED memory file name
    arg2 = argList[1]
    #get max linecount for arg2
    arg2MaxLines = mapcountLINES([arg2])
    #HINT: INDEX STARTS AT 1!!!!!!!, so for x in range (0,maxlines) is ok!!
    #arg2MovedName = arg2[:-4]+ "old" + arg2[-4:]
    #similarly assume extension is after last period:
    namelist = arg2.split(".")[:-1]
    thename = "".join(namelist)
    arg2MovedName = thename + "old." + arg2.split(".")[-1]
    print("namehere",arg2MovedName)
    #rename arg2 file
    os.rename(arg2, arg2MovedName)
    #open renamed file
    arg2MovedOpen = open(arg2MovedName,'r+')
    #have clean arg2 file
    arg2Clean = open(arg2,'a+')
    #close so I can insert
    arg2Clean.close()
    #for each line in the renamed arg2 file, use bisectioninsert into clean arg2 file
    for x in range (0, arg2MaxLines):
        #insertstring = arg2MovedOpen.readline().strip()
        insertstring = rchop(arg2MovedOpen.readline(), '\n')
        ########print("what is obj?",insertstring)
        bisectionInsert([arg2,insertstring,arg1])
    #close renamed file
    arg2MovedOpen.close()
    #remove renamed file
    os.remove(arg2MovedName)
    
def lexicoSort(argList):
    '''
    need function that does lexicographic ordering on ORDERED AND UNORDERED memory files using basislist
    arg1 = basis FILENAME
    arg2 = linearly ordered memory FILENAME in open(filename,???) format
        HINT: arg2 can be an empty file
    arg3 = unordered memory FILENAME

    stats:
    >linearly ordered memory
    >linearly UNordered memory
    >basislist

    strategy:
    attempt to append from unordered to ordered
    keep the pairs: [obj,index]
    figure out the offset

    then in one go, just rewrite and append properly

    plan:
    >on bisectioninsert/min, add a flag
    then on bisectioninsertmin if flag is true, then instead of writing, just return the pair: [obj,index]
        >look at .write()
        and fileinsertat

        if len(arg) > 0:
            return [obj,index]
        else:
            #write shit
    
    then on lexico sort, change the argument to include the unordered memory
    
    do a 'hard' sort on the unordered memory so insertion order doesn't matter
    =
    attempt to append from recentlyordered to ordered
    figure out the offset
    write stuff down in one go


    PROBLEM:
    INSERTING UNORDERED LIST INTO ORDERED LIST THAT IS EMPTY
    THEN YOU INSERT IN ORDER OF INSERTION WHICH IS NOT ACCORDING TO ORDER
    HINT:
    ORDER UNORDERED LIST FIRST,THEN INSERT INTO ORDERED LIST
    hint: order unordered list in the 'hardcore' mode, aka just rewriting file and renaming so you guarantee insertion is ok
    '''

    #arg1 = basis file name
    arg1 = argList[0]
    #arg2 = linearly ordered memory file NAME in open(filename,???) format
    #    HINT: arg2 can be an empty file
    arg2 = argList[1]
    #arg3 = unordered memory file name
    arg3 = argList[2]
    #hard sort the unordered memory file
    lexicoSortHARD([arg1,arg3])
    print("lexicosorthard done")
    #get maxlines of recently ordered file
    arg3maxlines = mapcountLINES([arg3])
    #get maxlines for ordered memory file
    arg2maxlines = mapcountLINES([arg2])
    #hint, range(start,max) is to -1 of max, and since maxlines index starts at 1 you have your +1 already
    #hint: 'with' keyword automatically closes opened files
    #append from recentlyordered to ordered
    
    with open(arg3,'r+') as recentlyordered:
        #USE A NEW FILE TO STORE INSERTION DATA FROM RECENTLY ORDERED TO MEMFILE
        InsertKey = open("InsertKey.txt",'a+')
        #hint: I STILL HAVEN'T ATTEMPTED TO INSERT FROM RECENTLYORDERED TO MEMFILE
        for x in range(0,arg3maxlines):
            #strippin = recentlyordered.readline()
            #print("obj before strip!",strippin)
            #OBJ = strippin.strip()
            OBJ = rchop(recentlyordered.readline(), "\n")
            #print("obj after strip!",OBJ)
            insertlineprep = str(bisectionInsert([arg2,OBJ,arg1,[1]]))
            ########print("bisection args",[arg2,OBJ,arg1,[1]])
            #print("wtf is going on",str(bisectionInsert([arg2,OBJ,arg1,[1]])))
            #print("what is being written as None?", insertlineprep)
            insertlinewrite = insertlineprep+"\n"
            ########print(insertlinewrite)
            if insertlineprep == "5WRONG":
                print("force stop")
                return
            InsertKey.write(insertlinewrite)
        ########print("THIS IS INSERTKEYSTART===============================================")
        InsertKey.seek(0)
        ########print(InsertKey.read())
        #InsertKey.seek(0)
        #print("check first line strat!",InsertKey.readline())
        timetostop = mapcountLINES(["InsertKey.txt"])
        ########print("THIS IS INSERTKEYEND===============================================")
        #rename memfile
        namelist = arg2.split(".")[:-1]
        arg2rename = "".join(namelist) + "NEW" + arg2.split(".")[-1]
        print("arg2rename",arg2rename)
        os.rename(arg2,arg2rename)
        #rewrite MEMFILE
        #open renamed memfile
        ########print("=============================================")
        #hint: we know that Insertkey is ordered as insertion from recentlyordered to memfile, so we can just match the index with Insertkey
        #hint: offset is just +1 for each line you have already inserted #NEWHINT: don't need offset anymore
        InsertKey.seek(0)
        insertline = InsertKey.readline()
        ########print("insertline is", insertline)
        try:
            insertionkey = ast.literal_eval(insertline)[0][1]
            insertionline = ast.literal_eval(insertline)[0][0]
            ########print("what is insertionline?1", insertionline)
        except:
            pass
        stopwhen = 1
        
        with open(arg2rename,'r+') as MEMFILEOLD:
            #open clean memfile
            MEMFILECLEAN = open(arg2,'a+')
            for x in range(0,arg2maxlines+1):
                #strategy:
                #open renamed file and when we hit insertion index of InsertKey, we insert until we run out of renamed file
                ########print("qhat about max lines?",arg2maxlines,arg3maxlines)
                ########print("readline from memfileold")
                OGline = MEMFILEOLD.readline()
                ########print("go to ???")
                ########print(x,insertionkey)
                ########print("if x == insertionkey:", x , insertionkey)
                if x == insertionkey:
                    ########print("sanity check1",x,insertionkey,stopwhen, timetostop)
                    MEMFILECLEAN.write(insertionline + "\n")
                    ########print("readline is RESET to next line after I write")
                    insertline = InsertKey.readline()
                    stopwhen += 1
                    ########print(insertline)
                    try:
                        insertionkey = ast.literal_eval(insertline)[0][1]
                        insertionline = ast.literal_eval(insertline)[0][0]
                        ########print("what is insertionline?2", insertionline)
                        ########print("2:",x,insertionkey)
                    except:
                        pass
                    ########print("check if next line is the same index",insertionkey)
                    while x == insertionkey and stopwhen <= timetostop:
                        ########print("sanity check2",x,insertionkey,stopwhen, timetostop)
                        #yes = insert
                        MEMFILECLEAN.write(insertionline + "\n")
                        ########print("attempt to read another line")
                        insertline = InsertKey.readline()
                        stopwhen += 1
                        ########print(insertline)
                        '''
                        lastinsert = str(tail(InsertKey,1,0)[0])
                        print(" AND is not last line", insertline + "|VS|")
                        print(lastinsert)
                        print("OR last line is empty NOT DONE YET")
                        print(insertline)
                        if insertline == lastinsert:
                            break
                        '''
                        try:
                            insertionkey = ast.literal_eval(insertline)[0][1]
                            insertionline = ast.literal_eval(insertline)[0][0]
                            ########print("what is insertionline?3", insertionline)
                            ########print("3:",x,insertionkey)
                        except:
                            pass
                        #no = keep variable for later
                    MEMFILECLEAN.write(OGline)
                    #read new line
                else:
                    ########print("sanity check3",x,insertionkey)
                    MEMFILECLEAN.write(OGline)
    #hint: remember to delete InsertKey
    InsertKey.close()
    os.remove(InsertKey.name)
    #REMEMBER TO DELETE RENAMED MEMFILE
    os.remove(arg2rename)
    #delete UNORDERED file so that you don't duplicate stuff

def mapcountLINES(argList):
    '''
    this function counts lines in a file using mmap
    arg1 is file name
    HINT: INDEX STARTS AT 1!!!!!!!
    '''
    arg1 = open(argList[0], 'r+')
    #just make sure
    arg1.seek(0)
    buf = mmap.mmap(arg1.fileno(), 0)
    lines = 0
    readline = buf.readline
    #print("what does readline see?",readline())
    while readline():
        lines += 1
    arg1.close()
    return lines

def shittySearch(argList):
    '''
    HINT: BASE 0
    why not
    arg1 = fileNAME to search for
    arg2 = obj to search
   
    '''
    #arg1 = fileNAME
    arg1 = argList[0]
    #arg2 = obj to insert
    arg2 = argList[1]
    ANS = []
    index = 0
    with open(arg1,"r+") as hotPotato:
        line = rchop(hotPotato.readline(), '\n')
        while line:
            #print("line vs arg2")
            try:
                a1 = str(eval(line))
                a2 = arg2
                #print(a1, type(a1))
                #print(a2, type(a2))
                #print(a1 == a2)
                if a1 == a2:
                    ANS.append(index)
            except:
                pass
            line = rchop(hotPotato.readline(), '\n')
            index += 1
    return ANS

#print("bullyhunters omegalul",shittySearch(['MemoryUnordered.txt',str([['argument_1 == "b"', 'd'],['argument_2 == "AF"', 'Y'],[str('TOTAL_ARGUMENT' + '==' + str(['f','AF'])),'TOTALCHECK']])]))

def bisectionSearch(argList):
    '''
    HINT: BASE 0
    why not
    arg1 = fileNAME to search for
    arg2 = obj to search
    arg3 = basisNAME for addressfunc 
    HINT: YOU NEED TO APPLY THIS SET TO AN ALREADY LINEAR LIST (or else address(x)< address(y) < address(z) won't work)
   
    '''
    #arg1 = fileNAME
    arg1 = argList[0]
    #arg2 = obj to insert
    arg2 = argList[1]
    #arg3 = basisNAME
    arg3 = argList[2]
    #assume arg4 since we want search
    arg4 = [1]

    #get right hand side index (LHS index is 0)
    #total = mapcountLINES([arg1])-1
    #can't map an empty file for some reason\
    try:
        total = mapcountLINES([arg1])-1
    except ValueError:
        if len(arg4) > 0:
            #return empty answer
            return []
        return "WRONGWHY"
    #figure out where it SHOULD be:
    shouldbe = bisectionInsertmin([0,total,arg1,arg3,arg2,arg4])[0][1]
    ###########print("OG is", arg2)
    ###########print("shouldbe",shouldbe)

    #assume no answer:
    ANS = []
    ###########print("check AT",FILEindexread([arg1,shouldbe]))
    if arg2 == FILEindexread([arg1,shouldbe]):
        ANS.append(shouldbe)
    filler = 1
    ###########print("check LEFT AS FAR AS YOU CAN")
    while True:
        try:
            ###########print("leftstrats",filler, shouldbe-filler,FILEindexread([arg1,shouldbe-filler]))
            ###########print(arg2)
            ###########print(arg2 == FILEindexread([arg1,shouldbe-filler]))
            if arg2 == FILEindexread([arg1,shouldbe-filler]):
                ANS.append(shouldbe-filler)
                filler += 1
            else:
                break
        except:
            break
    filler = 1
    #check RIGHT AS FAR AS YOU CAN
    while True:
        try:
            if arg2 == FILEindexread([arg1,shouldbe+filler]):
                ANS.append(shouldbe+filler)
                filler += 1
            else:
                break
        except:
            break
        
    #return the index/indicies OR NO ANSWER [] (which is empty list)
    #sort answer for niceness
    ANS = sorted(ANS, key=int)
    return ANS

def bisectionInsert(argList):
    '''
    need this because lexicosort on a bajillion number comparisons is just dumb
    arg1 = fileNAME to insert to 
    arg2 = obj to insert
    arg3 = basisNAME for addressfunc 
    HINT: YOU NEED TO APPLY THIS SET TO AN ALREADY LINEAR LIST (or else address(x)< address(y) < address(z) won't work)
    
    arg4 = existence flag. basically if this exists we have bisectioninsert/min print insertion data [obj,index] instead of attempting to print
    '''
    #arg1 = fileNAME
    arg1 = argList[0]
    #arg2 = obj to insert
    arg2 = argList[1]
    #arg3 = basisNAME
    arg3 = argList[2]
    #arg4 = existence flag. basically if this exists we have bisectioninsert/min print insertion data [obj,index] instead of attempting to print
    #EX: [1] since I check for len > 0 so use a list or smth!
    try:
        arg4 = argList[3]
    except:
        #[] is basically null answer
        #hint:  len([]) == 0
        arg4 = []
    #get right hand side index (LHS index is 0)
    #total = mapcountLINES([arg1])-1
    #can't map an empty file for some reason\
    try:
        total = mapcountLINES([arg1])-1
    except ValueError:
        if len(arg4) > 0:
            return [arg2,0]
        else:
            #write shit
            #assume file is size 0
            #init the file instead
            arg1file = open(arg1,'r+')
            arg1file.write(arg2 + "\n")
            arg1file.close()
            #print("should insert arg2",arg2,arg1)
        return
    return bisectionInsertmin([0,total,arg1,arg3,arg2,arg4])
    

def bisectionInsertmin(argList):
    '''
    need this because lexicosort on a bajillion number comparisons is just dumb
    
    #needs:
    LHSINDEX
    RHSINDEX
    filestream to insert to (form= open('filename', 'r+'))
    basisstream for addressfunc (form= open('filename', 'r+'))
    OBJTOINSERT (is a string)

    what this does:
    either: writes to file
    OR
    calls itself with new LHS/RHS
    (it's guaranteed to terminate b/c if I write it properly it should 'run out of space' on a linearly ordered listing)

    HINT: YOU NEED TO APPLY THIS SET TO AN ALREADY LINEAR LIST (or else address(x)< address(y) < address(z) won't work)
    HINT: file format is where each line is an obj 
    
    '''
    #LHSINDEX
    arg1 = argList[0]
    #RHSINDEX
    arg2 = argList[1]
    #fileNAME
    arg3 = argList[2]
    #basisNAME
    arg4 = argList[3]
    #the string OBJ to insert
    arg5 = argList[4]
    #arg6 = existence flag. basically if this exists we have bisectioninsert/min print insertion data [obj,index] instead of attempting to print
    try:
        arg6 = argList[5]
    except:
        #[] is basically null answer
        #hint:  len([]) == 0
        arg6 = []

    #need to know filename so I can reopen file
    data1 = arg1

    #get to floor(half of Left and Right)
    half = arg1+floor((arg2-arg1)/2)
    '''
    picture:
    ----
     ^ is half
    -----
      ^ is half
    so half is on the lower side so do half and half + 1

    HINT:
    check for this condition:
    address(half)< address(y) < address(half+1)
    #AddressFILE([basisfile,obj])

    do i use quine or not? (just be consistent. question: is M_ OR Q_ shorter on "average"??)
        USE M_
    
    how does [[1,1]] return an address when [1,[[1,1]]] AND [[1,1]] IS NOT IN BASIS
        is this a per char thing????
            ya it's a per char thing
            print("chars only?",M_(tail(arg3, half, 0))) -> [['0', '['], ['1', '['], ['2', '1'], ['3', ','], ['4', '1'], ['5', ']'], ['6', ']'], ['7', '\n']]

    EDGE CASE LIST:
    length of filestream is 0,1 lines
    should insert at beginning or end of file
    ???
    '''
    ##########print("stats",argList)

    #took care of size 0 in original function
    #print("if length is 1 (AKA index of 0), check boundaries")
    if arg2 == 0:
        #
        ##########print("#insert left? for size 0? (obj < line)",M_(arg5),M_(FILEindexread([arg3,0])),AddressFILE([arg4,M_(arg5)]) < AddressFILE([arg4,M_(FILEindexread([arg3,0]))]))
        if AddressFILE([arg4,M_(arg5)]) < AddressFILE([arg4,M_(FILEindexread([arg3,0]))]):
            ##########
            ##########print("insert1",len(arg6) > 0,[[arg5,0]])
            if len(arg6) > 0:
                return [[arg5,0]]
            else:
                #write shit
                FILEinsertAt([arg3,arg5,0])
            #print("inserted left")
        else:
            ##########
            ##########print("insert2")
            #print("insert right",len(arg6) > 0,arg6)
            if len(arg6) > 0:
                return [[arg5,1]]
            else:
                #write shit
                FILEinsertAt([arg3,arg5,1])
        return "1WRONG" + str(argList)

    #IF LENGTH >1, check edge cases first to save a lot of time
    #NOTE: I STILL ASSUME THAT INSERTION FILE IS LINEARLY ORDERED BY ADDRESS < IN THE FIRST PLACE

    #
    ##########print("check if obj < first line",M_(arg5),'<',M_(FILEindexread([arg3,0])))
    #
    ##########print(AddressFILE([arg4,M_(arg5)]) < AddressFILE([arg4,M_(FILEindexread([arg3,0]))]))
    if AddressFILE([arg4,M_(arg5)]) < AddressFILE([arg4,M_(FILEindexread([arg3,0]))]):
        ##########
        ##########print("insert3")
        #print("insert at front:")
        if len(arg6) > 0:
            return [[arg5,0]]
        else:
            #write shit
            FILEinsertAt([arg3,arg5,0])
        return "2WRONG" + str(argList)

    ##########
    #print("check if last line < obj",arg5)
    #FML TAIL IS OPENING FILE SO I NEVER CLOSE IT

    #print("omg so tail is slightly fucked?",tail(open(arg3,'r+'),1,0)[0])
    #print("check type",type(tail(open(arg3,'r+'),1,0)[0]) is str)
    #print("WTF???",M_(tail(open(arg3,'r+'),1,0)[0]))
    #print("FML",M_(arg5))
    
    openarg3 = open(arg3,'r+')
    #
    ##########print("check ineq",AddressFILE([arg4,M_(tail(openarg3,1,0)[0])]) < AddressFILE([arg4,M_(arg5)]))
    if AddressFILE([arg4,M_(tail(openarg3,1,0)[0])]) < AddressFILE([arg4,M_(arg5)]):
        ##########
        ##########print("insert4")
        if len(arg6) > 0:
            return [[arg5,mapcountLINES([arg3])]]
        else:
            #write shit
            #print("then insert after last obj",[arg3,arg5,mapcountLINES([arg3])])
            FILEinsertAt([arg3,arg5,mapcountLINES([arg3])])
        return "3WRONG" + str(argList)
    openarg3.close()
    
    #now for meat:
    #how to tell odd from even? index is 0 so normally odds are even now and normally evens are odd:
    '''
    mapcountLINES([filestream])
    ^NOT THIS ANYMORE
    it's per segment that I check, so maxlength is
    RHS-LHS is 'even' or not

    num % 2 == 0
        ODD
    else
        EVEN
    
    PLAN
    check on EVEN:
    HALF <= OBJ <= HALF+1
     -> LEFT      -> RIGHT

    check on ODD:
    HALF <= OBJ <= HALF+1
     -> LEFT
     
    HALF+1 <= OBJ <= HALF+2
                -> RIGHT
    ===============
    check fails:
    HALF < OBJ > HALF+1
     -> LEFT
     
    HALF+1 > OBJ > HALF+2
                -> RIGHT
    ===============
    check on ODD:
        CONFIRM THIS INEQ       NOT THIS
    HALF <= OBJ                 <= HALF+1
     -> LEFT

                    THEN ALL THAT MATTERS IS CONFIRMING THIS EQUALITY  SINCE WE KNOW OBJ > HALF+1
    HALF+1 <= OBJ <= HALF+2
                -> RIGHT
    '''

    #TAIL PROBLEMS print("check solns", AddressFILE([arg4,M_(tail(arg3, half, 0)[0])]) < AddressFILE([arg4,M_(arg5)]))
    #TAIL PROBLEMS print("check solns2",AddressFILE([arg4,M_(arg5)]) < AddressFILE([arg4,M_(tail(arg3, half+1, 0))]))

    ##########
    ##########print("check args half<= obj",FILEindexread([arg3, half]),arg5)
    ##########
    ##########print(AddressFILE([arg4,M_(FILEindexread([arg3, half]))]) <= AddressFILE([arg4,M_(arg5)]))
    if AddressFILE([arg4,M_(FILEindexread([arg3, half]))]) <= AddressFILE([arg4,M_(arg5)]):
        pass
    else:
        #print("go left", FILEindexread([arg3, half]) + " !<= " + arg5)
        #going left is basically choosing new LHS/RHS
        #know: LHS,RHS,HALF
        #going left means:
        #new LHS/RHS is: LHS,HALF
        return bisectionInsertmin([arg1,half,arg3,arg4,arg5,arg6])

    ##########
    ##########print("arglist",argList)
    ##########print("check this address(y) < address(half+1) \n",arg5 +"| VS |"+ FILEindexread([arg3, half+1]))
    ##########print("half is",half,FILEindexread([arg3, half]))
    ##########print("half+1 is",half+1,FILEindexread([arg3, half+1]))
    ##########print("half+2 is",half+2,FILEindexread([arg3, half+2]))
    ##########print(AddressFILE([arg4,M_(arg5)]) <= AddressFILE([arg4,M_(FILEindexread([arg3, half+1]))]))
    if AddressFILE([arg4,M_(arg5)]) <= AddressFILE([arg4,M_(FILEindexread([arg3, half+1]))]):
        #if this works AND IT'S EVEN MAX LENGTH
        #if (arg2 - arg1) % 2 == 1:
        if AddressFILE([arg4,M_(FILEindexread([arg3, half]))]) <= AddressFILE([arg4,M_(arg5)]) and AddressFILE([arg4,M_(arg5)]) <= AddressFILE([arg4,M_(FILEindexread([arg3, half+1]))]):
            ##########
            ##########print("insert5")
            if len(arg6) > 0:
                return [[arg5,half+1]]
            else:
                #write shit
                #
                ##########print("append properly on 1st check============",[arg3,arg5,half+1])
                FILEinsertAt([arg3,arg5,half+1])
                #+ str(argList)
            return "5WRONG" + str(argList)
        else:
            #
            ##########print("else go right", arg5 + " !<= " + FILEindexread([arg3, half+1]))
            return bisectionInsertmin([half,arg2,arg3,arg4,arg5,arg6])

    #if length is odd number you have to check half+1 and half+2

    #don't need to check HALF+1 <= OBJ since OBJ <= HALF+1 failed already
    ##########
    ##########print("check this address(y) < address(half+2) \n",arg5 +"| VS |"+ FILEindexread([arg3, half+2]))
    ##########
    ##########print(AddressFILE([arg4,M_(arg5)]) <= AddressFILE([arg4,M_(FILEindexread([arg3, half+2]))]))
    if AddressFILE([arg4,M_(arg5)]) <= AddressFILE([arg4,M_(FILEindexread([arg3, half+2]))]):
        ##########
        ##########print("insert6")
        if len(arg6) > 0:
            return [[arg5,half+2]]
        else:
            #write shit
            #print("append properly")
            FILEinsertAt([arg3,arg5,half+2])
        return "7WRONG" + str(argList)
    else:
        ##########
        ##########print("it's gold mine1",arg5, FILEindexread([arg3, half+2]))
        ##########
        ##########print("check argList",argList)
        ##########
        ##########print("else go right",[arg1+half,arg2,arg3,arg4,arg5])
        return bisectionInsertmin([half,arg2,arg3,arg4,arg5,arg6])
    
def FILEinsertAt(ArgList):
    '''
    function to insert text at a specific line in file
    arg1 = fileNAME
    arg2 = string to insert
    arg3 = index to insert at (index starts at 0)

    HINT: this closes the file to fileinput works
    needs 'import fileinput'
    '''
    arg1 = ArgList[0]
    #have to close this for fileinput to work
    #print("I tried closing it",arg1)
    arg2 = ArgList[1]
    arg3 = ArgList[2]
    #print('stats',ArgList)
    i = 0

    #open new file
    #print("shit arg1 might have .txt",arg1)
    #FILTER OUT FILEEXTENSION with [:-4] (assume length of extension is 3)
    #arg1New = open(arg1[:-4] + "1.txt",'a+')
    #new strat: just get everything before the last period (assume extension is after last period)
    namelist = arg1.split(".")[:-1]
    thename = "".join(namelist)
    print("thename",thename)
    arg1New = open(thename + "1.txt",'a+')

    #get max lines for old file (index starts at 1 so just -1 to get index 0)
    maxlines = mapcountLINES([arg1])

    #if index is within filemaxlength:
    if arg3 < maxlines:
        #print("write old file into new file line by line")
        with open(arg1,'r+') as arg1Old:
            #print("go until you hit max lines",maxlines)
            for x in range(0,maxlines):
                #print("when you get to the right index, insert")
                if x == arg3:
                    #print("where do I go?",i)
                    oldline = arg1Old.readline()
                    insertedline = arg2 + "\n"
                    #print("check oldnew stats", oldline)
                    #print("=")
                    #print(insertedline)
                    #print("=")
                    arg1New.write(insertedline)
                    arg1New.write(oldline)
                else:
                    #print("where do I go?2",i,arg3)
                    oldline = arg1Old.readline()
                    #print("checkoldline",oldline)
                    arg1New.write(oldline)
        #delete old file
        os.remove(arg1)
        #close file(s)
        #hint: arg1Old closed by with
        arg1New.close()
        #rename new file
        os.rename(arg1[:-4] + "1.txt",arg1)
    else:
        #if your index is past the maxlength:
        #print("insertstats", arg3,mapcountLINES([arg1]))
        diff = arg3 - mapcountLINES([arg1])
        #print("#check difference of indices (arg3-maxlength) >= 0",diff)
        if diff >= 0:
            #how many new lines to insert?
            appending = open(arg1,'r+')
            appending.seek(0,2)
            #print("does arg2 have newline char?",arg2)
            for x in range(diff-1):
                print('inserting empty line',x)
                appending.write("\n")
            #then append the object
            appending.write(arg2+"\n")
            #close the file
            appending.close()
    #hint: arg1Old closed by with
    arg1New.close()
    '''
    #doesn't work for some reason when I nest functions:
    for line in fileinput.input(arg1, inplace=1):
        if i == arg3:
            print(arg2)
        i += 1
        print(line, end='')
    #CLOSE THE FILE SO I CAN CHECK MAXLINES LATER
    fileinput.close()
    ^^^^
    THIS WORKED BUT NOT WHEN I NEST FUNCTIONS
    ===================
    with arg1 as infile:
        for line in infile:
            print("line",line)
    ===================



    for line in fileinput.input(arg1, inplace=1):
        if i == arg3:
            print(arg2)
        i += 1
        print(line, end='')

    THIS IS NOT END OF FUNCTION!!!!!



    
    #what if I need to append to end???
    #check if it is at end OR LATER???
    #problem: fileinput.input(arg1, inplace=1) has a max length
    #want to exceed max length (if it's 0 then do nothing)

    #check difference of indices (arg3-maxlength) >= 0
    picture:
    insert at: index 7
    object has: 3 items OR index 2
    then 7-3 = 4
    ---|----|-
    so insert 4 newline
    #HINT: Damn this remainder is a lucky count for number of newlines
    then append the object
    
    #append appropriate amount of newlines
    #append object (arg2)

    
    '''

def seqstring(argList):
    '''
    arg1 = string
    RETURNS THIS SEQUENCE AS A LIST
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
    #print("wtfstats", arg1, maxlength)
    x = 0
    y = 0
    stopAt = maxlength-1
    total = (maxlength*(maxlength+1))/2
    #print("check if total is int or float",total)
    ''''''
    for alpha in range(0,int(total)):
        #print("more stats", x,y,stopAt)
        #print("check if x == 0",x==0)
        if x == 0:
            #print("1",arg1[y:])
            ANS.append(arg1[y:])
        else:
            #print("2",arg1[y:-x])
            ANS.append(arg1[y:-x])
        #print arg1[y:-x]
        if x == stopAt:
            stopAt += -1
            y += 1
            x = 0
        else:
            x += 1
    return ANS

def delta1(argList):
    '''
    input: arbitary string (or maybe file name?) that we assume is code
    output: [code,(eval(code),err(code))]

    STEPS:
        1. write code into .py file
        2. run it with popen and see eval/err code
      '''
    #input: arbitary string (or maybe file name?) that we assume is code
    arg1 = argList[0]
    
    nametest = nametestFUNC(["TestPYFILE.py"])[1]
    
    #now that we have a valid filename, run the goal and read the stdout and sterr line by line until exit:
    #PROBLEM: what about functions that have no end, or very long functions?
    #^^^ SI problem, you're kinda fucked and you just have to see if manually
    ANS = []
    #print("test nametest func RETURN",nametestFUNC([nametest]))
    
    nameCreateFile = open(nametest,'a+')
    nameCreateFile.write(arg1)
    nameCreateFile.close()
    pytest = Popen(['python', nametest], stdout=PIPE, stderr=PIPE)
    #print("this is output",pytest.communicate()[0].decode())
    output = pytest.communicate()[0].decode()
    #print("this is error",pytest.communicate()[1].decode())
    err = pytest.communicate()[1].decode()
    ANS.append([arg1,(output,err)])
    os.remove(nametest)
    return ANS

def nametestFUNC(argList):
    '''
    arg1 = filename with extension
    #check if a file exists by the name of arg1
        yes = check new filename with +1 UNTIL it works
        no = then it's ok
    RETURN:
    TRUE: [False,filename that does work]
    FALSE: [True, (can write a new file with arg1 name)]
    '''
    arg1 = argList[0]
    ExistenceCheck = os.path.isfile(arg1)
    #print("testfunc2", arg1, ExistenceCheck)
    if ExistenceCheck:
        x = 0
        while ExistenceCheck == True:
            #make new name
            newnameprep = arg1.split(".")[:-1]
            newnameprep2 = "".join(newnameprep)
            print("newnameprep2",newnameprep2)
            newname = newnameprep2 + str(x) + "." + arg1.split(".")[-1]
            #print("qhat is new name?",newname)
            #test new name
            ExistenceCheck = os.path.isfile(newname)
            x += 1
        #if new name works, then return [False,filename that does work]
        return [False, newname]
    else:
        return [True, arg1]

def dequals(x,y):
    #just need == in the form of a function:
    return x == y

def maxlongestcontig(argList):
    LHS = argList[0]
    RHS = argList[1]
    LHSinit = argList[2]
    RHSinit = argList[3]
    try:
        commfunc = argList[4]
    except:
        commfunc = dequals
    
    #hint: this is commutative
    #print("LHS")
    #print(LHS)
    #print("RHS")
    #print(RHS)
    Candidatelist = []
    ANS = []
    RHSCounter = RHSinit
    for y in RHS[RHSinit:]:
        LHSCounter = LHSinit
        for x in LHS[LHSinit:]:
            #::AM I SUPPOSED TO SCALE THIS
            #print("checking how to pass a func as arg",commfunc(x,y))
            #if x == y:
            if commfunc(x,y):
                #get x pos for LHS start 
                lhscheckpos = LHSCounter
                #get y pos for RHS start 
                rhscheckpos = RHSCounter
                length = 0
                #print("stats", x, LHSCounter, y, RHSCounter)
                #print("=======WTF STATS",LHS[lhscheckpos+length] == RHS[rhscheckpos+length])
                while LHS[lhscheckpos+length] == RHS[rhscheckpos+length]:
                    length += 1
                    if len(LHS) > lhscheckpos+length and len(RHS) > rhscheckpos+length:
                        pass
                    else:
                        break
                #add candidate to Candidatelist
                #datareq: LHSstart RHSstart Length
                Candidatelist.append([lhscheckpos,rhscheckpos,length])
            LHSCounter += 1
        RHSCounter += 1
    #double check info
    #print("CandidateList", Candidatelist)
    #print(LHS)
    #print(RHS)
    for i in Candidatelist:
        #print("Candidate",i)
        #print("NOTE: [:] format doesn't do singletons")
        #print("matching left (singletons will fuck up)",LHS,i[0],i[0]+i[2])
        #print(LHS[i[0]:i[0]+i[2]+1])
        #print("matching right (singletons will fuck up)",RHS,i[1],i[1]+i[2])
        #print(RHS[i[1]:i[1]+i[2]+1])
        if ANS == []:
            ANS = i
        else:
            if i[2] > ANS[2]:
                ANS = i
    return ANS

def delta2(argList):
    LHS = argList[0]
    RHS = argList[1]
    try:
        commrel = argList[2]
    except:
        commrel = dequals
    #need ending strat
    #generic: apply maxlongestcontig on splits until it fails
    LCont = maxlongestcontig([LHS,RHS,0,0])
    #print("is LCont empty?",LCont)
    ##what to do with nil answer??
    ##nullansweralready:
    if LCont == []:
        #return [[['Symbol0'], [0]]]
        #return [[['α0'], [0]]]
        return [[['α0'], ['α0']]]
    
    #match like segments together (try: from left to right)
    Connections = []
    Connections = seqsplitmin([LHS,RHS,LCont,Connections, [-1, -1, -1]])
    
    #for each part in Connections, if NOT same parts OR either part is empty, reapply maxlongestcontig
    #then at the end stitch similar parts together
    #print("================checking Connections")
    #print(Connections)
    i = 0
    for x in Connections:
        LContmin = maxlongestcontig([x[0][0],x[1][0],0,0,commrel])
        if x[0][0] == x[1][0] or len(x[0][0]) == 0 or len(x[1][0]) == 0 or len(LContmin) == 0:
            pass
            i += 1
        else:
            #print("WTF BUCK",x,LContmin)
            #print("DELETE CURRENT X",x)
            #print(Connections[i])
            #print("old Con", Connections)
            del Connections[i]
            #print("new Con", Connections)
            
            #INSERT NEW X PARTS (NOTE: WE ALSO INSERT ENOUGHT EMPTY LISTS SO MAKING STATEMENT+REPLACE IS EASIER)
            #replace the current x with this:
            ##################LHS/RHS are diff, LCont is now LContmin##################
            #print("part 1",[[x[0][0][:LContmin[0]]],[x[1][0][:LContmin[1]]]])
            #print("part 2",[[x[0][0][LContmin[0]:LContmin[0]+LContmin[2]+1]],[x[1][0][LContmin[1]:LContmin[1]+LContmin[2]+1]]])
            #print("part 3",[[x[0][0][LContmin[0]+LContmin[2]+1:]],[x[1][0][LContmin[1]+LContmin[2]+1:]]])
            #Connections = InsertAt(Connections, [[x[0][0][:LContmin[0]]],[x[1][0][:LContmin[1]]]], i)
            #Connections = InsertAt(Connections, [[x[0][0][LContmin[0]:LContmin[0]+LContmin[2]]],[x[1][0][LContmin[1]:LContmin[1]+LContmin[2]]]], i+1)
            #Connections = InsertAt(Connections, [[x[0][0][LContmin[0]+LContmin[2]:]],[x[1][0][LContmin[1]+LContmin[2]:]]], i+2)
            #print("oh baby, oh oh baby \n", x[0][0], "\n", x[1][0], "\n", LContmin, "\n", Connections, "\n", [i, i+1, i+2])
            Connections = seqsplitmin([x[0][0],x[1][0],LContmin,Connections,[i, i+1, i+2]])
            #print("new connections")
            #print(Connections)
            i += 1
    #construct statement:
    ANS = []
    symboli = 0
    #print("what are connections?",Connections)
    #print("ANS",ANS)
    for x in Connections:
        if x[0] == x[1]:
            ANS.append(x)
        elif len(x[0][0])!= 0 and len(x[1][0])!= 0:
            #ANS.append([["Symbol" + str(symboli)], [symboli]])
            ANS.append([["α" + str(symboli)], ["α" + str(symboli)]])
            symboli += 1
        #print("ANS at each step", ANS)
    return ANS

def seqsplitmin(argList):
    LHS = argList[0]
    RHS = argList[1]
    LCont = argList[2]
    Connections = argList[3]
    index = argList[4]
    ###this is because I might as well make a generic now as well as try to optimize instead of wait for later
    #what this does is take LHS,RHS, and LCont and appends the right connections
    #if there is an empty connection, refuse to append
    #index is a list of indicies to add objects
    ANS = Connections
    #print("CHECKANS1",ANS)
    #if it's an empty connection, refuse
    #print("trendytrendytrendy \n", LHS, "\n",RHS, "\n",LCont, "\n",Connections, "\n",index)
    
    if len(LHS[:LCont[0]]) == 0 and len(RHS[:LCont[1]]) == 0:
        pass
    #else: append
    else:
        #ANS.append([[LHS[:LCont[0]]],[RHS[:LCont[1]]]])
        ANS = InsertAt(ANS,[[LHS[:LCont[0]]],[RHS[:LCont[1]]]],index[0])

    #print("CHECKANS2",ANS)
    if len(LHS[LCont[0]:LCont[0]+LCont[2]]) == 0 and len(RHS[LCont[1]:LCont[1]+LCont[2]]) == 0:
        pass
    else:
        #ANS.append([[LHS[LCont[0]:LCont[0]+LCont[2]]],[RHS[LCont[1]:LCont[1]+LCont[2]]]])
        ANS = InsertAt(ANS,[[LHS[LCont[0]:LCont[0]+LCont[2]]],[RHS[LCont[1]:LCont[1]+LCont[2]]]],index[1])

    #print("CHECKANS3",ANS)
    if len(LHS[LCont[0]+LCont[2]:]) == 0 and len(RHS[LCont[1]+LCont[2]:]) == 0:
        pass
    else:
        ANS = InsertAt(ANS,[[LHS[LCont[0]+LCont[2]:]],[RHS[LCont[1]+LCont[2]:]]],index[2])

    #print("CHECKANS4",ANS)
    return ANS

def firstlongestcontig(argList):
    LHS = argList[0]
    RHS = argList[1]
    LHSinit = argList[2]
    RHSinit = argList[3]
    try:
        antitoggle = argList[4]
    except:
        antitoggle = 0
    #print("argList for firstlongestcontig",argList)
    #print("LHS")
    #print(LHS)
    #print("RHS")
    #print(RHS)
    Candidatelist = []
    ANS = []
    RHSCounter = RHSinit
    for y in RHS[RHSinit:]:
        #print("stats", LHS[LHSinit], LHSinit, y, RHSCounter)
        #::AM I SUPPOSED TO SCALE THIS
        if LHS[LHSinit] == y:
            #get x pos for LHS start 
            lhscheckpos = LHSinit
            #get y pos for RHS start 
            rhscheckpos = RHSCounter
            length = 0
            while LHS[lhscheckpos+length] == RHS[rhscheckpos+length]:
                #print("WTF IS GOING ON", len(LHS), lhscheckpos+length, len(RHS), rhscheckpos+length,LHS[lhscheckpos+length],RHS[rhscheckpos+length],LHS[lhscheckpos+length] == RHS[rhscheckpos+length], "length is", length )
                length += 1
                #print("check breakpoint",lhscheckpos+length , len(LHS) , rhscheckpos+length , len(RHS))
                if lhscheckpos+length == len(LHS) or rhscheckpos+length == len(RHS):
                    break
            #print("the info",[lhscheckpos,rhscheckpos,length])
            #add candidate to Candidatelist
            #datareq: LHSstart RHSstart Length
            Candidatelist.append([lhscheckpos,rhscheckpos,length])
        RHSCounter += 1
    #double check info
    #print("CandidateList", Candidatelist)
    #print(LHS)
    #print(RHS)
    for i in Candidatelist:
        #print("Candidate",i)
        #print("NOTE: [:] format doesn't do singletons")
        #print("matching left (singletons will fuck up)",LHS,i[0],i[0]+i[2])
        #print(LHS[i[0]:i[0]+i[2]+1])
        #print("matching right (singletons will fuck up)",RHS,i[1],i[1]+i[2])
        #print(RHS[i[1]:i[1]+i[2]+1])
        if ANS == []:
            ANS = i
        else:
            if i[2] > ANS[2]:
                ANS = i

    if len(Candidatelist) > 0:
        #print("===================START")
        #print("check ans",ANS)
        #print("matching left (singletons will fuck up)",LHS,ANS[0],ANS[0]+ANS[2])
        #print(LHS[ANS[0]:ANS[0]+ANS[2]])
        #print("matching right (singletons will fuck up)",RHS,ANS[1],ANS[1]+ANS[2])
        #print(RHS[ANS[1]:ANS[1]+ANS[2]])
        #print("===================END")
        if antitoggle == 1:
            ANS = [ANS[1],ANS[0],ANS[2]]
    #print("BEWARE OF ANTITOGGLE!",ANS)
    return ANS

def delta3(argList):
    '''
    input: (obj1,obj2)
    output: replacement function
    NEED THEOREM: deltav2(obj1,obj2)
        :if one obj is the abstraction of the other then the answer of deltav2 is the abstraction
    
    '''
    arg1 = argList[0]
    arg2 = argList[1]
    try:
        commrel = argList[2]
    except:
        commrel = dequals
    #plan
    #find abstraction in one of the arguments:
    abstractionfunc = delta2([arg1,arg2,commrel])
    #print("abstr func is", abstractionfunc)
    abstractionstr = toString([dom(abstractionfunc),"naive"])
    #print("abstr",abstractionstr)
    if abstractionstr == arg1:
        TheObj = arg2
    elif abstractionstr == arg2:
        TheObj = arg1
    else:
        return "Can't find abstraction"

    #now we know TheObj and abstraction
    #next we need to find replacement string:
    #try to match abstraction to obj then the rest of the string for obj we attach to symbols in abstraction
    '''
    REQUIREMENTS FOR MATCHING ABSTRACTION TO OBJECT PROPERLY
    >'exhaust' abstraction
    >recognize symbols
    '''
    #keep track of where we are in the obj
    TheObjIndex = 0
    alphatrigger = False
    ANS = []
    for x in abstractionfunc:
        #print("=====if symbol, 'skip'",x,x[0][0][0],"α",x[0][0][0] == "α")
        if x[0][0][0] == "α":
            symbolis = x[0][0]
            #if we're at the end of abstractionfunc assume rest of theobj is symbol:
            if x == abstractionfunc[-1]:
                ANS.append([symbolis,TheObj[TheObjIndex:]])
            alphatrigger = True
        #else: we attempt to match to first (why first? #1: we can't tell difference between two matches #2: if first doesn't work then our obj has too much noise)
        else:
            #print("feed into firstlongest",x[0][0])
            stringmatching = firstlongestcontig([x[0][0],TheObj[TheObjIndex:],0,0])
            #print("try firstlongestcontig",stringmatching)
            target = TheObj[TheObjIndex+stringmatching[1]:TheObjIndex+stringmatching[1]+stringmatching[2]]
            #print("targetvalue",target)
            
            oldIndex = TheObjIndex
            TheObjIndex = TheObjIndex + stringmatching[2]
            #print("updating TheObjIndex", TheObjIndex)
            if alphatrigger == True:
                #print(oldIndex,TheObjIndex)
                symbolguess = TheObj[oldIndex:oldIndex+stringmatching[1]]
                #print("now we try to construct alphastring replacement|", [symbolis,symbolguess])
                ANS.append([symbolis,symbolguess])
            #add here so we preserve order
            ANS.append([target,target])
            alphatrigger = False
    return ANS

def CurrentClone():
    '''
    idea is that you edit the other clone and keep current clone as backup
    this function takes no inputs and just tells you which clone you are in: (MIRA OR MIRA_B)
    HINT:
        MIRA IS UPPER DIRECTORY (C:\An\MIRA) == return is "MIRA"
        MIRA_B IS LOWER DIRECTORY (C:\An\MIRA\MIRA_B) == return is "MIRA_B"
    '''
    cwdLIST = os.getcwd()
    cwd = os.getcwd().split("\\")[-1]
    basics= os.getcwd().split("\\")[:len(os.getcwd().split("\\"))-1]

    PLACE = []
    if cwd == "MIRA":
        #print("IN MIRA")
        #check if opposite dir exists
        if os.path.exists(cwdLIST + "\\MIRA_B"):
            PLACE = "MIRA"
        else:
            #if not, make it
            os.makedirs(cwdLIST + "\\MIRA_B")
    elif cwd == "MIRA_B":
        #print("NOT IN MIRA")
        #check if opposite dir exists
        #print("#GO UP ONE DIRECTORY", "\\".join(basics))
        #print("didnt need to combo", basics[-1])
        #print("MAKE THIS DIRECTORY","\\".join(basics[:len(basics)-1]) +"\\MIRA" )
        if basics[-1] == "MIRA":
            PLACE = "MIRA_B"
        else:
            #if not, make it
            os.makedirs("\\".join(basics[:len(basics)-1]) +"\\MIRA")
    else:
        print("WHERE THE FUCK AM I")
        exit()
    return PLACE

def OtherClone():
    '''
    tells me the location of the other clone
    '''
    PLACE = CurrentClone()
    cwdLIST = os.getcwd()
    if PLACE == "MIRA":
        #print("make new file in new directory",cwdLIST + "\\MIRA_B" + "\\")
        NEW = cwdLIST + "\\MIRA_B"
        #print("total name NEXT", NEW)

    elif PLACE == "MIRA_B":
        #print("make new file in new directory","\\".join(basics[:len(basics)-1]) +"\\MIRA" + "\\")
        NEW = "\\".join(basics[:len(basics)-1]) +"\\MIRA"
    return NEW

def Cloneinit():
    '''
    just clone the whole MIRA directory OR MIRA_B directory
    FILE STRUCTURE: MIRA\MIRA_B
    '''
    #need to know:
    cwdLIST = os.getcwd()
    #print("files in directory",os.listdir(cwdLIST))
    #if you're in smaller or larger directory
    cwd = os.getcwd().split("\\")[-1]
    basics= os.getcwd().split("\\")[:len(os.getcwd().split("\\"))-1]

    PLACE = []
    if cwd == "MIRA":
        #print("IN MIRA")
        #check if opposite dir exists
        if os.path.exists(cwdLIST + "\\MIRA_B"):
            PLACE = "MIRA"
        else:
            #if not, make it
            os.makedirs(cwdLIST + "\\MIRA_B")
    elif cwd == "MIRA_B":
        #print("NOT IN MIRA")
        #check if opposite dir exists
        #print("#GO UP ONE DIRECTORY", "\\".join(basics))
        #print("didnt need to combo", basics[-1])
        #print("MAKE THIS DIRECTORY","\\".join(basics[:len(basics)-1]) +"\\MIRA" )
        if basics[-1] == "MIRA":
            PLACE = "MIRA_B"
        else:
            #if not, make it
            os.makedirs("\\".join(basics[:len(basics)-1]) +"\\MIRA")
    else:
        print("WHERE THE FUCK AM I")
        exit()
    #if files you are about to copy are usable
    #just check fileopen
    #for x in [y for y in os.listdir(cwdLIST) if y != "__pycache__" and os.path.isdir(os.getcwd()+ "\\" +y) == False]:
    #    try:
    #        botburger = open(x,'r+')
    #        botburger.close()
    #        #print(x, "is available")
    #    except Exception as e:
    #        print(x, "NOT AVAILABLE, STOPPING NOW")
    #        print(e)
    #        exit()
    #have everything under with condition and if we cannot access, throw an error <--- DIDN'T REALLY DO THIS
    #if we're here we can clone into 'opposite' directory

    for x in [y for y in os.listdir(cwdLIST) if y != "__pycache__" and os.path.isdir(os.getcwd()+ "\\" +y) == False]:
        try:
            botburger = open(x,'r+')
            botburger.close()
            #print(x, "is available")
        except Exception as e:
            print(x, "NOT AVAILABLE, STOPPING NOW")
            print(e)
            exit()
        #print("this is filename",x)
        CURRENT = os.getcwd() + "\\" + x
        #print("total name CURRENT", CURRENT)
        
        if PLACE == "MIRA":
            #print("make new file in new directory",cwdLIST + "\\MIRA_B" + "\\")
            NEW = cwdLIST + "\\MIRA_B" + "\\" + x
            #print("total name NEXT", NEW)

        elif PLACE == "MIRA_B":
            #print("make new file in new directory","\\".join(basics[:len(basics)-1]) +"\\MIRA" + "\\")
            NEW = "\\".join(basics[:len(basics)-1]) +"\\MIRA" + "\\" + x
        #then copy and close
        #print(CURRENT,NEW)
        copy2(CURRENT, NEW)

def AutoPicked(ArgList):
    '''
    arg1 = filename
    arg2 = line to find autopicked universe
    RETURN = ??
    WHAT THIS IS SUPPOSED TO DO IS MAKE THE AUTOPICKED UNIVERSE, BUT I AM SUPPOSED TO CHECK THROUGH Long and UNORDERED FILES

OTHER PROBLEM
problem:
I wanted to use Quine function to guarantee that given an arbitrary input, I would have a function to feed into AutoPicked function
shitty answer:
if function, leave alone
not function = use Quine 



REASONING FOR COMPOSEPREP
PROBLEM:
given (concept space, composemeta), a function X in concept space and a function Y that is observed, 
and you want X compose Y (DO Y then X), and insertion to concept space is done through quine function,
 is there a way to modify the input Y into Y~ such that you preserve X compose Y in concept space 
 (AKA X conpose Y observed IRL == X compose Y~ in concept space)

ANSWER

KNOW: X is fixed = [[a in dom(X), b in ran(X)]]
we have access to any concept space of arbitrary basis size/ elements (know: size -> elements through some basis bijection)
Y is some finite function/ Y is also "fixed", [[a in dom(Y), b in ran(Y)]]
what does Q_(Y) look like?
[[[a in dom(y), b in ran(y)]],[[a in dom(y), b in ran(y)]]]

X compose Y looks like:
[[a in dom(y),b in ran(x)] | the arrows exist]

PROBLEM:
Q_(Y) looks horrendous
dom(x) probably does not accept ran(Q_(Y))
want:
>dom Q_(Y) is sufficiently good to match X COMPOSE Y. TO BE CLEAR: a in ran(Q_(Y)) iff [[a in dom(y),b in ran(x)] | the arrows exist] (a's are same)
>ran Q_(Y) to be sufficiently good to match X COMPOSE Y. TO BE CLEAR: b in ran(Q_(Y)) iff [[a in dom(y),b in ran(x)] | the arrows exist] (b's are same)
hint: Y~ probably only exists for certain special kinds of finite functions (guaranteed for identity funcs, or already quined functions)
			Y									X
[[a in dom(Y), b in ran(Y)]]		[[a in dom(X), b in ran(X)]]

			X compose Y looks like:
[[a in dom(y),b in ran(x)] | the arrows exist]


			Q_(Y)
[[[a in dom(y), b in ran(y)]],[[a in dom(y), b in ran(y)]]]

PROBLEM: X IS FIXED, Q_(function) repeats the element

so if pair in Y has different coords, dom(X) would not be able to "attach" to ran(Q_(Y~))


the domain of X that works would force ran(Q_(Y~)) and also force domQ_(Y~).
So such method of making Y~ does not exist

=> FUCK ME 

C:\An>git commit -a -m "fuck if I observe a Y and want to compose with X I cannot make a Y~ such that X COMPOSE Q_(Y~) matches in some concept space which means I cannot always quine when making autopicked universe"
    '''
    arg1 = ArgList[0]
    arg2 = ArgList[1]
    ANS = []
    try:
        #problem:
        #if you eval print("whatever") and set arg2 = eval(arg2) blindly the input of print escapes out knowledge
        #so just keep everything as a list through eval then just default to string (which should be our input anyways)
        if type(eval(arg2)) == str or type(eval(arg2)) == list:
            arg2 = eval(arg2)
    except:
        pass

    #if function, DONT quine:
    if fCheck(arg2) == True:
        composeprep = arg2
    #else, quine
    else:
        composeprep = Q_(arg2)

    with open(arg1, "r+") as fileref:
        fileref.seek(0)
        line = rchop(fileref.readline(), '\n')
        while line:
            #print("THIS IS the LINE", line) #type(line)
            #print("THIS IS ARG2 AFTER EVAL CHECK",arg2) #type(arg2)
            #print("arglist is", ArgList)
            #print("line",line)
            #print("composeprep is arg2", composeprep)
            try:
                #ComposeMETA([eval(str([['TOTAL_ARGUMENT == \'print("qhy")\'', 'None']])),Q_(str('print("qhy")'))])
                exist = ComposeMETA([eval(str(line)),composeprep])
                #print("what should return be?", exist)
                #HINT: my test data doesn't need quining BUT I do need it for random inputs
                #QUESTION: IS IT POSSIBLE TO WORK ON QUINE OF FUNCTIONS OR NO?: PROBABLY YES, BUT YOU HAVE TO MODIFY ACTION FUNCTION (or f1 of f1 compose f2)
                #exist = ComposeMETA([eval(str(line)),eval(arg2)])
                #print("WHAT IS COMPOSEMETA",exist)
                if exist != []:
                    ANS.append(line)
            except Exception as e:
                #print("ERROR IS ",e)
                if e != []:
                    #ANS.append(e)
                    pass
                pass
            line = rchop(fileref.readline(), '\n')
    return ANS
#print("FINAL ANSWER", AutoPicked(['MemoryUNORDERED.txt',"[['a',['b']],['Z',['f','AF']]]"]))
#print(AutoPicked(['MemoryUNORDERED.txt',"what the"]))

def Applyfunc(argList):
    '''
    arg1 = finite function
    arg2 = argument for arg1
    what this does is eval the finite function given arg2 as input
    '''
    #arg1 = finite function
    arg1 = argList[0]
    #arg2 = argument for arg1
    arg2 = argList[1]

    ANS = []
    #check if arg1 is actually a function
    if fCheck(arg1) == False:
        print("f1 is function? Applyfunc", fCheck(arg1))
        return []
    print("monkaS",arg1,Q_(arg2))
    ANS = ran(ComposeMETA([arg1,Q_(arg2)]))
    #ComposeMETA([[['TOTAL_ARGUMENT == "b"', 'd'],['TOTAL_ARGUMENT == "b"', 'e'],['TOTAL_ARGUMENT == "b"', 'f']],[['a','b']]])
    #Applyfunc([[['TOTAL_ARGUMENT == "b"', 'd'],['TOTAL_ARGUMENT == "b"', 'e'],['TOTAL_ARGUMENT == "b"', 'f']],'b'])
    return ANS

def SeekForce(ArgList):
    '''
    arg1 = filename
    arg2 = specifc arg
    arg3 = function to use
    RETURN = ??
    THIS IS SUPPOSED TO take a filename with finite functions in it, a specific argument X, and a binary function
    then it composes X with everything in the file and returns all the answers (make empty a nonrepeating answer!)
    '''
    arg1 = ArgList[0]
    arg2 = ArgList[1]
    arg3 = ArgList[2]
    ANS = []

    print("checking how to call func",arg3(["alphaprint('')","betrprint('')"]))
    
    with open(arg1, "r+") as fileref:
        fileref.seek(0)
        line = rchop(fileref.readline(), '\n')
        while line:
            try:
                #print("this is line",line,type(line))
                #print("this is arg2",arg2,type(arg2))
                exist = arg3([line,arg2])
                #print("exist test",exist)
                if exist != []:
                    ANS.append(exist)
            except Exception as e:
                #print("ERROR IS ",e)
                if e != []:
                    #ANS.append(e)
                    pass
                pass
            line = rchop(fileref.readline(), '\n')
    return ANS

#print("NOW TO TEST SEEKFORCE",SeekForce(['MemoryUNORDERED.txt','argument_1 == "b"',Applyfunc]))
##############################################################

def printpls(obj):
    return str(obj)
            
#TESTING STAGE

test1 = "print('alpha')"
#test2 = "print('beta')"
test2 = "print('α0')"

#print(maxlongestcontig(test2,test1,0,0))
#print(maxlongestcontig(test1,test2,0,0))
#print(delta2([test1,test2]))
#== test2
#print("what about range?",ran(delta2([test1,test2])))
#print(toString([dom(delta2([test1,test2])),"naive"]))

#print("say yay!",delta3([test1,test2]))

#testing out basic edge cases:

#print("#delta2 symbol at beginning",delta2(["alphaprint('')","betrprint('')"]))
#print("#delta3 symbol at beginning",delta3(["α0print('')","betrprint('')"]))
#print("#delta2 symbol at end",delta2(["print('')alpha","print('')betr"]))
#print("#delta3 symbol at end",delta3(["print('')alpha","print('')α0"]))
#ANS KEY
#delta2 symbol at beginning [[['α0'], ['α0']], [["print('')"], ["print('')"]]]
#delta3 symbol at beginning [['α0', 'betr'], ["print('')", "print('')"]]
#delta2 symbol at end [[["print('')"], ["print('')"]], [['α0'], ['α0']]]
#delta3 symbol at end [["print('')", "print('')"], ['α0', 'alpha']]

#print("let me figure out how deltav2 works for making delta1 on code:")
#print(delta2(["printpls('alpha')",eval("printpls('alpha')")]))
#NOT AN L IT'S INTEGER 1

'''
HINT: I can pass abstracted argument into function then track it along the way then construct proper symbol

delta1answer = ["printpls('input')",eval("printpls('input')")]
delta1answer2 = ["printpls('test')",eval("printpls('test')")]
print("delta1 looks like this", delta1answer)
print("delta1 2 looks like this", delta1answer2)
print("just tell me, tell me", delta2([str(delta1answer),str(delta1answer2)]))
statementattempt = delta2([str(delta1answer),str(delta1answer2)])
print("STATEMENTATTMPT",statementattempt)
stringattempt = toString([dom(statementattempt),"naive"])
print("stringattemtp is",stringattempt)
print("just tell me, tell me V3 ATTEMPT", delta3([str(delta1answer),stringattempt]))
print("just tell me, tell me2", delta2([str(delta1answer[0]),str(delta1answer[1])]))
print("LHS|",delta1answer[0])
print("RHS|",delta1answer[1])
print("deltav2 determines abstraction",delta2([delta1answer[0],delta1answer[1]]))
print("try deltav3 instead of v2",delta3([delta1answer[0],delta1answer[1]]))

#print("check eval",eval("printpls('alpha')"))

print("nchoose2 is already done",list(itertools.combinations('abcd',2)))

====checking for file validity for clone func
cwd = os.getcwd()
print("check current working directory",cwd)

for x in os.listdir(cwd):
    print("check for files in dir",x)


>have to log changes using github?
CLONING STRATS:
>idea is to make a program to clone mira:
spawning independent process python


#TEST:
RUN testprogram.py that just waits for input
close this program
then check if testprogram closes as well


print( output.stdout.read())


HINT: I DONT NEED SEPARATE PROCESS BECAUSE PYTHON COMPILES A SEPARATE THINGY
'''





#print(delta1(["print('check this out')"]))
#print('check this out')


#NOT CLOSING ===== NOT COMMITTING WRITES
testfile = '1.txt'
basisfile = 'basis.txt'

#lexicoSortHARD([basisfile,'Memory.txt'])
##########
##########lexicoSort([basisfile,'Memory.txt', 'MemoryUNORDERED.txt'])
##########
##########print("why none?",bisectionInsert(['Memory.txt', 'stats:', 'basis.txt', [1]]))

#CHECK BISECTION SEARCH
#print("check empty answer",bisectionSearch(['Memory.txt',"?",basisfile]))
##print("check single answer",bisectionSearch(['Memory.txt',"    stats:",basisfile]))
#print("check multiple answer to left",bisectionSearch(['Memory.txt',"    figure out the offset",basisfile]))
#check multiple answer to right
#check multiple answer to left & right

##########PROBLEM WITH RECOGNIZING TAB (\t) and spaces which fucked bisection insert 
##########print("check bisection insert sanity",bisectionInsert(['Memory.txt', "    stats:", 'basis.txt',[1]]))

#print("hint is spacing",FILEindexread(['Memory.txt',12]))
#print("hint is spacing",FILEindexread(['Memory.txt',13]))
#print("hint is spacing",FILEindexread(['Memory.txt',14]))
#print("hint is spacing",FILEindexread(['Memory.txt',15]))
#idk = open('Memory.txt','rb')
#print("open in bytes mode", idk.read())



#ADDRESS FAILS ON EMPTY
#print(AddressFILE([basisfile,M_("")]))
#print("wtf is this", M_(""))



'''
TEST INSERTING SAME OBJECT
'''


#print(FILEinsertAt([testfile,"insert at index 27 pls",27]))

#emptyfile
#test 0
#bisectionInsert([testfile,"SIZE+",basisfile])

#SIZE+
#test LEFT for size 1 file
#bisectionInsert([testfile,"SIZE4",basisfile])
#test RIGHT for size 1 file
#bisectionInsert([testfile,"SIZEp",basisfile])

#SIZE+,SIZEZ
#test MIDDLE for "size 2 file"
#bisectionInsert([testfile,"SIZEp",basisfile])
#test BEGINNING for "size 2 file"
#bisectionInsert([testfile,"SIZE4",basisfile])
#test END for "size 2 file"
#bisectionInsert([testfile,"SIZEZZZ",basisfile])

#SIZE+,SIZEZZ
#test MIDDLE for "size X file"
#bisectionInsert([testfile,"SIZEp",basisfile])
#bisectionInsert([testfile,"SIZEZ",basisfile])
#test BEGINNING for "size X file"
#bisectionInsert([testfile,"SIZE4",basisfile])
#test END for "size X file"
#bisectionInsert([testfile,"SIZEZZZ",basisfile])


#can't test twice: you have to close and open the file to update in order to insert again
#bisectionInsert([testfile,"testobjinsertto1",basisfile])


#emptyfile
#test 0
#bisectionInsert([testfile,"ONETURN",basisfile])

#ONETURN
#test LEFT for size 1 file
#bisectionInsert([testfile,"ABLE",basisfile])
#test RIGHT for size 1 file
#bisectionInsert([testfile,"OBSESSION",basisfile])

#ONETURN,TREEKILL
#test MIDDLE for "size 2 file"
#bisectionInsert([testfile,"OBSESSION",basisfile])
#test BEGINNING for "size 2 file"
#bisectionInsert([testfile,"ABLE",basisfile])
#test END for "size 2 file"
#bisectionInsert([testfile,"ZvezdaPlot",basisfile])


#emptyfile
#test 0
#print(bisectionInsert([testfile,"ONETURN",basisfile,[1]]))

#ONETURN
#test LEFT for size 1 file
#print(bisectionInsert([testfile,"ABLE",basisfile,[1]]))
#test RIGHT for size 1 file
#print(bisectionInsert([testfile,"OBSESSION",basisfile,[1]]))

#ONETURN,TREEKILL
#test MIDDLE for "size 2 file"
#print(bisectionInsert([testfile,"OBSESSION",basisfile,[1]]))
#test BEGINNING for "size 2 file"
#print(bisectionInsert([testfile,"ABLE",basisfile,[1]]))
#test END for "size 2 file"
#print(bisectionInsert([testfile,"ZvezdaPlot",basisfile,[1]]))



'''
SIZE4
SIZE+
SIZEp
SIZEZ
SIZEZZ
SIZEZZZ

=====
ABLE
ONETURN
OBSESSION
TREEKILL
ZvezdaPlot



AddressFILE(['basis.txt',M_('SIZEZZ')]) < AddressFILE(['basis.txt',M_('SIZEZZZ')])
'''
 


#print("basislist", basislist)
#print("fml", Address(basislist,M_(inputtext)))
#print(AutoVision(Address(basislist,M_(inputtext)),1))
#test
#f2 = [[4,5],['r','g'],[1,3],[7,7],["t","y"],[555,33],[8746,8946]]
#f1 = [[3,1],['g','t'],['r','y'],['y',"art"],[7,7],[90,9],[0,9],['o','o']]
#print(f1)
#print(f2)
