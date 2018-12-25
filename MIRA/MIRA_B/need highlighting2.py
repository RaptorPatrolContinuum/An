ef abstractionGENERAL(argList):
    '''
    intput: ???
        argList = [[MemoryUNORDEREDvar,memoryLongvar],inputtextvar]
    output: ???
    THIS FUNCTION SOLVES THIS PROBLEM:
    
    given:
        general sense function that pairs inputs and outputs
        delta2
        an example
        memoryfiles of finite functions
    
    we want:
        abstraction guess (if any) that is checked with the memory files or sense using delta2 on LHS and RHS
        
    
	
    NEED:
    memfiles as a list
        MemoryUNORDERED var
	memoryLong
    inputtext var
    ABSTRACTFILE
    nearfield
    sense function
    consistency function
        NOTE: usage is for delta checking. so idea is we have delta2 as the consistency function and we compare
        our guesses with consistency

        looks like this:
        guesslist
        for x in guesslist
            compare consistency(x,sense function)

        BUT THIS ONLY WORKS IF OUR SENSE FUNCTION IS LIKE CODE WHERE YOU CAN JUST RUN IT ALL THE TIME, NOT ON RECORDED SENSES WHERE
        YOU HAVE TO COMPOSE ON THE MEMORIZED FUNCTIONS

    EXAMPLE:
    abstractionGENERAL([[MemoryUNORDERED,memoryLong,eval,delta2],eval(x)[0][0]])
    '''
    MemoryUNORDEREDvar = argList[0][0]
    memoryLongvar = argList[0][1]
    inputtextvar = argList[1]
    try:
        inputfunc = argList[0][2]
    except:
        print("INPUT NOT IN ABSTRACTIONGENERAL")
        inputfunc = eval
    try:
        consistencyfunc = argList[0][3]
    except:
        print("CONSISTENCYFUNC NOT IN ABSTRACTIONGENERAL")
        consistencyfunc = delta2
    

    #look for/through AutoPicked Universe
    shortAuto = AutoPicked([MemoryUNORDEREDvar,inputtextvar])
    longAuto = AutoPicked([memoryLongvar,inputtextvar])
    #print("ShortMem",shortAuto)
    #print("LongMem",longAuto)
    autoPickedUniv = shortAuto + longAuto
    #print("near field is", autoPickedUniv)

    #eval the return <--- REMEMBER TO EVAL THE RETURN (need:hint: if I have finite functions, hav ea function that takes a finite function and an input then returns what the finite function would say if given that input)
    suppANS = []
    for x in autoPickedUniv:
        suppANSmin = Applyfunc([inputfunc(x),inputtextvar])
        #print("apply test", eval(x), inputtextvar,suppANSmin)
        suppANS.append(x)
    print("supposed answer",suppANS)
    for x in suppANS:
        try:
            attempt = inputfunc(x)
            memoryfile = open(MemoryUNORDEREDvar, 'a+')
            print('insertionline10',str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]) + "\n")
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]) + "\n")
            #nearfield.append(str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]))
            memoryfile.close()
        except Exception as e:
            memoryfile = open(MemoryUNORDEREDvar, 'a+')
            print('insertionline11',str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]) + "\n")
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]) + "\n")
            #nearfield.append(str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]))
            memoryfile.close()
            pass

    #LEXICO IMMEDIATELY BECAUSE I AM STILL TESTING
    #lexicoSort([basisname,memoryLongvar,MemoryUNORDEREDvar])
    
    #DELTA ANALYSIS:
    #deltav2 on x in combined memory and new obj
    #print("NOW TO TEST SEEKFORCE",SeekForce(['MemoryUNORDEREDvar.txt','argument_1 == "b"',delta2]))
    #THIS MEMcomposeinput WAS USED TO ABSTRACT THE INPUT, BUT NOW I WANT TO ABSTRACT THE INPUT OUTPUT PAIR PRODUCED BY MIRA SEEING THE EVAL OF INPUT
    #print("dogshit2",delta2(["alphaprint('')","betrprint('')"])) #arg3 should be delta2()
    #with open(MemoryUNORDEREDvar,'a+',encoding='utf-8') as theMEMun:
    #    theMEMun.write(str([["THIS IS CULPRIT",""]]) + "\n")
    MEMcomposeinput = SeekForce([MemoryUNORDEREDvar,inputtextvar,consistencyfunc,SeekForcemin1,[]]) + SeekForce([memoryLongvar,inputtextvar,consistencyfunc,SeekForcemin1,[]])
    #with open(MemoryUNORDEREDvar,'a+',encoding='utf-8') as theMEMun:
    #    theMEMun.write(str([["THIS IS CULPRITEND",""]]) + "\n")
    #deltav2 on pairs in new obj -> guessing similar inputs/variables (find abstractions) ->#eval using (deltav3 COMPOSE deltav2) and get answers
    #for each object in seekforce, check if new obj or x in seekforce is an abstraction by checking deltav2(obj,x in seekforce) == obj OR deltav2(obj,x in seekforce) == x in seekforce
    guessAbst = []
    for x in MEMcomposeinput:
        #print("WTF IS X",x)
        xmod = toString([ran(x),"naive"])
        #print("args fpr thedelta", [inputtextvar,xmod])
        thedelta = consistencyfunc([inputtextvar,xmod])
        print("what's thedelta?" + str(datetime.now()),thedelta)
        abstractcheck = toString([ran(thedelta),"naive"])
        test1 = abstractcheck == inputtextvar
        test2 = abstractcheck == xmod
        if test1 or test2:
            #unused stuff
            #replacementguess = delta3META([abstractcheck,inputtextvar])
            #metaeval = ComposeMETA([replacementguess,thedelta])
            if len([y for y in guessAbst if y == thedelta]) == 0:
                guessAbst.append(thedelta)
    #print("COMPART MEMCOMPOSE WITH GUESSABST")
    #print("MEMCOMPOSE",str(MEMcomposeinput).encode('utf-8'))
    #print("MEMCOMPOSE",str(MEMcomposeinput))
    print("guessAbst TOTAL",len(guessAbst),guessAbst)
    #print("what am I guessing an abstraction OF INPUT to be?",guessAbst)
    abstractiondict = {}
    icounter = 0
    #since abstractiondict is a list
    abstractioninnertotal = 0
    for x in guessAbst:
        print("x in guessAbst" + str(datetime.now()),x)
        ##
        print("x in guessAbst",toString([ran(x),"naive"]))
        minforce1 = SeekForce([MemoryUNORDEREDvar,x,SeekForcemin2,[],[]])
        minforce2 = SeekForce([memoryLongvar,x,SeekForcemin2,[],[]])
        print("minforce1 args",[MemoryUNORDEREDvar,x,SeekForcemin2,[],[]])
        print("minforce1",minforce1)
        print("minforce2",minforce2)
        #
        print("try to seekforce with this and something else")
        ##
        print("abstracting RHS once1!",maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]))
        ##
        print("abstracting RHS once2!",maxlargestequivclasses([minforce2,maxlargestequivclassesmin1]))
        totalabstractions = maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]) + maxlargestequivclasses([minforce2,maxlargestequivclassesmin1])
        abstractiondict[str(icounter)] = totalabstractions
        icounter += 1
        #hint: TOTALABSTRACTIONS IS A LIST
        ##
        print("TOTALABSTRACTIONS IS A LIST",totalabstractions)
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
    #print("double check dict",abstractiondict)
    print("do I get past this long bs?"+ str(datetime.now()))
    len1 = len(abstractiondict)
    len1int = 0
    len2 = len(guessAbst)
    len2int = 0
    print("check lengths",len1,len2)
    anothersum = 0
    print("am I stuck here?" + str(datetime.now()))
    for x in range(len1):
        print("electric feel" + str(datetime.now()),len(abstractiondict[str(len1int)]))
        anothersum += len(abstractiondict[str(len1int)])
        if len(abstractiondict[str(len1int)]) == 0:
            anothersum += 1
        len1int += 1
    print("what is anothersum?",anothersum)
    len1int = 0
    len3int = 0)
    with open("ABSTRACTFILE.txt", 'a+', encoding='utf-8') as ABSTRACTFILE:
        for x in range(anothersum*len2):
            #print("x in totalabstractions" + str(datetime.now()),x)
            if (len3int == len(abstractiondict[str(len1int)]) or len(abstractiondict[str(len1int)]) == 0 )and x != 0:
                len3int = 0
                len1int += 1
            if len1int == len1:
                len1int = 0
                len2int += 1
            theguy = abstractiondict[str(len1int)]
            if theguy == []:
                cleanup1 = ""
            else:
                #print("don't tell me cause it hurts",len1int, len3int)
                cleanup1 = abstractiondict[str(len1int)][len3int]
                #print("don't tell me cause it hurts2",cleanup1)
            ##print("need fucking stats",len1int,len2int,len3int)
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

            #hint: write to 2nd file and search through that
            with open("ABSTRACTFILE2.txt", 'a+', encoding='utf-8') as ABSTRACTFILE2:
                #print("abstractfile had too many duplicate lines")
                stopdupe = str([[guessAbst[len2int],cleanup1]])
                #print(stopdupe)
                #print(["ABSTRACTFILE2.txt",stopdupe])
                #print(shittySearch(["ABSTRACTFILE2.txt",stopdupe]))
                #print(len(shittySearch(["ABSTRACTFILE2.txt",stopdupe])) == 0)
                if len(shittySearch(["ABSTRACTFILE2.txt",stopdupe])) == 0:
                    print('insertionline12',stopdupe + "\n")
                    ABSTRACTFILE.write(stopdupe + "\n")
                    ABSTRACTFILE2.write(stopdupe + "\n")
                    #print("written")
                else:
                    #print("unwritten")
                    pass
                ABSTRACTFILE2.close()
            #nearfield.append(str([[guessAbst[len2int],cleanup1]]))
            '''
            if delta2([cleanup1,MEMcomposeinput[len2int]]) == cleanup1:
                memoryfile = open(MemoryUNORDEREDvar, 'a+')
                memoryfile.write(str(cleanup1) + "\n")
                memoryfile.close()
            '''
            len3int += 1


    writeNoDupes = []
    with open(MemoryUNORDEREDvar, 'r+', encoding='utf-8') as ordered1:
        ordered1.seek(0)
        guessint = 0
        thenextline = rchop(ordered1.readline(), '\n')
        #hint: memoryLongvar is only one line fuck
        print("WTRFFFFF" + str(datetime.now()),mapcountLINES([MemoryUNORDEREDvar])*anothersum*len2)
        print("skipfactor" + str(datetime.now()),anothersum*len2)
        for lineint in range(mapcountLINES([MemoryUNORDEREDvar])*anothersum*len2):

            #if guessint == anothersum*len2:
            if guessint == len2:
                thenextline = rchop(ordered1.readline(), '\n')
                guessint = 0

            #special characters destroy the meaning so just do try block and if it fails to []
            try:
                memX = inputfunc(thenextline)[0][0]
            except:
                #print("thenextline failed!X",thenextline)
                memX = []
            #memX = eval(eval(repr(thenextline)))[0][0]
            #
            try:
                memY = inputfunc(thenextline)[0][1]
            except:
                #print("thenextline failed!Y",thenextline)
                memY = []
            #memY = eval(eval(repr(thenextline)))[0][1]
            guessX = toString([ran(inputfunc(emptycheck)[0][0]),"naive"])
            guessY = toString([ran(inputfunc(emptycheck)[0][1]),"naive"])
            LHSTest = toString([ran(consistencyfunc([memX,guessX])),"naive"]) == guessX
            RHSTest = toString([ran(consistencyfunc([memY,guessY])),"naive"]) == guessY

            if LHSTest and RHSTest:
                print("this guy passed" + str(datetime.now()),[[guessX,guessY]])
                possibleDupe = abstractionGENERALmin1([guessX,guessY,MemoryUNORDEREDvar,"STRFIX"])
                dupeList = [y for y in writeNoDupes if y == possibleDupe]
                print("FILTER THIS INSTEAD",possibleDupe)
                print("dupeList",dupeList)
                print("len",len(dupeList))
                if len(dupeList) == 0:
                    writeNoDupes.append(possibleDupe)
                #next testing step would be to check with ComposeMeta
            guessint += 1
    #now I can look through MemoryUNORDEREDvar to check for dupes
    with open(MemoryUNORDEREDvar, 'a+', encoding='utf-8') as ordered1:
        for candidate in writeNoDupes:
            if len(shittySearch([MemoryUNORDEREDvar,candidate])) == 0:
                ordered1.write(candidate + "\n")

    #HERE I DELETE THE ABSTRACT FILE TO CLEANUP
    #FIX THIS| could be causing problems if called repeatedly and not clearing
    #print("STARTHERE")
    with open('ABSTRACTFILE.txt', 'r+', encoding='utf-8') as ordered1:
        ordered1.seek(0)
        for line in range(mapcountLINES(['ABSTRACTFILE.txt'])):
            nextguy = rchop(ordered1.readline(), '\n')
   
    #
    os.remove("ABSTRACTFILE.txt")
    #
    os.remove("ABSTRACTFILE2.txt")
    try:
        os.remove(OtherClone() + "\\" + "ABSTRACTFILE.txt")
        os.remove(OtherClone() + "\\" + "ABSTRACTFILE2.txt")
    except:
        pass
=======================================================================================================================
=======================================================================================================================

def ShittySI(ListItems):
    '''
	ShittySI([[GraphX,GraphY],"Auto" OR "" (which means empty), "all" or EMPTY])
    NOTE: THIS IS BIDIRECTIONAL ACTUALLY!! SO SAYS YES IF E_G SI E_H OR E_H SI E_G!
    input is a list of the form: [[E_G,E_H], "Auto"]
    says if E_G SI to some E_J in E_H
    '''
    E_G = ListItems[0][0]
    E_H = ListItems[0][1]
    try:
        ALLTRIGGER = ListItems[2]
    except:
        ALLTRIGGER = ""
    #if they're exact same they're SI
    if E_G == E_H:
        return [True, "same" ]
    #else:
    if len(E_G) < len(E_H):
        WLOG = E_G
        Larger = E_H
    else:
        WLOG = E_H
        Larger = E_G

    #problem is "all" doesn't have 2nd element as list so have to add preans
    preans = []

    #print("REMEMBER TO ADD ZEROLINKS TO EDGESORTbyLINKS")
    #print("sort by links START")
    #print(WLOG)
    #print(Larger)
    #print(EdgeSortbyLinks(WLOG))
    #print(EdgeSortbyLinks(Larger))
    #print(LinkPoolGen(EdgeSortbyLinks(WLOG),EdgeSortbyLinks(Larger)))
    #print("sort by links END")

    LinkPool = LinkPoolGen(EdgeSortbyLinks(WLOG),EdgeSortbyLinks(Larger))
    
    #add Zerolinks to LinkPoolGen
    #a zeronode is a node that doesn't actually link to anything (just recieves links in the graph)
    #just check LinkPool VS Vertex_(WLOG)
    #print("ran keys",ranDict(LinkPool)) 
    ZeroNodes = [x for x in Vertex_(WLOG) if x not in ranDict(LinkPool)]
    #print("Zeronodes?",ZeroNodes) 
    for x in ZeroNodes:
        if type(x) != str:
            LinkPool[str(x)] = Vertex_(Larger)
        else:
            LinkPool[x] = Vertex_(Larger)
    #print("LinkPool+Zeronodes?",LinkPool)

    #make sure LinkPool lists contain each other when you go down the list
    LinkPoolList = []
    #print("OK LINKPOOL BETTER NOT BE FUCKED",LinkPool)
    for x in LinkPool:
        #print("LPL START======",LinkPoolList)
        #print("what is X START",x)
        if len(LinkPoolList) == 0:
            LinkPoolList.append([x,LinkPool[x]])
            #print("WHEN DOES LPL CHANGE",LinkPoolList)
        else:
            for y in LinkPoolList:
                Linked = False
                #print("stats", LinkPoolList)
                #print("y",y)
                ##"new object length is smaller, you add it to keep connection lengths similar"
                #print("I don't understand <=", len(LinkPool[x]),len(y[1]))
                if len(LinkPool[x]) <= len(y[1]):
                    #print("GOT ADDED ALREADY WTF",LinkPoolList)
                    LinkPoolList = InsertAt(LinkPoolList,[x,LinkPool[x]],LinkPoolList.index(y)) 
                    #print("LPL Insert",LinkPoolList)
                    Linked = True
                    break
                #append at end if largest
                if Linked == False:
                    LinkPoolList = LinkPoolList + [[x,LinkPool[x]]]
                    #print("WHEN DOES LPL CHANGE2",LinkPoolList)
                    break
        #print("LPL END=======",LinkPoolList)
    #print("check LinkPoolList",LinkPoolList)

    LinkSize = []
    LinkList = []
    #LinkSize is the size of each list in LinkPool
    #need to subtract 1 each time we append to LinkSize because we are making a choice and excluding them from the rest
    #LinkPool is the corresponding list at the right index
    i = 0
    for x in LinkPoolList:
        LinkSize.append(len(x[1])-i)
        i += 1
        LinkList.append(x[1])
    #print("check linksize",LinkSize)
    #print("check linklist",LinkList)

    #print("DOUBLE CHECK LINKPOOL START")
    #print("smaller", WLOG)
    #print("larger", Larger)
    #print(LinkPool)
    #print("DOUBLE CHECK LINKPOOL END")

    AutoCheck = IsAuto(WLOG) and IsAuto(Larger)
    #print("what is LinkPoolList?",LinkPoolList)
    
    NumberIndex = []
    ANS = []
    #print('FUCK I DONT KNOW WHAT IM DOING TO THIS CODE')
    fuckingskip = False
    for G in LinkSize:
        if len(NumberIndex) > 0:
            NumberNew = []
            for H in range(0,G):
                for J in NumberIndex:
                    Appendage = J + [H]
                    NumberNew.append(Appendage)
                    if len(Appendage) == len(LinkPool):
                        Indexer = []
                        #Phiconstruct needs Indsx ran: [node,elem]
                        i = 0
                        for K in Appendage:
                            Indexer.append([LinkPoolList[i][0],Appendage[i]])
                            i += 1
                        #print("WTF WHY IS ANS TRUE",ANS)
                        #print("here we test SI iwth",Appendage)
                        #print("Indexer is", Indexer)
                        #print("PhiConstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                        #If |V_H| > |V_G|, then construct H* to use instead:
                        if len(Vertex_(Larger)) > len(Vertex_(WLOG)):
                            #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                            HStar = []
                            print("whats larger=======================",Larger)
                            for L in Larger:
                                print("what;s L",L)
                                passA = True
                                passB = True
                                print("Minv and phiconstruct",Minv_(Beta_(WLOG)))
                                print("phicosntruct",PhiConstruct(Indexer,LinkPool,False))
                                print("what failsA",Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)))
                                print("what failsA2",L[0])
                                print("what failsA3",RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0]))
                                print("what failsA4",len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])))
                                print("what fails2",Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)))
                                print("what fails2",L[1])
                                print("what fails2",RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1]))
                                print("what fails2",len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])))
                                if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                    passA = False
                                if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                    passB = False
                                if passA == True and passB == True:
                                    HStar.append(L)
                            #this is failing
                            #ShittySI([[[['A', 'D'], ['D', 'A']], [['A', 'D'], ['B', 'D'], ['D', 'B']]], '', 'all'])
                            #ShittySI([[[['Z', 'Y'], ['Y', 'Z']], [['A', 'D'], ['B', 'D'], ['D', 'B']]], '', 'all'])
                            #
                            print("ok check out H*!",HStar)
                        else:
                            HStar = Larger

                        tryit = True
                        try: 
                            ListItems[1]
                        except IndexError:
                            tryit = False
                        if tryit == True:
                            if ListItems[1] == "Auto":
                                Vertex_Max = '0'
                                #print("vertexmax lolwut",Vertex_(WLOG) + Vertex_(Larger))
                                for NUM in Vertex_(WLOG) + Vertex_(Larger):
                                    if int(NUM) > int(Vertex_Max):
                                        Vertex_Max = str(NUM)
                                #print("WTF WHY IS ANS TRUE2",ANS)
                                #print("V_G",Vertex_(WLOG))
                                #print("V_H",Vertex_(Larger))
                                #print("TheMax",Vertex_Max)
                                #print("parts for AD1",WLOG)
                                #print("Larger",Larger)
                                #print("Indexer",Indexer)
                                #print("LinkPool",LinkPool)
                                #print("PhiConstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                                #print("need to pick right max",rchiINT(Vertex_Max))
                                #print("basis",Minv_(rchiINT(Vertex_Max)))
                                #print("compose",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))

                                if len(Vertex_(Larger)) >= len(Vertex_(WLOG)):
                                    #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                                    HStar = []
                                    for L in Larger:
                                        passA = True
                                        passB = True
                                        if len(RelEval(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                            passA = False
                                        if len(RelEval(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                            passB = False
                                        if passA == True and passB == True:
                                            HStar.append(L)
                                    print("ok check out H*!",HStar)
                                else:
                                    HStar = Larger
                                #print("DATA =======")
                                #print("smaller", WLOG)
                                #print("Larger", Larger)
                                #print("Vertex_Max",Vertex_Max)
                                #print("rchiINT",rchiINT(Vertex_Max))
                                #print("Minv_",Minv_(rchiINT(Vertex_Max)))
                                #print("Indexer IS THE PROBLEM",Indexer)
                                #print("LinkPool",LinkPool)
                                #print("AutoCheck",AutoCheck)
                                #print("phi",PhiConstruct(Indexer,LinkPool,AutoCheck))
                                #print("Compose",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))
                                #print("DATA END =-=========")
                                #print("=======died at 100MB", Minv_(rchiINT(Vertex_Max)))
                                #print("more stats", PhiConstruct(Indexer,LinkPool,AutoCheck))
                                #print("ok?",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))

                                AD1 = AddressFunc(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                                AD2 = AddressFunc(Minv_(rchiINT(Vertex_Max)),HStar)
                                #print("stats")
                                #print(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                                #print(Minv_(rchiINT(Vertex_Max)),HStar)
                                #print("AD checks prior",AD1,AD2)
                                #print("======= DIED END")
                                #print("WTF WHY IS ANS TRUE3",ANS)
                            else:
                                #
                                print("WTF WHY IS ANS TRUE4",ANS)
                                #
                                print("WLOG",WLOG)
                                #
                                print("bad boy down",Minv_(Beta_(WLOG)))
                                #
                                print("red velvet bad boy",Indexer)
                                #
                                print("red velvet bad boy2",LinkPool)
                                #
                                print("red velvet bad boy3",AutoCheck)
                                #
                                print("bb4",PhiConstruct(Indexer,LinkPool,AutoCheck))
                                ##problem is Minv_
                                ##problem is in phiconstruct or Minv_ on LIST
                                ##problem is probably in compose and quotes on that triple length thing
                                #
                                print("F U C K1",Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)))
                                #
                                print("F U C K2",HStar)
                                #
                                print("F U C K3 args",Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                                #
                                print("F U C K3",AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar))
                                ######AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                                #time to check SI:
                                AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                                AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                        else:
                            #time to check SI:
                            '''
                            empty HStar fix
                            '''
                            if HStar == []:
                                fuckingskip = True
                            else:
                                AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                                AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                        #print("WTF WHY IS ANS TRUE5",ANS)
                        #print("ADchecks",AD1,AD2)
                        #print("tobin AD1","{0:b}".format(AD1)[::-1])
                        #print("tobin AD2","{0:b}".format(AD2)[::-1])
                        #print("LessthanC",LessThan_C(AD1,AD2))
                        #print("len(ALLTRIGGER) == 0",len(ALLTRIGGER) == 0)

                        #I'm just going to do a fast fix: if HStar is empty then set fuckingskip to true
                        if HStar == []:
                            fuckingskip = True

                        if fuckingskip == True:
                            fuckingskip = False
                        elif LessThan_C(AD1,AD2) and len(ALLTRIGGER) == 0:
                            #print("where to look2")
                            return [True,PhiConstruct(Indexer,LinkPool,AutoCheck)]
                        elif len(ANS) > 0:
                            #ANS.append(PhiConstruct(Indexer,LinkPool,AutoCheck))
                            preans.append(PhiConstruct(Indexer,LinkPool,AutoCheck))
                        elif LessThan_C(AD1,AD2):
                            ANS.append(True)
                            #ANS.append(PhiConstruct(Indexer,LinkPool,AutoCheck))
                            preans = [PhiConstruct(Indexer,LinkPool,AutoCheck)]
                        #print("WTF IS ANS1",ANS)
            NumberIndex = NumberNew
        else:
            for H in range(0,G):
                NumberIndex.append([H])
                if len(LinkList) == 1:
                    #print("should test tiny SI with",NumberIndex)
                    Indexer = []
                    #Phiconstruct needs Indsx ran: [node,elem]
                    i = 0
                    for K in range(0,len(LinkList)):
                        Indexer.append([LinkPoolList[i][0],H])
                        i += 1
                    #print("Indexer is ", Indexer)
                    #print("Phiconstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                    #this isn't working on Auto either:
                    #ShittySI([[[['dot', 'dot']],[['triaX', 'triaY'], ['triaY', 'triaZ'], ['triaZ', 'triaX']]]])
                    #example that works
                    #ShittySI([[[['B', 'B']],[['A', 'A'], ['C', 'C']]]])
                    #If |V_H| > |V_G|, then construct H* to use instead:
                    if len(Vertex_(Larger)) > len(Vertex_(WLOG)):
                        #H* is the list of pairs in E_H s.t. indexer \circ phi doesn't fail:
                        HStar = []
                        for L in Larger:
                            passA = True
                            passB = True
                            #both not true means HStar isn't being appended to
                            #ShittySI([[[['dot', 'dot']],[['triaX', 'triaY'], ['triaY', 'triaZ'], ['triaZ', 'triaX']]]])
                            #ShittySI([[[['1', '1']],[['2', '3'], ['3', '4'], ['4', '2']]], "Auto"])
                            #print("L",L)
                            #print("COMPOSE LHS",Minv_(Beta_(WLOG)))
                            #print("INDEXER",Indexer)
                            #print("phiconstruct",PhiConstruct(Indexer,LinkPool,False))
                            #print("compose",Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)))
                            #print("L[0]",L[0])
                            #print("releval",RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0]))
                            #print("L[1]",L[1])
                            #print("releval",RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1]))
                            #print(len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])))
                            #print(len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])))
                            if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[0])) == 0:
                                passA = False
                            if len(RelEval(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,False)),L[1])) == 0:
                                passB = False
                            
                            if passA == True and passB == True:
                                HStar.append(L)
                        #print("ok check out H*!",HStar)
                    else:
                        HStar = Larger
                    tryit = True
                    try: 
                        ListItems[1]
                    except IndexError:
                        tryit = False
                    if tryit == True:
                        if ListItems[1] == "Auto":
                            Vertex_Max = '0'
                            for NUM in Vertex_(WLOG) + Vertex_(Larger):
                                if int(NUM) > int(Vertex_Max):
                                    Vertex_Max = str(NUM)
                            #print("parts for AD1",WLOG)
                            #print("Larger",Larger)
                            #print("Indexer",Indexer)
                            #print("LinkPool",LinkPool)
                            #print("PhiConstruct",PhiConstruct(Indexer,LinkPool,AutoCheck))
                            #print("basis",Minv_(rchiINT(Vertex_Max)))
                            #print("compose",Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)))
                            AD1 = AddressFunc(Compose(Minv_(rchiINT(Vertex_Max)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                            AD2 = AddressFunc(Minv_(rchiINT(Vertex_Max)),HStar)
                        else:
                            #time to check SI:
                            AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                            AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar)
                    else:
                        #time to check SI:
                        '''
                        question: address is failing because H* is empty set [], meaning that you have to take the cantor pair of a null coord for one of the pair coords,
                        my solution:
                        just intercept the error here and go to next check
                        problem: MAKE SURE NOT TO BREAK AND TO ACTUALLY GO TO NEXT INDEX TO CHECK IT
                        '''
                        #print("what is HStar",HStar)
                        if HStar == []:
                            fuckingskip = True
                        else:
                            AD1 = AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG)
                            AD2 = AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar) 
                    #print("ADchecks",AD1,AD2)
                    #print("tobin AD1","{0:b}".format(AD1)[::-1])
                    #print("tobin AD2","{0:b}".format(AD2)[::-1])
                    #print("LessthanC",LessThan_C(AD1,AD2))

                    #I'm just going to do a fast fix: if HStar is empty then set fuckingskip to true
                    if HStar == []:
                        fuckingskip = True

                    if fuckingskip == True:
                        fuckingskip = False
                    elif LessThan_C(AD1,AD2) and len(ALLTRIGGER) == 0:
                        #print("where to look3")
                        return [True,PhiConstruct(Indexer,LinkPool,AutoCheck)]
                    elif len(ANS) > 0:
                        #ANS.append(PhiConstruct(Indexer,LinkPool,AutoCheck))
                        preans.append(PhiConstruct(Indexer,LinkPool,AutoCheck))
                    elif LessThan_C(AD1,AD2):
                        #print("do this by hand tomorrow",Indexer)
                        #print("HStar not empty means WTF IS GOIGN ON",HStar)
                        #print("what is fucking skip -> means I didn't catch all the flow",fuckingskip)
                        #print("INDEX",Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)))
                        #print("OBJ",WLOG)
                        #print("AD1",AddressFunc(Compose(Minv_(Beta_(HStar)),PhiConstruct(Indexer,LinkPool,AutoCheck)),WLOG))
                        #print("INDEX2",Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)))
                        #print("OBJ2",HStar)
                        #print("AD2",AddressFunc(Compose(Minv_(Beta_(WLOG)),PhiConstruct(Indexer,LinkPool,AutoCheck)),HStar) )
                        #print("more stats",LessThan_C(AD1,AD2))
                        ANS.append(True)
                        #ANS.append(PhiConstruct(Indexer,LinkPool,AutoCheck))
                        preans = [PhiConstruct(Indexer,LinkPool,AutoCheck)]
                    #print("WTF IS ANS2",ANS)
    if len(ANS) > 0:
        #print("where to look4")
        return ANS + [preans]
    return ["Assume False"]