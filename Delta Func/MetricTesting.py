

test1 = "oktestingthis"
test2 = "thisisokothertesting"


def firstlongestcontig(LHS,RHS,LHSinit,RHSinit):
    print("LHS")
    print(LHS)
    print("RHS")
    print(RHS)
    Candidatelist = []
    ANS = []
    RHSCounter = RHSinit
    for y in RHS[RHSinit:]:
        print("stats", LHS[LHSinit], LHSinit, y, RHSCounter)
        #::AM I SUPPOSED TO SCALE THIS
        if LHS[LHSinit] == y:
            #get x pos for LHS start 
            lhscheckpos = LHSinit
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

print(firstlongestcontig(test2,test1,0,0))
#idea: this function is just one direction, then outside the function I compare distances and do the ladder strategy
