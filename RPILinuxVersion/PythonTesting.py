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
#print("is vertex fucked?", Vertex_([['0','0'],['1','0']]))
#print(IsAuto([['0','0'],['1','0']]))
#print(IsAuto([['0','0'],['1','R']]))
#print(int('R'))

print("element relation work? False",Elem_My('1',[['1','1']]))
print("element relation work? True",Elem_My(['1','1'],[['1','1']]))
test = [['1','1']]
print(Inspector_M(test))
print(M_(test))
print(PreImage(test))
print(Compose(M_(test),PreImage(test)))
print("element relation work? True",Elem_My('1',['1','5']))
