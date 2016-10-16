from math import *
#import networkx as nx
#from networkx.algorithms import isomorphism
from collections import Counter
import ast

def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

def Address(string, file):
    #returns [basis,1,partialbinary]
    #make charbasis
    charbasis = ["[","]", "\\","\"", "True", "False"]
    file.seek(0)
    for c in file.read():
        if c not in charbasis:
            charbasis.append(c)
    #make Xn
    Xn = []
    n = 1
    for x in range(getSize(file)):
         Xn.append(n)
         n += 1
    basis = charbasis + Xn
    i = 1
    #have to make a list of lists since I need vision to work on higher powersets
    upperresult = []
    partialbinary= []
    for c in string:
        #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
        #(x,y)= (1/2)(x+y)(x+y+1)+y
        x = basis.index(i)+1
        y = basis.index(c)+1
        appendthis = (1/2)*(x+y)*(x+y+1)+y
        partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
        i += 1
    upperresult.append(partialbinary)
    return [basis,1,upperresult]

def Address2(string, *args):
    #*args should be a list of bases
    #return a list of addresses:
        #element of value looks like: [[basis,1,address],missing chars]
    value = []
    for basis in args:
        i = 1
        upperresult = []
        partialbinary= []
        missing = []
        for c in string:
            #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
            #(x,y)= (1/2)(x+y)(x+y+1)+y
            err = []
            try:
                #pairing func starts at 1!(?)
                x = basis.index(str(i))+1
            except(ValueError,IndexError):
                print("i is missing", i)
                err.append(i)
            try:
                y = basis.index(c)+1
            except(ValueError,IndexError):
                print("char is missing", c)
                err.append(c)
            if len(err) >= 1:
                missing.append([i,c])
            else:
                appendthis = (1/2)*(x+y)*(x+y+1)+y
                partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
            i += 1
        upperresult.append(partialbinary)
        value.append([[basis,1,upperresult],missing])
    #return a list of addresses:
        #element of value looks like: [[basis,1,address],missing chars]
    return value

def ConcatAddress(elem, AddressElem):
    #takes an element in the basis, and and Addresslist = [basis,L,partialbinary]
    #returns the set {elem, representation(AddressElem)} in the form of an Addresslist
    '''
    idea:
    [address of parts] is subset in Powerset^some power
    address(total)= sum of [address of parts] is element in Powerset^some power +1
    WANT:{(1,1),address(total)}
    since we do powerset again, and our basis is well ordered by our address func, can straight up calculate the address of parts again on the old powerset:
    [address((1,1)), address^2(total)] in Powerset^some power + 1
    sum([address((1,1)), address^2(total)]) is address of this element in Powerset^some power + 2
    hints:
        partial binary starts at 2^0
        powerset indexing starts at 0
        partial binary is always a subset
    old idea:
    #pairing func starts at 1!(?)
    #takes coord locations and returns the address
    #Number = (1/2)*(x+y)*(x+y+1)+y
    '''
    newPartial = []
    if elem in AddressElem[0]:
        #append address of elem to AddressElem
        #print("REMOVING EXTRA PAIRS", Address2(elem,AddressElem[0])[0][0][2][0])
        #print("REMOVING EXTRA PAIRS", AddressElem[2][0])
        newPartial.append(Address2(elem,AddressElem[0])[0][0][2][0])
        newPartial.append(AddressElem[2][0])
        '''
        for number in Address2(elem,AddressElem[0])[0][0][2]:
            newPartial.append(number)
        '''
        return [AddressElem[0],AddressElem[1]+1,newPartial]
    else:
        print("something went wrong with ConcatAddress")    

def Vision(Addresslist):
    #Addresslist = [basis,1,partialbinary]
    #note: partialbinary now is a list of lists which contain values
    #representation is a list of values: (x,f(x))
    representation = []
    for listseq in Addresslist[2]:
        #print("what is listseq?", listseq)
        function = []
        i = 1
        for pair in listseq:
            z = pair
            w = floor((sqrt(8*z+1)-1)/2)
            t = (w*w+w)/2
            y = z - t
            x = w - y
            if i == len(listseq):
                function.append([Addresslist[0][int(x)-1],Addresslist[0][int(y)-1]])
                representation.append(function)
            else:
                function.append([Addresslist[0][int(x)-1],Addresslist[0][int(y)-1]])
            i+= 1
    return representation
    
def Stringify(representation):
    #returns string
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

    splicedelimiters=[",", ";", ":", "-", "—", "\n"]
    SpliceStartPos = 0
    i = 0
    for x in string:
        if i == len(string)-1:
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

def readable(file):
    for x in file:
        if x == ",":
            file.write("\n")
def readable2(listcode, file):
    for x in str(listcode):
        file.write(x)
        if x == ",":
            file.write("\n")

def MstringtoList(string):
    #MAKE SURE THAT LINES DON'T HAVE SPACES BEFORE NEWLINE ON THE FIRST LINE
    #format is matrix with spaces between them and newlines for new rows
    #format is:
    #MstringtoList(string)[row # starting from 0][column # starting from 0]
    Value = []
    row = []
    i = 0
    lastpos = 0
    for x in string:
        if x == " ":
            #check how strings with newlines work
            if string[lastpos:i].strip(" ") != "":
                row.append(string[lastpos:i].strip(" "))
            lastpos = i
        if x == "\n":
            row.append(string[lastpos:i].strip(" "))
            lastpos = i+1
            Value.append(row)
            row = []
        if i == len(string)-1:
            row.append(string[lastpos:i+1].strip(" "))
            lastpos = i+1
            Value.append(row)
            row = []
        i+=1
    return Value
    
def MlistMult(LeftM, RightM):
    #left and right matrices need to be matrix lists[list of rows]
    #return Matrix List:
    #format: Matrix[row # from 0][column # from 0]
    MList = []
    #check if they fit size req:
    #columns left matrix =/= # rows of right matrix
    if len(LeftM[0]) != len(RightM):
        print("fix your sizes")
        return False
    #multiply matrices (row by row):
    #row
    i = 0
    #column
    j = 0
    row = []
    for i in range(0, len(LeftM)):
        #construct the row:
        #print("range(0,len(RightM[0])):",range(int(len(RightM[0]))))
        for j in range(0,len(RightM[0])):
            #construct AB[i][j]
            #do the sum of A[i][k]B[k][j] from k = 0 to #rows of A -1
            k = 0
            value = 0
            for k in range(0, len(LeftM[0])):
                value = value + int(LeftM[i][k])*int(RightM[k][j])
            #append value to the row:
            row.append(value)
            #if j == len(RightM)-1:
            if j == len(RightM[0])-1:
                #append row to MList
                MList.append(row)
                #clear row
                row = []
    return MList

def MlistTranspose(M):
    #takes a Matrix List
    MList = []
    #switch the x,y coords
    #X coord
    i = 0
    #Y coord
    j = 0
    #clean row:
    row = []
    #print("start",M)
    #switch for i and for j, 
    for i in range(len(M[0])):
        for j in range(len(M)):
            #build the row
            #print("values",j,i,M[j],M[j][i])
            row.append(M[j][i])
            if j == len(M)-1:
                #append the row
                MList.append(row)
                #clear the row
                row = []
    return MList

def MlistLSComponent(check,test):
    #new version only considers nonzero elements for componentwise checking
    #check and test are Mlists
    #you check against the test and see if check matrix has the same values as test at each value
    #check if size(check) < size(test)
    if len(check)> len(test) or len(check[0])> len(test[0]):
        return False
    #x
    i = 0
    #y
    j = 0
    #enumerate through check:
    for i in range(len(check)):
        for j in range(len(check[0])):
            #at each point, check if value at check is the same as value at test:
            #if not, return false:
            if check[i][j] != 0 and check[i][j] != test[i][j]:
                return False
    else: 
        return True

def MlistLSComponentOG(check,test):
    #OG checks componentwise
    #check and test are Mlists
    #you check against the test and see if check matrix has the same values as test at each value
    #check if size(check) < size(test)
    if len(check)> len(test) or len(check[0])> len(test[0]):
        return False
    #x
    i = 0
    #y
    j = 0
    #enumerate through check:
    for i in range(len(check)):
        for j in range(len(check[0])):
            #at each point, check if value at check is the same as value at test:
            #if not, return false:
            if check[i][j] != test[i][j]:
                return False
    else: 
        return True

def AddresstoMlist(Address):
    MList = []
    #create null matrix
    #x
    i = 0
    #y
    j = 0
    row = []
    for x in range(len(Address[0])):
        for y in range(len(Address[0])):
            row.append(0)
            if y == len(Address[0])-1:
                MList.append(row)
                row = []
    #MList[2][2] = "tree"
    #print("checking modifiers") (works as intended with the null matrix)
    #need address -> matrix list function
    for pair in Vision(Address):
        #X value should always be int:
        #check if x val is int
        if type(pair[0]) is int:
            #y value should be checked with relation to basis: Address[0].index(pair[1])
            #then make MList[x][y] = 1
            MList[Address[0].index(pair[0])][Address[0].index(pair[1])] = 1
        else:
            print("x val for Address was not an int")
            return MList
    return MList

def MList1Square(size):
    #makes Mlist square matrix of specified size 
    x = 0
    y = 0
    MList = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(1)
            if y == len(range(size))-1:
                MList.append(row)
                row = []
    return MList

def UllmanSI(used_columns, cur_row, G, P, M):
    #note: to start UllmanSI
        #used_columns={range of columns of G as list}
            #format is:
            #column number: "used" or "unused"
            #set them all to "unused" ON INIT
        #cur_row = 0
    #G, P, M are all Matrix lists
    #checks if graph G has a subgraph G' isom to graph P
        #returns True/False if P isom to some subgraph of G
    #print("what the fuck do I have", used_columns, cur_row, G, P, M)
    if cur_row == len(M)-1:
        print("tried the check at cur row=", cur_row)
        print("M is ", M)
        if MlistLSComponent(P,MlistMult(M, MlistTranspose(MlistMult(M,G)))):
            return True
    MClone = M
    #print("M and Mclone",M,MClone)
    #prune(MClone)
    for W in range(len(M)):
        if used_columns[W] == "unused":
            #set column c in M' to 1 and other columns to 0
            i = 0
            j = 0
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if j == W:
                        M[i][W] = 1
                    else:
                        M[i][j] = 0
            #mark c as used
            used_columns[W] = "used"
            #print("new used   is [w]",W,used_columns)
            UllmanSI(used_columns, cur_row+1, G, P, MClone)
            #print("new unused is [w]",W,used_columns)
            used_columns[W] = "unused"
    '''
    M' = M
    prune(M')

    for all unused columns c
        set column c in M' to 1 and other columns to 0
        mark c as used
        recurse(used_column, cur_row+1, G, P, M')
        mark c as unused

    output no
    '''
    return "random shit"

def prune(M):
    #M is an MList
    i = 0
    j = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 1:
                #find neighbors x of i in P:
                z = 0
                #all neighbors are on the same row (and exclude itself):
                neighborsinP = []
                for z in range(len(M[0])):
                    if M[i][z] != 1 and z != j:
                        neighborsinP.append(j)
                
    '''
    do
        for all (i,j) where M is 1
            for all neighbors x of vi in P
                if there is no neighbor y of vj s.t. M(x,y)=1
                    M(i,j)=0
    while M was changed
    '''
    pass
    
def SI(P, G, Basis):
    #checks if P subgraph isomorphic to G
    #P,G MLists
    #Basis is a list
    G1 = nx.Graph()
    #if P[i][j] == 1, then add i and j as nodes and add their edge
    i = 0
    j = 0
    for i in range(len(P)):
        for j in range(len(P[0])):
            if P[i][j] == 1:
                G1.add_node(Basis[i])
                G1.add_node(Basis[j])
                G1.add_edge(Basis[i],Basis[j])
    print("WTF???", G1.nodes(),G1.edges())
    G2 = nx.Graph()
    i = 0
    j = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == 1:
                G2.add_node(Basis[i])
                G2.add_node(Basis[j])
                G2.add_edge(Basis[i],Basis[j])
    GM = isomorphism.GraphMatcher(G1,G2)
    print("WTF???", G1.nodes(),G1.edges())
    return GM.is_isomorphic()
'''
def ShittySI():
    #make MasterListByEdgeCountP:=[[count of 5][count of 4][count of 3]...]
    #make MasterListByEdgeCountG:=[[count of 5][count of 4][count of 3]...]
    for Vp in MLBECP:
        make exhaustVpOG
        make exhaustVpClone
    Pindex = 0
    for Vg in Exhaust(Vp)Clone# the first Vp in MLBECP
        map Vp to exhaustVpClone[0]
        remove Vp from exhaustVpClone
        if (map passes connection check):
            [go to next Pindex]
            Pindex += 1
            GoToNextP()
        else:
            remove 

    return False

def GoToNextP():
'''    

def SINaive(P, G, Basis):
    #P, G MLists
    Answer = False
    #check trivial:
    if MlistLSComponent(P,G):
        print("use trivial isom")
        Answer = True
    #fuck it just enum through all possible transformation matrices:
    #take M to be a function from P->G
    MTemp = []
    Temprow = []
    #MSequence powerset of M
    #plan is to just go through all the possible isomorphisms because I'm stupid and can't do VF2 properly for some reason
    MSequence = []
    row = []
    for i in range(2 ** (len(P)* len(G[0]))):
        for j in range(len(P)* len(G[0])):
            if ceil((i + 1)/((2 ** (len(P)*len(G[0])))/(2 ** (j + 1)))) % 2 == 0:
                 row.append(0)
            else:
                 row.append(1)
            if j == len(P)* len(G[0])-1:
                MSequence.append(row)
                #print("what is row?", row)
                #the row is a matrix so just check if P <= M(MG)^transpose:
                s = 1
                for elem in row:
                    Temprow.append(elem)
                    #print("wtf check: len, s, scheck", len(G[0]), s, s % len(G[0]) == 0)
                    if s % len(G[0]) == 0:
                        MTemp.append(Temprow)
                        Temprow = []
                    s += 1
                #map the "isom"
                    ###TODO
                print("check for isom", MlistLSComponent(P,MlistMult(MTemp, MlistTranspose(MlistMult(MTemp,G)))))
                print("MTemp is:", MTemp)
                if MlistLSComponent(P,MlistMult(MTemp, MlistTranspose(MlistMult(MTemp,G)))):
                    #then after going through the whole row, check out MTemp:
                    #print("checking MTemp", MTemp)
                    #if yes, check if MTemp really is an isom:
                    #@ most one 1 in a row and one 1 in a column
                    isomQuery = True
                    sumCheck = 0
                    columnCheck = []
                    rowPos = 0
                    for theRow in MTemp:
                        for theElement in theRow:
                            #print("varchecks", theRow, theElement, sumCheck, rowPos)
                            sumCheck += theElement
                            rowPos += 1
                            if sumCheck > 1:
                                #print("MTemp not isom in row!")
                                isomQuery = False
                            if theElement == 1:
                                #print("colcheck", columnCheck)
                                columnCheck.append(rowPos)
                                #print("colcheckEND", columnCheck)
                                #check if there are duplicates in columnCheck
                                if len([k for k,v in Counter(columnCheck).items() if v>1])>=1:
                                    #print("MTemp not isom in column!")
                                    isomQuery = False
                        sumCheck = 0
                        rowPos = 0
                    if isomQuery == True:
                        print("The isom matrix is:", MTemp)
                        return True
                #clear MTemp:
                MTemp = []
                
                row = []
    #print("check powerset", MSequence)
    return Answer

def ChainEval(AList1, AList2):
    #idea: takes two objects in some "finite extension" then composes their arrows togther
    #so then f compose g is taking arrows of g and following them to the range of f
    #function takes two address lists then returns the addresslist of the their "composition"

    #f compose g means do g first then f:

    data = [AList1, AList2]
    #AList# is an addresslist
    #IDEA: Use a dictionary implementation
    '''
    EX:
    >>> tel = {'jack': 4098, 'sape': 4139}
    >>> tel['guido'] = 4127
    >>> tel
    {'sape': 4139, 'guido': 4127, 'jack': 4098}
    >>> tel['jack']
    4098
    >>> del tel['sape']
    >>> tel['irv'] = 4127
    >>> tel
    {'guido': 4127, 'irv': 4127, 'jack': 4098}
    >>> list(tel.keys())
    ['irv', 'guido', 'jack']
    >>> sorted(tel.keys())
    ['guido', 'irv', 'jack']
    >>> 'guido' in tel
    True
    >>> 'jack' not in tel
    False
    '''
    ENCYCLO = {}
    i = 0
    for function in data:
        #have a dynamic dict name:
        ENCYCLO["function" + str(i) + "dom"] = None
        ENCYCLO["function" + str(i) + "ran"] = None
        print("function is ", function[2])
        print("vision is ", Vision(function))
        #PROBLEM: Not respecting the upper level pairs
        for thing in Vision(function):
            print("what isthing?", thing)
            for pairelem in thing:
                #print("what is pairelem?", pairelem[0], pairelem[1], ENCYCLO["function" + str(i) + "dom"], ENCYCLO["function" + str(i) + "ran"])
                #check if they are empty> init lists:
                if ENCYCLO["function" + str(i) + "dom"] is None:
                    ENCYCLO["function" + str(i) + "dom"] =  [pairelem[0]]
                    #print("NONETYPE",ENCYCLO["function" + str(i) + "dom"])
                else:
                    #print("before append",ENCYCLO["function" + str(i) + "dom"])
                    ENCYCLO["function" + str(i) + "dom"].append(pairelem[0])
                    #print("after append",ENCYCLO["function" + str(i) + "dom"])
                if ENCYCLO["function" + str(i) + "ran"] is None:
                    ENCYCLO["function" + str(i) + "ran"] =  [pairelem[1]]
                    #print("NONETYPE",ENCYCLO["function" + str(i) + "ran"])
                else:
                    #print("before append",ENCYCLO["function" + str(i) + "ran"])
                    ENCYCLO["function" + str(i) + "ran"].append(pairelem[1])
                    #print("after append",ENCYCLO["function" + str(i) + "ran"])
                
                
                
                
        print("======","function" + str(i) + "dom",ENCYCLO["function" + str(i) + "dom"])
        print("======","function" + str(i) + "ran",ENCYCLO["function" + str(i) + "ran"])
        #function.ran
        #function.dom
        i += 1
        pass

    #then for each value in the domain of AList2:
    #    look at same pos in AList2.range = ValueX
    #    if ValueX is in range of AList1.dom:
    #       for all those values:
    #           return.append([ValueX, value at pos in f])
    
    return 

'''
def Idle(number, basis, listsofaddresses):
    #number: is how many more do you want to do
    #basis: is the basis you are using
        #from basis.txt
    #listsofaddresses: list of all the stuff you've seen, it's ASSUMED that lists has no "holes":
        #listsofaddresses is from memory.txt
    ######
    #what happens to old addresses if I add an element to basis????
    #I think it's ok to leave as-is since we already know the powerset # since our bases contain each other
    #Answer: at each powerset level, the numbering is preserved if I use my numbering scheme + one basis is contained in the other
    ######
    #plan:
    for i in range(number):
        go to last of lists + 1:
        eval that element
        map successively higher subgraph isom to high objects
'''

def Train():
    #idea: have a question-answer key:
        #two options,
            #interact
            #premade question-answer key
    #then it tries each question:
    #fail> metatheorem about truth is "False"
    #pass> metatheorem about truth is "True"
    '''
    problem: don't memorize everything, rather train it so that it knows how to navigate the upper concept spaces very fast
    '''
    
    return

file = open('INP.txt', 'r')
basis = open('Basis.txt', 'r+')
memory = open('Memory.txt', 'r+')
while True:
    inputtext = str(input("Exit or logout to leave \n"))
    if inputtext == "exit" or inputtext == "logout":
        break
    else:
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

        #have conversation
        #idea: information>read>analyze>response

        for char in inputtext:
            #if stuff is not in the basis:
            if char in basislist:
                pass
            else:
                #append to basis
                basislist.append(char)
        
        #then do address of cheat(inputtext)
        if len(inputtext) in basislist:
            pass
        else:
            for k in range(len(inputtext)+1):
                if str(k) in basislist:
                    pass
                else:
                    basislist.append(str(k))

        #if address is not in memory, then add it
        for morpheme in Cheat(inputtext):
            if len(Address2(morpheme, basislist)) == 0:
                print("basis is missing", Address2(inputtext, basislist)[0][1])
            else:
                #if you can find Address2(inputtext, basislist)[0][0] in memory
                if Address2(inputtext, basislist)[0][0] in memorylist:
                    #do nothing
                    pass
                else:
                    #add Address2(inputtext, basislist)[0][0] to memory
                    memorylist.append(Address2(inputtext, basislist)[0][0])
        
        basis.seek(0)


        
        #print(Address2(inputtext, basislist)[0])
        #print(Address2(inputtext, basislist)[0][0]) #this is what I need to add to memory if missing elements list is null
        #print(Address2(inputtext, basislist)[0][1]) #this is the missing elements list
        #    print("what about everyone else?", Address2(inputtext, basislist)[0][0])
        #print("what about everyone else?", Vision(Address2(inputtext, basislist)[0][0]))
        #    print("fuck", ConcatAddress("1", Address2(inputtext, basislist)[0][0]))
        #    print(Vision(ConcatAddress("1", Address2(inputtext, basislist)[0][0])))
        print(ChainEval(ConcatAddress("1", Address2(inputtext, basislist)[0][0]), Address2(inputtext, basislist)[0][0]))
        
        #print(ConcatAddress("1", Address2(inputtext, basislist)[0][0]))
        #print(Vision(ConcatAddress("1", Address2(inputtext, basislist)[0][0])))

        #ConcatAddress(elem, AddressElem)
        #Vision(Addresslist)
        


        
        #update basis
        #clear basis:
        basis.seek(0)
        basis.truncate()
        #then write the basis:
        basis.write(str(basislist))

        #update memory
        #clear memory:
        memory.seek(0)
        memory.truncate()
        #then write the memory:
        memory.write(str(memorylist))
        


file.close()
basis.close()
memory.close()
