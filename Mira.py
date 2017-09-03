from MiraExternals import *

while True:
    inputtext = str(input("Exit or logout to leave \n"))
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


        ##test SI condition: I_G \circ phi, number and I_H \circ phi, number
        print("TESTING SI CONDITION ON A BASIC LEVEL")
        '''
        G = fml, I_G = [[f,1],[m,2][l,3]] = ["f","m","l","0","1","2"]
        H = abc, I_H = [[a,1],[b,3],[c,3]] = ["a","b","c","0","1","2"]
        DID I FUCK UP THE ORDER???
        no i didn't but the address func in python just takes the actual object instead of the index of the obj
        REMAKE ADDRESS FUNC
    
        
        new graph is abc
        phi is gonna be
        [["f","a"],["m","b"],["l","c"],["a","f"],["b","m"],["c","l"]]
        
        '''
        print("fml", Address(["f","m","l","0","1","2"],M_("fml")))
        print("abc", Address(["a","b","c","0","1","2"],M_("abc")))
        #print("CAN'T FUCKING READ",Minv_(["f","m","l","0","1","2"]))
        #print("wtf does compose give", Compose(Minv_(["f","m","l","0","1","2"]),[["f","a"],["m","b"],["l","c"],["a","f"],["b","m"],["l","c"]]))
        print("I_G circ phi")
        print(Address(toString(PreImage(Compose(Minv_(["a","b","c","0","1","2"]),[["f","a"],["m","b"],["l","c"],["a","f"],["b","m"],["c","l"]]))),M_("fml")))
        print("I_H circ phi")
        print(Address(toString(PreImage(Compose(Minv_(["f","m","l","0","1","2"]),[["f","a"],["m","b"],["l","c"],["a","f"],["b","m"],["c","l"]]))),M_("abc")))

