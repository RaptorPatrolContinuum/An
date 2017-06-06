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
        print("x",x)
        g = i
        print("g, max",g, len(fixed))
        maxlength = 0
        #print(maxlength)
        #y = fixed[g+1]
        #if g+1 < len(fixed):
        #    y = fixed[g+1]
        try:
            y = fixed[g+1]
        except(IndexError):
            return eval(fixed)
        '''

        '''
        #print("y",y)
        if str(x) != "\"" and str(x) != "[" and str(x) != "]" and str(x) != ",":
            #1: figure out the length of alphas:
            while str(y) != "\"" and str(y) != "[" and str(y) != "]" and str(y) != ",":
                maxlength += 1
                print("how the fuck did I get over",x, maxlength, g+1, len(fixed), fixed)
                if g+1 < len(fixed):
                    y = fixed[g+1]
                g += 1
            print("maxl,x",maxlength, x)
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
            print("wtf does fixed look like",fixed)
            try:
                y = fixed[i+2]
            except(IndexError):
                print("wtf does fixed look like KIZUTU",fixed)
                print(eval(fixed))
                return eval(fixed)
        i += 1
        try:
            fixed[i]
        except(IndexError):
            return eval(fixed)
    return eval(fixed)





#fixed = "[c,[t,[a],[t]],cat]"
cnacer = "[[c],[[t],[a],[t]],[cat]]"
print("OG")
print(cnacer)
#print(fixed[:3])
#print(fixed[3:])
print("wtf is the answer", fixedeval(cnacer))
print(fixedeval("[[c]]"))
