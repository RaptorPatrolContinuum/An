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
            
            #pattern recognition:
            #~
            #\cong (property preserved under some X)
            #"use delta < some # " and look in some topo space
            #append basis again

            
            #DELTA ANALYSIS:
            #deltav2 on x in combined memory and new obj
            #print("NOW TO TEST SEEKFORCE",SeekForce(['MemoryUNORDERED.txt','argument_1 == "b"',delta2]))
            #THIS MEMcomposeinput WAS USED TO ABSTRACT THE INPUT, BUT NOW I WANT TO ABSTRACT THE INPUT OUTPUT PAIR PRODUCED BY MIRA SEEING THE EVAL OF INPUT
            MEMcomposeinput = SeekForce([MemoryUNORDERED,inputtext,delta2,SeekForcemin1,[]]) + SeekForce([memoryLong,inputtext,delta2,SeekForcemin1,[]])
            #deltav2 on pairs in new obj -> guessing similar inputs/variables (find abstractions) ->#eval using (deltav3 COMPOSE deltav2) and get answers
            #for each object in seekforce, check if new obj or x in seekforce is an abstraction by checking deltav2(obj,x in seekforce) == obj OR deltav2(obj,x in seekforce) == x in seekforce
            #print("checking memcomposeinput",str(MEMcomposeinput).encode('utf-8'))
            #print("checking memcomposeinput HINT: before is evaling with what we know, now we guess abstraction",MEMcomposeinput)
            #print("is list?", type(MEMcomposeinput))
            #print("qhat is argv?",argv)
            #print("checking memcomposeinput",MEMcomposeinput)
            #print("alpha and stout fucking up","α".encode('utf-8'))
            guessAbst = []
            for x in MEMcomposeinput:
                #print("WTF IS X",x)
                xmod = toString([ran(x),"naive"])
                #print("args fpr thedelta", [inputtext,xmod])
                thedelta = delta2([inputtext,xmod])
                #print("what's thedelta?",thedelta)
                abstractcheck = toString([ran(thedelta),"naive"])
                #print("what is inputtext?",inputtext)
                #print("BECOME THE ONE YOU LOVE abstractcheck",abstractcheck)
                #print("I'm abusing x as a symbol",xmod)
                #print("abstractcheck  == inputtext",abstractcheck  == inputtext)
                #print("abstractcheck == xmod",abstractcheck == xmod)
                test1 = abstractcheck == inputtext
                test2 = abstractcheck == xmod
                if test1 or test2:
                    #print("small steps you fuck",xmod) #can't encode α for some reason
                    #print("small steps you fuck2",inputtext)
                    #print("this is guess",abstractcheck)
                    #print("args for delta3",[abstractcheck,inputtext])
                    replacementguess = delta3META([abstractcheck,inputtext])
                    #print("guess substitution", replacementguess)
                    #print("composemeta arguments", replacementguess,thedelta)
                    #print("CHECKING EVAL THROUGH COMPOSE FUCK", Compose(replacementguess,thedelta))
                    metaeval = ComposeMETA([replacementguess,thedelta])
                    #print("#1 WTF IS METAEVAL AND #2 WHY IS IT ALWAYS EMPTY",[replacementguess,thedelta])
                    #print("CHECKING EVAL THROUGH COMPOSEMETA", metaeval)
                    #print("checking list comprehension",thedelta)
                    #print("checking list comprehension2",[y for y in guessAbst if y == thedelta])
                    if len([y for y in guessAbst if y == thedelta]) == 0:
                        guessAbst.append(thedelta)
            #print("what am I guessing an abstraction OF INPUT to be?",guessAbst)
            abstractiondict = {}
            icounter = 0
            for x in guessAbst:
                #print("x in guessAbst",x)
                print("x in guessAbst",toString([ran(x),"naive"]))
                minforce1 = SeekForce([MemoryUNORDERED,x,SeekForcemin2,[],[]])
                minforce2 = SeekForce([memoryLong,x,SeekForcemin2,[],[]])
                #print("try to seekforce with this and something else")
                #print(minforce1)
                #print(minforce2)
                #print("abstracting RHS once1!",maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]))
                #print("abstracting RHS once2!",maxlargestequivclasses([minforce2,maxlargestequivclassesmin1]))
                totalabstractions = maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]) + maxlargestequivclasses([minforce2,maxlargestequivclassesmin1])
                abstractiondict[str(icounter)] = totalabstractions
                icounter += 1
                print("no respect wtf",totalabstractions)
                for art in totalabstractions:
                    print("fCheck this shit",art)
                    print("fCheck this shit",fCheck(art))
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
            len2 = len(MEMcomposeinput)
            len2int = 0
            print("check lengths",len1,len2)
            for x in range(len1*len2):
                if len1int == len1:
                    len1int = 0
                if len2int == len2:
                    len2int = 0
                print("x in totalabstractions",x)
                #now we check for fixed point property
                #delta2(abstractoin,otherguy) = abstraction
                #HINT: DO y in totalabstractions VS z in SeekForce union
                #print("source1",abstractiondict)
                print("comparisons1",abstractiondict[str(len1int)])
                print("comparisons1",toString([ran(abstractiondict[str(len1int)]),"naive"]))
                #print("source2",MEMcomposeinput)
                print("comparisons2",MEMcomposeinput[len2int])
                print("comparisons2",toString([ran(MEMcomposeinput[len2int]),"naive"]))
                print("pass or fail",delta2([abstractiondict[str(len1int)],MEMcomposeinput[len2int]]) == abstractiondict[str(len1int)])
                if delta2([abstractiondict[str(len1int)],MEMcomposeinput[len2int]]) == abstractiondict[str(len1int)]:
                    memoryfile = open(MemoryUNORDERED, 'a+')
                    memoryfile.write(str(abstractiondict[str(len1int)]) + "\n")
                    memoryfile.close()
                len1int += 1
                len2int += 1


            
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
