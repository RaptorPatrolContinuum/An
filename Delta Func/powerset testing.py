from itertools import *
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

#for x in list(powerset(list(powerset([[0,0],[0,1],[1,0],[2,0]])))):
#for x in list(powerset("12")):
#    print(x)

#print(list(powerset([[0,0],[1,0],[0,1][1,1]])))

#for x in range(0,16):
#    print("{0:b}".format(x).zfill(4)[::-1])

print(["C","Z","Y","C","R"].index("C"))
