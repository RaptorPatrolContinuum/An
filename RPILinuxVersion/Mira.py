#!/usr/bin/python3.6.3
from MiraExternals import *

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

file = open('INP.txt', 'r')
basis = open('Basis.txt','r+')
memory = open('Memory.txt','r+')

while True:
    inputtext = str(input("exit or logout to leave \n"))
    if inputtext == "exit" or inputtext == "logout":
        break
    else:
        '''
        What's the plan?

        for U unknown, see M_U
        fix basis to accomodate info
        \omega(I_basis_U,U) & vision
        eval info: M_U compose MIRA and M_U in MIRA?
        append basus w/ M_U compose MIRA and M_U in MIRA
        pattern recognition:
        ~
        \cong
        "use delta < some # " and look in some topo space
        append basis again
        
        '''
        #init basis
        basis.seek(0)
        if len(basis.read()) == 0:
            basislist = ["True","False"]
            
        else:
            #get basistext as list:
            basis.seek(0)
            basislist = ast.literal_eval(basis.read())

        #init memory:
        memory.seek(0)
        if len(memory.read()) == 0:
            memorylist = []
        else:
            #get basistext as list:
            memory.seek(0)
            memorylist = ast.literal_eval(memory.read())

        #fix basis
        for char in inputtext:
            #if stuff is not in the basis:
            if char in basislist:
                pass
            else:
                #append to basis
                basislist.append(char)
        
        if len(inputtext) in basislist:
            pass
        else:
            for k in range(len(inputtext)+1):
                if str(k) in basislist:
                    pass
                else:
                    basislist.append(str(k))
                    

                
        #for U unknown, see M_U
        print("what is input", inputtext)
        print("end of alg")
        #\omega(I_basis_U,U) & vision
        print(basislist)
        print(M_(inputtext))
        print("Address of obj", Address(basislist,M_(inputtext)))
        print("wtf why is there an L?",AutoVision(Address(basislist,M_(inputtext)),1))
        print(VisionBasis(basislist,AutoVision(Address(basislist,M_(inputtext)),1)))

        #questions to ask:/ALWAYS REMEMBER TO APPEND AFTER
        #REMEMBER, AT EACH STEP YOU NEED TO APPEND THAT ANSWER TO MIRA

        
        ##have I seen this before?
        #print("input in memory?",inputtext,Elem_My(inputtext,memorylist))
        #should know if she knows it
        Elem_My(inputtext,memorylist)
        memorylist.append(inputtext)

        
        ##try to eval it
        try:
            eval(inputtext)
            memorylist.append([inputtext,eval(inputtext)])
        except:
            pass
        
        #get nearest topo: M_U compose MIRA and M_U in MIRA?
        for x in memorylist:
            #just do fast compose to express "close" possibilities
            fast = Compose(x,M_(inputtext)) 
            if fast != None:
                memorylist.append(fast)

                
                

        #memorylist = list of addresses/functions

        
        #append basis w/ M_U compose MIRA and M_U in MIRA
        #pattern recognition:
        #~
        #\cong
        #"use delta < some # " and look in some topo space
        #append basis again

        #check what the stuff is
        #print("blist",basislist)
        #print("mlist",memorylist)
        #write everything down
        basis.seek(0)
        basis.write(str(basislist))
        memory.seek(0)
        memory.write(str(memorylist))
