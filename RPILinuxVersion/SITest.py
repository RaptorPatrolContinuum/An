from MiraExternals import *

#print("testing shittySI",ShittySI([[[['0','0'],['1','0']],[]],"Auto"]))


def IsAuto(E_G):
    '''
    checks if a graph is just on integers or not (so we can figure out to use autovision or not)
    '''
    for x in Vertex_(E_G):
        try:
            int(x)
        except ValueError:
            return False
        return True
print(IsAuto([['0','0'],['1','0']]))

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
