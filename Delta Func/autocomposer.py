from math import *

'''
TODO:
finish this then update casual with fixed cheat and all these dumb functions
then plow through the paperslist and respond to real life
'''

def fixedeval(theinput):
    #takes a string and preps 'naked' alphanumeric chars as strings:
    fixed = theinput
    #if there's nothing to do return the string:
    if pairfinder(theinput,["[","]"])[1] == 0:
        return theinput
    i = 0
    print(fixed,i)
    for x in fixed:
    #for i in range(0,len(fixed)):
        #x = fixed[i]
        #if it's not a number, assume character:
        g = i
        maxlength = 0
        #print(maxlength)
        y = fixed[g+1]
        #if g+1 < len(fixed):
        #    y = fixed[g+1]
        '''

        '''
        #print("y",y)
        if str(x) != "\"" and str(x) != "[" and str(x) != "]" and str(x) != ",":
            #1: figure out the length of alphas:
            while str(y) != "\"" and str(y) != "[" and str(y) != "]" and str(y) != ",":
                maxlength += 1
                if g+1 < len(fixed):
                    y = fixed[g+1]
                g += 1
            try:
                int(x)
            except(NameError,ValueError):
                if maxlength > 0:
                    FASTLANE = fixed[i:i+maxlength]
                    TAKEITSLOW = fixed[i+maxlength:]
                else:
                    FASTLANE = FASTLANE = fixed[i]
                    TAKEITSLOW = fixed[i+maxlength+1:]
                fixed = fixed[:i] + "\"" + FASTLANE + "\"" + TAKEITSLOW
                if maxlength > 0:
                    i += 2 + maxlength
                else:
                    i += 2
            try:
                y = fixed[i+2]
            except(IndexError):
                return eval(fixed)
        i += 1
        try:
            fixed[i]
        except(IndexError):
            return eval(fixed)
    return eval(fixed)

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
    problem: what is the int "mean"?
    facts:
    int that is supposed to map to something:
    Lval to tell us how autistic to go
    choice: what mapping?
    have to use cantor pairing so that :
    idea:
    bin(int)  == "{0:b}".format(x).zfill(4)[::-1] so it goes left to right and smallest exp to largest
    find the 1's then iterate down:

    example:
    L == 1
    110100111
    #1: what is the basis?
    NxN with cantor address:
    idea:
    123456789,10...... are pairs
    so:
    1,2,4,7,8,9 are in there
    1 == 1,0
    2 == 0,1
    4 == 1,1
    7 == 2,1
    8 == 1,2
    9 == 0,3

========
    L == 2
    110100111
    idea:
    123456789,10 are elements of P(NxN)
    what are they?????
    you can always take an initial portion:
    idea:
    from L == 1:
     123456789,10...... are pairs
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    .
    .
    .
    so then::
    the vertical is the way to go
    then elements are...
    		 123456789,10...... are pairs
1		1
1		2
0		3
1		4
0		5
0		6
1		7
1		8
1		9
		10
		.
		.
		.

    idea:
    #1: to binary
    #2: figure out L-val
    #3: for each one, construct the part recursively:
        go down 1 Lval



        
'''

    
        


def AutoVision(number,Lval):
    '''
    this is for 
    '''
    ANS = []
    binary = "{0:b}".format(number)[::-1]
    #print("number, binary", number, binary, Lval)
    if Lval == 1:
        z = number
        w = floor((sqrt(8*z+1)-1)/2)
        t = (w*w+w)/2
        y = z - t
        x = w - y
        #print("number, append", number, [x,y])
        ANS.append([x,y])
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
    return ANS

#print(AutoVision(128,2))
#print(AutoVision(1,2))#GOTEM
#print(AutoVision(78,2))
#note: 0,2 fails, 0,y fails for y>1
#note: remove extra brackets
'''
need an example:


NOTE: ISN"T THIS IT????? WE DON't NEED TO KEEP CANTOR PAIRING TO GET PAST L-VALS
'''

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
            #print("x,y", x,y)
            #print(x,"wtf",y)
            #print(y[0])
            #print(x[1])
            yfail = 0
            xfail = 0
            try:
                y[0]
            except(ValueError,IndexError):
                #print("y failed")
                yfail = 1
            try:
                x[1]
            except(ValueError,IndexError):
                #print("x failed")
                xfail = 1
            '''
            HINT:
            use the try: except block hax
            
            '''
            if xfail == 0 and yfail == 0:
                if y[0] == x[1]:
                    ANS.append([x[0],y[1]])
    return ANS

#print(gcomposition(AutoVision(1,1),AutoVision(2,2)))
file = open('Auto.txt', 'r+')

final = 5
for top in range(0,final):
    for x in range(0,top+1):
        for y in range(0,top+1):
            #print(x,y,top)
            #print("input first:" ,AutoVision(x,top),AutoVision(y,top))
            
            file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
    
###this has a problem with objects that aren't in there:: "IndexError: list index out of range"
file.close()

'''
working on:
address:
idea:
facts:
have string
want: address which is a specific number when assigned a basis:
need a basis:



have:
string to address
basis
pairing chars

job #1: figure out L-vals
idea: I think I build the address from the "bottom up" right?
function
    if l-val not 1
    call itself with lval-1
    then append to ans



example:
string = test

#1: check basis (all the way down to the "bottom")
#2: go down levels until you can do L=1:
#3: how to put it all together?


F U C K there is like a compression theorem here somewhere
thm ==  everything can be set to L value of 1???

>so wtf if you add the pair chars like everything is expressible as long as you have a long enough (enough integers) basis and have the right chars
picture:
limited/small basis: [ALPHA OPTION]
requres a few powersets to get to an object

huge basis + special chars: [BETA OPTION]
can express a lot of shit and is a "wider" catch
also reduces the distances to theorems significantly


new question: even if you can express it, can you evaluate it properly?
[ALPHA:]
yes
[BETA:]
no, too "limited" in a sense if I only use gcomposition

example:
L == 2
[[[],[]],[]] <-- I can get this from the cheat() function
string>list
for each element in list(string):
    if every element is in basis:
        assign a number then return answer
    else:
        call this function again with one less l-val on each element of element in list





for each element in list(string):
    if we can't go down "further"
    if element[0] fails:
        address the objects here
    else:
        call this function again and address with one less lval
         


goal: string + basis > output a unique integer
problem: when string in higher powersets of the basis:
example:
basis = c,a,t
BUT I have
"cat"
    

'''

#insert into a list at the right index
def InsertAt (List,obj,Index):
    '''
    Inserts obj at List[Index] and appends the rest of list after it
    '''
    VALUE = List[:Index]
    VALUE.append(obj)
    for x in range(0,len(List[Index:])):
        VALUE.append(List[Index + x])
    return VALUE




'''
FUCK THIS MIGHT BE WRONG BECAUSE IT DOESN"T GIVE METATHEOREMS????
MIGHT NEED ANOTHER FUNC FOR THAT
'''

def Addresspls(info):
    #info = [string,basis,pairchars,Lval,maxLval]

    '''
    TODO
    when do I check for fucked up basis
    return the right amount for LVAL
    '''


    
    ANS = []
    Interim = []
    #IT"S TIME TO STOP
    '''
    if info[3] < 0:
        print("IT'S TIME TO STOP")
    '''

    
    for x in fixedeval(info[0]):
        #print(x)
        #print("wtf is failure anymore",pairfinder(str(x),info[2])[1])
        if pairfinder(str(x),info[2])[1] == 0:
            try:
                Interim.append(info[1].index(x))
            except(ValueError):
                print("when do I check for fucked up basis")
                Addresspls([x,info[1],info[2],info[3],info[4]])
        else:
            Addresspls([x,info[1],info[2],info[3],info[4]])
            
    longest = 0
    for x in Interim:
        if x > longest:
            longest = x
    #init binary:

    ANS="1".zfill(int(longest)+1)
    Interim = list(filter(lambda x: x != longest, Interim))
    for x in Interim:
        ANS = ANS[:x] + "1" + ANS[x+1:]
    ANS = int(ANS, 2)
    return ANS

#note: this has no cantor pairings
def AddressCANCER(info):
    print("==========================WHEN DO I START", info[0])
    #info = [string,basis,pairchars,Lval,maxLval]
    #NOTE: WE ARE GIVEN LVAL
    ANS = []
    maxLval = info[4]
    Interim = []

    #does this have pairs:
    pairs = pairfinder(info[0],info[2])[1]
    if pairs > 0:
        # go up or down
        up = 0
        maxL = 0
        for I in range(0,len(fixedeval(info[0]))-1):
            #print("check the pairs and the equals")
            #print(str(fixedeval(info[0])[I]))
            #print(pairfinder(str(fixedeval(info[0])[I]),info[2])[1])
            #print(str(fixedeval(info[0])[I+1]))
            #print(pairfinder(str(fixedeval(info[0])[I+1]),info[2])[1])
            #print(pairfinder(str(fixedeval(info[0])[I]),info[2])[1] != pairfinder(str(fixedeval(info[0])[I+1]),info[2])[1])
            if pairfinder(str(fixedeval(info[0])[I]),info[2])[1] != pairfinder(str(fixedeval(info[0])[I+1]),info[2])[1]:
                up = 1
                maxLval += 1
        #print("gg", eval(info[0])) #IF I TAKE THE EVAL ROUTE I NEED TO ADD ' or " TO THE STRING WHICH FUCKING SUCKS
        #tlist = pairfinderSTRING(pairfinder(info[0],info[2]),info[0])
        tlist = fixedeval(info[0])
        #print("DOING WAY TOO MUCH FOR ONE FUNCTION", tlist, "MAX IS", len(tlist))
        #print("pairfinder pls don't fuck up", tlist[0],tlist[1],tlist[2],tlist[3])
        
        for x in fixedeval(info[0]):
            print(x)
            print("Lval is", pairfinder(str(x),info[2])[1])
            if pairfinder(str(x),info[2])[1] == 0:
                #check if it's in basis:
                basisyes = 1
                for y in list(str(x)):
                    print("what is y?", y)
                    try:
                        info[1].index(y)
                    except(ValueError,IndexError):
                        basisyes = 0
                        print("THE CULPRIT IS",y)
                    if basisyes == 1:
                        print("appending this", info[1].index(y))
                        Interim.append(info[1].index(y))
            else:
                print("too big", x)
                print(Addresspls([x,info[1],info[2],pairfinder(str(x),info[2])[1],info[4]]))
                print("what are results?")
        print("stats", fixedeval(info[0]),len(fixedeval(info[0])))    
        print("Interim is??????????????????????", Interim)    
        
        #findmaxlength:
        longest = 0
        for x in Interim:
            if x > longest:
                longest = x
        #init binary:
    
        ANS="1".zfill(int(longest)+1)
        Interim = list(filter(lambda x: x != longest, Interim))
        for x in Interim:
            ANS = ANS[:x] + "1" + ANS[x+1:]
        ANS = int(ANS, 2)
        return ANS

    else:
        #assume Lval = 1:
        
        #check if every element is in basis:
        basisyes = 1
        for x in list(info[0]):
            try:
                info[1].index(x)
            except(ValueError,IndexError):
                basisyes = 0
            if basisyes == 1:
                Interim.append(info[1].index(x))


    #print("This function is doing like way too much shit, interim")#, info[0]
    #print(Interim)
    
    # if we're at pairs, then for each elem:
        #if local lval == 1:
            #check if it's in basis:
                #yes: return #
                #no: print missing char and what it is
        #if lval != 1:
            #call this again with a smaller lval
    #### somewhere in here we need a function that turns a list of ints into a binary



    #findmaxlength:
    longest = 0
    for x in Interim:
        if x > longest:
            longest = x
    #init binary:
    
    ANS="1".zfill(int(longest)+1)
    Interim = list(filter(lambda x: x != longest, Interim))
    for x in Interim:
        ANS = ANS[:x] + "1" + ANS[x+1:]
    ANS = int(ANS, 2)
    return ANS
    







def Addresspieces(stuff):


    ##print("checking Lval", info[3])
    if info[3] == info[4]:
        #check if every element is in basis:
        basisyes = 1
        for x in list(info[0]):
            try:
                info[1].index(x)
            except(ValueError,IndexError):
                print("this is fucking it up","\n", x,"\n", info[0])
                basisyes = 0
                
    #now we try to assign values
    #interim tells you which parts of a binary number is 1

    Interim = []
    print("need right amount of 0's")
    '''
    trick: converting string of numbers into 'binary'"
    idea:
    turn string into list
    for x in list:
        if ????

    problem:
    L = 2
    [t, [[]]]
    where is t in L = 2????

    the object is :
    [[t]]
    know:
    t is in basis
    but for L = 2 there is some kind of fuckery with the pairings
    theorem:
    L = n, then each object SHOULD have n pairings of brackets
    new question
    [t, [[]]] == [[t], [[]]]

    '''
    

    
    ##print("stats", list(info[0]))
    for x in list(info[0]):
        if basisyes == 1:
            #assign a number then return answer
            #assign a number:
            #print(info[1].index(x))
            Interim.append(info[1].index(x))
        else:
            #fucking stop this
            if int(info[3]) < 1:
                print("stats3", info)
                print("it's time to STOP")
                return
            print("morestats", info, x, [x,info[1],info[2],info[3]-1])
            #call this function again with one less l-val on each element of element in list
            Addresspls([x,info[1],info[2],info[3]-1])
    #change interim into actual binary:
    #findmaxlength:
    longest = 0
    for x in Interim:
        if x > longest:
            longest = x
    #init binary:
    
    ANS="1".zfill(int(longest)+1)
    Interim = list(filter(lambda x: x != longest, Interim))
    for x in Interim:
        ANS = ANS[:x] + "1" + ANS[x+1:]
    ANS = int(ANS, 2)
    return ANS

def AddressplsAME(info):
    #info = [string,basis,pairchars,Lval]
    #NOTE: WE ARE GIVEN LVAL
    ANS = []
    
    ##print("checking Lval", info[3])
    #check if every element is in basis:
    basisyes = 1
    for x in list(info[0]):
        try:
            info[1].index(x)
        except(ValueError,IndexError):
            print("this is fucking it up","\n", x,"\n", info[0])
            basisyes = 0
    #now we try to assign values
    #interim tells you which parts of a binary number is 1

    if info[3] == 1 and basisyes == 0:
        print("missing chars in basis")
        return

    Interim = []
    ##print("stats", list(info[0]))
    for x in list(info[0]):
        if basisyes == 1:
            #assign a number then return answer
            #assign a number:
            #print(info[1].index(x))
            Interim.append(info[1].index(x))
        else:
            #fucking stop this
            if int(info[3]) < 1:
                print("stats3", info)
                print("it's time to STOP")
                return
            print("morestats", info, x, [x,info[1],info[2],info[3]-1])
            #call this function again with one less l-val on each element of element in list
            Addresspls([x,info[1],info[2],info[3]-1])
    #change interim into actual binary:
    #findmaxlength:
    longest = 0
    for x in Interim:
        if x > longest:
            longest = x
    #init binary:
    
    ANS="1".zfill(int(longest)+1)
    Interim = list(filter(lambda x: x != longest, Interim))
    for x in Interim:
        ANS = ANS[:x] + "1" + ANS[x+1:]
    ANS = int(ANS, 2)
    return ANS

'''
problem: I need to know what kind of string to give addresspls AND how to start at the bottom then make the right number
'''

def Addressplsffff(info):
    #info = [string,basis,pairchars,Lval]
    #NOTE: WE ARE GIVEN LVAL
    ANS = []
    #check if every element is in basis:
    basisyes = 1
    for x in list(info[0]):
        try:
            info[1].index(x)
        except(ValueError,IndexError):
            basisyes = 0
    #now we try to assign values
    #interim tells you which parts of a binary number is 1

    if info[3] == 1 and basisyes == 0:
        print("missing chars in basis")
        return

    Interim = []
    for x in list(info[0]):
        if basisyes == 1 and info[3] == 1:
            #assign a number then return answer
            #assign a number:
            Interim.append(info[1].index(x))
        else:
            #call this function again with one less l-val on each element of element in list
            Addresspls([x,info[1],info[2],info[3]-1])
    #change interim into actual binary:
    #findmaxlength:
    longest = 0
    for x in Interim:
        if x > longest:
            longest = x
    #init binary:
    
    ANS="1".zfill(int(longest)+1)
    Interim = list(filter(lambda x: x != longest, Interim))
    for x in Interim:
        ANS = ANS[:x] + "1" + ANS[x+1:]
    ANS = int(ANS, 2)
    return ANS


#now to modify AutoVision to work with an arbitrary basis:

def Vision(number,basis,Lval):
    '''
    this is for 
    '''
    ANS = ""
    binary = "{0:b}".format(number)[::-1]
    if Lval == 1:
        indexer = 0
        for x in binary:
            if x == "1":
                try:
                    basis[indexer]
                except(ValueError,IndexError):
                    print("FML")
            ANS = ANS + basis[indexer]
            indexer +=1
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
                ANS = ANS + Vision(i,basis,Lval-1)
            i += 1
    return ANS

#print("checking addresspls")
compress = Addresspls(["cat",["c","a","t"],["[","]"],pairfinder("cat",["[","]"])[1],pairfinder("cat",["[","]"])[1]])
print("A1","cat",compress)
print("checking A1", Vision(compress,["c","a","t"],1))
print("checking vision",AutoVision(compress,pairfinder("cat",["[","]"])[1]))
##print(Vision(compress,["c","a","t"],1))
print("try L >1 ")
#theinput = "[c,[t,[a],[t]],cat]"
theinput = "[[c],[[t],[a],[t]],[cat]]" #this is proper parens right
#theinput = ["c",["t",["a"],["t"]],"cat"]
print("what is the string to use for manual numbering?", theinput)
LL = Addresspls([theinput,["c","a","t","[","]",","," ","'"],["[","]"],pairfinder(theinput,["[","]"])[1],pairfinder(theinput,["[","]"])[1]])
'''
problem: addresspls gives a "dead" number in the sense that it is the same syntactically (the way it's written) but not semantically because compposing the number doesn't give the "right" values
'''
print("A2",theinput,LL)
print("check A2", Vision(LL,["c","a","t","[","]",","," ","'"],4))
##print("what does pairstrings say","\n", pairfinderSTRING(pairfinder(str(theinput),["[","]"]),str(theinput)),"\n",pairfinder(str(theinput),["[","]"]))
print("check vision arbitrary", Vision(3,["c","a","t","[","]",","," "],3))
print("check vision", Vision(LL,["c","a","t","[","]",","," "],3))
#print("checking if at each level you need to have same amt of pairs", AutoVision(550,10))
print("checking if at each level you need to have same amt of pairs", AutoVision(550,3))
print("I don't know how to check AutoVision", AutoVision(64,3))
##print("check cheat","\n",str(theinput),"\n", Cheat(str(theinput)),"\n",Cheat(str(theinput)),"\n",Cheat("Why [[What [the] fuck] it doesn't look like it works as intended.]"))
#problem: we need to be given an L-val first instead of figuring it out beforehand... :/
def AddressplsWRONG(info):
    #info = [string,basis,pairchars,Lval]
    ANS = []
    #1: figure out L-val if L-val is missing:
    try:
        info[3]
    except(ValueError,IndexError):
        info[3] = pairfinder(info[0])[1]
    if info[3] != 1:
        #1: you need to get the right string to input into nested addresspls:
        Addresspls([info[0],info[1],info[2],info[3]-1])
    return ANS


def omg(number):
    z = number
    w = floor((sqrt(8*z+1)-1)/2)
    t = (w*w+w)/2
    y = z - t
    x = w - y
    return [x,y]
    
print("why the fuck is autovision failing", omg(0))
