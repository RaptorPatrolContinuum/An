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
        
        '''
        V_G = ["A","B","C","H"]
        E_G = [["A","B"],["B","C"],["C","H"],["H","B"],["H","A"]]
        Basis_G = V_G + E_G + rchi(E_G)

        #print(Minv_(Basis_G))
        print("ARU", AddressFunc(Minv_(Basis_G),E_G))
        #print(AutoVision(AddressFunc(Minv_(Basis_G),E_G),1))
        print(AutoVisionHAX(AutoVision(AddressFunc(Minv_(Basis_G),E_G),1),M_(Basis_G)))

        V_H = ["Z","Y","X","V"]
        E_H = [["Z","Y"],["Y","X"],["X","V"],["V","Y"],["V","Z"]]
        Basis_H = V_H + E_H + rchi(E_H)
        print("TACHI", AddressFunc(Minv_(Basis_H),E_H))
        print(AutoVisionHAX(AutoVision(AddressFunc(Minv_(Basis_H),E_H),1),M_(Basis_H)))

        phi = [["A","Z"],["B","Y"],["C","X"],["H","V"],["Z","A"],["Y","B"],["X","C"],["V","H"]]
        #condition is: (I_B_G compose phi, H),(I_B_H compose phi, G)
        print("fuck I feel like compose will miss a lot", Compose(Minv_(Basis_G),phi))
        print("G,H", AddressFunc(Compose(Minv_(Basis_G),phi),E_H))
        print("H,G", AddressFunc(Compose(Minv_(Basis_H),phi),E_G))
        
        E_A = [["A","B"],["B","C"],["C","H"],["H","B"],["H","A"],["H","C"]]
        E_B = [["Z","Y"],["Y","X"],["X","V"],["V","Y"],["V","Z"],["Y","Z"]]

        print("==========================================",print("test E_G and E_H",ShittySI(E_G,E_H)))
        #REDOING E_G/E_H!!!!!
        E_G = [["A","B"],["B","C"],["C","H"],["H","B"],["H","A"]]
        E_H = [["X","V"],["V","Y"],["V","Z"],["Z","Y"],["Y","X"]]
        #print("Realitytesting",ShittySI(E_B,E_A))
        print("test E_G and E_H",ShittySI(E_G,E_H))
