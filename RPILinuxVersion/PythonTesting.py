from MiraExternals import *

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def IsAuto(E_G):
    '''
    checks if a graph is just on integers or not (so we can figure out to use auto functions or not)
    '''
    for x in Vertex_(E_G):
        print("what is x?",x)
        try:
            int(x)
        except ValueError:
            return False
            break
    return True
#print("is vertex fucked?", Vertex_([['0','0'],['1','0']]))
#print(IsAuto([['0','0'],['1','0']]))
#print(IsAuto([['0','0'],['1','R']]))
#print(int('R'))

#print("element relation work? False",Elem_My('1',[['1','1']]))
#print("element relation work? True",Elem_My(['1','1'],[['1','1']]))
#test = [['1','1']]
#print(Inspector_M(test))
#print(M_(test))
#print(PreImage(test))
#print(Compose(M_(test),PreImage(test)))
#print("element relation work? True",Elem_My('1',['1','5']))
#print(CantorPair(5,2))
#print(CantorPair(6,3))
#print(CantorPair(7,4))
#print(CantorPair(8,2))
Interim = [CantorPair(5,2),CantorPair(6,3),CantorPair(7,4),CantorPair(8,2)]


ANS="1".zfill(int(max(Interim))+1)
#print("need Interim Data", Interim)
Interim = list(filter(lambda x: x != max(Interim), Interim))
for x in Interim:
        ANS = ANS[:int(x)] + "1" + ANS[int(x)+1:]
#print(ANS)
ANS = int(ANS[::-1], 2)
#print(ANS)
#print("==========================")
#print("int(" + str(ANS) + "[::-1], 2)")
#print("int(" + str(ANS) + "monkeys")
#print(ShittySI([[[['0', '0'], ['1', '0'], ['0', '1'], ['2', '0'], ['1', '1'], ['1', '2']], [['0', '0'], ['1', '0'], ['0', '1'], ['0', '2']]],"Auto"]))
#print(ShittySI([[[['0','1'],['1','2'],['2','1']],[['1','2'],['2','0'],['0','2'],['0','1']]],"Auto"]))
#print(ShittySI([[[['1','2'],['2','0'],['0','2'],['0','1']],[['0','1'],['1','2'],['2','1']]],"Auto"]))
#print(CantorPair(AutoAddressFunc([['1', '0'], ['0', '1'], ['0', '2'], ['3', '0']]),AutoAddressFunc([['0', '0'], ['1', '0'], ['3', '0'], ['1', '2']])))
print("wtf?",AutoAddressFunc([]))
#print("testing why shittySI is []", ShittySI([[[['0','0']],[['0','0'],['1','0'],['2','0'],['1','1'],['0','3']]],"Auto"]))
print("testing why shittySI is []", ShittySI([[[],[['0','1'],['2','0'],['1','1'],['0','3']]],"Auto"]))
