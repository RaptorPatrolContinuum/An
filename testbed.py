#import itertools
from itertools import *
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
    

