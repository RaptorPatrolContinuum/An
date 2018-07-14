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
            else:
                #just write the OG test once
                internaltest2 = [["TOTAL_ARGUMENT == '"+ str(inputtext) +"'",[str(eval(inputtext)),""]]]
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

        #guessing abstractions
        #need to stop clone mira from duplicating responses:
        if Descent == True:
            #look for/through AutoPicked Universe
            shortAuto = AutoPicked([MemoryUNORDERED,inputtext])
            longAuto = AutoPicked([memoryLong,inputtext])
            #print("ShortMem",shortAuto)
            #print("LongMem",longAuto)
            autoPickedUniv = shortAuto + longAuto
            #print("near field is", autoPickedUniv)

            #eval the return <--- REMEMBER TO EVAL THE RETURN (need:hint: if I have finite functions, hav ea function that takes a finite function and an input then returns what the finite function would say if given that input)
            suppANS = []
            for x in autoPickedUniv:
                suppANSmin = Applyfunc([eval(x),inputtext])
                #print("apply test", eval(x), inputtext,suppANSmin)
                suppANS.append(x)
            #print("supposed answer",suppANS)
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
            
            #DELTA ANALYSIS:
            #deltav2 on x in combined memory and new obj
            #print("NOW TO TEST SEEKFORCE",SeekForce(['MemoryUNORDERED.txt','argument_1 == "b"',delta2]))
            #THIS MEMcomposeinput WAS USED TO ABSTRACT THE INPUT, BUT NOW I WANT TO ABSTRACT THE INPUT OUTPUT PAIR PRODUCED BY MIRA SEEING THE EVAL OF INPUT
            MEMcomposeinput = SeekForce([MemoryUNORDERED,inputtext,delta2,SeekForcemin1,[]]) + SeekForce([memoryLong,inputtext,delta2,SeekForcemin1,[]])
            #deltav2 on pairs in new obj -> guessing similar inputs/variables (find abstractions) ->#eval using (deltav3 COMPOSE deltav2) and get answers
            #for each object in seekforce, check if new obj or x in seekforce is an abstraction by checking deltav2(obj,x in seekforce) == obj OR deltav2(obj,x in seekforce) == x in seekforce
            guessAbst = []
            for x in MEMcomposeinput:
                #print("WTF IS X",x)
                xmod = toString([ran(x),"naive"])
                #print("args fpr thedelta", [inputtext,xmod])
                thedelta = delta2([inputtext,xmod])
                #print("what's thedelta?",thedelta)
                abstractcheck = toString([ran(thedelta),"naive"])
                test1 = abstractcheck == inputtext
                test2 = abstractcheck == xmod
                if test1 or test2:
                    #unused stuff
                    #replacementguess = delta3META([abstractcheck,inputtext])
                    #metaeval = ComposeMETA([replacementguess,thedelta])
                    if len([y for y in guessAbst if y == thedelta]) == 0:
                        guessAbst.append(thedelta)
            print("COMPART MEMCOMPOSE WITH GUESSABST")
            print("MEMCOMPOSE",MEMcomposeinput)
            print("guessAbst",guessAbst)
            #print("what am I guessing an abstraction OF INPUT to be?",guessAbst)
            abstractiondict = {}
            icounter = 0
            #since abstractiondict is a list
            abstractioninnertotal = 0
            for x in guessAbst:
                #print("x in guessAbst",x)
                print("x in guessAbst",toString([ran(x),"naive"]))
                minforce1 = SeekForce([MemoryUNORDERED,x,SeekForcemin2,[],[]])
                minforce2 = SeekForce([memoryLong,x,SeekForcemin2,[],[]])
                #print("try to seekforce with this and something else")
                print("abstracting RHS once1!",maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]))
                print("abstracting RHS once2!",maxlargestequivclasses([minforce2,maxlargestequivclassesmin1]))
                totalabstractions = maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]) + maxlargestequivclasses([minforce2,maxlargestequivclassesmin1])
                abstractiondict[str(icounter)] = totalabstractions
                icounter += 1
                #hint: TOTALABSTRACTIONS IS A LIST
                print("who cares dude",totalabstractions)
                abstractioninnertotal += len(totalabstractions)
                #having issue of not counting empties but not being able to skip them so just account for them
                if len(totalabstractions) == 0:
                    abstractioninnertotal += 1
                #for art in totalabstractions:
                #    print("fCheck this shit",art)
                #    print("fCheck this shit",fCheck(art))
            '''
            plan:
            >check if we know the answer already (whether with compose or composeMETA)
            >else check with sense and CONFIRM or DENY expectations
            >confirm, skip
            >deny -> MEMORIZE AND ADD TO MEMORY
            = might be the other way around? ^^^
            >confirm, -> MEMORIZE AND ADD TO MEMORY
            >deny, skip
            DONE
            '''
            #new plan:
            #for each abstraction, collect the answers
            #then delta2 on all the answers
            #then SI on delta2(inputs) and delta2(outputs)
            #MEMcomposeinput
            print("double check dict",abstractiondict)
            len1 = len(abstractiondict)
            len1int = 0
            len2 = len(guessAbst)
            len2int = 0
            print("check lengths",len1,len2)
            anothersum = 0
            for x in range(len1):
                #print("electric feel",len(abstractiondict[str(len1int)]))
                anothersum += len(abstractiondict[str(len1int)])
                if len(abstractiondict[str(len1int)]) == 0:
                    anothersum += 1
                len1int += 1
            print("what is anothersum?",anothersum)
            len1int = 0
            len3int = 0
            functionguessdict = {}
            print("totalcheck",anothersum*len2)
            for x in range(len(abstractiondict)):
                print(abstractiondict[str(x)])
                print(len(abstractiondict[str(x)]))
            for x in range(anothersum*len2):
                print("x in totalabstractions",x)
                if len3int == len(abstractiondict[str(len1int)]) or len(abstractiondict[str(len1int)]) == 0:
                    len3int = 0
                    len1int += 1
                if len1int == len1:
                    len1int = 0
                    len2int += 1
                theguy = abstractiondict[str(len1int)]
                print('the guy is empty',theguy)
                print("length of this guy",len(theguy))
                if theguy == []:
                    cleanup1 = ""
                else:
                    print("don't tell me cause it hurts",len1int, len3int)
                    cleanup1 = abstractiondict[str(len1int)][len3int]
                    print("don't tell me cause it hurts2",cleanup1)
                print("need fucking stats",len1int,len2int,len3int)
                #now we check for fixed point property
                #delta2(abstractoin,otherguy) = abstraction
                #HINT: DO y in totalabstractions VS z in SeekForce union
                #print("source1",abstractiondict)

                '''
                problem
                #1: i want to open memory as minimally as possible
                #2: i don't want to commit the memory file to memory tho
                '''
                #HINT: 3 things to do
                #hint2: COMPARE USING DELTAV2 AND FIXED POINT PROPERTY -> IMPLYING THAT OBJECT IS ABSTRACTION
                #1- compare with memory
                #match reality
                #2- compare with MIRA
                #3- compare with blank python
                
                print("ABSTRACTION FUCNTION GUESS WITH ABSTRACTED LHS AND RHS")
                print("ABSTRACTION GUESS:",[[guessAbst[len2int],cleanup1]])
                functionguessdict[str(x)] = [[guessAbst[len2int],cleanup1]]
                '''
                if delta2([cleanup1,MEMcomposeinput[len2int]]) == cleanup1:
                    memoryfile = open(MemoryUNORDERED, 'a+')
                    memoryfile.write(str(cleanup1) + "\n")
                    memoryfile.close()
                '''
                len3int += 1
            print("what does functionguessdict look like",functionguessdict)
            #problem: nested for loops are garbage
            #answer: have to commit all the function guesses to a list then just open memory total (unordered + ordered) and then use fixed point property + deltav2
            #open ordered

            #with open(memoryLong, 'r+') as ordered1:
            #    guessint = 0
            #    print("WTRFFFFF",mapcountLINES([memoryLong])*anothersum*len2)
            #    for line in range(mapcountLINES([memoryLong])*anothersum*len2):
            #        thenextline = rchop(ordered1.readline(), '\n')
            #        if guessint == anothersum*len2:
            #            guessint = 0
            #        print("OK WE ARE COMPARING ",thenextline)
            #        print("AND THIS LINE",functionguessdict[str(guessint)])
            #        guessint += 1
                
            
            #open unordered
        
            
            #eval using (deltav3 COMPOSE deltav2) and get answers AND WRITE THOSE DOWN TO memory
            #ComposeMETA([arg1,arg2])
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
