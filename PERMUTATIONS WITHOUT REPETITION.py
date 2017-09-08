from MiraExternals import *
LinkPool = {'A': ['X', 'Z', 'Y'], 'B': ['X', 'Z', 'Y'], 'C': ['X', 'Z', 'Y', 'G', 'H', 'I']}


def ran(func):
    ANS = []
    for x in func:
        ANS.append(x[1])
    return ANS

LinkAlg = []

TheChoice = []
Exclusion = []

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
            
        
