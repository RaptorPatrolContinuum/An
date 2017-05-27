basis = ["1","2","A","B","3","4","5","6","7","y","u","k","o","s","t","r","a","n","i","e","n","l",",","'"]
G1 = [[1,2],["A","B"],[[3,4],[5,6]],[7,["yuku yo"]],["so transiently","Kotoko"]]
simple = [[1,2]]
pairdepth = [[],[[],[[3],1],[2]],[[],"superhard"]]
pairdepth2 = []
#L = 2 right?

def pairfinder(string,charpair):
    #delete pairs:
    thefuckinganswer = []
    i = 0
    index = 0
    maxi = 0
    for x in string:
        index += 1
        if x == charpair[0]:
            i+= 1
            thefuckinganswer.append([index,i])
            if i > maxi:
                maxi = i
        if x == charpair[1]:
            i= i - 1
            thefuckinganswer.append([index,i])
    return [thefuckinganswer,maxi]

def Address2(string, *args):
    #*args should be a list of bases
    #return a list of addresses:
        #element of value looks like: [[basis,1,address],missing chars]
    value = []

    #PART 3: FINDING ADDRESSES IF L-VAL > 1
    #[[1,2],["A","B"],[[3,4],[5,6]],[7,["yuku yo"]],["so transiently","Kotoko"]]
    '''
    does [1,2] keeps its number from L = 1 to L =3 ????

    no do basis z basis of the new powerset then you apply cantor pairing on that to get the address
    holy shit wtf
    NO WAY THE NUMBER IS TOO BIG
    '''
    for basis in args:
        i = 1
        partialbinary= []
        missing = []
        #1: test basis properly:
        testing = str(string).replace("[","").replace("]","")
        print("-=====", testing)
        for c in testing:
            #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
            #(x,y)= (1/2)(x+y)(x+y+1)+y
            err = []
            try:
                #pairing func starts at 1!(?) F U C K
                x = basis.index(str(i))
            except(ValueError,IndexError):
                #print("i is missing", i)
                err.append(i)
            try:
                y = basis.index(c)
            except(ValueError,IndexError):
                print("char is missing", c)
                err.append(c)
            if len(err) >= 1:
                missing.append([i,c])
            else:
                appendthis = (1/2)*(x+y)*(x+y+1)+y
                partialbinary.append((1/2)*(x+y)*(x+y+1)+y)
            i += 1
        #2: use pairfinder()[1] to find L-val
        value.append([[basis,pairfinder(string,["[","]"])[1],partialbinary],missing])
    #return a list of addresses:
        #element of value looks like: [[[basis, L-value, partialbinary], missingchars with respect to 1st basis]...]
    return value

'''
problems:
    [1,2] and [[3,4],[5,6]] have different L-values
    if even when we go down the basis is missing objects
    GOAL:GET TO THE "BOTTOM" OF LISTS
'''
#for x in G1:
#    print (x)

print(Address2(G1, basis))
#check to see if we can stack try:
#str.replace(old, new[, max])

#1: test basis properly:
testy = str(G1).replace("[","").replace("]","")
#for x in testy:
#    print(x)

#2: how to assign address properly?
#3: checking pair depth:
'''
REAL PROBLEM:
I don't know how to do nested for loops
I want the for loop to "keep going" until it can't
failstate:
    1. not found
    2. can't go deeper
3. calls itself until it stops?
4. what is this object? I feel like it's unique and something I have trouble with
'''

def depthtestFAIL(string,startingL):
    #returns proper L-value
    #I think just put in 1 as startingL
    zerocheck = 0
    print(string, "???")
    for x in string:        
        print("pls work",x)
        if len(x) > 1:
            zerocheck = 1
            print(x,"changed our minds about L = ",startingL)
            break
            #break and continue apply to the innermost loop.
    if zerocheck == 0:
        return startingL
    else:
        currentL = startingL + 1
        #THIS IS WRONG
        depthtest(string,currentL)






#function that goes up when ] and down when [ right:: then getting to 0 is right pair

#print(depthtest(pairdepth,1))

