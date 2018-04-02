#!/usr/bin/env python
import sys
sys.path.insert(0, 'C:\An\MIRA')


from MiraExternals import *

'''
HUGE CAVEAT:
THE INPUT MUST BE NONEMPTY BECAUSE ShittySI(AutoVision(0,1),AutoVision(0,1))] on empty graph [] doesn't work. but we know that [] is SI to [] so watch out



idea:
Use the compression theorem to know that it's more important to know the SI of object where the basis is large and "L = 1"
then the idea is that for idle time we do:
SI(Vision(x),Vision(y)) as x,y go to infinity
then when we start appending things to the basis we already know what things are isom


problems:
what is the data format?
try:
[[x,y],[yes/no]] as an entry

how to start from where you left off?
then assume that we add each info sequentially,
Look at the "final entry": FE
then FE[0][0] is X and FE[0][1] is Y
then we continue:

problem: 
this function takes a long time


idea:
just run every hour x


'''




while True:
    theFilename = "SIData.txt"
    SIData = open(theFilename,"r+")
    if len(SIData.read()) == 0:
        #tester = AutoVisionString(0,1)
        #print("check what vision shows",tester)
        #print("check stats", ShittySI(tester,tester))
        #SIData.write(str([[[tester,tester],ShittySI(tester,tester)]]))
        Start = CantorInvSTR(0)
        #print("this is start!",Start)
        GraphX = AutoVisionString(int(Start[0]),1)
        GraphY = AutoVisionString(int(Start[1]),1)
        #print("check graphs!",GraphX,GraphY)
        #print("check shitty SI",ShittySI([[GraphX,GraphY],"Auto"]))
        SIData.write(str([[GraphX,GraphY],ShittySI([[GraphX,GraphY],"Auto"])])+"\n")
    else:
        #get the last item from SIData
        SIData.seek(0)
        ###print("Check Out SI Data!", SIData.read()) HINT: seek again if I enable this
        ###SIData.seek(0)
        
        #print("WTF MALFORMED1?????", tail(SIData,1,0))
        #print("WTF MALFORMED?????",ast.literal_eval(tail(SIData,1,0)[0]))
        #new tail func, next line is tailOld
        #last = [ast.literal_eval(tail(SIData,1,0)[0])]
        #last = [ast.literal_eval(tailOpened([SIData,1])[0])]
        
        #close sidata
        SIData.close()
        #get max lines
        maxlinenumber = mapcountLINES([testfile])
        #read last line
        last = FILEindexread([theFilename,maxlinenumber])
        #open sidata
        SIData = open(theFilename,"r+")
        
        #print("what is last?",last)
        SIData.seek(0)
        ######print("what about this", ast.literal_eval(tail(SIData,1,0))[-1][0][0])
        #print("what to literal eval", [ast.literal_eval(tail(SIData,1,0)[0])][-1][0][0])
        ##print("trendy trendy trendy", ast.literal_eval(tail(SIData,1,0))[-1][0][0])


        '''
        26 make constructPNXN faster by making a "ram" file and append to original file 50MB at a time

        hints:
        SIDATA
        SIDATAsmol
 
        #PROBLEM: SIDATA IS WHAT THIS FILE WRITES TO
        #HINT:
        #SIDATA IS "small" file and write to LARGER FILE!
        #HINT: this naming scheme is fucked/reversed
        HINT:
        WRITING FROM SIDATA TO --> SIDatamax

        PROBLEMS:
        double lines from old SI
        some files don't end with newline
        HINTS:
        since I pick up where I last left off I shouldn't have duplicate lines
        if I end lines with \n there shouldn't be a problem
        '''

        SImaxname = "SIDatamax.txt"
        SIData.close()
        #if small file is >10MB:
        if os.path.getsize(theFilename) > 10000000:
            #print("WORKS")
            #break
            #append to OG file
            #get max lines of SIData
            ramfilemaxlines = mapcountLINES([theFilename])
            with open(theFilename,'r+') as SIDatamin:
                #open SImaxname in append mode
                with open(SImaxname,'a+') as SIDataAppend:
                    SIDatamin.seek(0)
                    for x in range(0,ramfilemaxlines+1):
                        #readline from ramfile
                        newread = SIDatamin.readline()
                        #append that line to OG file
                        SIDataAppend.write(newread)
            #what about SIDATAMIN not closing?
            #one of the old python idle windows was accessing the file for some reason
            #SIDatamin,close()
            #delete min file
            os.remove(theFilename)
            #make new minfile/open SIData
            SIData = open(theFilename,"a+")
            #go to beginning
            SIData.seek(0)
            #fucking tail function is fucked
            SImaxnameopen = open(SImaxname,'r+')
            #get last entry on max file
            #this is old tail func
            #last = [ast.literal_eval(tail(SImaxnameopen,1,0)[0])]
            last = [ast.literal_eval(tailOpened([SImaxnameopen,1])[0])]
            #try:
            #    last = [ast.literal_eval(tailOpened([SImaxnameopen,1])[0])]
            #except Exception as e:
            #    print("WTF IS GOING ON")
            #    print(e)
            #    break
            SImaxnameopen.close()
            #continue from there
            #print("stop here!")
            #break
        #reset SIData in case if statement doesn't trigger
        SIData = open(theFilename,"r+")
        #seek to beginning
        SIData.seek(0)
    
        #print("check address of []",AddressFunc(Minv_(Beta_([])),[]))
        #print("Address on [] fails so what about vision on 0?", AutoVision(0,1))
        #print("What is last?",last)
        #figure out what the last x/y as graphs are
        xGraph = last[-1][0][0]
        #print("what is xGraph?",xGraph)
        yGraph = last[-1][0][1]
        #print("what is yGraph?",yGraph)
    
        #PROBLEM: using beta might be bad because if you mess with the basis then you get a diff address (AKA we might write/read things the wrong way and skip something)
        #I just looked at Beta_ and saw for x in E_G so if we write E_G properly we get Basis_ properly (hoping >.<)
        xAddress = AutoAddressFunc(xGraph)
        yAddress = AutoAddressFunc(yGraph)
        #print(xAddress)
        #print(yAddress)
        #pick new target integer T such that T = max(x,y) + 1
        #problem is when this gets huge solving SI up to  SI(R_T,R_T) gets astronomically impossible
        #continue on
    
        WorkOn = CantorPair(xAddress,yAddress)
        #print("what is WorkON?",WorkOn)
        NewSI = CantorInvSTR(WorkOn + 1)
        #print("what is NEWSI? NOTE: EACH COORD IS THE ADDRESS OF A GRAPH",NewSI)
        #print("check SI parts",NewSI[0],NewSI[1])
        AddressX = AutoVisionString(int(NewSI[0]),1)
        AddressY = AutoVisionString(int(NewSI[1]),1)
        #print("Address X",AddressX)
        #print("Address Y",AddressY)
        #print("do their addresses match",AddressFunc(Minv_(Beta_(AddressX)),AddressX))
        #print("do their addresses match",AddressFunc(Minv_(Beta_(AddressY)),AddressY))
        #print("what will future say for WorkON?",CantorPair(AddressFunc(Minv_(Beta_(AddressX)),AddressX),AddressFunc(Minv_(Beta_(AddressY)),AddressY)))
        #print("what will future say for WorkON?",CantorPair(AutoAddressFunc(AddressX),AutoAddressFunc(AddressY)))
        print("Address X",AddressX)
        print("Address Y",AddressY)
        #print("uh checking if SI works on empty set",ShittySI([[AddressX,AddressY], "Auto"]))
        #print("newtest",ShittySI([[[['1', '0'], ['0', '1'], ['2', '0'], ['3', '0'], ['4', '0']],[['0', '1'], ['2', '0'], ['3', '0']]],"Auto"]))
        '''        
        #STILL WORKING ON SHITTYSI
        last.append([[AddressX,AddressY],ShittySI([[AddressX,AddressY],"Auto"])])


        T = max(xAddress,yAddress) + 3 
        for x in range(xAddress,T):
            for y in range(yAddress,T):
	        print("==========================================================")
	        print("stats", "startx" ,xAddress, "starty", yAddress, "t", T)
	        print("currentx",x,"currenty",y)
	        NewXGraph = AutoVisionString(x,1)
                NewYGraph = AutoVisionString(y,1)
	        print("NewXGraph",NewXGraph)
	        print("NewYGraph",NewYGraph)
	        print("check for y/n",ShittySI(NewXGraph,NewYGraph))
	        last.append([[NewXGraph,NewYGraph],ShittySI(NewXGraph,NewYGraph)])
        '''
        #duh I forgot that you should just write to file last
        #FOR SOME FUCKING REASON I MESSED UP A SIMPLE LENGTH CHECK
        #print("CHECKING AUTO SI YET AGAIN",AutoShittySI([['0', '0'], ['1', '0']], [['0', '0'], ['1', '0'], ['0', '1']]))
        #print("CHECKING AUTO SI YET AGAIN",AutoShittySI([['0', '0']], [['0', '0'], ['1', '0']]))
        #print("CHECKING AUTO SI but with replacements so no # spam",ShittySI([['A', 'A'], ['A','C']], [['A', 'A'], ['B', 'A'], ['A','C']]))

        #SIData.seek(0)
        #SIData.write(str(last))
        SIData.close()
        SIData = open(theFilename,"a")
        SIData.write(str([[AddressX,AddressY],ShittySI([[AddressX,AddressY],"Auto"])])+"\n")
        
#then remember to seek the cursor to the beginning
#also close the file	
'''
facts:
[0,0]
[0,1]
0 "can only" map to 1
but the indexer composed with 0 then fails

is it enough to say that the requirement for the indexer composed failing means SI fails totally/altogether?
'''
