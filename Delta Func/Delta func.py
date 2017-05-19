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

def Eps(str1,str2):
    '''
    checks if str1 is in str2
    returns -1 means str1 not in str2
    '''
    try:
        str2.index(str1)
    except Exception:
        return -1
    return str2.index(str1)

def deltamin1(j,str1,str2):
    '''
    minor func in delta
    takes dummy var and 2 strings and figures out longest contiguous [on both sides] mapping from str1 to str2 starting from str1[j]
    '''
    #k is the index on str2
    k = j
    mapping = []
    #print("CANCERSTART")
    #print("CANCER",j,k, str1,str2)
    while -1 < Eps(str1[j],str2[k:]):
        #print("CANCERG",str1[j],str2[k:])
        #print("CANCERD",j,k,Eps(str1[j],str2[k:]))
        #before you append check str2 is contiguous:
        if len(mapping)>0:
            #print(str1,str2)
            #print("CANCERIFFFUUUUUUCCCKKK",[j,k+Eps(str1[j],str2[k:])],mapping, mapping[-1][1]== k+Eps(str1[j],str2[k:])-1)
            #check if it's contiguous on both sides
            if mapping[-1][1] == k+Eps(str1[j],str2[k:])-1:
                mapping.append([j,k+Eps(str1[j],str2[k:])])
            else:
                #if it's not contiguous we are done, so just return mapping
                return mapping
        else:
            #init mapping
            mapping.append([j,k+Eps(str1[j],str2[k:])])
        if j == len(str1)-1:
            break
        else:
            k = k+Eps(str1[j],str2[k:])+1
            j += 1
    #need to check if map doesn't fail:
    #fail = if there is a better map on the other side: then set mapping to 0:
    #1: make list of competing maps:
    #2: check if each map fails too:
    #if competing maps is nonempty, return null map
    #else: return original mapping
    #print("CANCEREND=====",mapping)
            #NEWPLAN: FIX THIS AND deltamin2 to extend then keep testing
    return mapping

def deltamin2(Delta,FirstHS,SecondHS,Firstinit,Secondinit,separator):
    '''
    keep in mind this is LHS empty
    idea:
    replace
    DELTA>Delta
    LHS>FirstHS
    RHS>SecondHS
    Linit>Firstinit
    Rinit>Secondinit
    need a way to set Linit,Rinit, and DELTA from this function
    '''
    NEWLIST = []
    Delta.append(separator)
    #plan: check if the next LtoR is also not in RHS then we append the ---- at the end of that
    #print(FirstHS,SecondHS)
    #print("Firstunique",FirstHS[Firstinit])
    #print("what are we doing,",FirstHS[Firstinit],FirstHS[Firstinit:])
    Uniquelength = 0
    #if we're not already at the end:
    keep = 1
    while Firstinit < len(FirstHS)-1 and keep == 1:
        #keep going until LtoR2 is nonempty or we hit end of string
        #print("firstinit was:", FirstHS[Firstinit+1:],SecondHS[Secondinit:])
        FirsttoSecond2 = deltamin1(0,FirstHS[Firstinit+1:],SecondHS[Secondinit:])
        ##print("check qualifier THIS IS START",FirstHS[Firstinit+1:], SecondHS[Secondinit:], len(FirsttoSecond2) > 0, FirsttoSecond2)
        ##print("1>2", FirsttoSecond2)
        if len(FirsttoSecond2) == 0:
            #then next element in LHS is also unique:
            Uniquelength += 1
            Firstinit += 1
        elif len(FirsttoSecond2) > 0:
            #print("this should turn on too",)
            #init check
            check = []
            #even if FirsttoSecond2 is nonempty, the map can still fail:
            #enum on other side:
            for x in range(Secondinit,FirsttoSecond2[-1][1]):
                #print("wtf is FirsttoSecond2???", FirsttoSecond2,FirstHS[Firstinit+1:],SecondHS[Secondinit:])
                #print("for loop", FirstHS[Firstinit+1:],":",x,SecondHS[x+Secondinit:],FirstHS[Firstinit+1:])
                candidate = deltamin1(0,SecondHS[x+Secondinit:],FirstHS[Firstinit:])
                if len(candidate) > 0:
                    #print(candidate)
                    #check if candidate works (aka no cross map)
                    #can optimize here f u c k
                    #add = 1 means we add candidate
                    add = 1
                    for y in range(Firstinit+1,Secondinit+candidate[0][1]-1):
                        #for candidate to fail we want size deltamin1(0,FirstHS[y:],SecondHS[candidate[-1][1]:]) > size candidate
                        if len(deltamin1(0,FirstHS[y:],SecondHS[candidate[-1][1]-1:])) > len(candidate):
                            add = 0
                    if add == 1:
                        #print("CANCER",len(candidate)> len(FirsttoSecond2),candidate,"VS",FirsttoSecond2)
                        if len(candidate)> len(FirsttoSecond2):
                            #then we finally add to check list:
                            check.append(candidate)
            #print("holy shit what are candidates:", check, "current:", FirstHS[Firstinit])
            #check != 0 means our initial pick was best so just increment uniquelength and call it a day, otherwise do nothing
            #print("WHAT DID I FIGURE OUT THIS PASS?", FirstHS[Firstinit], len(check) == 0 ,"I stopped at:", FirstHS[Firstinit+1],"wtf is check",check )
            if len(check) == 0:
                #print("I stopped at:", FirstHS[Firstinit+1],Uniquelength)
                for x in range(0,Uniquelength+1):
                    #print("wtf is,",Firstinit-Uniquelength+x,FirstHS[Firstinit-Uniquelength+x])
                    Delta.append(FirstHS[Firstinit-Uniquelength+x])
                keep = 0
                Firstinit += 1
            else:
                Uniquelength += 1
                Firstinit += 1
                #print("*****************8newstats:",FirstHS[Firstinit:])
            '''
            if len(check)== 0:
                print("===============stop point?", FirstHS[Firstinit:])
            '''    
            #print("MASAYUME CHASING", Uniquelength, Firstinit)
            #TODO:
            '''
            basically check if the next elements in line fail their tests
            fail tests = append
            don't fail test = append them and then update init values accordingly
            >what is test?
            if deltamin3 is empty or not ???
            '''
        '''
        if Uniquelength>0:
            print("wtf is uniquelength ", Uniquelength)
            for x in range(0,Uniquelength+1):
                print("wtf is,",Firstinit-Uniquelength+x,FirstHS[Firstinit-Uniquelength+x])
                Delta.append(FirstHS[Firstinit-Uniquelength+x])
            keep = 0
        '''
        #Firstinit += Uniquelength+1
    Delta.append(separator)
    Delta.append("\n")
    NEWLIST.append([Firstinit,Secondinit,Delta])
    #print("wtf is NEWLIST????????????",NEWLIST)
    return NEWLIST

def deltamin3(Delta,FirstHS,SecondHS,Firstinit,Secondinit,FirsttoSecond,SecondtoFirst, separator, separator2):
    NEWLIST = []
    '''
    Is there a case when this does not terminate???:: probably not on finite strings
    check if the "middle" has a bigger contiguous mapping
    yes:
         Use that instead [aka pass?], but then check that one for a bigger contiguous mapping
              yes: use original
            no: use that one instead
    no:
         then continue
    LtoR[-1][1]

    replacement:
    LHS>FirstHS
    RHS
    Linit>Firstinit
    Rinit
    LtoR>FirsttoSecond
    RtoL
    '''
    check = []
    for k in range(FirsttoSecond[0][0],FirsttoSecond[-1][1]):
        '''
        you can optimize this by ignoring some k if some checkcandidates of check are continuous [but maybe a continuous mapping does not mean it is "final"]
        '''
        '''
        TODO:
        at this point before adding to check might as well check if each candidate is OK to append.
        then at the end of this in one nesting above get the first element of checkcandidate and append properly to DELTA
        '''
        checkcandidate = deltamin1(k,SecondHS,FirstHS)
        if len(checkcandidate) > len(FirsttoSecond):
            #if check is empty, init
            if len(check) == 0:
                check.append(checkcandidate)
            else:
                #if new candidate is bigger, get it
                for x in check:
                    if len(checkcandidate) > len(x):
                        check = InsertAt(check,checkcandidate,check.index(x))
                        check = checkcandidate
                    #if not, then order by distance from start:
                    if len(checkcandidate) == len(x):
                        if checkcandidate [0][0]> x[0][0]:
                            check = InsertAt(check,checkcandidate,check.index(x))
                        else:
                            check = InsertAt(check,checkcandidate,check.index(x)+1)
    ##F U C K If current check fails I have to check all the other elements in check if they don't fail
    if len(check) != 0:
        Delta.append(separator2)
        #append FirsttoSecond as only on First's side
        for x in FirsttoSecond:
            Delta.append(FirstHS[x[0]+Firstinit])
        Delta.append(separator2)
        Delta.append("\n")
        Firstinit += len(FirsttoSecond)
    else:
        #pick RHS and keep going:
        #if you pick RHS, that means append LHS first then RHS mapping, 
        #make sure to start i on the right side if you pick right or LHS if you pick left
        if FirsttoSecond[0][0] != FirsttoSecond[0][1]:
            Delta.append(separator)
            for y in range(FirsttoSecond[0][0],FirsttoSecond[0][1]):
                Delta.append(SecondHS[y+Secondinit])
            Delta.append(separator)
            Delta.append("\n")
        for x in FirsttoSecond:
            Delta.append(FirstHS[x[0]+Firstinit])
        Delta.append("\n")
        Firstinit += FirsttoSecond[-1][0]+1
        Secondinit += FirsttoSecond[-1][1]+1
    NEWLIST = [Firstinit,Secondinit,Delta]
    return NEWLIST

def shittydelta(LHS,RHS):
    '''
    takes two stringsand produces output
    --- means x in LHS and not in RHS
    +++ means x in RHS and not in LHS
    '''
    DELTA = []
    '''
    get the 1st char in LHS and map to RHS then slice everything before the map
    get the 1st char in RHS and map to LHS then slice everything before the map
    continue until one side fails first
    then pick the side that 'kept going'
    '''
    #pairs of matching indices from LHS to RHS
    LtoR = []
    #pairs of matching indices from RHS to LHS
    RtoL = []
    if len(LHS) < len(RHS):
        smaller = len(LHS)
    elif len(LHS) > len(RHS):
        smaller = len(RHS)
    else:
        smaller = len(RHS)
    i = 0
    while i < smaller - 1:
        print(i,smaller)
        LtoR = deltamin1(i,LHS,RHS)
        RtoL = deltamin1(i,RHS,LHS)
        #check the sizes of LtoR and RtoL
        '''
        check:
        size 0 means either +++ or ---
        then check for LtoR > RtoL
        '''
        
        if len(LtoR) == 0:
            DELTA.append("----")
            DELTA.append(LHS[i])
            DELTA.append("----")
            i+= 1
        if len(RtoL) == 0:
            DELTA.append("++++")
            DELTA.append(RHS[i])
            DELTA.append("++++")
            i+= 1
        #print(LtoR)
        #print(RtoL)
        if len(LtoR) > len(RtoL):
            #pick LHS and keep going:
            extra = []
            for x in LtoR:
                DELTA.append(LHS[x[0]])
                extra.append(RHS[x[0]])
            DELTA.append("++++")
            for x in extra:
                DELTA.append(x)
            DELTA.append("++++")
            i += len(LtoR)
        if len(RtoL) > len(LtoR):
            #pick RHS and keep going:
            extra = []
            for x in RtoL:
                DELTA.append(RHS[x[0]])
                extra.append(LHS[x[0]])
            DELTA.append("----")
            for x in extra:
                DELTA.append(x)
            DELTA.append("----")
            i += len(RtoL)
        #R I P switch func
        if len(RtoL) == len(LtoR):
            for x in RtoL:
                DELTA.append(RHS[x[0]])
            i += len(RtoL)
    return ''.join(str(e) for e in DELTA)

def delta(LHS,RHS):
    '''
    takes two stringsand produces output
    --- means x in LHS and not in RHS
    +++ means x in RHS and not in LHS
    '''
    DELTA = []
    '''
    get the 1st char in LHS and map to RHS then slice everything before the map
    get the 1st char in RHS and map to LHS then slice everything before the map
    continue until one side fails first
    then pick the side that 'kept going'
    '''
    #pairs of matching indices from LHS to RHS
    LtoR = []
    #pairs of matching indices from RHS to LHS
    RtoL = []
    if len(LHS) < len(RHS):
        smaller = len(LHS)
    elif len(LHS) > len(RHS):
        smaller = len(RHS)
    else:
        smaller = len(RHS)
    Linit = 0
    Rinit = 0
    print(LHS,RHS)
    while Linit < len(LHS) and Rinit < len(RHS):
        print("what pass? =====", Linit, Rinit)
        print("strings", LHS[Linit:],RHS[Rinit:])
        LtoR = deltamin1(0,LHS[Linit:],RHS[Rinit:])
        RtoL = deltamin1(0,RHS[Rinit:],LHS[Linit:])
        print("what the actual fuck", LtoR,RtoL)
        '''
        problem:
        L>R&R>L same size,what do
        '''
        '''
        check:
        size 0 means either +++ or ---
        then check for LtoR > RtoL
        '''
        #print("fuck zero answers",len(LtoR) > len(RtoL),LtoR,RtoL)

        if len(LtoR) > len(RtoL):
            plswork = deltamin3(DELTA,LHS,RHS,Linit,Rinit,LtoR,RtoL,"++++", "----")
            Linit = plswork[0]
            Rinit = plswork[1]
            DELTA = plswork[2]
            print("DELTA1",DELTA)
        elif len(RtoL) > len(LtoR):
            plswork = deltamin3(DELTA,RHS,LHS,Rinit,Linit,RtoL,LtoR,"----", "++++")
            Rinit = plswork[0]
            Linit = plswork[1]
            DELTA = plswork[2]
            print("DELTA2",DELTA)
        elif len(LtoR) == 0:
            runonce = deltamin2(DELTA,LHS,RHS,Linit,Rinit,"----")
            Linit = runonce[0][0]
            Rinit = runonce[0][1]
            DELTA = runonce[0][2]
            print("DELTA3",DELTA)
        elif len(RtoL) == 0:
            runonce = deltamin2(DELTA,RHS,LHS,Rinit,Linit,"++++")
            Rinit = runonce[0][0]
            Linit = runonce[0][1]
            DELTA = runonce[0][2]
            print("DELTA4",DELTA)
        #print("what pass END?", Linit, Rinit, LtoR,RtoL)
        #same
        elif LtoR == RtoL:
            for x in range(0,len(LtoR)):
                DELTA.append(LHS[x])
            DELTA.append("\n")
            Linit += len(LtoR)
            Rinit += len(LtoR)
            print("DELTA4F",DELTA)
    if Linit < len(LHS):
        print("wtf left",Linit,Rinit)
        DELTA.append("----")
        for x in LHS[Linit:]:
            DELTA.append(x)
        DELTA.append("----")
        DELTA.append("\n")
    if Rinit < len(RHS):
        print("wtf right",Linit,Rinit)
        DELTA.append("++++")
        for x in RHS[Rinit:]:
            DELTA.append(x)
        DELTA.append("++++")
        DELTA.append("\n")
    print(LHS,RHS)
    return ''.join(str(e) for e in DELTA)







#need example where right goes to left:
#print(delta("ZCDEFGHAB","ABCDEFGH"))
#print(delta("ABCDEFGH","ZCDEFGHAB"))
##print(delta("baade", "cdeaf"))#<------------ F U C K E D
#OK! print(delta("baade","zaacdeaf"))
##print(delta("baade","zaacdeaf"))

#OK! print(delta("aade", "deaf"))
##print(delta("aade", "deaf"))
#OK! print(delta("deaf", "aade"))
##print(delta("deaf", "aade"))
#OK! print(delta("AGG","GGA"))
##print(delta("AGG","GGA"))
#uh oh print(delta("GGA","AGG"))
##print(delta("GGA","AGG"))

#uh oh print(delta("aa", "aba"))
#print(delta("aa", "aba"))#<------------ F U C K E D

#example where RHS gets picked
#OK! print(delta("aadeafgh","deaf"))
#print(delta("aadeafgh","deaf"))
#example where RHS gets picked but is not long enough
#uh oh print(delta("154zyxgb","gb123zyx"))#<------------ F U C K E D
#print(delta("154zyxgb","gb123zyx"))
f = open("MACHINE TASKLIST.tdl", "r+", encoding="utf-16")
g = open("othercomp.tdl", "r+")
h = open("OUT.txt", "w+")
#delta(f.read(),g.read())
h.write(f.read())
h.close()
