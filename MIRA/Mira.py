#!/usr/bin/python3.6.3
from MiraExternals import *

#import sys
import codecs

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

#fucking rip I have to close to commit
#file = open('INP.txt', 'r')
fileinput = 'INP.txt'
#basis = open('Basis.txt','r+')
basisname = 'Basis.txt'
#memory = open('Memory.txt','r+')
MemoryUNORDERED = 'MemoryUNORDERED.txt'
memoryLong = 'Memory.txt'

'''
NEED TO WORK ON MEMORY RAM + MEMORY FILE 
'''

#use Descent as a way to trigger infinitely spawning/looping current MIRA or not
Descent = True

while Descent:
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
        #inputtext = "exit"
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
        #print("morphemes through cheat!", Cheat(str(inputtext)))

        #print("what is inputtext", inputtext)
        #print("ARGINPUT IS monkaS", argv)
        #INIT OTHER CLONE AS IM MAKING A LOT OF CHANGES
        Cloneinit()
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
            else:
                #just write the OG test once
                #[['TOTAL_ARGUMENT == "b"', 'd']]
                #str([str(inputtext),str(eval(inputtext))]) + "\n"
                internaltest2 = [["TOTAL_ARGUMENT == '"+ str(inputtext) +"'",str(eval(inputtext))]]
                orsequence2 = bisectionSearch([memoryLong,str(internaltest2),basisname]) + shittySearch([MemoryUNORDERED,str(internaltest2)])
                if len(orsequence2) > 0:
                    print("already saw that 2")
                else:
                    memoryfile.write(str(internaltest2) + "\n")
            memoryfile.close()
            
        except Exception as e:
            print("error is ", e)
            print("code died")
            memoryfile = open(MemoryUNORDERED, 'a+')
            #HINT: ["",e] IS BECAUSE popen has error as 2nd element
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ str(inputtext) +"'", ["",e]]]) + "\n")
            memoryfile.close()
            pass

        #need to stop clone mira from duplicating responses:
        if Descent == True:
            #look for/through AutoPicked Universe
            shortAuto = AutoPicked([MemoryUNORDERED,inputtext])
            longAuto = AutoPicked([memoryLong,inputtext])
            #print("ShortMem",shortAuto)
            #print("LongMem",longAuto)
            autoPickedUniv = shortAuto + longAuto
            print("near field is", autoPickedUniv)

            #eval the return <--- REMEMBER TO EVAL THE RETURN (need:hint: if I have finite functions, hav ea function that takes a finite function and an input then returns what the finite function would say if given that input)
            suppANS = []
            for x in autoPickedUniv:
                suppANSmin = Applyfunc([eval(x),inputtext])
                print("apply test", eval(x), inputtext,suppANSmin)
                suppANS.append(x)
            print("supposed answer",suppANS)
            for x in suppANS:
                try:
                    attempt = eval(x)
                    memoryfile = open(MemoryUNORDERED, 'a+')
                    memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]) + "\n")
                    memoryfile.close()
                except Exception as e:
                    memoryfile = open(MemoryUNORDERED, 'a+')
                    memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]) + "\n")
                    memoryfile.close()
                    pass
            

            #LEXICO IMMEDIATELY BECAUSE I AM STILL TESTING
            #lexicoSort([basisname,memoryLong,MemoryUNORDERED])
                    
            
            
            #pattern recognition:
            #~
            #\cong (property preserved under some X)
            #"use delta < some # " and look in some topo space
            #append basis again

            
            #DELTA ANALYSIS:
            #deltav2 on x in combined memory and new obj
            #print("NOW TO TEST SEEKFORCE",SeekForce(['MemoryUNORDERED.txt','argument_1 == "b"',delta2]))
            MEMcomposeinput = SeekForce([MemoryUNORDERED,inputtext,delta2,[],"get0"]) + SeekForce([memoryLong,inputtext,delta2,[],"get0"])
            #deltav2 on pairs in new obj -> guessing similar inputs/variables (find abstractions) ->#eval using (deltav3 COMPOSE deltav2) and get answers
            #for each object in seekforce, check if new obj or x in seekforce is an abstraction by checking deltav2(obj,x in seekforce) == obj OR deltav2(obj,x in seekforce) == x in seekforce
            #print("checking memcomposeinput",str(MEMcomposeinput).encode('utf-8'))
            print("qhat is argv?",argv)
            #print("checking memcomposeinput",MEMcomposeinput)
            #print("alpha and stout fucking up","α".encode('utf-8'))
            guessAbst = []
            for x in MEMcomposeinput:
                abstractcheck = delta2([inputtext,x])
                
                #print("3",abstractcheck)
                #print("abstractcheck  == inputtext",abstractcheck  == inputtext)
                #print("abstractcheck == x",abstractcheck == x)
                if abstractcheck  == inputtext or abstractcheck == x:
                    print("small steps you fuck",x) #can't encode α for some reason
                    print("small steps you fuck2",inputtext)
                    print("this is guess",abstractcheck)
                    guessAbst.append(abstractcheck)
            print("what am I guessing an abstraction to be?",guessAbst)
            #eval using (deltav3 COMPOSE deltav2) and get answers AND WRITE THOSE DOWN TO memory
        

        
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
