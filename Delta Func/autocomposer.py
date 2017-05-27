from math import *
'''
top = 5
for x in range(0,top):
    for y in range(0,top):
        print(x,y)
'''
'''
    problem: what is the int "mean"?
    facts:
    int that is supposed to map to something:
    Lval to tell us how autistic to go
    choice: what mapping?
    have to use cantor pairing so that :
    idea:
    bin(int)  == "{0:b}".format(x).zfill(4)[::-1] so it goes left to right and smallest exp to largest
    find the 1's then iterate down:

    example:
    L == 1
    110100111
    #1: what is the basis?
    NxN with cantor address:
    idea:
    123456789,10...... are pairs
    so:
    1,2,4,7,8,9 are in there
    1 == 1,0
    2 == 0,1
    4 == 1,1
    7 == 2,1
    8 == 1,2
    9 == 0,3

========
    L == 2
    110100111
    idea:
    123456789,10 are elements of P(NxN)
    what are they?????
    you can always take an initial portion:
    idea:
    from L == 1:
     123456789,10...... are pairs
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    .
    .
    .
    so then::
    the vertical is the way to go
    then elements are...
    		 123456789,10...... are pairs
1		1
1		2
0		3
1		4
0		5
0		6
1		7
1		8
1		9
		10
		.
		.
		.

    idea:
    #1: to binary
    #2: figure out L-val
    #3: for each one, construct the part recursively:
        go down 1 Lval



        
'''

    
        


def AutoVision(int,Lval):
    ANS = []
    binary = "{0:b}".format(int)[::-1]
    if Lval == 1:
        z = int
        w = floor((sqrt(8*z+1)-1)/2)
        t = (w*w+w)/2
        y = z - t
        x = w - y
        ANS.append([x,y])
    else:
        '''
        for each one, construct the part recursively:
	go down 1 Lval
	'''	
        i = 0
        for x in binary:
            if x == "1":
                print("yes at", i)
                '''
                what do we do?
                L-1
                because L == 1 we eval and append
                '''
                ANS.append(AutoVision(i,Lval-1))
            i += 1
    return ANS
#print(AutoVision(128,2))
print(AutoVision(3,1))
#note: remove extra brackets
    
