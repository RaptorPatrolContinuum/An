#!/usr/bin/env python
from MiraExternals import *

file = open('INP.txt', 'r')
basis = open('Basis.txt','r+')
memory = open('Memory.txt','r+')

while True:
    inputtext = str(raw_input("exit or logout to leave \n"))
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
        print(M_(inputtext))
        print("end of alg")
        #\omega(I_basis_U,U) & vision
        ##print("fml", Address(basislist,M_(inputtext)))
        ##print(AutoVision(Address(basislist,M_(inputtext)),1))
        ##print(VisionBasis(basislist,AutoVision(Address(basislist,M_(inputtext)),1)))

        #eval info: M_U compose MIRA and M_U in MIRA?
        for x in memorylist:
            print(memorylist)
            print(Compose(x,M_(inputtext)))

        Elem_My(M_(inputtext),Inspector_M(M_(memorylist)))


        
        #memorylist = list of functions

        
        #append basis w/ M_U compose MIRA and M_U in MIRA
        #pattern recognition:
        #~
        #\cong
        #"use delta < some # " and look in some topo space
        #append basis again


       
