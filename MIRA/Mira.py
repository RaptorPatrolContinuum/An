#!/usr/bin/python3.6.3
from MiraExternals import *

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

#fucking rip I have to close to commit
file = open('INP.txt', 'r')
basis = open('Basis.txt','r+')
memory = open('Memory.txt','r+')

#filedata = 'INP.txt'
#basis = 'Basis.txt'
#memory = 'Memory.txt'


while True:
    inputtext = str(input("exit or logout to leave \n"))
    if inputtext == "exit" or inputtext == "logout":
        raise SystemExit
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


        more old code
        ================================================================
        #init basis
        if len(basisCopy) == 0:
            basisCopy = ["True","False"]
            
        else:
            #get basistext as list:
            basis = ast.literal_eval(basis.read())

        #fix basis
        BasisFix(inputtext,basislist)         
        '''
        #init memory:
        memory.seek(0)
        if len(memory.read()) == 0:
            memorylist = []
        else:
            #get basistext as list:
            memory.seek(0)
            #memorylist = ast.literal_eval(memory.read())
            memorylist = memory.readlines()
            memorylistNEW = memory.readlines()       

        #####print("TEST LEXICO ORDERING")
        basis.seek(0)
        ##########print(fileindex([basis,"[" + "\n"]))
        #####print(AddressFILE([basis,"[" + "\n"]))
        #####lexicoSort([basis,memory])

        
        ##have I seen this before?
        '''
        WTF THIS IS ALREADY A META QUESTION
        have I seen this before means:
        MIRAMEMORY composeMETA input == REALWORLD compose input
        question: what is REALWORLD?
        in this case, let's take python evaluation as the real world since it provides fast feedback
        later it should be a later step in some timestream (AKA time1 is MIRA composeMETA input and REALWORLD whatever happens after that, whatever that is)

        IT COULD ALSO MEAN
        SI(object,miramemories)
        FUCK
        

        question: what is file format for memorylist? (hint: it shouldn't be a fucking list anymore)
        just be a list of written functions in [[a,b]] format
        
        '''
        
        #####print("what is memorylist \n",memorylist)
        for x in memorylist:
            try:
                #print("qhat is x?",x)
                second = eval(x)
                #####print("what is second?", second)

                #print("memorylist check again",Inspector_M(memorylist))
                #FUUUCK COMPOSEMETA OR COMPOSE ONLY
                #####print("ELEMENT OF AND MEMORYLIST",Elem_My("[['b','b']]\n",memorylist))
                '''
                WORKS FOR THIS MEMORYTEXT
                [[print(,'b']]
                [['argument_1 == "a"', 1+1]]
                [['b','b']]
                '''
                
                first = [['a',['a']]]
                #####print("2nd",second)
                #####print("1st",first)
                #####print(str(ComposeMETA(second,first)))
                #####print(Q_(str(ComposeMETA(second,first)) + "\n"))
                #print("memorylist check again",Inspector_M(memorylist))
                #####print("ELEMENT OF AND MEMORYLIST VER2",Elem_My(str(ComposeMETA(second,first)) + "\n",memorylist))
                #print("how to add to memorylist", memorylist.append(str(ComposeMETA(second,first)) + "\n"))
                
                #if ComposeMETA(second,first) HAS NOT BEEN SEEN BEFORE
                if Elem_My(str(ComposeMETA(second,first)) + "\n",memorylist) == False:
                    #####print("attempt to add!")
                    #add compositions as answers if you haven't seen it already
                    memorylistNEW.append(str(ComposeMETA(second,first)) + "\n")
                    #####print("newlist is", memorylistNEW)
                    #COMPARE WITH PYTHON INPUT
                    
            except:
                pass








        
        #print("input in memory?",inputtext,Elem_My(inputtext,memorylist))
        #should know if she knows it
        Elem_My(inputtext,memorylist)
        ###print("ORIGINAL MEMORY?",memorylist)
        #escape = "[Elem_My("+inputtext+","+str(memorylist)+")",str(Elem_My(inputtext,memorylist))+"]"
        escape = str(bytes("[Elem_My("+inputtext+","+str(memorylist)+"),"+str(Elem_My(inputtext,memorylist))+"]", "utf-8").decode("unicode_escape"))
        #####print("wtf is escape",escape)
        #escape = bytes(str(Elem_My(inputtext,memorylist)), "utf-8").decode("unicode_escape")
        ###print("WTF ESCAPE CHARS",escape)
        
        ###memorylist.append(escape)
        ###memorylist.append(M_(inputtext))

        #print("THIS WAS MISSING COMMAS",Address(basislist,[["1","print"],["2","("],["3","test"],["4",")"]])) 
        ##try to eval it
        #####print("before the try -> eval!")
        #print("morphemes through cheat!", Cheat(str(inputtext)))
        try:
            eval(inputtext)
            ###memorylist.append([inputtext,eval(inputtext)])
            #####print("ok evaling inputtext",eval(inputtext))
            #####print("what she should see:",[str(inputtext),str(eval(inputtext))])
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
        #basis.seek(0)
        #basis.write(str(basislist))

        '''
        NEED TO REENABLE THIS
        
        print("what is memorystlist new?", memorylistNEW)
        memory.seek(0)
        memory.write(str(memorylistNEW))
        '''


        '''
        ==================================================================================================
        PUT ALL THE TESTING CODE PAST HERE
        ==================================================================================================

        cool technique, but not required right now
        
        fileObj = open('INP.txt', 'r')
        fileCopy = fileObj.read()

        basisObj = open('Basis.txt','r+')
        basisCopy = basisObj.read()

        memoryObj = open('Memory.txt','r+')
        memoryCopy = memoryObj.read()

        #close files
        fileObj.close()
        basisObj.close()
        memoryObj.close()
        '''
        #=================================================
        #for U unknown, see M_U
        #print("what is input", inputtext)
        #print("end of alg")

        #\omega(I_basis_U,U) & vision
        #print(basislist)
        #print(M_(inputtext))
        #print("Address of obj", Address(basislist,M_(inputtext)))
        #print(VisionBasis(basislist,AutoVision(Address(basislist,M_(inputtext)),1)))
        #print("want the X address of this",AutoAddressFunc([['1', '0'], ['0', '1'], ['2', '0'], ['0', '2'], ['3', '0'], ['2', '1']]))
        #print("want the Y address of this",AutoAddressFunc([['0', '1'], ['0', '2'], ['3', '1']]))
        #print("what number am I on then?",CantorPair(238,2084))
        #print("make a tostring func since we have the info but not the order ||||",toString(VisionBasis(basislist,AutoVision(Address(basislist,M_(inputtext)),1)),"INTEGERS"))

        ##function2 = [['a','b']]
        ##functionList2 = [['a',['b']],['Z',['f','AF']]]
        ##function1 = [['TOTAL_ARGUMENT == "b"', 'd']]
        ##functionList = [['argument_1 == "b"', 'd'],['argument_2 == "AF"', 'Y'],[str('TOTAL_ARGUMENT' + '==' + str(['f','AF'])),'TOTALCHECK']]
        ##print("ok testing ComposeMETA===================",ComposeMETA(function1,function2))
        ##print("ok testing ComposeMETA LIST",ComposeMETA(functionList,functionList2))
        ##ANSWERS:
        ##ok testing ComposeMETA=================== [['a', 'd']]
        ##ok testing ComposeMETA LIST [['a', 'd'], ['Z', 'Y'], ['Z', 'TOTALCHECK']]
        #=================================================
