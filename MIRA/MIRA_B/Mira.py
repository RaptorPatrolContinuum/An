#!/usr/bin/python3.6.3
from MiraExternals import *

#import sys
import codecs

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

fileinput = 'INP.txt'
basisname = 'Basis.txt'
MemoryUNORDERED = 'MemoryUNORDERED.txt'
memoryLong = 'Memory.txt'

'''
NEED TO WORK ON MEMORY RAM + MEMORY FILE 
'''

#use Descent as a way to trigger infinitely spawning/looping current MIRA or not
Descent = True

while Descent:
    nearfield = []
    #print("how many attempts?",len(argv[1:]) > 0,argv[1:])
    try:
        if len(argv[1:]) > 0:
            inputtext = argv[1:][0]
            Descent = False
        else:
            inputtext = str(input("exit or logout to leave \n"))
    except EOFError as e:
        inputtext = str(input("exit or logout to leave \n"))
    except Exception as e:
        FILEinsertAt([MemoryUNORDERED,input,mapcountLINES([MemoryUNORDERED])])
        print("this is the error",e)
        inputtext = str(input("exit or logout to leave \n"))

    if inputtext == "exit" or inputtext == "logout":
        raise SystemExit
        break
    else:
        #print("morphemes through cheat!", Cheat(str(inputtext)))
        #print("what is inputtext", inputtext)
        #print("ARGINPUT IS monkaS", argv)
        
        #INIT OTHER CLONE AS IM MAKING A LOT OF CHANGES
        Cloneinit()

        #THIS TRYBLOCK DOCUMENTS WHAT INPUT>MIRACLONE DOES
        try:
            #write input/output to memory RAM file:
            memoryfile = open(MemoryUNORDERED, 'a+')
            #stderr=subprocess.STDOUT
            #with Popen(['python', 'test.py'], stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True) as p:
            #with Popen(['python', 'Mira.py', inputtext], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True) as p:
            miralist = ['python', OtherClone() + '\\Mira.py', inputtext]
            #print("this should be miralist", miralist)
            if Descent == True:
                #print("NEED TO MAKE CLONE!",argv)
                seesANS = []
                with Popen(miralist, stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True) as p:
                    #print("ARGINPUT IS", argv)
                    for line in p.stdout:
                        print(line, end='')
                        sees = str([line]) + "\n"
                        #print("WTF IS SEES",sees)
                        seesANS.append(sees)
                    '''
                    for line in fileinput.input():
                        print("WTF DOES THIS DO",line)
                        #process(line)
                    '''
                internaltest = [["Popen(['python'," + str(os.getcwd()) + "\\Mira.py, "+inputtext+"], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)",seesANS]]
                orsequence = bisectionSearch([memoryLong,str(internaltest),basisname]) + shittySearch([MemoryUNORDERED,str(internaltest)])
                if len(orsequence) > 0:
                    print("I already saw that!")
                else:
                    memoryfile.write(str(internaltest) + "\n")
                    nearfield.append(str(internaltest))
            else:
                #just write the OG test once
                internaltest2 = [["TOTAL_ARGUMENT == '"+ str(inputtext) +"'",[str(eval(inputtext)),""]]]
                orsequence2 = bisectionSearch([memoryLong,str(internaltest2),basisname]) + shittySearch([MemoryUNORDERED,str(internaltest2)])
                if len(orsequence2) > 0:
                    print("already saw that 2")
                else:
                    memoryfile.write(str(internaltest2) + "\n")
                    nearfield.append(str(internaltest2))
            memoryfile.close()
        except Exception as e:
            print("error is ", e)
            print("code died")
            memoryfile = open(MemoryUNORDERED, 'a+')
            #HINT: ["",e] IS BECAUSE popen has error as 2nd element
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ str(inputtext) +"'", ["",e]]]) + "\n")
            nearfield.append(str([["TOTAL_ARGUMENT == '"+ str(inputtext) +"'", ["",e]]]))
            memoryfile.close()
            pass

        #guessing abstractions
        #need to stop clone mira from duplicating responses:
        if Descent == True:
            for x in nearfield:
                print("x in nearfield",x)
                #abstractionGENERAL([[MemoryUNORDERED,memoryLong],x])
                abstractionGENERAL([[MemoryUNORDERED,memoryLong],inputtext])
            '''
            guess abstractions properly:
            delta2(a,b) == a OR b means the similar one is the abstraction
            use delta3 on the NON abstraction to get a replacement guess
            attempt abstraction with composeMETA([delta3, delta2])

            THEN CHECK ABSTRACTION WITH REALITY <---

            IF ALIGNS, WRITE IT DOWN

            THEN NEXT STEP IS PROBLEM SOLVING ON AN ABSTRACT TIMELINE WHERE YOU DONT GET INSTANT CALL-RESPONSE

            ANOTHER THING TO DO IS TO DO INSTANT CALL-RESPONSE
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
        ##print("ok testing ComposeMETA===================",ComposeMETA([function1,function2]))
        ##print("ok testing ComposeMETA LIST",ComposeMETA([functionList,functionList2]))
        ##ANSWERS:
        ##ok testing ComposeMETA=================== [['a', 'd']]
        ##ok testing ComposeMETA LIST [['a', 'd'], ['Z', 'Y'], ['Z', 'TOTALCHECK']]
        #=================================================
