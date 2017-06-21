from autocomposer import *


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

print(PERSISTENTfixer(Chi_basis1,"wtf man") == SomeChi_basis1)

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
    FixedBasis = PERSISTENTfixer(Chi_basis1,string1)
    ANS = 0
    for x in fixedeval(string1):
        try:
            #???FixedBasis.index([])
        except(ValueError,IndexError):
    return ANS

print(fixedeval(TEST)[0][0])  
