from math import *
#import networkx as nx
#from networkx.algorithms import isomorphism
from collections import Counter
import ast

def STAddress(string, *args):
    return "not done"

def STVision(Addresslist):
    '''
    note: this func is expecting aa # from 1>2^some N
    addresslist:
    [basis, L value, number]
    take addresslist and return ??? [fk I can only return algorithms]
    [it's ok because you have an ordered basis and dealing with directed graphs so you just use lexicographic ordering to produce algorithm for everything]
    '''
    #do PBL?
    #check if error (?)(?)(?)(?)
        #tobinary
        #return the algorithm
    #problem: how to do L>2
    
    return "not done"


def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

def Address(string, file):
    '''
    returns the address of the string with respect to file but doesn't say if file is missing elements wtf
    '''
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
    partialbinary= []
    for c in string:
        #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
        #(x,y)= (1/2)(x+y)(x+y+1)+y
        x = basis.index(i)
        y = basis.index(c)
        appendthis = (1/2)*(x+y)*(x+y+1)+y
        partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
        i += 1
    return [basis,1,partialbinary]

def Address2(string, *args):
    #*args should be a list of bases
    #return a list of addresses:
        #element of value looks like: [[basis,1,address],missing chars]
    value = []
    for basis in args:
        i = 1
        partialbinary= []
        missing = []
        for c in string:
            #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
            #(x,y)= (1/2)(x+y)(x+y+1)+y
            err = []
            try:
                #pairing func starts at 1!(?) F U C K
                x = basis.index(str(i))
            except(ValueError,IndexError):
                print("i is missing", i)
                err.append(i)
            try:
                y = basis.index(c)
            except(ValueError,IndexError):
                print("char is missing", c)
                err.append(c)
            if len(err) >= 1:
                missing.append([i,c])
            else:
                appendthis = (1/2)*(x+y)*(x+y+1)+y
                partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
            i += 1
        value.append([[basis,1,partialbinary],missing])
    #return a list of addresses:
        #element of value looks like: [[[basis, L-value, partialbinary], missingchars with respect to 1st basis]...]
    return value

def CantorPair(x,y):
    return (1/2)*(x+y)*(x+y+1)+y

def GraphAddress(graph, *args):
    #graph is a list of nodes: [[pair],[pair],...]
    #*args should be a list of bases
    #return a list of addresses:
        #element of value looks like: [[basis,1,address],missing chars]
    value = []
    for basis in args:
        partialbinary= []
        missing = []
        '''
        WANT:
        [basis,L value,partialbinary]
        '''
        for pair in graph:
            #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
            #do some error catching
            err = []
            try:
                x = basis.index(pair[0])
            except(ValueError,IndexError):
                print("x is missing", pair[0])
                err.append(i)
            try:
                y = basis.index(pair[1])
            except(ValueError,IndexError):
                print("char is missing", pair[1])
                err.append(pair[1])
            if len(err) >= 1:
                missing.append([pair[0],pair[1]])
            else:
                partialbinary.append(CantorPair(x,y))
        value.append([[basis,1,partialbinary],missing])
        
        '''
        for c in string:
            #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
            #(x,y)= (1/2)(x+y)(x+y+1)+y
            err = []
            try:
                #pairing func starts at 1!(?) F U C K
                x = basis.index(str(i))
            except(ValueError,IndexError):
                print("i is missing", i)
                err.append(i)
            try:
                y = basis.index(c)
            except(ValueError,IndexError):
                print("char is missing", c)
                err.append(c)
            if len(err) >= 1:
                missing.append([i,c])
            else:
                appendthis = (1/2)*(x+y)*(x+y+1)+y
                partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
            i += 1
        
        value.append([[basis,1,partialbinary],missing])
        '''
    #return a list of addresses:
        #element of value looks like: [[[basis, L-value, partialbinary], missingchars with respect to 1st basis]...]
    return value

def ConcatAddress(elem, AddressElem):
    #takes an element in the basis(?????) and Addresslist = [basis,L,partialbinary]
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
    #EVERYTHING DEPENDS ON THE L-VALUE
    #if both L values are 1 then just concat together what they have
    #if one L value is 2, 
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

def BL(B,L):
    '''
    B is size of basis
    L is current L value
    BL(B,L) returns max size of powerset seq
    '''
    size = B ** 2
    for wtf in range(0,L):
        size = 1 << size
    return size

def PBL(z,B,L):
    '''
    "Problem of BL"
    if Z > BL(B,L), what is minimal L such that Z < BL(B,new L)?
    since BL increases super fast, naive solution should either solve fast or integer overflow LOL
    so PBL(z,B,L) returns the minimal L such that Z < BL(B,new L) where
    Z is number
    B is size of basis
    L is current L value
    '''
    while z > BL(B,L):
        L += 1
        if z <= BL(B,L):
            return L
    else:
        print("z<BL(B,L)",z,BL(B,L))

def wtfVision(Addresslist):
    #Addresslist = [basis,1,partialbinary]
    #note: partialbinary now is a list of lists which contain values
    #representation is a list of values: (x,f(x))
    '''
    L VALUE TELLS YOU HOW FAR TO LOOK DOWN BEFORE "UNRAVELING"
    idea: instead of repeated for loops you can screw with the brackets:
    define a bracket distance that defines each braket's "nestedness" then clear them appropriately
    '''
    representation = []
    print("check list", Addresslist[2])
    for pair in Addresslist[2]:
        print("pair is: ", pair)
    
    print("what is representation?", representation)    
    return representation         

def LSkip(List, number):
    '''
    takes a list and a number, then returns a list that "goes down" based on that number
    '''
    ANS = []
    for x in List:
        L = 0
        while L < number-1:
            x=x[0]
            L+=1   
        ANS.append(x)
    return ANS

def Vision(Addresslist):
    #Addresslist = [basis,1,partialbinary]
    #note: partialbinary now is a list of lists which contain values
    #representation is a list of values: (x,f(x))
    '''
    what do you fucking know the Addresslist is supposed to fucking tell you
    because I am dealing with graphs they all have to have the same # of brackets so LSkip works just fine


    L VALUE TELLS YOU HOW FAR TO LOOK DOWN BEFORE "UNRAVELING"
    idea: instead of repeated for loops you can screw with the brackets:
    define a bracket distance that defines each braket's "nestedness" then clear them appropriately
    '''
    representation = []
    LVal = 1
    print("input", Addresslist[2])
    for pair in Addresslist[2]:
        print("pair is", pair)
        while type(pair) is not int:
            print(pair, "is not int!")
            #go down one more
            pair = pair[0]
            LVal += 1
        print("LVal is ", LVal)
        '''
        z = pair
        B = len(Addresslist[0])
        L = Addresslist[1]
        w = floor((sqrt(8*z+1)-1)/2)
        t = (w*w+w)/2
        y = z - t
        x = w - y
        representation.append([Addresslist[0][int(x)],Addresslist[0][int(y)]])
        '''
    #print("what is representation?", representation)    
    return representation

def STRcompose(address1, address2):
    #do address1 first then address2
    #find ran(address1) = ranA1 first
    #do address2(ran(address1))
    ranA1 = []
    for number in address1[2]:
        ranA1.append(Vision([address1[0],address1[1],[number]])[0][1])
    '''
    idea is that since we are only transversing through sets all we do is find if X in ranA1 and X in domA2 then return A2(X)
    '''
    domA2 = []
    for number in address2[2]:
        domA2.append(Vision([address2[0],address2[1],[number]])[0][0])
    Value = []
    for elem in ranA1:
        for pair in address2[2]:
            if elem == Vision([address2[0],address2[1],[pair]])[0][0]:
                if Vision([address2[0],address2[1],[pair]])[0][1] not in Value:
                    Value.append(Vision([address2[0],address2[1],[pair]])[0][1])
    return Value

def topartialbin(number):
    thing = "{0:b}".format(number)[::-1]
    partialbinary = []
    for g in range(0,len(thing)):
        if thing[g] == str(1):
            partialbinary.append(g)
    return partialbinary

def tointeger(listX):
    sum = 0
    for x in range(0,len(listX)):
        sum = sum + 2 ** listX[x] ** 1
    return sum

def idle(basis,X,Y,M):
    #info to keep track of:
    '''
    where we are:
    top level: M
    right now:
    x,y,l
    then, as x,y,l -> M:
    compute and print
    (x,y) is where to start, just do 1,1,M for now
    '''
    for m in range(1,M+1):
        for x in range(X,M+1):
            for y in range(Y,M+1):
                #now do x compose y:
                thing = "{0:b}".format(x)[::-1]
                #print("reverse binary is",thing)
                '''
                partialbinary = []
                for g in range(0,len(thing)):
                    if thing[g] == str(1):
                        #print("test is :", thing[g], str[1],thing[g] == str(1))
                        #print("test is", thing[g],g)
                        partialbinary.append(g+1)
                #print("thing, partial",thing, partialbinary)

                thingy = "{0:b}".format(y)[::-1]
                partialbinaryY = []
                for g in range(0,len(thingy)):
                    if thingy[g] == str(1):
                        partialbinaryY.append(g+1)
                '''
                #print("what M value?", m)
                #print("setup", x,y,m,partialbinary,partialbinaryY)
                #print("x is ",[basis,m,partialbinary])
                #print("y is ",[basis,m,partialbinaryY])
                '''
                size = len(basis) ** 2
                for wtf in range(0,m):
                    check = 2 ** size
                    AKA holy fucking shit what I'm doing takes too long when L>=3
                '''    
                    
                print(Vision([basis,m,[x]]),Vision([basis,m,[y]]),STRcompose([basis,m,[x]],[basis,m,[y]]))
                #print(Vision([basis,m,partialbinary]),Vision([basis,m,partialbinaryY]),STRcompose([basis,m,partialbinary],[basis,m,partialbinaryY]))

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
    #what is listcode???
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
        print("function is ", function)
        print("vision is ", Vision(function))
        #PROBLEM: Not respecting the upper level pairs
        for thing in Vision(function):
            print("what isthing?", thing)
            '''
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
            '''
                
                
                
                
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

def gcomposition(graph1,graph2):
    ### composes graph 1 with graph 2 by following arrows and returns a graph
    #g2dom = []
    ANS= []
    #for y in graph2:
    #    g2dom.append(y[0])
    for x in graph1:
        #print(x[1],Eps(x[1],g2dom))
        #if Eps(x[1],g2dom) > -1:
        for y in graph2:
            if y[0] == x[1]:
                ANS.append([x[0],y[1]])
    return ANS

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

        #print("wtf1")
        #print(GraphAddress([['B', 'A'], ['B', 'B'], ['A', 'C']], ["A","B","C"]))
        #print(Vision(GraphAddress([['B', 'A'], ['B', 'B'], ['A', 'C']], ["A","B","C"])[0][0]))
        #print(Vision(Address2(inputtext, basislist)[0][0]))
        #print("wtf")
            
        ### LAST TIME print(Vision([["A","B","C"],1,topartialbin(31600)]))
        #print(STRcompose([["A","B","C"],1,[2,1,12]], [["A","B","C"],1,[0,3,5]]))
        ### print("==")
        #idle(["A","B","C"],0,0,3)


        
        #print(Address2(inputtext, basislist)[0][0])
        #print(Vision(Address2(inputtext, basislist)[0][0]))
        #print(Vision([['True', 'False', 't', 'e', 's', '0', '1', '2', '3', '4'],1,[1]]))

        #print(Vision([["A","B"],1,[1]]))

        
        #print(Address(inputtext, basis))

        
        #idle(['True', 'False', 't', 'e', 's', '0', '1', '2', '3', '4'],0,0,3)




        #STRcompose([['True', 'False', 't', 'e', 's', '0', '1', '2', '3', '4'], 1, [58.0, 82.0, 110.0, 94.0]],[['True', 'False', 't', 'e', 's', '0', '1', '2', '3', '4'], 1, [58.0, 82.0, 110.0, 94.0]])
            #STRcompose([['True', 'False', 't', 'e', 's', '0', '1', '2', '3', '4'], 1, [112.0, 127.0, 143.0]],[['True', 'False', 't', 'e', 's', '0', '1', '2', '3', '4'], 1, [112.0, 127.0, 143.0]])
        #print(Address2(inputtext, basislist)[0])
        #print(Address2(inputtext, basislist)[0][0]) #this is what I need to add to memory if missing elements list is null
        #print(Address2(inputtext, basislist)[0][1]) #this is the missing elements list
        #    print("what about everyone else?", Address2(inputtext, basislist)[0][0])
        #print("what about everyone else?", Vision(Address2(inputtext, basislist)[0][0]))
        #    print("fuck", ConcatAddress("1", Address2(inputtext, basislist)[0][0]))
        #    print(Vision(ConcatAddress("1", Address2(inputtext, basislist)[0][0])))
            #print("original input1", Address2(inputtext, basislist)[0][0])
            #print("kmn1", Vision(Address2(inputtext, basislist)[0][0]))
            #print("original input", ConcatAddress("1", Address2(inputtext, basislist)[0][0]))
            #print("kmn", Vision(ConcatAddress("1", Address2(inputtext, basislist)[0][0])))
        #print(ChainEval(ConcatAddress("1", Address2(inputtext, basislist)[0][0]), Address2(inputtext, basislist)[0][0]))
        
        #print(ConcatAddress("1", Address2(inputtext, basislist)[0][0]))
        #print(Vision(ConcatAddress("1", Address2(inputtext, basislist)[0][0])))

        #ConcatAddress(elem, AddressElem)
        #Vision(Addresslist)
        
        #####then do address of cheat(inputtext)
        ##### W T F   print(Cheat(inputtext))
        ##print(Address2(inputtext, basislist)[0][0])
        ##print(Vision(Address2(inputtext, basislist)[0][0]))
        #[['True', 'False', 'w', 'h', 'a', 't', ' ', 'e', 'c', 'u', 'l', 'f', 'k', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 's', 'm'], 1, [1210.0, 1310.0, 214.0, 388.0, 416.0]]
        #print(Vision([['True', 'False', 'w', 'h', 'a', 't', ' ', 'e', 'c', 'u', 'l', 'f', 'k', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 's', 'm'], 1, topartialbin(1000)]))
        '''
        what is address of something that went through cheat:
        '''
        printout = []
        for x in Cheat(inputtext):
            printout.append(Address2(x,basislist)[0][0][2:])
        #print(printout)

        
        #it's saying it's missing chars F U C K .
        #checking out autocomposer
        '''
        one problem: in G1, the L-val is fucked because they all don't have the same amt of paren pairs
        '''
        G1 = [[1,2],["A","B"],[[3,4],[5,6]],[7,["yuku yo"]],["so transiently","Kotoko"]]
        G2 = [["subversively",[1,5]],[[1,2],[1,2]],["B","D"],["B","F"],["Kotoko","works with strings"],[9,10],[11,5],["Dwarf fortress","wtf"]]
        
        print(gcomposition(Vision(Address2(G1, basislist)[0][0]),Vision(Address2(G2, basislist)[0][0])))
        print("the issue is that I haven't implemented lemma 1.5.1/2 (? this actually might be its own theorem) because address is complaining but each element is part of the basis so basically I just have to bump up the L-value and return the address properly")
        print("really need to fix address so that it inputs the right Lvalues")

        #so composition works, just have to use N as basis now and keep going:
        #address of x when L > 1?
        print(Vision([[0,1,2,3],3,[3,6,11]]))
        print(Vision([[0,1,2,3],5,[[3,6,11]]]))
        '''
        print("does this return an error?", 
              gcomposition(Vision([[0,1,2,3],1,[5]]),Vision([[0,1,2,3],1,[6]])
                  )
              )
        '''
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
        #maybe python eval is a special case
        #eval(inputtext)


file.close()
basis.close()
memory.close()
