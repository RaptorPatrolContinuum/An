

test1 = "oktestingthis"
test2 = "thisisokothertesting"


def ladder(LHS,RHS):
    #compare max lengths of firstlongestcontig from A->B and B->A
    print(firstlongestcontig(test1,test2,0,0))
    print(firstlongestcontig(test2,test1,0,0))
    return "no return yet"


def firstlongestcontig(LHS,RHS,LHSinit,RHSinit):
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
    print("===================START")
    print("check ans")
    print("matching left (singletons will fuck up)",LHS,ANS[0],ANS[0]+ANS[2])
    print(LHS[ANS[0]:ANS[0]+ANS[2]])
    print("matching right (singletons will fuck up)",RHS,ANS[1],ANS[1]+ANS[2])
    print(RHS[ANS[1]:ANS[1]+ANS[2]])
    print("===================END")
    return ANS

#print(firstlongestcontig(test2,test1,0,0))
#print(firstlongestcontig(test1,test2,0,0))
print(ladder(test1,test2))



#idea: this function is just one direction, then outside the function I compare distances and do the ladder strategy


def maxlongestcontig(LHS,RHS,LHSinit,RHSinit):
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
            print("stats", x, LHSCounter, y, RHSCounter)
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
        print("Candidate",i)
        print("NOTE: [:] format doesn't do singletons")
        print("matching left (singletons will fuck up)",LHS,i[0],i[0]+i[2])
        print(LHS[i[0]:i[0]+i[2]+1])
        print("matching right (singletons will fuck up)",RHS,i[1],i[1]+i[2])
        print(RHS[i[1]:i[1]+i[2]+1])
        if ANS == []:
            ANS = i
        else:
            if i[2] > ANS[2]:
                ANS = i
    return ANS
