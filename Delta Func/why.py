print("list eqauls",[[1,3],[0,0]] == [[1,3],[0,0]],[[1,3],[0,0]] == [[1,3],[0,1]])

f = open("MACHINE TASKLIST.tdl", "r+")
#print("the length is ", len(f.read()))
wtfsum = 0
testsum = 0
for x in range (0, 1045991):
    wtfsum+= (x*x + x)/2
#print(wtfsum)
empty = []
'''
for x in range(0,len(empty)):
    print("wtf")
'''

#how to insert into a list at the right index
def InsertAt (List,obj,Index):
    '''
    Inserts obj at List[Index] and appends the rest of list after it
    '''
    VALUE = List[:Index]
    VALUE.append(obj)
    for x in range(0,len(List[Index:])):
        VALUE.append(List[Index + x])
    return VALUE


'''
for x in range(0,3):
    
    if x > 1:
        print("does break kill whole nest?")
        break
    
    print(x)
'''
Thing = [1, 2, 3, 4]
#print(InsertAt(Thing,13,3))
