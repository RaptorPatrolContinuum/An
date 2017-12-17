#!/usr/bin/python3.6.3
from MiraExternals import *

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

file = open('INP.txt', 'r')
basis = open('Basis.txt','r+')
memory = open('Memory.txt','r+')

def BasisFix(inp,basis):
    '''
    this fixes basis so I can call address whenever
    '''
    for char in inp:
        #if stuff is not in the basis:
        if char in basis:
            pass
        else:
            #append to basis
            basis.append(char)
    if len(inp) in basis:
        pass
    else:
        for k in range(len(inputtext)+1):
            if str(k) in basis:
                pass
            else:
                basis.append(str(k))
    return

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
        BasisFix(inputtext,basislist)                

                        
        #for U unknown, see M_U
        print("what is input", inputtext)
        print("end of alg")

        #\omega(I_basis_U,U) & vision
        #print(basislist)
        #print(M_(inputtext))
        print("Address of obj", Address(basislist,M_(inputtext)))
        print(VisionBasis(basislist,AutoVision(Address(basislist,M_(inputtext)),1)))
        print("want the X address of this",AutoAddressFunc([['0', '1'], ['1', '2']]))
        print("want the Y address of this",AutoAddressFunc([['0', '0'], ['1', '1'], ['2', '1']]))
        print("what number am I on then?",CantorPair(260,145))
        print("make a tostring func since we have the info but not the order",ran(VisionBasis(basislist,AutoVision(Address(basislist,M_(inputtext)),1))))


        #questions to ask:/ALWAYS REMEMBER TO APPEND AFTER
        #REMEMBER, AT EACH STEP YOU NEED TO APPEND THAT ANSWER TO MIRA

        
        ##have I seen this before?
        #print("input in memory?",inputtext,Elem_My(inputtext,memorylist))
        #should know if she knows it
        Elem_My(inputtext,memorylist)
        ###print("ORIGINAL MEMORY?",memorylist)
        #escape = "[Elem_My("+inputtext+","+str(memorylist)+")",str(Elem_My(inputtext,memorylist))+"]"
        escape = str(bytes("[Elem_My("+inputtext+","+str(memorylist)+"),"+str(Elem_My(inputtext,memorylist))+"]", "utf-8").decode("unicode_escape"))
        #escape = bytes(str(Elem_My(inputtext,memorylist)), "utf-8").decode("unicode_escape")
        ###print("WTF ESCAPE CHARS",escape)
        
        ###memorylist.append(escape)
        ###memorylist.append(M_(inputtext))

        print("need to see error lol",Address(basislist,[["1","print"]["2","("]["3","test"]["4",")"]])) 
        ##try to eval it
        print("before the try -> eval!")
        #print("morphemes through cheat!", Cheat(str(inputtext)))
        try:
            eval(inputtext)
            ###memorylist.append([inputtext,eval(inputtext)])
            print("ok evaling inputtext",eval(inputtext))
            print("what she should see:",[str(inputtext),str(eval(inputtext))])
            BasisFix(str(eval(inputtext)),basislist)
            
        except:
            print("code died")
            pass
        
        #print("MEMORYLIST IS", memorylist)
        #get nearest topo: M_U compose MIRA and M_U in MIRA?
        '''
        for x in memorylist[0:]:
            #just do fast compose to express "close" possibilities
            
            print("stats",x,memorylist)
            print("composing",M_(x),M_(inputtext),Compose(M_(x),M_(inputtext)))
            fast = Compose(M_(x),M_(inputtext))
            print("what she sees",["Compose(M_("+str(x)+"),"+str(M_(inputtext))+")",fast]) 
            if fast != None:
                memorylist.append(["Compose(M_("+str(x)+"),"+str(M_(inputtext))+")",fast])
        '''     
                

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
