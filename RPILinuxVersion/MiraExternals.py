from __future__ import division
from math import *
from inspect import *
import ast

file = open('INP.txt', 'r')
basis = open('Basis.txt', 'r+')
memory = open('Memory.txt', 'r+')

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

def dom(func):
    ANS = []
    for x in func:
        ANS.append(x[0])
    return ANS

def M_(thestr):
    ANS = []
    i = 0
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
    for obj in fcandidate:
        if len(obj) != 2:
            ANS = False
    return ANS

def toString(f):
    '''
    assume f is a finite function of the form for all x in f, x = [a,b]
    return a string that is the range of f "in order"
    '''
    ANS = ""
    if fCheck(f) == False:
        print("f1 is function? toString", fCheck(f1))
        return
    for x in f:
        ANS = ANS + x[1]
    print("hoping lists retain some kind of order",f,ANS)
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
    
    print("obj for reference!",obj)
    for x in obj:
	#print("index stats",index)
	#print("other stats",obj,Interim)
        #print("stats",x,x[0],int(RelEval(index,x[0])[0]))
	#print("suspected wtf",index,x[1])

	print("x obj", x)
	print("index",index)
	print("x[0]",x[0])
	print("Cantor 1st coord",int(RelEval(index,x[0])[0]))
	print("Cantor 2nd coord",int(RelEval(index,x[1])[0]))
	#print("CANTOR PAIR IS FUCKED? C(0,1)",CantorPair(0,1))
	print("the pair",CantorPair(int(RelEval(index,x[0])[0]),int(RelEval(index,x[1])[0])))
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
	#print("CANTOR PAIR IS FUCKED? C(0,1)",CantorPair(0,1))
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
    if fCheck(y) == False:
        print("y is function? INSPECTOR", fCheck(y))
        return
    return Compose(y,PreImage(y))

def Elem_My(x,y):
    '''
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

def VisionBasis(basis,vision):
    ANS = []
    if fCheck(vision) == False:
        print("vision is function?", fCheck(vision))
        return
    for x in vision:
        ANS.append([basis[int(x[0])],basis[int(x[1])]])
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
    #print("================",smallLinks,largeLinks)
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
    #print("================")
    return LinkPool

#insert into a list at the right index
def InsertAt(List,obj,Index):
    '''
    Inserts obj at List[Index] and appends the rest of list after it
    '''
    VALUE = List[:Index]
    VALUE.append(obj)
    for x in range(0,len(List[Index:])):
        VALUE.append(List[Index + x])
    return VALUE

def PhiConstruct(IndexRan,ZeroStart,LinkPool):
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
    #print("what is IndexRan?",IndexRan,ZeroStart)
    for x in IndexRan:
	#print("what's failing?",x,x[0],LinkPool,LinkPool[x[0]])
	#print("failing 2 probably",[y for y in LinkPool[x[0]] if y not in ran(Exclusion)])
        ThePick = [y for y in LinkPool[x[0]] if y not in ran(Exclusion)][x[1]]
        Exclusion.append([x[0],ThePick])
	#print("check pick and exclusion/ran exclusion", ThePick, Exclusion, ran(Exclusion))
        TheChoice = TheChoice + [[ThePick,x[0]],[x[0],ThePick]]
	#print("choice?",TheChoice)
    return TheChoice

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
    binary = "{0:b}".format(i)[::-1]
    bin2 = "{0:b}".format(j)[::-1]
    if str(binary) == str(bin2[:len(binary)]):
        return True
    else:
        return False

def PermutePrep(LinkPool,E_G,E_H):
    #idea: just make a list with sizes instead of dicking around with LinkPool and rewrite the rest
    #ADD THEM IN TERMS OF SIZE (since if we made the lists properly they should all include each other if one linkpool is bigger than the other)
    LinkPoolList = []
    
    for x in LinkPool:
        if len(LinkPoolList) == 0:
            LinkPoolList.append([x,LinkPool[x]])
        else:
            for y in LinkPoolList:
                #print("what is LinkPoolList?",LinkPoolList)
                #print("the stuff",LinkPool[x] , y[1])
                #print("the test",len(LinkPool[x]) >= len(y[1]))
                if len(LinkPool[x]) <= len(y[1]):
                    LinkPoolList = InsertAt(LinkPoolList,[x,LinkPool[x]],LinkPoolList.index(y))
                    break
                else:
                    LinkPoolList.append([x,LinkPool[x]])
                    break
                #print("LinkPoolList UPdate?",LinkPoolList)
    #print("testing LinkPoolList",LinkPoolList)
    
    TheSize = []
    TheList = []
    i = 0
    for x in LinkPoolList:
        TheSize.append([x,len(x[1]) - i])
        TheList.append(x[0])
        i += 1

    #NOTE: BECAUSE THERE ARE REPEATS IN THE NUMBERS, YOU NEED TO FILTER OUT THE SETS
    #idea: once you are done with making a candidate, you construct phi by sequentially picking from the first set and excluding that pick from the rest, then construct phi and test SI

    #I don't want to fuck with the working code so I'm just going to make a new if statement:
    #print("REAL TESTING")
    #print("E_G",E_G)
    #print("E_H",E_H)
    #print("dom of E_G",dom(E_G))
    #print("ran of E_G",ran(E_G))
    Zero = []
    for what in ran(E_G):
	if what not in dom(E_G):
	    Zero.append(what)
    #print("do I have an accurate list of Zeronodes?", Zero)
    Zero2 = []
    for what in ran(E_H):
	if what not in dom(E_H):
	    Zero2.append(what)
    #make ZeroLinks:
    ZeroLinksList = []
    ZeroLinks = {}
    #assume phi is from E_G to E_H
    #ACTUALLY I'M PRETTY SURE ZERO NODES CAN LINK TO ANYTHING IN V_G
    for x in Zero:
        #ZeroLinksList.append([x,Zero2])
	ZeroLinksList.append([x,Vertex_(E_H)])
	ZeroLinks[x] = Vertex_(E_H)
    #print("test if ZeroLinks works",ZeroLinksList)
    #print("REALTESTING END") 

    ZeroSize = []
    ZeroList = []
    i = 0
    for x in ZeroLinksList:
	ZeroSize.append([x,len(x[1]) - i])
	ZeroList.append(x[0])
        i += 1
   
    #print("testing ZeroSize", ZeroSize)
    #print("testing ZeroList", ZeroList)

    ZeroPhiIndex = []    
    for x in ZeroSize:
	if len(ZeroPhiIndex) > 0:
            ZeroPhiNew = []
            for H in range(0,x[1]):
                for J in ZeroPhiIndex:
                    Appendage = J + [H]
                    ZeroPhiNew.append(Appendage)
                    #if len(Appendage) == len(ZeroPool):
			#print("this got fucking complicated again, index is:",ZeroPhiIndex)
			
	else:
	    #print("ok so apparently G[1] is super important",G[1])
            for H in range(0,x[1]):
		#print("ok need to check what H is",[H])
                ZeroPhiIndex.append([H])
		#print("this got fucking complicated again, index is2:",ZeroPhiIndex)
    #print("WHAT IS ZEROPHIINDEX?",ZeroPhiIndex)
    #so TRY:
    #if zeronodes is nonempty and ZeroLinks IS EMPTY, say NOT SI
    # so asumme we either are doing smaller -> larger or same size -> larger

    #PhiConstrcut(Indexer,LinkPool)

    #if there are nodes that are just end points, then we need to map endpoints to endpoints:
    #if number of endpoint nodes are diff between the two AND same edge size then just say NOT SI
    #^^^ this sounds too convoluted wtf
    #then use two PhiConstructs and append them then test into the large addressfunc



    #print("Thesize",TheSize)
    #print("TheList",TheList)
    Consistency = []
    #modify for Zeronodes
    TheSize = TheSize + ZeroSize
    TheList = TheList + ZeroList
    #print("check if dictMerge is right",LinkPool)
    #print("B",ZeroLinks)
    LinkPool = dictMerge(LinkPool,ZeroLinks)
    #print("LinkPool", LinkPool)
    #print("theSize", TheSize)
   

    for G in TheSize:
	#print("check consistency",Consistency,len(Consistency) > 0)
        if len(Consistency) > 0:
            ConsistencyNew = []
            #print("test G and G[1]",G)
            #print(G[1])
            for H in range(0,G[1]):
                for J in Consistency:
                    Appendage = J + [H]
		    
                    ConsistencyNew.append(Appendage)
                    #print("appendage?",Appendage,len(Appendage) == len(LinkPool))
                    if len(Appendage) == len(LinkPool):
                        #construct phi
                        #RULE: construct phi sequentially by picking from first set and excluding that pick from the rest
                        ZeroStart = len(Appendage)
			Indexer = []
                        for i in range(0,len(TheList)):
                            Indexer.append([TheList[i],Appendage[i]])
			#print("BAD INDEXER?",Indexer)
			#print("WTF IS AN INDEXER1!!!!",Indexer)
                        #print("what is phi?",Appendage,PhiConstruct(Indexer,ZeroStart,LinkPool))
			#OK FUCK THIS
			#if Releval fails we just say NOT SI
			try: 
			    AddressFunc(Compose(Minv_(Beta_(E_H)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_G) 
			except IndexError:
			    print("N1Address failed so assume NOT SI!")
			    return False
			try:
			    AddressFunc(Compose(Minv_(Beta_(E_G)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_H)
			except IndexError:
			    print("N2Address failed so assume NOT SI!")
			    return False 
                        #print("Achecking if address works with at least one choice func",AddressFunc(Compose(Minv_(Beta_(E_H)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_G))
                        #print("Achecking if address works with other choice func",AddressFunc(Compose(Minv_(Beta_(E_G)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_H))
			AD1 = AddressFunc(Compose(Minv_(Beta_(E_H)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_G) 
			AD2 = AddressFunc(Compose(Minv_(Beta_(E_G)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_H)
                        if LessThan_C(AD1,AD2):
                            return True
            Consistency = ConsistencyNew
        else:
	    #print("ok so apparently G[1] is super important",G[1])
            for H in range(0,G[1]):
		#print("ok need to check what H is",[H])
                Consistency.append([H])
		#NOTE: When I wake up you need to add the SI ocndition here if there is only one choice for the phi function
		#print("what is consistency/IndexRan?",Consistency)
		#print("what are the graphs?",E_G)
		#print(E_H)
		#print("ok now check LinkPoolList",LinkPoolList)
		#print("check if LinkPool is messed up too",LinkPool)
		#print("use TheList = 1?",TheList)
		if len(TheList) == 1:
		    Indexer = []
		    #print("what is the real problem and is Consistency being empty it?",Consistency)
		    #print("what is TheList",TheList)
                    for i in range(0,len(TheList)):
			#print("wtf is i?",i, TheList[i],"Consistency[i][0]")
                        Indexer.append([TheList[i],Consistency[i][0]])
		    #print("WTF IS AN INDEXER2",Indexer)
		    ZeroStart = 1
		    #print("bad indexer?",Indexer)
		    #print("=======================")
		    #print("index I feed is fucked,E_H", E_H)
		    #print("E_G",E_G)
		    #print("Beta_",Beta_(E_H))
		    #print("Indexer for phiconst",Indexer)
		    #print("Phiconstruct",PhiConstruct(Indexer,ZeroStart,LinkPool))
		    #print("normies",Compose(Minv_(Beta_(E_H)),PhiConstruct(Indexer,ZeroStart,LinkPool)))
		    #print("=======================")
		    #print("wtf is wrong",AddressFunc(Compose(Minv_(Beta_(E_H)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_G))

		    #CHECK IF Addressfuncs fail (it's not strong enough to say NOT SI: EX THIS SI SET:[[['A','A']],[['A','A'],['B','A']]])
		    Bool1 = True
		    Bool2 = True
		    try: 
		        AddressFunc(Compose(Minv_(Beta_(E_H)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_G) 
		    except IndexError:
		        print("N3Address failed so SKIP!")
			Bool1 = False
		        #return False
		    #FUCK I deleted a huge swath of code and all I have is old shit from 3 days ago
		    print("watch Star Driver",AddressFunc(Compose(BasisAttempt,PhiConstruct(Indexer,ZeroStart,LinkPool)),WLOG))
		    try: 
		        AddressFunc(Compose(Inspector_M(M_(rchi(Vertex_(Larger)))),PhiConstruct(Indexer,ZeroStart,LinkPool)),WLOG)
		    except IndexError:
		        print("3Address failed so assume NOT SI!")
		        return False
		    #print("check error ",AddressFunc(Compose(Inspector_M(M_(rchi(Vertex_(WLOG)))),PhiConstruct(Indexer,ZeroStart,LinkPool)),Larger))
		    print("wtf?",Inspector_M(M_(rchi(Vertex_(WLOG)))))
		    print("over what you to be",PhiConstruct(Indexer,ZeroStart,LinkPool))
		    print("Larger",Larger)
		    try:
		        AddressFunc(Compose(Inspector_M(M_(rchi(Vertex_(WLOG)))),PhiConstruct(Indexer,ZeroStart,LinkPool)),Larger)
		    except IndexError:
		        print("4Address failed so assume NOT SI!")
		        return False 
		    #print("what is indexer?",Indexer)
                    #print("what is phi?",PhiConstruct(Indexer,ZeroStart,LinkPool))
		    #print("Bchecking if address works with at least one choice func",AddressFunc(Compose(Minv_(Beta_(E_H)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_G))
                    #print("Bchecking if address works with other choice func",AddressFunc(Compose(Minv_(Beta_(E_G)),PhiConstruct(Indexer,ZeroStart,LinkPool)),E_H))
		    AD1 = AddressFunc(Compose(Inspector_M(M_(rchi(Vertex_(Larger)))),PhiConstruct(Indexer,ZeroStart,LinkPool)),WLOG)
		    AD2 = AddressFunc(Compose(Inspector_M(M_(rchi(Vertex_(WLOG)))),PhiConstruct(Indexer,ZeroStart,LinkPool)),Larger)
                    if LessThan_C(AD1,AD2):
                        return True
    return "can't tell"

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

def ShittySI(E_G,E_H):
    '''
    organize by # of links
    then make picks
    test with SI until picks are exhausted
    if picks are exhausted then G not SI H
    '''

    if fCheck(E_G) == False or fCheck(E_H) == False:
        print("shittysi funcchecking E_G is", fCheck(E_G), "E_H is ",fCheck(E_H))
        return
    #figure out which one is the bigger one

    if len(E_G) < len (E_H):
        WLOG = E_G
        Larger = E_H
    else:
        WLOG = E_H
        Larger = E_G
    #organize by # of links
    #print(EdgeSortbyLinks(WLOG))
    #print(EdgeSortbyLinks(Larger))
    smallLinks = EdgeSortbyLinks(WLOG)
    largeLinks = EdgeSortbyLinks(Larger)

    LinkPool = LinkPoolGen(smallLinks,largeLinks)

    #rule: we cannot inject a node with X links to a node with <X links
    #now to make a list of pics for each node in WLOG:
    
    '''
    there is a "problem" with same size sets
    #1:
    {1: ['A', 'B', 'C'], 3: ['H']}
    {1: ['Z', 'X'], 2: ['Y', 'V']}
    can't inject H into other graph but other graph might be able to inject into H's graph
    #2: new theorem:
    two graphs, A,B of the same edge size:
    graph A has a node with linksize of X that exceeds all the linksizes of graph B
    then A not SI B
    for this check:
    if not all nodes in smalllinks are in LinkPool, say NOT ISOMORPHIC
    if graph sizes are the same, try this check 
    '''
    #SI disqualification
    for x in smallLinks:
        for y in smallLinks[x]:
            #print("is y what I'm looking for?",y)
            if y not in LinkPool:
                print(y,"not in LinkPool!", LinkPool)
                print("so NOT ISOMORPHIC!")
                return False
    if len(E_G) == len(E_H):
        smallLinks2 = EdgeSortbyLinks(Larger)
        largeLinks2 = EdgeSortbyLinks(WLOG)
        #print(smallLinks2)
        #print(largeLinks2)

        LinkPool2 = LinkPoolGen(smallLinks2,largeLinks2)

        #SI disqualification
        for x in smallLinks2:
            for y in smallLinks2[x]:
                #print("is y what I'm looking for?",y)
                if y not in LinkPool2:
                    print(y,"not in LinkPool!", LinkPool2)
                    print("so NOT ISOMORPHIC!")
                    return False
    #ORGANIZE LINKPOOL FROM SMALLEST TO LARGEST
    #print("ok so what do I have?", LinkPool)

    #similar edge count but diff vertex count = NOT SI
    if len(E_G) == len(E_H) and len(Vertex_(E_G)) != len(Vertex_(E_H)):
	print("NOT SI by edge and vertex count!",E_G,E_H)
	return False
    '''
    rules:
    choices are mutally exclusive: so if a node can only connect to Y we can't pick Y "earlier" or we mess up the picking
    idea:
    list by # of picks, the smaller first
    and only start alternating when # picks >1
    
    TheChoice = []
    
    delList = []
    #filter LinkPool by # choices -> also because each choice is mutually exclusive remove them from the other pools
    for x in LinkPool:
        if len(LinkPool[x]) == 1:
            TheChoice = TheChoice + [[x,LinkPool[x][0]],[LinkPool[x][0],x]]
            delList.append(x)
    #filter out LinkPool[x][0] in the other choices
    for x in LinkPool:
        for z in delList:
            LinkPool[x] = [y for y in LinkPool[x] if y != LinkPool[z][0]]
        
    for x in delList:
        del LinkPool[x]
    
    #once number of choices >1 then we start picking/alternating
    '''
    
    
    
    
    '''
    idea:
    pick one then exhaust that choice on the other sets
    pick one ....
    then at the last, test out the SI condition
    then exhaust all the picks at the last
    then back up once, and then repeat
    one the back up is exhausted, repeat again
    ...
    
    idea:
    [the choice1, 2, ....]
    then we need a function that "alternates the last X choices for TheChoice"
    try alternating the last choice
    then
    the last two choices
    etc
    
    Exclusion = []
    Vertices = []
    print("what the ", LinkPool)
    print("I need to make all possible choices!==", TheChoice)
    for x in LinkPool:
        Vertices.append(x)
        ThePick = [y for y in LinkPool[x] if y not in Exclusion][0]
        Exclusion.append(ThePick)
        TheChoice = TheChoice + [[x,ThePick],[ThePick,x]]
    
    path = len(Vertices) - 1
    print("I need to make all possible choices!BBBBBB", TheChoice)
    if AddressFunc(Compose(Minv_(Beta_(E_H)),TheChoice),E_G) == AddressFunc(Compose(Minv_(Beta_(E_G)),TheChoice),E_H):
        print("E_G isom to E_H!")
        return True
    else:
        #go "down" the "current path" or "go back"
        #go back
        if len([y for y in LinkPool[Vertices[path]] if y not in Exclusion]) == 1:
            path = path -1
            #reset exclusion
            Exclusion = []
        #down current path
            
        #if we have exhausted the space, say False and NOT ISOMORPHIC
        
    '''
    
    #print("E_G",E_G)
    #print("E_H",E_H)
    #print("finalchoice",TheChoice)
    #print("newpool",LinkPool)
    #print("???",Minv_(Beta_(E_H)))
    #print("checking address for a sec",Compose(Minv_(Beta_(E_H)),TheChoice))
    #print("checking if address works with at least one choice func",AddressFunc(Compose(Minv_(Beta_(E_H)),TheChoice),E_G))
    #print("checking if address works with other choice func",AddressFunc(Compose(Minv_(Beta_(E_G)),TheChoice),E_H))
    #PermutePrep(LinkPool,E_G,E_H)
    return PermutePrep(LinkPool,WLOG,Larger)

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

##############################################################
#TESTING STAGE


#print("basislist", basislist)
#print("fml", Address(basislist,M_(inputtext)))
#print(AutoVision(Address(basislist,M_(inputtext)),1))
#test
#f2 = [[4,5],['r','g'],[1,3],[7,7],["t","y"],[555,33],[8746,8946]]
#f1 = [[3,1],['g','t'],['r','y'],['y',"art"],[7,7],[90,9],[0,9],['o','o']]
#print(f1)
#print(f2)
