from autocomposer import *

test1 = "oktestingthis"
test2 = "??thisisokothertesting"
#test2 = "LAYon-theLINE"

def ladder(LHS,RHS):
    #compare max lengths of firstlongestcontig from A->B and B->A
    #TRICK: LHS AND RHS HAVE TO BE IN THE SAME ORDER, BUT I SWITCH IN firstlongestcontig
    Candidates = []
    print("A->B",firstlongestcontig(test1,test2,0,0,0))
    Candidates.append(firstlongestcontig(test1,test2,0,0,0))
    print("B->A",firstlongestcontig(test2,test1,0,0,1))
    Candidates.append(firstlongestcontig(test2,test1,0,0,1))
    CurrentPick = []
    #if all are 0, fail
    ####NEW IDEA: do maxlongestcontig repeatedly on split parts
    for x in Candidates:
        if len(CurrentPick) == 0 and len(x) != 0:
            CurrentPick = x
        elif CurrentPick[2] < x[2]:
            CurrentPick = x
    print("ok this is CurrentPick",CurrentPick)
    print("split LHS and RHS")
    
            
    return "no return for ladder"


def firstlongestcontig(LHS,RHS,LHSinit,RHSinit,antitoggle):
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
    print("BEWARE OF ANTITOGGLE!",ANS)
    return ANS

#print(firstlongestcontig(test2,test1,0,0))
#print(firstlongestcontig(test1,test2,0,0))
#print(ladder(test1,test2))



#idea: this function is just one direction, then outside the function I compare distances and do the ladder strategy


def maxlongestcontig(LHS,RHS,LHSinit,RHSinit):
    #hint: this is commutative
    print("LHS")
    print(LHS)
    print("RHS")
    print(RHS)
    Candidatelist = []
    ANS = []
    RHSCounter = RHSinit
    for y in RHS[RHSinit:]:
        LHSCounter = LHSinit
        for x in LHS[LHSinit:]:
            #::AM I SUPPOSED TO SCALE THIS
            if x == y:
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
    print(LHS)
    print(RHS)
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
        print("===================START")
        print("check ans",ANS)
        print("matching left (singletons will fuck up)",LHS,ANS[0],ANS[0]+ANS[2])
        print(LHS[ANS[0]:ANS[0]+ANS[2]])
        print("matching right (singletons will fuck up)",RHS,ANS[1],ANS[1]+ANS[2])
        print(RHS[ANS[1]:ANS[1]+ANS[2]])
        print("===================END")
    return ANS

def seqsplit(LHS,RHS):
    #need ending strat
    #generic: apply maxlongestcontig on splits until it fails
    ##what to do with nil answer??
    LCont = maxlongestcontig(LHS,RHS,0,0)
    print("match LCont",LCont)
    if len(LCont) == 3:
        print("LHS is",LHS)
        print("LHS",LHS[:LCont[0]], "+",LHS[LCont[0]:LCont[0]+LCont[2]], "+",LHS[LCont[0]+LCont[2]:])
        print("RHS is",RHS)
        print("RHS",RHS[:LCont[1]], "+",RHS[LCont[1]:LCont[1]+LCont[2]], "+",RHS[LCont[1]+LCont[2]:])
    #match like segments together (try: from left to right)
    Connections = []
    #Connections.append([[LHS[:LCont[0]]],[RHS[:LCont[1]]]])
    #Connections.append([[LHS[LCont[0]:LCont[0]+LCont[2]]],[RHS[LCont[1]:LCont[1]+LCont[2]]]])
    #Connections.append([[LHS[LCont[0]+LCont[2]:]],[RHS[LCont[1]+LCont[2]:]]])
    Connections = seqsplitmin(LHS,RHS,LCont,Connections, [-1, -1, -1])
    
    #for each part in Connections, if NOT same parts OR either part is empty, reapply maxlongestcontig
    #then at the end stitch similar parts together
    print("================checking Connections")
    print(Connections)
    i = 0
    for x in Connections:
        LContmin = maxlongestcontig(x[0][0],x[1][0],0,0)
        if x[0][0] == x[1][0] or len(x[0][0]) == 0 or len(x[1][0]) == 0: #or len(LContmin) == 0
            pass
            i += 1
        else:
            print("WTF BUCK",x,LContmin)
            print("DELETE CURRENT X",x)
            print(Connections[i])
            print("old Con", Connections)
            del Connections[i]
            print("new Con", Connections)
            
            #INSERT NEW X PARTS (NOTE: WE ALSO INSERT ENOUGHT EMPTY LISTS SO MAKING STATEMENT+REPLACE IS EASIER)
            #replace the current x with this:
            ##################LHS/RHS are diff, LCont is now LContmin##################
            #print("part 1",[[x[0][0][:LContmin[0]]],[x[1][0][:LContmin[1]]]])
            #print("part 2",[[x[0][0][LContmin[0]:LContmin[0]+LContmin[2]+1]],[x[1][0][LContmin[1]:LContmin[1]+LContmin[2]+1]]])
            #print("part 3",[[x[0][0][LContmin[0]+LContmin[2]+1:]],[x[1][0][LContmin[1]+LContmin[2]+1:]]])
            #Connections = InsertAt(Connections, [[x[0][0][:LContmin[0]]],[x[1][0][:LContmin[1]]]], i)
            #Connections = InsertAt(Connections, [[x[0][0][LContmin[0]:LContmin[0]+LContmin[2]]],[x[1][0][LContmin[1]:LContmin[1]+LContmin[2]]]], i+1)
            #Connections = InsertAt(Connections, [[x[0][0][LContmin[0]+LContmin[2]:]],[x[1][0][LContmin[1]+LContmin[2]:]]], i+2)
            Connections = seqsplitmin(x[0][0],x[1][0],LContmin,Connections,[i, i+1, i+2])
            print("new connections")
            print(Connections)
            i += 1
    #construct statement:
    ANS = []
    for x in Connections:
        if x[0] == x[1]:
            ANS.append(x)
        elif len(x[0][0])!= 0 and len(x[1][0])!= 0:
            ANS.append("Symbol")
    return ANS

def seqsplitmin(LHS,RHS,LCont,Connections,index):
    ###this is because I might as well make a generic now as well as try to optimize instead of wait for later
    #what this does is take LHS,RHS, and LCont and appends the right connections
    #if there is an empty connection, refuse to append
    #index is a list of indicies to add objects
    ANS = Connections
    #print("CHECKANS1",ANS)
    #if it's an empty connection, refuse
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
        #ANS.append([[LHS[LCont[0]+LCont[2]:]],[RHS[LCont[1]+LCont[2]:]]])
        #print("wtf is LCont?", LCont,LCont[0],LCont[1],LCont[2])
        #print("cancer",   [[LHS[LCont[0]+LCont[2]:]],[RHS[LCont[1]+LCont[2]:]]])
        #print("index2",index[2])
        ANS = InsertAt(ANS,[[LHS[LCont[0]+LCont[2]:]],[RHS[LCont[1]+LCont[2]:]]],index[2])

    print("CHECKANS4",ANS)
    return ANS
    


#print(maxlongestcontig(test2,test1,0,0))
#print(maxlongestcontig(test1,test2,0,0))
print(seqsplit(test1,test2))
####something is wrong with maxlongestcontig ???
####print(maxlongestcontig("ok","??thisisokother",0,0))
##print(seqsplit("print('alpha')","print('beta')"))
#print(maxlongestcontig("print(\"alpha\")","print(\"beta\")",0,0))
#print("===========================================")
#print(seqsplit("ok","??thisisokother"))
