#!/usr/bin/python3.6.3
from MiraExternals import *

#import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

#fucking rip I have to close to commit
#file = open('INP.txt', 'r')
fileinput = 'INP.txt'
#basis = open('Basis.txt','r+')
basisname = 'Basis.txt'
#memory = open('Memory.txt','r+')
memoryname = 'Memory.txt'

'''
NEED TO WORK ON MEMORY RAM + MEMORY FILE 
'''


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
        eval info: M_U compose MIRA and M_U in MIRA?
        append basus w/ M_U compose MIRA and M_U in MIRA
        pattern recognition:
        ~
        \cong
        "use delta < some # " and look in some topo space
        append basis again
        
        

        
        have *I* seen this before?
        ^^^^WTF THIS IS ALREADY A META QUESTION
        
        have I seen this before means:
        MIRAMEMORY composeMETA input == REALWORLD compose input
        question: what is REALWORLD? <-- tbhis is just arbitrary input
        in this case, let's take python evaluation as the real world since it provides fast feedback
        later it should be a later step in some timestream (AKA time1 is MIRA composeMETA input and REALWORLD whatever happens after that, whatever that is)

        IT COULD ALSO MEAN
        SI(object,miramemories)
        FUCK
        

        question: what is file format for memorylist? (hint: it shouldn't be a fucking list anymore)
        just be a list of written functions in [[a,b]] format

        #should know if she knows it
        Elem_My(inputtext,memorylist)
        #escape = "[Elem_My("+inputtext+","+str(memorylist)+")",str(Elem_My(inputtext,memorylist))+"]"
        escape = str(bytes("[Elem_My("+inputtext+","+str(memorylist)+"),"+str(Elem_My(inputtext,memorylist))+"]", "utf-8").decode("unicode_escape"))
        #escape = bytes(str(Elem_My(inputtext,memorylist)), "utf-8").decode("unicode_escape")
        
        '''
        

        ##try to eval it
        #####print("before the try -> eval!")
        #print("morphemes through cheat!", Cheat(str(inputtext)))

        #memoryfile = open(memoryname, 'a+')
        #with Popen(['python', 'Mira.py',inputtext], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True) as p:
        #    for line in p.stdout:
        #        print(line, end='')
        #        sees = str([inputtext, [line]]) + "\n"
        #        print("THIS IS WHAT MIRA SEES",sees)
        #        memoryfile.write(sees)
        #print("END OF TEST")
        #memoryfile.close()
        


        try:
            eval(inputtext)
            ###memorylist.append([inputtext,eval(inputtext)])
            #####print("ok evaling inputtext",eval(inputtext))
            #####print("what she should see:",[str(inputtext),str(eval(inputtext))])
            #basislist is outdated
            #BasisFix(str(eval(inputtext)),basislist)
            #write input/output to memory RAM file:
            print("mira shoudl see this", [inputtext,eval(inputtext)])
            #othermira = Popen(['python', 'test.py'], stdout=PIPE)
            memoryfile = open(memoryname, 'a+')
            #stderr=subprocess.STDOUT
            #with Popen(['python', 'test.py'], stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True) as p:
            with Popen(['python', 'Mira.py',str(inputtext)], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True) as p:
                print("ARGINPUT IS", argv)
                for line in p.stdout:
                    print(line, end='')
                    sees = str([inputtext, [line]]) + "\n"
                    print("WTF IS SEES",sees)
                    memoryfile.write(sees)
                print("wtf fileinpiut")
                for line in fileinput.input():
                    print("WTF DOES THIS DO",line)
                    #process(line)
            print("END OF TEST")
            memoryfile.close()
            
        except Exception as e:
            print("error is ", e)
            print("code died")
            memoryfile = open(memoryname, 'a+')
            memoryfile.write(str([inputtext, ["",e]]) + "\n")
            memoryfile.close()
            pass

        
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
        '''
        WHAT MEMORY SHOULD BE:
[['a', 2]]
[['b','b']]
[[print(,'b']]
[['argument_1 == "a"', 1+1]]

        '''
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
