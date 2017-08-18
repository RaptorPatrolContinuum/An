from itertools import *
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

timer = 0
#for x in list(powerset(list(powerset("t,3,5")))):
#for x in list(powerset(list(powerset([[0,0],[0,1],[1,0],[2,0]])))):
#>???for x in list(powerset(["a","b"])):
#for x in (list(powerset(list(powerset("cat"))))):
'''
for x in list(powerset("12")):
    #print(x)
    if timer % 10 == 0:
        print(x)
    timer +=1
'''
#print(list(powerset([[0,0],[1,0],[0,1][1,1]])))

#for x in range(0,16):
#    print("{0:b}".format(x).zfill(4)[::-1])

#print(["C","Z","Y","C","R"].index("C"))

#WTF
#for x in list(powerset([[0,"a"],[1,"b"]])):
#basis is 0,"a", want

#for x in list(powerset([[0,0],[0,"a"],["a",0],["a","a"]])):
for x in list(powerset([[0,0],[0,1],[0,"a"],[1,0],[1,1],[1,"a"],["a",0],["a",1],["a","a"]])):
    print(x)




#print(list(powerset([[0,"a"],[1,"b"]])).index(([0, 'a'], [1, 'b'])))
