from math import *

def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

def Address(string, file):
    #returns [basis,1,partialbinary]
    #make charbasis
    charbasis = ["[","]", "\\","\""]
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
    partialbinary= []
    for c in string:
        #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
        #(x,y)= (1/2)(x+y)(x+y+1)+y
        x = basis.index(i)+1
        y = basis.index(c)+1
        appendthis = (1/2)*(x+y)*(x+y+1)+y
        partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
        i += 1
    return [basis,1,partialbinary]

def Address2(string, *args):
    #*args should be a list of bases
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
                x = basis.index(str(i))+1
            except(ValueError,IndexError):
                err.append(i)
            try:
                y = basis.index(c)+1
            except(ValueError,IndexError):
                err.append(c)
            if len(err) >= 1:
                missing.append([i,c])
            else:
                appendthis = (1/2)*(x+y)*(x+y+1)+y
                partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
            i += 1
        value.append([[basis,1,partialbinary],missing])
    #retun a list of addresses:
        #element of value looks like: [[basis,1,address],missing chars]
    return value

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
        pairdelimiterpos[pair + "Location"]= [0]
        pairdelimiterpos[pair + "List"]= []

    pairdelimiterpos["AllList"] = ["0","0"]

    splicedelimiters=[",", ";", ":", "-", "—", "\n"]
    SpliceStartPos = 0
    i = 0
    for x in string:
        #you need a hierarchy to get sentence start pos to ignore pairdelimiter rules
        if x in splicedelimiters:
            if max(SentenceStartPos,SpliceStartPos) in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1) and len(pairdelimiterpos["AllList"])>=4:
                #find one that isn't in most recent pair
                k = 1
                for y in SentenceStartPosList:
                    K = len(SentenceStartPosList)
                    if SentenceStartPosList[K-k] not in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1):
                        delimstart = SentenceStartPosList[K-k]
                    else:
                        delimstart = 0
                    k += 1
            else:
                delimstart = max(SentenceStartPos,SpliceStartPos)
            Morphemes.append(string[delimstart:i+1])
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
            else:
                #if it's on for this particular character, slice the string then turn off
                if pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "On"] == 1:
                    pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "On"] = 0
                    #slice the string and append to Morphemes
                    Morphemes.append(string[pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "Location"][-1]:i+1])
                    #add to both location lists
                    pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "Location"].append(i)
                    #NEW
                    #pairdelimiterpos["AllList"].append(i)
                else:
                    pairdelimiterpos[x + "Location"].append(i)
                #be smart about how to turn this on:
                if pairdelimiters.index(x)%2 == 0:
                    pairdelimiterpos[x + "On"] = 1
        if x in sentencedelimiters:
            #know the last .?! , (if any) then cut between first and last .?!
            #ignore pair delimiters
            if SentenceStartPos in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1) and len(pairdelimiterpos["AllList"])>=4:
                #find one that isn't in most recent pair
                k = 1
                for y in SentenceStartPosList:
                    K = len(SentenceStartPosList)
                    if SentenceStartPosList[K-k] not in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1):
                        delimstart = SentenceStartPosList[K-k]
                    else:
                        delimstart = 0
                    k += 1
            else:
                delimstart = SentenceStartPos
            Morphemes.append(string[delimstart:i+1])
            #NEW
            #adding this line since words "stuck" next to punctuation get lost:
            #Morphemes.append(string[int(pairdelimiterpos["AllList"][-1]):i+1])
            
            SentenceStartPos = i+1
            SentenceStartPosList.append(i+1)
        i += 1
    #Morphemes
    return Morphemes

def kys(string):
    #take a string and return a list of strings that represent the important morphemes:
    #punctuation:
    #.?!,;:-—)}]'"...
    #line break
    #paragraph break(?)
    
    #FUCKING USE CASES FOR "'"
    Morphemes = []
    
    sentencedelimiters = [] #...
    SentenceStartPos = 0
    SentenceStartPosList = []
    #every even is start and odd is close for each pair
    pairdelimiters=[ "[", "]"]
    pairdelimiterpos={}
    #EACH PAIR CHAR NEEDS ITS OWN START POS
    for pair in pairdelimiters:
        #use dictionaries
        pairdelimiterpos[pair + "On"]= 0
        pairdelimiterpos[pair + "Location"]= [0]
        pairdelimiterpos[pair + "List"]= []

    pairdelimiterpos["AllList"] = ["0","0"]

    splicedelimiters=[]
    SpliceStartPos = 0
    i = 0
    for x in string:
        #you need a hierarchy to get sentence start pos to ignore pairdelimiter rules
        if x in splicedelimiters:
            if max(SentenceStartPos,SpliceStartPos) in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1) and len(pairdelimiterpos["AllList"])>=4:
                #find one that isn't in most recent pair
                k = 1
                for y in SentenceStartPosList:
                    K = len(SentenceStartPosList)
                    if SentenceStartPosList[K-k] not in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1):
                        delimstart = SentenceStartPosList[K-k]
                    else:
                        delimstart = 0
                    k += 1
            else:
                delimstart = max(SentenceStartPos,SpliceStartPos)
            Morphemes.append(string[delimstart:i+1])
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
            else:
                #if it's on for this particular character, slice the string then turn off
                if pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "On"] == 1:
                    pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "On"] = 0
                    #slice the string and append to Morphemes
                    Morphemes.append(string[pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "Location"][-1]:i+1])
                    #add to both location lists
                    pairdelimiterpos[pairdelimiters[pairdelimiters.index(x)-1] + "Location"].append(i)
                    #NEW
                    #pairdelimiterpos["AllList"].append(i)
                else:
                    pairdelimiterpos[x + "Location"].append(i)
                #be smart about how to turn this on:
                if pairdelimiters.index(x)%2 == 0:
                    pairdelimiterpos[x + "On"] = 1
        if x in sentencedelimiters:
            #know the last .?! , (if any) then cut between first and last .?!
            #ignore pair delimiters
            if SentenceStartPos in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1) and len(pairdelimiterpos["AllList"])>=4:
                #find one that isn't in most recent pair
                k = 1
                for y in SentenceStartPosList:
                    K = len(SentenceStartPosList)
                    if SentenceStartPosList[K-k] not in range(int(pairdelimiterpos["AllList"][-2]),int(pairdelimiterpos["AllList"][-1])+1):
                        delimstart = SentenceStartPosList[K-k]
                    else:
                        delimstart = 0
                    k += 1
            else:
                delimstart = SentenceStartPos
            Morphemes.append(string[delimstart:i+1])
            #NEW
            #adding this line since words "stuck" next to punctuation get lost:
            #Morphemes.append(string[int(pairdelimiterpos["AllList"][-1]):i+1])
            
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
        MList = []
    #multiply matrices (row by row):
    #row
    i = 0
    #column
    j = 0
    row = []
    for i in range(0, len(LeftM)):
        #construct the row:
        #print("range(0,len(RightM[0])):",range(int(len(RightM[0]))))
        ''''''
        for j in range(0,len(RightM[0])):
            #construct AB[i][j]
            #do the sum of A[i][k]B[k][j] from k = 0 to #rows of A -1
            k = 0
            value = 0
            for k in range(0, len(LeftM[0])):
                value = value + int(LeftM[i][k])*int(RightM[k][j])
            #append value to the row:
            row.append(value)
            if j == len(RightM)-1:
                #append row to MList
                MList.append(row)
                #clear row
                row = []
        
    return MList

def UllmanSI(used_columns, cur_row, G, P, M):
    #checks if graph G has a subgraph G' isom to graph P
    #checks if graph G' has a subgraph H isom to graph G
    cur_row = 0
    #if cur_row == len (M):
        #P = M(MG)^transpose
        #M encoded as:
        # M = [[],[],[]]
        #Omega(M) <-> matrix
            #file omega to matrix as list (->)
            #MstringtoList(Stringify(Vision(Address(str(matrix.read()),matrix))))
        #need matrix multiplication
        
        #need matrix transpose
        
    
    
    

file = open('INP.txt', 'r')
#print("checking address return:", Address("don't", file))
#print("checking vision return:", Vision(Address("don't", file)))
#print("checking stringify return:", Stringify(Vision(Address("don't", file))))
#print("cheating by preprogramming stuff \n", Cheat("let's test this out. \"Shall we?\", she said."))
#print("let's test this out. \"Shall we?\", she said.")
#file2 = open('Test Text.txt', 'r')
#file.seek(0)
#print("checking morphology return:", str(Cheat(file.read())))
OUTPUTFILE = open('OUT.txt','a')
#OUTPUTFILE.write(str(Cheat(file.read())))
#OUTPUTFILE.write("==================== /n")
readable2(Cheat(str(file.read())),OUTPUTFILE)
OUTPUTFILE.close()
file.close()
'''
file2 = open('INP2.txt', 'r')
file3 = open('OUTPUT.txt', 'a')
MORPH = Cheat(file2.read())
#file3.write(str(MORPH) + " \n")

J = 0
file3.write(str(Address(str(MORPH[J]),file2)[0]))
for x in MORPH:
    test =str(MORPH[J]) 
    #file3.write("test START \n" + test + "\n" + "test END \n")
    #file3.write(str(Address(test,file2)) + "\n")
    file3.write("['" + str(Address(test,file2)[1]) + "', '" + str(Address(test,file2)[2]) + "']" + "\n")
    
    #file3.write(str(Address(test,file2)) + " \n")
    #file3.write(str(Address(x,file2)[2]) + " \n")
    #print("wtf life", x, Address(x,file2)[1],Address(x,file2)[2],str(Address(x,file2)[1])+str(Address(x,file2)[2]))
    #file3.write(str(Address(test,file2)[2])+ " \n")
    J+=1


#readable(file3)
    
file3.close()
'''
#print("testing out test text", Cheat(file2.read()))

#file.seek(0)
#print("address2check",Address2("don't", file.read(), ["2","3","4"]))
#print("address2check",Address2("don't", ["d","o","n","'","t","2","3","4"],["d","o","n","'","t","2","3","4","5","6"],["2","d","o","n","'","t","2","3","4","5","6"]))



#IDLE TIME:



#make persistent basis:
#check if mem.txt exists:
#if not create it


mem = open("memory.txt",'a')
#put in everything in there
mem.close()
'''
def Vision(Addresslist):
    #Addresslist = [basis,1,partialbinary]
 
 Vision(Addresslist)
'''

matrix = open('matrix check.txt', 'r')
cleanfile = open('test3.txt', 'a')
#cleanfile.write(str(Vision(Address(str(matrix.read()), matrix.read()))))

#print("vision is ",Vision(Address(str(matrix.read()),matrix.read())))
#Stringify
OGstring = Stringify(Vision(Address(str(matrix.read()),matrix)))

#OGSTRING2 = matrix.read().splitlines().split(',')
print(OGstring)
print("lastchar is ", OGstring[-1])
#print("check1", OGstring[2]==" ")
#print("check2", OGstring[9]=="\n")
print(MstringtoList(OGstring))
print(MstringtoList(OGstring)[2][0])
#print(kys(OGstring[1:-1]))
#print(kys(OGstring[1:-1])[0][1:-1])
#print(kys(OGstring[1:-1])[0][1:-1].strip("\"").strip("'").split(","))
#.replace() makes a copy!
#print(kys(OGstring[1:-1])[0][1:-1].replace(',', ""))
#print(OGSTRING2[1][3])
print("kys3",MlistMult(MstringtoList(OGstring), MstringtoList(OGstring)))
matrix.close()


#ListTEST = []
#ListTEST.append(["1", "2", "3"])
#ListTEST.append(["5", "6", "7"])
#ListTEST.append(["3", "4", "5"])
#print("ListTEST is ", ListTEST)

print("end")
