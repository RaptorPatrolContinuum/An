from autocomposer import *
#from Casual import *
def CantorPair(x,y):
    return (1/2)*(x+y)*(x+y+1)+y

'''
FACTS:
    STRING
    BASIS = Beta 
    PERSISTENT = Chi_Beta X Chi_Beta

KNOW:
    M_STRING
    

WANTS:
    Generate Chi_Beta
    Persistent Basis
    ADDRESS FUNCTION

#1: TEST PERSISTENT
if x in M_STRING
    x NOT in PERSISTENT
    appent missing parts of x to Basis
    then we know:
    x in M_STRING => x in PERSISTENT

#2: Now we can do the Adress function


==
FUCK DUNNO IF FUNCTIONS ARE FUCKED OR NOT
problems:
pairfuncs
cheat func
#1: so when we have a string, generate M_STRING
#2: TEST PERSISTENT
#3: now do address func

'''
def M_String(string):
    i = 0
    ANS = []
    for x in string:
        ANS.append([i,x])
        i+=1
    return ANS

SomeChi_basis = [0, 'w', 1, 't', 2, 'f', 3, ' ', 4, 'm', 5, 'a', 6, 'n']

def PERSISTENTfixer(Chi_basis,string):
    ANS = Chi_basis
    for x in M_String(string):
        for y in x:
            if y not in Chi_basis:
                ANS.append(y)
    return ANS

print(PERSISTENTfixer(SomeChi_basis,"wtf man") == SomeChi_basis)

#now to do address function
'''
given:
persistent basis
string

want:
address for that string according to the basis

wary:
different L-vals and shit
also evaling stuff like [[][]] (you can stay at a particular lval) and [t[[]]] (go up one Lval)

problem:
1: can be given strings
2: strings can be lists :?
3: there is a diff between syntax/semantics

check if string elements are "taken care of", then we can address the eval form
string > evaluated form > address that


if you can address it, ok return the number
else: go down and look for address

'''



TEST = "[c,a,t]"

#need: fixedeval
def AddressThis(Chi_Basis1,string1):
    print("oldbasis", Chi_Basis1)
    FixedBasis = PERSISTENTfixer(Chi_Basis1,string1)
    print("basus is", FixedBasis)
    ANS = []
    i = 0
    Interim = []
    for x in fixedeval(string1):
        try:
            print(string1,i,x,[FixedBasis.index(i),FixedBasis.index(x)],CantorPair(FixedBasis.index(i),FixedBasis.index(x)))
            Interim.append(CantorPair(FixedBasis.index(i),FixedBasis.index(x)))
            #???FixedBasis.index([])
        except(ValueError,IndexError):
            print("F U C K")
        i+=1
    print("Interim is this guy",Interim)
    #===

    longest = 0
    for x in Interim:
        if x > longest:
            longest = x
    #init binary:
    #print("what is longest?",longest)
    #print("what the fuck is happening to Interim?", Interim)
    ANS="1".zfill(int(longest)+1)
    Interim = list(filter(lambda x: x != longest, Interim))
    for x in Interim:
        ANS = ANS[:int(x)] + "1" + ANS[int(x+1):]
    #print("what is binary ANS?", ANS)
    #print("FML I need to reverse ANS to get actual basis")
    ANS = int(ANS[::-1], 2)
    #print("What is ANS?",ANS)
    '''
    HOW TO FIGURE OUT L-VAL
    def: L-val is where the object lives in:
    example:
    single elements are in L == 1
    collection like "cat" are in L == 2,
    etc..
    '''
    

    return ANS




thenumber = AddressThis([],TEST)
print(thenumber)
print(AutoVision(thenumber,2))

print(CantorPair(300,200))
print(AutoVision(int(CantorPair(300,200)),1))
print("turn your lvoe around")
print(AutoVision(30000,4))
print("ffffffffffffffffff")
def manualkys(number):
    z = number
    w = floor((sqrt(8*z+1)-1)/2)
    t = (w*w+w)/2
    y = z - t
    x = w - y
    print([x,y])
manualkys(0)
print("{0:b}".format(0)[::-1])


