LinkPool = {'A': ['X', 'Z', 'Y'], 'B': ['X', 'Z', 'Y'], 'C': ['X', 'Z', 'Y']}


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
'''


#HOW DO I DO THIS

LinkAlg = []
path = len(LinkPool) - 1
depth = []

TheChoice = []
Exclusion = []

for x in LinkPool:
    LinkAlg.append(x)
    ThePick = [y for y in LinkPool[x] if y not in Exclusion][0]
    depth.append([x,LinkPool[x].index(ThePick)])
    Exclusion.append(ThePick)
    TheChoice.append(ThePick)
    if len(TheChoice) == len(LinkPool):
        print(TheChoice)
        #"go down" or "go back"
        #go back
        if len([y for y in LinkPool[LinkAlg[path]] if y not in Exclusion]) == 0:
            path = path - 1
            Exclusion = []
            print("at least go back",path,LinkAlg[1])
        #go down

def ChooseFromLocation(Origin,PrevList,Pos):
    '''
    Origin is gonna be LinkPool
    PrevList is the old Choice
    Pos is a pair of where we start [path (the "column"),depth (the "row")]

    so ChooseFromLocation basically finishes TheChoice from a certain location and outputs:
    TheChoice, NewPos
    '''
            
        

