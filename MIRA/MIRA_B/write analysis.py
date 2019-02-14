	guessAbst = []
    for x in MEMcomposeinput:
        #print("WTF IS X",x)
        xmod = toString([ran(x),"naive"])
        #print("args fpr thedelta", [inputtextvar,xmod])
        thedelta = delta2([inputtextvar,xmod])
        print("what's thedelta?" + str(datetime.now()),thedelta)
        abstractcheck = toString([ran(thedelta),"naive"])
        test1 = abstractcheck == inputtextvar
        test2 = abstractcheck == xmod
        if test1 or test2:
             if len([y for y in guessAbst if y == thedelta]) == 0:
                guessAbst.append(thedelta)
    print("guessAbst TOTAL",len(guessAbst),guessAbst)
    abstractiondict = {}
    icounter = 0
    abstractioninnertotal = 0
    for x in guessAbst:
        print("x in guessAbst" + str(datetime.now()),x)
        print("x in guessAbst",toString([ran(x),"naive"]))
        minforce1 = SeekForce([MemoryUNORDEREDvar,x,SeekForcemin2,[],[]])
        minforce2 = SeekForce([memoryLongvar,x,SeekForcemin2,[],[]])
        print("minforce1 args",[MemoryUNORDEREDvar,x,SeekForcemin2,[],[]])
        print("minforce1",minforce1)
        print("minforce2",minforce2)
        print("try to seekforce with this and something else")
        print("abstracting RHS once1!",maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]))
        print("abstracting RHS once2!",maxlargestequivclasses([minforce2,maxlargestequivclassesmin1]))
        totalabstractions = maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]) + maxlargestequivclasses([minforce2,maxlargestequivclassesmin1])
        abstractiondict[str(icounter)] = totalabstractions
        icounter += 1
        print("TOTALABSTRACTIONS IS A LIST",totalabstractions)
        abstractioninnertotal += len(totalabstractions)
        #having issue of not counting empties but not being able to skip them so just account for them
        if len(totalabstractions) == 0:
            abstractioninnertotal += 1
    print("double check dict",abstractiondict)
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
    len3int = 0
    with open("ABSTRACTFILE.txt", 'a+', encoding='utf-8') as ABSTRACTFILE:
        for x in range(anothersum*len2):
            print("x in totalabstractions" + str(datetime.now()),x)
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
                cleanup1 = abstractiondict[str(len1int)][len3int]
            with open("ABSTRACTFILE2.txt", 'a+', encoding='utf-8') as ABSTRACTFILE2:
                print("abstractfile had too many duplicate lines")
                stopdupe = str([[guessAbst[len2int],cleanup1]])
                if len(shittySearch(["ABSTRACTFILE2.txt",stopdupe])) == 0:
                    ABSTRACTFILE.write(stopdupe + "\n")
                    ABSTRACTFILE2.write(stopdupe + "\n")
                    print("written")
                else:
                    print("unwritten")
                    pass
                ABSTRACTFILE2.close()
            len3int += 1
    with open(MemoryUNORDEREDvar, 'r+', encoding='utf-8') as ordered1:
        ordered1.seek(0)
        guessint = 0
        thenextline = rchop(ordered1.readline(), '\n')
        print("WTRFFFFF" + str(datetime.now()),mapcountLINES([MemoryUNORDEREDvar])*anothersum*len2)
        print("skipfactor" + str(datetime.now()),anothersum*len2)
        for lineint in range(mapcountLINES([MemoryUNORDEREDvar])*anothersum*len2):

            #if guessint == anothersum*len2:
            if guessint == len2:
                thenextline = rchop(ordered1.readline(), '\n')
                guessint = 0
            
            #print("OK WE ARE COMPARING ",lineint,thenextline)
            #print("AND THIS LINE",functionguessdict[str(guessint)])
            #problem with encoding empty string
            emptycheck = FILEindexread(["ABSTRACTFILE.txt",guessint])
            print("emptycheck stats",guessint,anothersum,len2,mapcountLINES([MemoryUNORDEREDvar])*anothersum*len2)
            print("emptycheckk",emptycheck)
            #if len(emptycheck) > 0:
            #    #print("AND THIS LINE",emptycheck.encode('utf-8').format(u"\u03B1"))
            #    #print("AND THIS LINE",emptycheck.format(u"\u03B1"))
            #    print("AND THIS LINE",emptycheck)
            #else:
            #   print("AND THIS LINE",emptycheck)
            #print("AND THIS LINE",guessint,emptycheck)
            #print("CHECK IS TO TRY delta2 single point condition on both LHS and RHS then if they both pass, write into mem")
            memX = eval(thenextline)[0][0]
            memY = eval(thenextline)[0][1]
            guessX = toString([ran(eval(emptycheck)[0][0]),"naive"])
            guessY = toString([ran(eval(emptycheck)[0][1]),"naive"])
            LHSTest = toString([ran(delta2([memX,guessX])),"naive"]) == guessX
            RHSTest = toString([ran(delta2([memY,guessY])),"naive"]) == guessY
            #print("check types",type(memX),type(guessX))
            #print("LHSpart1",memX,guessX)
            #print("LHS",LHSTest)
            #print("RHSpart1",memY,guessY)
            #print("RHS",RHSTest)
            if LHSTest and RHSTest:
                print("this guy passed" + str(datetime.now()),[[guessX,guessY]])
                #print("thjis is actual",emptycheck)
                #write the right qualifier
                #[[FixedQualifier([delta2,abstraction,testguy]),result]]
                #EXAMPLE-α
                #[["TOTAL_ARGUMENT == 'print('hold the line')'", ['None', '']]]
                #[["FixedQualifier([delta2,'print('α0')',TOTAL_ARGUMENT])",['None', '']],FixedQualifiermin1]
                #test using composemeta
                #hint: f1 compose f2 but do F2 THEN F1!
                #test:
                #ComposeMETA([[["FixedQualifier([delta2,\"print(\'α0\')\",TOTAL_ARGUMENT,FixedQualifiermin1])",['None', '']]],[['noob',"print(\'oof\')"]]])
                #returns
                #[['noob', ['None', '']]]
                #ComposeMETA([[["FixedQualifier([delta2,\"print(\'α0\')\",TOTAL_ARGUMENT,FixedQualifiermin1])",['None', '']]],[['noob',"print(\"oof\")"]]])
                #returns
                #[]
                #what do I write?
                #[["FixedQualifier([delta2,guessX,TOTAL_ARGUMENT,FixedQualifiermin1])",guessY]]
                #time to write to MemoryUNORDEREDvar
                #make sure not to add duplicates
                actualwtf = str([["FixedQualifier([delta2," + "\"" + str(guessX) + "\"" + ",TOTAL_ARGUMENT,FixedQualifiermin1])",guessY]]) + "\n"
                print("actual wtf why",actualwtf)
                if len(shittySearch(['MemoryUNORDERED.txt',actualwtf])) == 0:
                    with open(MemoryUNORDEREDvar,'a+',encoding='utf-8') as theMEMun:
                        print("what is guessX",guessX)
                        
                        #fixedmaybe = strFix([guessX])
                        #next question: strfix( " + guessX + ")
                        #theraw = "%r"%fixedmaybe
                        print("try this:",actualwtf)
                        print("need extra quotes",actualwtf)
                        theMEMun.write(actualwtf)
                #next testing step would be to check with ComposeMeta
            guessint += 1

    
    #open unordered












































===============================================================================
write analysis

            internaltest = [["Popen(['python'," + str(os.getcwd()) + "\\Mira.py, "+inputtext+"], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)",seesANS]]
            #print("shittysearch uses eval have to double check if it fucking works properly1",shittySearch([MemoryUNORDERED,str(internaltest)]),str(internaltest))
            orsequence = bisectionSearch([memoryLong,str(internaltest),basisname]) + shittySearch([MemoryUNORDERED,str(internaltest)])
            if len(orsequence) > 0:
                print("I already saw that!")
            else:
                memoryfile.write(str(internaltest) + "\n")
                nearfield.append(str(internaltest))
				
				
            #just write the OG test once
            internaltest2 = [["TOTAL_ARGUMENT == '"+ str(inputtext) +"'",[str(eval(inputtext)),""]]]
            #print("shittysearch uses eval have to double check if it fucking works properly2",shittySearch([MemoryUNORDERED,str(internaltest2)]),str(internaltest2))
            orsequence2 = bisectionSearch([memoryLong,str(internaltest2),basisname]) + shittySearch([MemoryUNORDERED,str(internaltest2)])
            if len(orsequence2) > 0:
                print("already saw that 2")
            else:
                memoryfile.write(str(internaltest2) + "\n")
                nearfield.append(str(internaltest2))
				
				
				internaltest = [["Popen(['python'," + str(os.getcwd()) + "\\Mira.py, "+inputtext+"], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)",seesANS]]
                #print("shittysearch uses eval have to double check if it fucking works properly3",shittySearch([MemoryUNORDERED,str(internaltest)]),str(internaltest))
                orsequence = bisectionSearch([memoryLong,str(internaltest),basisname]) + shittySearch([MemoryUNORDERED,str(internaltest)])
                if len(orsequence) > 0:
                    print("I already saw that!")
                else:
                    memoryfile.write(str(internaltest) + "\n")
                    nearfield.append(str(internaltest))
            else:
                #just write the OG test once
                internaltest2 = [["TOTAL_ARGUMENT == '"+ str(inputtext) +"'",[str(eval(inputtext)),""]]]
                #print("shittysearch uses eval have to double check if it fucking works properly4",shittySearch([MemoryUNORDERED,str(internaltest2)]),str(internaltest2))
                orsequence2 = bisectionSearch([memoryLong,str(internaltest2),basisname]) + shittySearch([MemoryUNORDERED,str(internaltest2)])
                if len(orsequence2) > 0:
                    print("already saw that 2")
                else:
                    memoryfile.write(str(internaltest2) + "\n")
                    nearfield.append(str(internaltest2))				
					
			memoryfile.write(str([["TOTAL_ARGUMENT == '"+ str(inputtext) +"'", ["",e]]]) + "\n")
			
			
    for x in suppANS:
        try:
            attempt = eval(x)
            memoryfile = open(MemoryUNORDEREDvar, 'a+')
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]) + "\n")
            #nearfield.append(str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]))
            memoryfile.close()
        except Exception as e:
            memoryfile = open(MemoryUNORDEREDvar, 'a+')
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]) + "\n")
            #nearfield.append(str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]))
            memoryfile.close()
            pass

			
	if len(shittySearch(['MemoryUNORDERED.txt',str([["FixedQualifier([delta2,"+guessX+",TOTAL_ARGUMENT,FixedQualifiermin1])",guessY]])])) == 0:
			with open(MemoryUNORDEREDvar,'a+',encoding='utf-8') as theMEMun:
				theMEMun.write(str([["FixedQualifier([delta2,"+guessX+",TOTAL_ARGUMENT,FixedQualifiermin1])",guessY]]) + "\n")