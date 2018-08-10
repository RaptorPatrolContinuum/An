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