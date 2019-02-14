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