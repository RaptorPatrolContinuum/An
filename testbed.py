#import itertools
from itertools import *
from math import *
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
#print(list(powerset(powerset("abcd")))[16])

for x in list(powerset("abcd")):
    print(x)
print(list(powerset("abcd"))[15])
#print(list(powerset(powerset("abcd")))[0:15])
print("omfg the numbering is diff in higher powersets")
for x in list(powerset(powerset("abcd")))[0:17]:
    print(x)
'''
print("bit shifting autism")
L = 3
basis = 5
for x in range (0,L):
    basis = 1 << basis
    print("x, basis", x, basis)
print("end??")


m = 2
size = len(["A","B","C"]) ** 2
print("size is ",size)
for wtf in range(0,m):
    print("wtf??", wtf)
    #size = 2 ** size
    size = 1 << size
    print("enum size is", size)
    #size = 5
print("last size is", size)
'''
def BL(B,L):
    '''
    B is size of basis
    L is current L value
    BL(B,L) returns max size of powerset seq
    '''
    size = B ** 2
    for wtf in range(0,L):
        size = 1 << size
    return size

print("check BL", BL(3,2))

def PBL(z,B,L):
    '''
    "Problem of BL"
    if Z > BL(B,L), what is minimal L such that Z < BL(B,new L)?
    since BL increases super fast, naive solution should either solve fast or integer overflow LOL
    so PBL(z,B,L) returns the minimal L such that Z < BL(B,new L) where
    Z is number
    B is size of basis
    L is current L value
    '''
    while z > BL(B,L):
        L += 1
        if z <= BL(B,L):
            return L
    else:
        print("z<BL(B,L)",z,BL(B,L))
print(PBL(5000,3,1))
print(5000,PBL(5000,3,1),BL(3,PBL(5000,3,1)))

'''
then:
if X > BL(B,L) in Vision, calculate PBL(z,B,L)
try:
    PBL(z,B,L)
except(OverflowError):
    print(Overflow in PBL)
    break
'''

def topartialbin(number):
    thing = "{0:b}".format(number)[::-1]
    partialbinary = []
    for g in range(0,len(thing)):
        if thing[g] == str(1):
            partialbinary.append(g)
    return partialbinary

def tointeger(listX):
    sum = 0
    for x in range(0,len(listX)):
        sum = sum + 2 ** listX[x] ** 1
    return sum
GGG = 3300
print(topartialbin(GGG))
print(tointeger(topartialbin(GGG)))

#print(list(powerset(powerset(powerset("ab"))))[0:15])
print("omfg the numbering is diff in higher powersets")
#OOO = powerset(powerset(powerset("ab")))
OOO = powerset("abc")
for x in list(OOO)[0:30]:
    print(x)
    
def Vision(Addresslist):
    #Addresslist = [basis,1,partialbinary]
    #note: partialbinary now is a list of lists which contain values
    #representation is a list of values: (x,f(x))
    '''
    L VALUE TELLS YOU HOW FAR TO LOOK DOWN BEFORE "UNRAVELING"
    idea: instead of repeated for loops you can screw with the brackets:
    define a bracket distance that defines each braket's "nestedness" then clear them appropriately
    '''
    representation = []
    print("check list", Addresslist[2])
    for pair in Addresslist[2]:
        '''
        #if pair is too big(>= P^(L)(|basis|^2)):
        size = len(Addresslist[0])**2
        for wtf in range(0,2):
            size = 1 << size
            print("enum size is", size)
            break
        if pair >= :
            print("Vision can't handle this kind of integer")
            break
        '''
        '''
        then:
        if X > BL(B,L) in Vision, calculate PBL(z,B,L)
        try:
            PBL(z,B,L)
        except(OverflowError):
            print(Overflow in PBL)
            break
        if it's ok, then look for z in P^(newL)(|B|^2) (make sure to not forget about the shifting!!)
        '''
        #TOINTEGER MIGHT BE A PROBLEM
        z = tointeger(Addresslist[2])
        B = len(Addresslist[0])
        L = Addresslist[1]
        if z <= BL(B,L):
            w = floor((sqrt(8*z+1)-1)/2)
            t = (w*w+w)/2
            y = z - t
            x = w - y
            #print("wtf???",Addresslist[2],x,y)
            representation.append([Addresslist[0][int(x)],Addresslist[0][int(y)]])
        else:
            print(z, ">", "BL(",B,",",L,")")
            '''
            look for z in higher powerset:
            make z w/o making powerset
            1. make basis of the current L:
            OMG
            '''
            print("PBL pls",PBL(z,B,L))
    
    print("what is representation?", representation)    
    return representation
def Address2(string, *args):
    #*args should be a list of bases
    #return a list of addresses:
        #element of value looks like: [[basis,1,address],missing chars]
    value = []
    for basis in args:
        i = 1
        partialbinary= []
        missing = []
        for c in string:
            #use cantor pairing func because my func is hard to invert although maybe this might not preserve some continuity
            #(x,y)= (1/2)(x+y)(x+y+1)+y
            err = []
            try:
                #pairing func starts at 1!(?) F U C K
                x = basis.index(str(i))
            except(ValueError,IndexError):
                print("i is missing", i)
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
        value.append([[basis,1,partialbinary],missing])
    #return a list of addresses:
        #element of value looks like: [[[basis, L-value, partialbinary], missingchars with respect to 1st basis]...]
    return value
def CantorPair (x,y):
    return (1/2)*(x+y)*(x+y+1)+y
def CantorInv (z):
    w = floor((sqrt(8*z+1)-1)/2)
    t = (w*w+w)/2
    y = z - t
    x = w - y
    print("return is ",x,y)
print("WTF=======")
print(Vision([["A","B"],1,topartialbin(4)]))
#print(Address2("BA",[["A","B"]]))
