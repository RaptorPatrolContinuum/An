from MiraExternals import *

#print("testing shittySI",ShittySI([[[['0','0'],['0','0']],[]],"Auto"]))
#print("testing shittySI",ShittySI([[[['2','0']],[['1','0']]],"Auto"]))
#print("testing shittySI",ShittySI([[[['1', '0'], ['2', '0'], ['2', '1']], [['1', '0'], ['0', '1'], ['1', '1'], ['0', '2'], ['2', '1']]],"Auto"]))
print("testing", ShittySI([[[['0', '0'], ['0', '1']], [['0', '0'], ['2', '0'], ['0', '2']]],"Auto"]))

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

#print("==========================================", print("test E_G and E_H",ShittySI(E_G,E_H)))
#REDOING E_G/E_H!!!!!
E_G = [["A","B"],["B","C"],["C","H"],["H","B"],["H","A"],["G","G"]]
E_H = [["X","V"],["V","Y"],["V","Z"],["Z","Y"],["Y","X"]]
#print("Realitytesting",ShittySI(E_B,E_A))
print("test E_G and E_H",ShittySI([[E_G,E_H]]))
print("ok now to sequence through with autovision. because of the 'compression theorem' we just need to expand the basis and not worry about Lvals",AutoVision(30000000,1))
#strat: for x,y -> infinity, append to memory SI(vision(x),vision(y))
#print("CHECK SI AGAIN FUCKING BASIS", ShittySI([[[['0','0'],['2','0']],[['1','0']]],"Auto"]))
print("CHECK SI AGAIN FUCKING BASIS", ShittySI([[[['2','0']],[['1','0']]],"Auto"]))


