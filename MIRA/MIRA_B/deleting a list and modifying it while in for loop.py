from MiraExternals import *

Connections = ['1','2','3','4','5','6','7']

i = 0
for x in range(len(Connections)):
    print("what's x",x)
    print("test i",Connections[i])
    print("oldcon", Connections)
    del Connections[i+1]
    print("newcon", Connections)
    Connections = InsertAt(Connections,"insert" + str(i),0)
    print("insertAT",)
    #add or delete more than 2
    i += 1
'''
for x in range(10):
    print(x)

0
1
2
3
4
5
6
7
8
9
'''
