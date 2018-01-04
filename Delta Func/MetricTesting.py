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
            #print("stats", x, LHSCounter, y, RHSCounter)
            #::AM I SUPPOSED TO SCALE THIS
            if x == y:
                #get x pos for LHS start 
                lhscheckpos = LHSCounter
                #get y pos for RHS start 
                rhscheckpos = RHSCounter
                length = 0
                while LHS[lhscheckpos+length] == RHS[rhscheckpos+length]:
                    if len(LHS)-1 > lhscheckpos+length and len(RHS)-1 > rhscheckpos+length:
                        length += 1
                    else:
                        break
                #add candidate to Candidatelist
                #datareq: LHSstart RHSstart Length
                Candidatelist.append([lhscheckpos,rhscheckpos,length])
            LHSCounter += 1
        RHSCounter += 1
    #double check info
    print("CandidateList", Candidatelist)
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
    return ANS

def seqsplit(LHS,RHS):
    ANS = []
    #need ending strat
    #generic: apply maxlongestcontig on splits until it fails
    ##what to do with nil answer??
    LCont = maxlongestcontig(LHS,RHS,0,0)
    if len(LCont) == 3:
        print("LHS is",LHS)
        print("LHS",LHS[:LCont[0]], "+",LHS[LCont[0]:LCont[0]+LCont[2]+1], "+",LHS[LCont[0]+LCont[2]+1:])
        print("RHS is",RHS)
        print("RHS",RHS[:LCont[1]], "+",RHS[LCont[1]:LCont[1]+LCont[2]+1], "+",RHS[LCont[1]+LCont[2]+1:])
    #match like segments together (try: from left to right)
    Connections = []
    Connections.append([[LHS[:LCont[0]]],[RHS[:LCont[1]]]])
    Connections.append([[LHS[LCont[0]:LCont[0]+LCont[2]+1]],[RHS[LCont[1]:LCont[1]+LCont[2]+1]]])
    Connections.append([[LHS[LCont[0]+LCont[2]+1:]],[RHS[LCont[1]+LCont[2]+1:]]])

    #for each part in Connections, if NOT same parts OR either part is empty, reapply maxlongestcontig
    #then at the end stitch similar parts together
    print("checking Connections")
    print(Connections)
    i = 0
    for x in Connections:
        i += 1
        #need stopping point
        LContmin = maxlongestcontig(x[0],x[1],0,0)
        #DELETE CURRENT X
        #INSERT NEW X PARTS (NOTE: WE ALSO INSERT ENOUGHT EMPTY LISTS SO MAKING STATEMENT+REPLACE IS EASIER)
        #replace the current x with this:
        InsertAt(Connections, "?????", i)
        Connections.append([[LHS[:LCont[0]]],[RHS[:LCont[1]]]])
        Connections.append([[LHS[LCont[0]:LCont[0]+LCont[2]+1]],[RHS[LCont[1]:LCont[1]+LCont[2]+1]]])
        Connections.append([[LHS[LCont[0]+LCont[2]+1:]],[RHS[LCont[1]+LCont[2]+1:]]])
    return ANS


#print(maxlongestcontig(test2,test1,0,0))
#print(maxlongestcontig(test1,test2,0,0))
print(seqsplit(test1,test2))
print("===========================================")
print(seqsplit("ok","??thisisokother"))
