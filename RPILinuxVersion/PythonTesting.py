from MiraExternals import *

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
print("is vertex fucked?", Vertex_([['0','0'],['1','0']]))
print(IsAuto([['0','0'],['1','0']]))
print(IsAuto([['0','0'],['1','R']]))
#print(int('R'))
