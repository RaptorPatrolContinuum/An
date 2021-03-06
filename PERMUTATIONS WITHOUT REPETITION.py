from MiraExternals import *
LinkPool = {'A': ['X', 'Z', 'Y'], 'B': ['X', 'Z', 'Y'], 'C': ['X', 'Z', 'Y', 'G', 'H', 'I']}


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

def PhiConstruct(IndexRan,LinkPool):
    '''
    IndexRan is a function where node corresponds to a list of indices that correspond to a number in LinkPool
    EX: [['A',0],['B',1],['C',0]]
    LinkPool is a dictionary that has nodes and possible node links
    EX: LinkPool = {'A': ['X', 'Z', 'Y'], 'B': ['X', 'Z', 'Y'], 'C': ['X', 'Z', 'Y', 'G', 'H', 'I']}

    REMEMBER: Each pick is mutually exclusive, so if you pick node X then you can't pick node X again but if node X has index Y index Y can appear again but it will NOT be node X
    RETURN: TheChoice: finite function phi that can be used to check SI
    '''
    TheChoice = []
    Exclusion = []
    for x in IndexRan:
        ThePick = [y for y in LinkPool[x[0]] if y not in ran(Exclusion)][x[1]]
        Exclusion.append([x[0],ThePick])
        TheChoice = TheChoice + [[ThePick,x[0]],[x[0],ThePick]]
    
    return TheChoice

def PermutePrep(LinkPool):
    TheSize = []
    TheList = []
    i = 0
    for x in LinkPool:
        TheSize.append([x,len(LinkPool[x]) - i])
        TheList.append(x)
        i += 1
    print("what is the size?",TheSize)
    #NOTE: BECAUSE THERE ARE REPEATS IN THE NUMBERS, YOU NEED TO FILTER OUT THE SETS
    #idea: once you are done with making a candidate, you construct phi by sequentially picking from the first set and excluding that pick from the rest, then construct phi and test SI
		
    Consistency = []
    for G in TheSize:
        if len(Consistency) > 0:
            ConsistencyNew = []
            for H in range(0,G[1]):
                for J in Consistency:
                    Appendage = J + [H]
                    ConsistencyNew.append(Appendage)
                    print("check if J + [H] length can be used to insert the SI condition", J + [H],len(J + [H]))
                    if len(Appendage) == len(LinkPool):
                        #construct phi
                        #RULE: construct phi sequentially by picking from first set and excluding that pick from the rest
                        Indexer = []
                        for i in range(0,len(TheList)):
                            Indexer.append([TheList[i],Appendage[i]])
                        PhiConstruct(Indexer,LinkPool)

            Consistency = ConsistencyNew
        else:
            for H in range(0,G[1]):
                Consistency.append([H])
    print("stats",Consistency)
    return 

PermutePrep(LinkPool)


'''
NEW IDEA:
there are 2 iterators:
one counting "down"
one counting "to the left"

p;an:
sort out LinkPool into an array where smaller pools are on the left

then iterate start is [top,rightmost]
then we go down rightmost (so top to bottom)
then iterator is (top,left of rightmost)
then we repeat: down left rightmost, and repeat "then we go down rightmost (so top to bottom)"

.
.
.
etc
so basically a pyramid type dealio (so for each new row we redo the last column/the last set of code we did)

technicallly we can view it as static up to the last point
then we have a list of last points
then a shift down is a NEW BASIS that relabels all the last points [BUT WE STILL HAVE THE GRAPH STRUCTURE]
etc..
then a column to the left..
a shift down alters two bases?
etc

new idea: some dealio about the rotation of a basis and the construction of a graph sequence after each column

LinkAlg = []
TheChoice = []
Exclusion = []
TheSize = []

for x in LinkPool:
    LinkAlg.append(x)
    ThePick = [y for y in LinkPool[x] if y not in ran(Exclusion)][0]
    Exclusion.append([x,ThePick])
    TheChoice.append(ThePick)
    if len(TheChoice) == len(LinkPool):
        print("1st choice is",TheChoice)
        #idea: run down mid on the right, then keep going
        #goal: gather some metadata so we know how big the whole thing is going to be
        #need: how to rotate bases?
        #ex: if I have 8 choices for last node, 4 for 2nd to last, 3 for 3rd to last, .... then 8*4! is the size
        #since I know how to make the 8*4! "as a matrix (for real???)" then I can just relabel them as I please
        #also, if at any point I "run out" of node picks, then I should skip that choice
        
        #for each tail end path, fix the start of choice and then cross product the tail end
        #then for each new tail end, mess with the bases a little bit and reset
        
        PotentialPicks = []
        #for i in range(-1,-len(Exclusion)-1,-1):
        for i in range(0,len(Exclusion)):
            #want: I want the size of picks per node

            #abuse fact: we know that all these sets should be nested (how to use??????), so it guarantees the fact that picking "earlier" means the size of each set "after" is -1 by each earlier pick
            print(dom(Exclusion).index(Exclusion[i][0])+1,LinkPool[Exclusion[i][0]],len(LinkPool[Exclusion[i][0]])-dom(Exclusion).index(Exclusion[i][0]))
            TheSize.append(len(LinkPool[Exclusion[i][0]])-dom(Exclusion).index(Exclusion[i][0]))

        #NOTE: BECAUSE THERE ARE REPEATS IN THE NUMBERS, YOU NEED TO FILTER OUT THE SETS
        #idea: once you are done with making a candidate, you construct phi by sequentially picking from the first set and excluding that pick from the rest, then construct phi and test SI
            
        Consistency = []
        for G in TheSize:
            if len(Consistency) > 0:
                ConsistencyNew = []
                for H in range(0,G):
                    for J in Consistency:
                        ConsistencyNew.append(J + [H])
                        print("check if J + [H] length can be used to insert the SI condition", J + [H],len(J + [H]))
                        #if len(J + [H]) == len(LinkPool):
                            #construct phi
                            #RULE: construct phi sequentially by picking from first set and excluding that pick from the rest
                            #for x in J + [H]:
                                 
                Consistency = ConsistencyNew
            else:
                for H in range(0,G):
                    Consistency.append([H])
        print("stats",Consistency)

==============================================================================================================
for x in LinkPool:
    LinkAlg.append(x)
    ThePick = [y for y in LinkPool[x] if y not in ran(Exclusion)][0]
    Exclusion.append([x,ThePick])
    TheChoice.append(ThePick)
    if len(TheChoice) == len(LinkPool):
        print("1st choice is",TheChoice)
        #idea: run down mid on the right, then keep going
        #goal: gather some metadata so we know how big the whole thing is going to be
        #need: how to rotate bases?
        #ex: if I have 8 choices for last node, 4 for 2nd to last, 3 for 3rd to last, .... then 8*4! is the size
        #since I know how to make the 8*4! "as a matrix (for real???)" then I can just relabel them as I please
        #also, if at any point I "run out" of node picks, then I should skip that choice
        
        #for each tail end path, fix the start of choice and then cross product the tail end
        #then for each new tail end, mess with the bases a little bit and reset
        
        PotentialPicks = []
        for i in range(-1,-len(Exclusion)-1,-1):
            #want: I want the size of picks per node
            #print("exclusion",Exclusion)
            #print("sayonara",dom(Exclusion),Exclusion[i][0])
            #print("ame",[t for t in Exclusion if t[0] != Exclusion[i][0]])
            #print("Im exhusted already",LinkPool[Exclusion[i][0]])
            #print("WTF is this nesting level", [y for y in LinkPool[Exclusion[i][0]] if y not in ran([t for t in Exclusion if t[0] != Exclusion[i][0]])])
            #print("nani?",i,Exclusion,Exclusion[i][0],len(LinkPool[Exclusion[i][0]]))
            #PotentialPicks.append([Exclusion[i][0],len([y for y in LinkPool[Exclusion[i][0]] if y not in ran([t for t in Exclusion if t[0] != Exclusion[i][0]])])])
            #print("so exhausted",PotentialPicks)

            #abuse fact: we know that all these sets should be nested (how to use??????), so it guarantees the fact that picking "earlier" means the size of each set "after" is -1 by each earlier pick
            print(dom(Exclusion).index(Exclusion[i][0])+1,LinkPool[Exclusion[i][0]],len(LinkPool[Exclusion[i][0]])-dom(Exclusion).index(Exclusion[i][0]))
            TheSize.append(len(LinkPool[Exclusion[i][0]])-dom(Exclusion).index(Exclusion[i][0]))
        
        Consistency = []
        for G in TheSize:
            if len(Consistency) > 0:
                ConsistencyNew = []
                for H in range(0,G):
                    #ConsistencyNew = []
                    print("for J in Consisency",Consistency)
                    for J in Consistency:
                        print("ConsistencyNew before append", ConsistencyNew)
                        print("no exclusions yet or substitutions",G,H,J,J + [H])
                        ConsistencyNew.append(J + [H])
                print("what is ConsistencyNEw before reset?", ConsistencyNew)
                Consistency = ConsistencyNew
            else:
                for H in range(0,G):
                    Consistency.append([H])
        print("stats",Consistency)



#HOW DO I DO THIS

LinkAlg = []
path = len(LinkPool) - 1
depth = []

TheChoice = []
Exclusion = []

for x in LinkPool:
    LinkAlg.append(x)
    ThePick = [y for y in LinkPool[x] if y not in ran(Exclusion)][0]
    depth.append([x,LinkPool[x].index(ThePick)])
    #depth.append([x,[y for y in LinkPool[x] if y not in ran(Exclusion)].index(ThePick)])
    Exclusion.append([x,ThePick])
    TheChoice.append(ThePick)
    if len(TheChoice) == len(LinkPool):
        print("first choice",TheChoice)
        #"go down" or "go back"
        #go back
        if len([y for y in LinkPool[LinkAlg[path]] if y not in ran(Exclusion)]) == 0:
            path = path - 1
            removalset = []
            for z in range(path,len(LinkAlg)):
                removalset.append(LinkAlg[z])
            Exclusion = [y for y in Exclusion if y[0] not in removalset]
            print("check exclusion",Exclusion)

            #print("at least go back",path,LinkAlg[path],)
            #THE INDEX IS FUCKED BECAUSE OF PRIOR CHOICES SO DEPTH IS FUCKING USELESS (?) - # path choices?
            #print("danger zone",[y for y in LinkPool[x] if y not in ran(Exclusion)])
            #print("new pick should be", [y for y in LinkPool[x] if y not in ran(Exclusion)][int(RelEval(depth,LinkAlg[path])[0])+1-path])
            for i in range(path,len(LinkAlg)):
                print("check first", LinkAlg[i])
                print("toki no kawa",LinkPool[LinkAlg[i]])
                print("??",LinkAlg[i])
                print("???",RelEval(depth,LinkAlg[i]))
                print("????",int(RelEval(depth,LinkAlg[path])[0]))
                print("what am I looking for?",[y for y in LinkPool[LinkAlg[i]] if y not in ran(Exclusion)])
                print("what is compose",depth,LinkAlg[i])
                print("what is path?",path)
                print("so 2nd int is bad",[int(RelEval(depth,LinkAlg[i])[0])+1-path])
                NewPick = [y for y in LinkPool[LinkAlg[i]] if y not in ran(Exclusion)][int(RelEval(depth,LinkAlg[i])[0])+1-path]
                print("choicewtf",NewPick)
                Exclusion.append([LinkAlg[path],NewPick])
                #pick the next: for x in ramge(path,maxlength....)
            #print("newChoice! is range of Exclusion!",ran(Exclusion))
        #go down

'''



def ChooseFromLocation(Origin,PrevList,Pos):
    '''
    Origin is gonna be LinkPool
    PrevList is the old Choice
    Pos is a pair of where we start [path (the "column"),depth (the "row")]

    so ChooseFromLocation basically finishes TheChoice from a certain location and outputs:
    TheChoice, NewPos
    '''
            
        
