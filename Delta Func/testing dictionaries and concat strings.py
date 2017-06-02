tel = {'jack': 4098, 'sape': 4139}
tel['jack'+'atlas'] = "5d's"
#print(tel['jackatlas'])
tel['jackatlas'] = tel['jackatlas'] + "pls concat"
#print(tel['jackatlas'])
tel[3] = ["1"]
tel[3].append("does this work?")
#print(tel[3])

theting = "[2,3,4,[5]]"

#print(list(theting)[0])





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


#print(pairfinderSTRING(pairfinder(theting,["[","]"]),theting))
print(eval(theting)[1])
