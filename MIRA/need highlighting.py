args for composereplace ['FixedQualifier([delta2,"print(\'α0\')",TOTAL_ARGUMENT,FixedQualifiermin1])', ['None', 'drastic ways']]
args for composereplacey ['noob', "print('oof')"] 

ComposeReplace(['FixedQualifier([delta2,"print(\'α0\')",TOTAL_ARGUMENT,FixedQualifiermin1])', ['None', 'drastic ways']],['noob', "print('oof')"])

>>> ComposeReplace(['FixedQualifier([delta2,"print(\'α0\')",TOTAL_ARGUMENT,FixedQualifiermin1])', ['None', 'drastic ways']],['noob', "print('oof')"])
[['noob', ['None', 'drastic ways']]]

def abstractionGENERAL(argList):

    MemoryUNORDEREDvar = argList[0][0]
    memoryLongvar = argList[0][1]
    inputtextvar = argList[1]

    #look for/through AutoPicked Universe
    shortAuto = AutoPicked([MemoryUNORDEREDvar,inputtextvar])
    longAuto = AutoPicked([memoryLongvar,inputtextvar])
    autoPickedUniv = shortAuto + longAuto

    #eval the return <--- REMEMBER TO EVAL THE RETURN (need:hint: if I have finite functions, hav ea function that takes a finite function and an input then returns what the finite function would say if given that input)
    suppANS = []
    for x in autoPickedUniv:
        suppANSmin = Applyfunc([eval(x),inputtextvar])
        suppANS.append(x)
    print("supposed answer",suppANS)
    for x in suppANS:
        try:
            attempt = eval(x)
            memoryfile = open(MemoryUNORDEREDvar, 'a+')
            print('insertionline10',str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]) + "\n")
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", attempt]]) + "\n")
            memoryfile.close()
        except Exception as e:
            memoryfile = open(MemoryUNORDEREDvar, 'a+')
            print('insertionline11',str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]) + "\n")
            memoryfile.write(str([["TOTAL_ARGUMENT == '"+ x +"'", ["",e]]]) + "\n")
            memoryfile.close()
            pass

    MEMcomposeinput = SeekForce([MemoryUNORDEREDvar,inputtextvar,delta2,SeekForcemin1,[]]) + SeekForce([memoryLongvar,inputtextvar,delta2,SeekForcemin1,[]])
    guessAbst = []
    for x in MEMcomposeinput:
        xmod = toString([ran(x),"naive"])
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
        minforce1 = SeekForce([MemoryUNORDEREDvar,x,SeekForcemin2,[],[]])
        minforce2 = SeekForce([memoryLongvar,x,SeekForcemin2,[],[]])
        totalabstractions = maxlargestequivclasses([minforce1,maxlargestequivclassesmin1]) + maxlargestequivclasses([minforce2,maxlargestequivclassesmin1])
        abstractiondict[str(icounter)] = totalabstractions
        icounter += 1
        abstractioninnertotal += len(totalabstractions)
        if len(totalabstractions) == 0:
            abstractioninnertotal += 1
    len1 = len(abstractiondict)
    len1int = 0
    len2 = len(guessAbst)
    len2int = 0
    anothersum = 0
    for x in range(len1):
        anothersum += len(abstractiondict[str(len1int)])
        if len(abstractiondict[str(len1int)]) == 0:
            anothersum += 1
        len1int += 1
    len1int = 0
    len3int = 0
    with open("ABSTRACTFILE.txt", 'a+', encoding='utf-8') as ABSTRACTFILE:
        for x in range(anothersum*len2):
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
                    print('insertionline12',stopdupe + "\n")
                    ABSTRACTFILE.write(stopdupe + "\n")
                    ABSTRACTFILE2.write(stopdupe + "\n")
                    print("written")
                else:
                    print("unwritten")
                    pass
                ABSTRACTFILE2.close()
            len3int += 1
    writeNoDupes = []
    with open(MemoryUNORDEREDvar, 'r+', encoding='utf-8') as ordered1:
        ordered1.seek(0)
        guessint = 0
        thenextline = rchop(ordered1.readline(), '\n')
        for lineint in range(mapcountLINES([MemoryUNORDEREDvar])*anothersum*len2):
            if guessint == len2:
                thenextline = rchop(ordered1.readline(), '\n')
                guessint = 0
            emptycheck = FILEindexread(["ABSTRACTFILE.txt",guessint])
            try:
                memX = eval(thenextline)[0][0]
            except:
                memX = []
            try:
                memY = eval(thenextline)[0][1]
            except:
                memY = []
            guessX = toString([ran(eval(emptycheck)[0][0]),"naive"])
            guessY = toString([ran(eval(emptycheck)[0][1]),"naive"])
            LHSTest = toString([ran(delta2([memX,guessX])),"naive"]) == guessX
            RHSTest = toString([ran(delta2([memY,guessY])),"naive"]) == guessY
            if LHSTest and RHSTest:
                possibleDupe = abstractionGENERALmin1([guessX,guessY,MemoryUNORDEREDvar,"STRFIX"])
                dupeList = [y for y in writeNoDupes if y == possibleDupe]
                if len(dupeList) == 0:
                    writeNoDupes.append(possibleDupe)
            guessint += 1
    with open(MemoryUNORDEREDvar, 'a+', encoding='utf-8') as ordered1:
        for candidate in writeNoDupes:
            if len(shittySearch([MemoryUNORDEREDvar,candidate])) == 0:
                ordered1.write(candidate + "\n")

    with open('ABSTRACTFILE.txt', 'r+', encoding='utf-8') as ordered1:
        ordered1.seek(0)
        for line in range(mapcountLINES(['ABSTRACTFILE.txt'])):
            nextguy = rchop(ordered1.readline(), '\n')
    os.remove("ABSTRACTFILE.txt")
    os.remove("ABSTRACTFILE2.txt")
    try:
        os.remove(OtherClone() + "\\" + "ABSTRACTFILE.txt")
    except:
        pass

"
U+0022 : QUOTATION MARK
“
U+201C : LEFT DOUBLE QUOTATION MARK {double turned comma quotation mark}
”
U+201D : RIGHT DOUBLE QUOTATION MARK {double comma quotation mark}

'[[[\'FixedQualifier([delta2,"α0α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\']], [[\'print("lost track of what I was doing")\', \'print("lost track of what I was doing")\']]]'

CURRENT Q:
print(ComposeMETA([eval('[[\'FixedQualifier([delta2,"α0α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\']]\n'), [['print("lost track of what I was doing")', 'print("lost track of what I was doing")']]]))

'[[\'FixedQualifier([delta2,"α0α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\']]'
  [\'FixedQualifier([delta2,"α0α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\'] 
   \'FixedQualifier([delta2,"α0α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\' 2
                    [delta2,"α0α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1] 3
                     delta2,"α0α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1 4
                                       


strFix(['FixedQualifier([delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])'])

'FixedQualifier([delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])'
				[delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1]
				 delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1
                                   "α2"            "lost track of what I was doing"
								   
IF I DO ATTEMPT SPLIT WITH , THAT MEANS I CANT HAVE COMMAS IN STRING INPUTS EVER: EX					
delta2,"α0α1print(",α2")α3","print("lost track of what I was doing")",FixedQualifiermin1 will fail

when to split?			

try this:
'delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1'.split(“,”)
'delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1'.split(“,”)
['delta2', '"α0α1print("α2")α3"', '"print("lost track of what I was doing")"', 'FixedQualifiermin1']
then force each element to be a single kind: either code or string depending on if you start with " or ' or not

CURRENT ANS:
'\'FixedQualifier([delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])\''				
ANS I WANT:			
print(ComposeMETA([eval('[[\'FixedQualifier([delta2,"α0α1print(\"α2\")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\']]\n'), [['print("lost track of what I was doing")', 'print("lost track of what I was doing")']]]))	  
				  
strFix(['FixedQualifier([delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])'])

'\'FixedQualifier([delta2,"α0α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])\''






=================================================================================================================================
>>> strFix(['FixedQualifier([delta2,"α0([α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])'])
start to end 			   ([delta2,"α0([α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])'
CHECK THIS WHILE FUNCTION  ([delta2,"α0([α1print("α2")α3","print("lost track of what I was doing")",FixedQualifiermin1])'






=================================================================================================================================
print(ComposeMETA([eval('[[\'FixedQualifier([delta2,"α0[α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\']]\n'), [['print("lost track of what I was doing")', 'print("lost track of what I was doing")']]]))



print(ComposeMETA([eval('[[\'FixedQualifier([delta2,"α0([α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\']]\n'), [['print("lost track of what I was doing")', 'print("lost track of what I was doing")']]]))
print(ComposeMETA([eval('[[\'FixedQualifier([delta2,"α0[α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])\', \'\']]\n'), [['print("lost track of what I was doing")', 'print("lost track of what I was doing")']]]))

FixedQualifier([delta2,"α0([α1print("α2")α3",TOTAL_ARGUMENT,FixedQualifiermin1])

FixedQualifier([delta2,"α0\\Mira.py", α1], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),"α0\Mira.py",FixedQualifiermin1])


>> ComposeMETA([[['FixedQualifier([delta2,str(print(\"α0\")),TOTAL_ARGUMENT,FixedQualifiermin1])', 'fix this']], [['check this guy', 'check this guy']]])
α0
why nonearg? [<function delta2 at 0x043A76A8>, 'None', 'check this guy', <function FixedQualifiermin1 at 0x043A7E40>]
fixedqualifiermin arglist [<function delta2 at 0x043A76A8>, 'None', 'check this guy', <function FixedQualifiermin1 at 0x043A7E40>]
LHS guy α0e
RHS guy None
[]
>>> 
>>> [delta2,'print(\"α0\")',TOTAL_ARGUMENT,FixedQualifiermin1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    [delta2,'print(\"α0\")',TOTAL_ARGUMENT,FixedQualifiermin1]
NameError: name 'TOTAL_ARGUMENT' is not defined
>>> ComposeMETA([[['FixedQualifier([delta2,\'print(\"α0\")\',TOTAL_ARGUMENT,FixedQualifiermin1])', 'fix this']], [['check this guy', 'check this guy']]])
why nonearg? [<function delta2 at 0x043A76A8>, 'print("α0")', 'check this guy', <function FixedQualifiermin1 at 0x043A7E40>]
fixedqualifiermin arglist [<function delta2 at 0x043A76A8>, 'print("α0")', 'check this guy', <function FixedQualifiermin1 at 0x043A7E40>]
LHS guy α0tα1
RHS guy print("α0")
[]
>>> ComposeMETA([[['FixedQualifier([delta2,str(print("α0")),TOTAL_ARGUMENT,FixedQualifiermin1])', 'fix this']], [['check this guy', 'check this guy']]])
α0
why nonearg? [<function delta2 at 0x043A76A8>, 'None', 'check this guy', <function FixedQualifiermin1 at 0x043A7E40>]
fixedqualifiermin arglist [<function delta2 at 0x043A76A8>, 'None', 'check this guy', <function FixedQualifiermin1 at 0x043A7E40>]
LHS guy α0e
RHS guy None
[]
>>> 


"print('alpha')"
"print('α0')"
WANT:
toString([dom(delta2(["print('alpha')","print('α0')"])),"naive"])
HAVE:
toString([dom(delta2(["print('alpha')","print('α0')"])),"naive"])

FixedQualifier([delta2,[α0print('yoikes')],'TOTAL_ARGUMENT == 'print('yoikes')'',FixedQualifiermin1])

[['Popen([\'python\',C:\\An\\MIRA\\Mira.py, print("rip")], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)', ["['rip\\n']\n"]]]



[[[['["'], ['["']], [['α0'], ['α0']], [['print('], ['print(']], [['α1'], ['α1']], [['"]'], ['"]']]], [[["['"], ["['"]], [['α0'], ['α0']], [['print('], ['print(']], [['α1'], ['α1']], [["']"], ["']"]]], [[['α0'], ['α0']], [["',C:\\\\An\\\\MIRA\\\\Mira.py, print("], ["',C:\\\\An\\\\MIRA\\\\Mira.py, print("]], [['α1'], ['α1']], [[')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)'], [')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)']], [["']"], ["']"]]], [[["['"], ["['"]], [['α0'], ['α0']], [['print('], ['print(']], [['α1'], ['α1']], [[' s'], [' s']], [['α2'], ['α2']]], [[['["Popen([\'python\',C:\\\\An\\\\MIRA\\\\Mira.py, print('], ['["Popen([\'python\',C:\\\\An\\\\MIRA\\\\Mira.py, print(']], [[')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)"'], [')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)"']], [[']'], [']']]], [[['[["'], ['[["']], [['α0'], ['α0']], [['print('], ['print(']], [['α1'], ['α1']], [['", ['], ['", [']], [['α2'], ['α2']]], [[['["'], ['["']], [['α0'], ['α0']], [["print('t')"], ["print('t')"]], [['α1'], ['α1']], [['"]'], ['"]']]], [[['["Popen([\'python\',C:\\\\An\\\\MIRA\\\\Mira.py, print(\'t\')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)"'], ['["Popen([\'python\',C:\\\\An\\\\MIRA\\\\Mira.py, print(\'t\')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)"']], [[']'], [']']]]]


strFixmin2([inpstr,inpstr[yS+1:yE],[yS+1,yE],strorCode([inpstr[yS+1:yE],len(inpstr[yS+1:yE]),"info"])])



[[TOTAL_ARGUMENT == 'print('yoikes')', ['None', '']]]
[[Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('yoikes')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True), ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'yoikes\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['yoikes\\n']\n", '[\'wtf nearfield3 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'yoikes\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', '[\'wtf nearfield4 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'yoikes\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', "['yoikes\\n']\n", "['already saw that 2\\n']\n", '[\'wtf nearfield5 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'yoikes\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n']]]

Popen(['python','C:\An\MIRA\MIRA_B\Mira.py', "print('yoikes')"], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)


[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('yoikes')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'yoikes\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['yoikes\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield3 []\\n']\n", "['wtf nearfield4 []\\n']\n", "['yoikes\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield5 []\\n']\n"]]]
[["FixedQualifier([delta2,[α0print('yoikes')],TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0\\Mira.py, print('yoikes')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('yoikes')],α2erα3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["TOTAL_ARGUMENT == 'print('cmonBrug')'", ['None', '']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('cmonBrug')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'cmonBrug\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['cmonBrug\\n']\n", '[\'wtf nearfield3 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'cmonBrug\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', '[\'wtf nearfield4 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'cmonBrug\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', "['cmonBrug\\n']\n", "['already saw that 2\\n']\n", '[\'wtf nearfield5 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'cmonBrug\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('cmonBrug')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'cmonBrug\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['cmonBrug\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield3 []\\n']\n", "['wtf nearfield4 []\\n']\n", "['cmonBrug\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield5 []\\n']\n"]]]
[["FixedQualifier([delta2,[α0print('α1')α2,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('α2')],α3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,[α0print('cmonBrug')],TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0\\Mira.py, print('cmonBrug')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('α2')α3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('cmonBrug')],α2erα3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["TOTAL_ARGUMENT == 'print('resetto')'", ['None', '']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('resetto')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'resetto\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['resetto\\n']\n", '[\'wtf nearfield3 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'resetto\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', '[\'wtf nearfield4 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'resetto\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', "['resetto\\n']\n", "['already saw that 2\\n']\n", '[\'wtf nearfield5 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'resetto\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('resetto')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'resetto\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['resetto\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield3 []\\n']\n", "['wtf nearfield4 []\\n']\n", "['resetto\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield5 []\\n']\n"]]]
[["FixedQualifier([delta2,[α0print('α1esα2,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,[α0print('resetto')],TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0\\Mira.py, print('resetto')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["TOTAL_ARGUMENT == 'print('check this')'", ['None', '']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('check this')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'check this\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['check this\\n']\n", '[\'wtf nearfield3 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'check this\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', '[\'wtf nearfield4 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'check this\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', "['check this\\n']\n", "['already saw that 2\\n']\n", '[\'wtf nearfield5 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'check this\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('check this')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'check this\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfield2 []\\n']\n", "['check this\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield3 []\\n']\n", "['wtf nearfield4 []\\n']\n", "['check this\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield5 []\\n']\n"]]]
[["FixedQualifier([delta2,[α0print('α1s')α2,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0s')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('α2s')],α3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('α2erα3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,[α0print('cα1')α2,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('cα2')],α3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,[α0print('check this')],TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0\\Mira.py, print('check this')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('α2s')α3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('cα2')α3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,α0([α1print('check this')],α2erα3,TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["TOTAL_ARGUMENT == 'print('hax')'", ['None', '']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('hax')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'hax\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfieldClone2 []\\n']\n", "['hax\\n']\n", '[\'wtf nearfieldClone3 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'hax\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', '[\'wtf nearfield4 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'hax\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', "['hax\\n']\n", "['already saw that 2\\n']\n", '[\'wtf nearfield5 [\\\'[["TOTAL_ARGUMENT == \\\\\\\'print(\\\\\\\'hax\\\\\\\')\\\\\\\'", [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n']]]
[["Popen(['python',C:\\An\\MIRA\\MIRA_B\\Mira.py, print('hax')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)", ["['wtf nearfield []\\n']\n", '[\'how many attempts? True ["print(\\\'hax\\\')"]\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfieldClone2 []\\n']\n", "['hax\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfieldClone3 []\\n']\n", "['wtf nearfield4 []\\n']\n", "['hax\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfield5 []\\n']\n"]]]
[['TOTAL_ARGUMENT == \'print("oof")\'', ['None', '']]]
[['Popen([\'python\',C:\\An\\MIRA\\MIRA_B\\Mira.py, print("oof")], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)', ["['wtf nearfield []\\n']\n", '[\'how many attempts? True [\\\'print("oof")\\\']\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfieldClone2 []\\n']\n", "['oof\\n']\n", '[\'wtf nearfieldClone3 [\\\'[[\\\\\\\'TOTAL_ARGUMENT == \\\\\\\\\\\\\\\'print("oof")\\\\\\\\\\\\\\\'\\\\\\\', [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', '[\'wtf nearfieldClone2 [\\\'[[\\\\\\\'TOTAL_ARGUMENT == \\\\\\\\\\\\\\\'print("oof")\\\\\\\\\\\\\\\'\\\\\\\', [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n', "['oof\\n']\n", "['already saw that 2\\n']\n", '[\'wtf nearfieldClone3 [\\\'[[\\\\\\\'TOTAL_ARGUMENT == \\\\\\\\\\\\\\\'print("oof")\\\\\\\\\\\\\\\'\\\\\\\', [\\\\\\\'None\\\\\\\', \\\\\\\'\\\\\\\']]]\\\']\\n\']\n']]]
[['Popen([\'python\',C:\\An\\MIRA\\MIRA_B\\Mira.py, print("oof")], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)', ["['wtf nearfield []\\n']\n", '[\'how many attempts? True [\\\'print("oof")\\\']\\n\']\n', "['tell me encoding cp1252\\n']\n", "['wtf nearfieldClone2 []\\n']\n", "['oof\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfieldClone3 []\\n']\n", "['wtf nearfieldClone2 []\\n']\n", "['oof\\n']\n", "['already saw that 2\\n']\n", "['wtf nearfieldClone3 []\\n']\n"]]]
[["FixedQualifier([delta2,[α0print('hax')],TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0\\Mira.py, print('hax')], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[['FixedQualifier([delta2,[α0print(α1esα2,TOTAL_ARGUMENT,FixedQualifiermin1])', '']]
[["FixedQualifier([delta2,Popen(['python',C:\\α0)], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])", '']]
[['FixedQualifier([delta2,α0([α1print(α2)],α3,TOTAL_ARGUMENT,FixedQualifiermin1])', '']]
[['FixedQualifier([delta2,[α0print(α1ruα2,TOTAL_ARGUMENT,FixedQualifiermin1])', '']]
[['FixedQualifier([delta2,α0([α1print(α2erα3,TOTAL_ARGUMENT,FixedQualifiermin1])', '']]
[['FixedQualifier([delta2,[\'α0print("oof")],TOTAL_ARGUMENT,FixedQualifiermin1])', '']]
[['FixedQualifier([delta2,Popen([α0\\Mira.py, print("oof")], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True),TOTAL_ARGUMENT,FixedQualifiermin1])', '']]






[['TOTAL_ARGUMENT == "b"', 'd']]
hint:
ON LHS
[0][0]

AND 
ON RHS
[0][1]

THEN WRITE:
delta2([TOTAL_ARGUMENT,])== 

THEN CHECK IF IT WORKS (don't code but just check)


========================


    NEED:
    memfiles as a list
	    MemoryUNORDERED var
		memoryLong
    inputtext var
	ABSTRACTFILE
	nearfield
	
	
	
=========================






=============================================================================================[	
	["[['loner','loner']]", "[['unrequited','unrequited']]"], 
	["[['unrequited','unrequited']]", "[['z','y'],['y','x'],['x','z']]"], 
	["[['z','y'],['y','x'],['x','z']]", "[['loner','loner']]"]
]
[
	[[['single', 'single']], [['oneway', 'oneway']]], 
	[[['oneway', 'oneway']], [['A', 'B'], ['B', 'C'], ['C', 'A']]], 
	[[['A', 'B'], ['B', 'C'], ['C', 'A']], [['single', 'single']]], 
	[[['A', 'B'], ['B', 'C'], ['C', 'A']], [['art', 'gallery'], ['gale', 'wind'], ['gallery', 'gale'], ['wind', 'art']]]
	]
[True, 

	[
		['4', '2'], 
		['2', '4'], 
		['3', '3'], 
		['0', '1'], 
		['1', '0']
	]
]

[
	[
		["[['A', 'B'], ['B', 'C'], ['C', 'A']]", "[['z','y'],['y','x'],['x','z']]"], 
		["[['z','y'],['y','x'],['x','z']]", "[['A', 'B'], ['B', 'C'], ['C', 'A']]"], 
		["[['single', 'single']]", "[['unrequited','unrequited']]"], 
		["[['unrequited','unrequited']]", "[['single', 'single']]"], 
		["[['oneway', 'oneway']]", "[['loner','loner']]"], 
		["[['loner','loner']]", "[['oneway', 'oneway']]"]
	], 
	[
		["[['A', 'B'], ['B', 'C'], ['C', 'A']]", "[['z','y'],['y','x'],['x','z']]"], 
		["[['z','y'],['y','x'],['x','z']]", "[['A', 'B'], ['B', 'C'], ['C', 'A']]"], 
		["[['oneway', 'oneway']]", "[['unrequited','unrequited']]"], 
		["[['unrequited','unrequited']]", "[['oneway', 'oneway']]"], 
		["[['single', 'single']]", "[['loner','loner']]"], 
		["[['loner','loner']]", "[['single', 'single']]"]
	]
]



vorposting:
1,3
4,2
2,3
1,7
4,8
7,8
9,3
7,10
10,9
8,10


10,9
8,9
9,2
1,8
2,1
1,3
7,1
3,4
4,7
4,5
5,6
6,4

=-========

[[1,3],[4,2],[2,3],[1,7],[4,8],[7,8],[9,3],[7,10],[10,9],[8,10]]


[[10,9],[8,9],[9,2],[1,8],[2,1],[1,3],[7,1],[3,4],[4,7],[4,5],[5,6],[6,4]]
[['10','9'],['8','9'],['9','2'],['1','8'],['2','1'],['1','3'],['7','1'],['3','4'],['4','7'],['4','5'],['5','6'],['6','4']]
[['10','9'],['8','9'],['9','2'],['1','8'],['2','1'],['1','3'],['7','1'],['3','4'],['4','7'],['4','5'],['5','6'],['6','4']]
[['1','2'],['3','2'],['2','9'],['9','10'],['10','3'],['10','8'],['4','10'],['8','7'],['7','4'],['7','6'],['6','5'],['5','7']]
1	10
2	9
3	8
4	7
5	6
6	5
7	4
8	3
9	2
10	1

ShittySI([[[['10','9'],['8','9'],['9','2'],['1','8'],['2','1'],['1','3'],['7','1'],['3','4'],['4','7'],['4','5'],['5','6'],['6','4']],[['1','2'],['3','2'],['2','9'],['9','10'],['10','3'],['10','8'],['4','10'],['8','7'],['7','4'],['7','6'],['6','5'],['5','7']]],"Auto","all"])



ShittySI([[[['1','3'],['4','2'],['2','3'],['1','7'],['4','8'],['7','8'],['9','3'],['7','10'],['10','9'],['8','10']],[['10','9'],['8','9'],['9','2'],['1','8'],['2','1'],['1','3'],['7','1'],['3','4'],['4','7'],['4','5'],['5','6'],['6','4']]],"Auto"])




[[['1','2'],['3','1']],[['4','4'],['5','5']]]
ShittySI([[[['1','2'],['3','1']],[['4','4'],['5','5']]],"Auto","all"])



[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]
{
'0': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\''], ['")\\\'\', [\'']], [['α1'], ['α1']]]], 
'1': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'2': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("bukDetect")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("bukDetect")\'', ['None', '']]]]]], 
'3': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print(""rasca;")\\\'\', [\'\', SyntaxError(\'invalid syntax\', (\'<string>\', 1, 13, \'print(""rasca;")\'))]]]\'', [['TOTAL_ARGUMENT == \'print(""rasca;")\'', ['', SyntaxError('invalid syntax', ('<string>', 1, 13, 'print(""rasca;")'))]]]]]], 
'4': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\''], ['")\\\'\', [\'']], [['α1'], ['α1']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [['rint('], ['rint(']], [['α2'], ['α2']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [[", ['', "], [", ['', "]], [['α2'], ['α2']]]], 
'5': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'6': [[[['α0'], ['α0']], [["['"], ["['"]], [['the bloom that flies away'], ['the bloom that flies away']], [['α1'], ['α1']], [["']"], ["']"]], [['α2'], ['α2']]], [[['["[\''], ['["[\'']], [['α0'], ['α0']], [['\\\\n\']\\n"]'], ['\\\\n\']\\n"]']]], [[['['], ['[']], [["['"], ["['"]], [['α0'], ['α0']], [["']"], ["']"]], [['α1'], ['α1']]], [[['α0'], ['α0']], [['"[\''], ['"[\'']], [['α1'], ['α1']], [['\\\\n\']\\n"]'], ['\\\\n\']\\n"]']]], [[['["'], ['["']], [["['"], ["['"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['α0'], ['α0']], [[" \\'"], [" \\'"]], [['rint'], ['rint']], [['α1'], ['α1']], [["', "], ["', "]], [['α2'], ['α2']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [['rint('], ['rint(']], [['α2'], ['α2']]], [[["['"], ["['"]], [['α0'], ['α0']], [[" \\'"], [" \\'"]], [['α1'], ['α1']], [["', "], ["', "]], [['α2'], ['α2']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [[", ['"], [", ['"]], [['α2'], ['α2']]], [[['['], ['[']], [["['"], ["['"]], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [[['α0'], ['α0']], [["['"], ["['"]], [['bukDetect'], ['bukDetect']], [['α1'], ['α1']], [["']"], ["']"]], [['α2'], ['α2']]], [[['α0'], ['α0']], [["['"], ["['"]], [['α1'], ['α1']], [['ect'], ['ect']], [['α2'], ['α2']], [['on'], ['on']], [['α3'], ['α3']]], [[['α0'], ['α0']], [["['"], ["['"]], [['xQc'], ['xQc']], [['α1'], ['α1']], [["']"], ["']"]], [['α2'], ['α2']]], [[['α0'], ['α0']], [["'rint"], ["'rint"]], [['α1'], ['α1']], [["' is not defined"], ["' is not defined"]], [['"'], ['"']], [['α2'], ['α2']]], [[['α0'], ['α0']], [['name '], ['name ']], [['α1'], ['α1']], [["' is not defined"], ["' is not defined"]], [['"'], ['"']], [['α2'], ['α2']]], [[['α0'], ['α0']], [["['"], ["['"]], [['UNLEASH FORCE'], ['UNLEASH FORCE']], [['α1'], ['α1']], [["']"], ["']"]], [['α2'], ['α2']]]], 
'7': [], 
'8': [[[['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [[", ['', SyntaxError('invalid syntax', ('<string>', 1, 1"], [", ['', SyntaxError('invalid syntax', ('<string>', 1, 1"]], [['α2'], ['α2']], [["'))]]]"], ["'))]]]"]]]], 
'9': [[[['α0'], ['α0']], [["['"], ["['"]], [['the bloom that flies away'], ['the bloom that flies away']], [['α1'], ['α1']], [["']"], ["']"]], [['α2'], ['α2']]], [[['['], ['[']], [["['"], ["['"]], [['α0'], ['α0']], [["']"], ["']"]], [['α1'], ['α1']]], [[['["[\''], ['["[\'']], [['α0'], ['α0']], [['\\\\n\']\\n"]'], ['\\\\n\']\\n"]']]], [[['['], ['[']], [["['"], ["['"]], [['α0'], ['α0']], [['li'], ['li']], [['α1'], ['α1']]], [[['α0'], ['α0']], [['"[\''], ['"[\'']], [['α1'], ['α1']], [['\\\\n\']\\n"]'], ['\\\\n\']\\n"]']]], [[['["'], ['["']], [["['"], ["['"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['α0'], ['α0']], [["['"], ["['"]], [['α1'], ['α1']], [['rin'], ['rin']], [['α2'], ['α2']], [[', '], [', ']], [['α3'], ['α3']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\''], ['")\\\'\', [\'']], [['α1'], ['α1']]], [[['α0'], ['α0']], [[" \\'"], [" \\'"]], [['rint'], ['rint']], [['α1'], ['α1']], [["', "], ["', "]], [['α2'], ['α2']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [['rint('], ['rint(']], [['α2'], ['α2']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [[", ['"], [", ['"]], [['α2'], ['α2']]], [[["['"], ["['"]], [['α0'], ['α0']], [[" \\'"], [" \\'"]], [['α1'], ['α1']], [["', "], ["', "]], [['α2'], ['α2']]], [[['['], ['[']], [["['"], ["['"]], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [[['α0'], ['α0']], [["['"], ["['"]], [['α1'], ['α1']], [['ect'], ['ect']], [['α2'], ['α2']], [['on'], ['on']], [['α3'], ['α3']]], [[['α0'], ['α0']], [['rror'], ['rror']], [['α1'], ['α1']], [['invalid syntax'], ['invalid syntax']], [['α2'], ['α2']], [['<string>'], ['<string>']], [['α3'], ['α3']]], [[['["'], ['["']], [['α0'], ['α0']], [['rror'], ['rror']], [[' is '], [' is ']], [['α1'], ['α1']]], [[['α0'], ['α0']], [["['"], ["['"]], [['α1'], ['α1']], [['rin'], ['rin']], [['α2'], ['α2']], [[')\\'], [')\\']], [['α3'], ['α3']]], [[["['"], ["['"]], [['α0'], ['α0']], [['rror'], ['rror']], [['α1'], ['α1']], [['rint'], ['rint']], [['α2'], ['α2']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [[", ['', "], [", ['', "]], [['α2'], ['α2']]], [[["['"], ["['"]], [['α0'], ['α0']], [['rror'], ['rror']], [['α1'], ['α1']], [["', "], ["', "]], [['α2'], ['α2']]], [[['['], ['[']], [["['"], ["['"]], [['α0'], ['α0']], [['i'], ['i']], [['α1'], ['α1']]], [[['α0'], ['α0']], [["'rint"], ["'rint"]], [['α1'], ['α1']], [["' is not defined"], ["' is not defined"]], [['"'], ['"']], [['α2'], ['α2']]], [[['α0'], ['α0']], [['["'], ['["']], [['α1'], ['α1']], [['rror'], ['rror']], [['α2'], ['α2']], [["', "], ["', "]], [['α3'], ['α3']]], [[['α0'], ['α0']], [['name '], ['name ']], [['α1'], ['α1']], [["' is not defined"], ["' is not defined"]], [['"'], ['"']], [['α2'], ['α2']]]], 
'10': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['α0'], ['α0']], [[" \\'"], [" \\'"]], [['rint'], ['rint']], [['α1'], ['α1']], [["', "], ["', "]], [['α2'], ['α2']]], [[['[['], ['[[']], [['α0'], ['α0']], [['TOTAL_ARGUMENT == '], ['TOTAL_ARGUMENT == ']], [['α1'], ['α1']], [['rint('], ['rint(']], [['α2'], ['α2']]], [[['α0'], ['α0']], [["'rint"], ["'rint"]], [['α1'], ['α1']], [["' is not defined"], ["' is not defined"]], [['"'], ['"']], [['α2'], ['α2']]]], 
'11': [], 
'12': []}

((critchancemod*critmultmod*(basedmgmod + basedmgmod*elementalstotal + basedmgmod*physicalbonusmod)) + ((1-critchancemod)(*basedmgmod + basedmgmod*elementalstotal + basedmgmod*physicalbonusmod)))*fireratemod


(
	(critchancemod*critmultmod*(basedmgmod + basedmgmod*elementalstotal + basedmgmod*physicalbonusmod)) + 
	((1-critchancemod)(*basedmgmod + basedmgmod*elementalstotal + basedmgmod*physicalbonusmod))
	)*fireratemod

TotalSI([[[['1', '0'], ['0', '1'], ['0', '2'], ['4', '0']], [['3', '0'], ['2', '1'], ['1', '2'], ['4', '0'], ['2', '2']]],"Auto"])


STEP 1: MAKE SI STRUCTURES

[['1','2'],['2','3'],['3','1'],['3','4']]

[['1b','2b'],['2b','3b'],['3b','1b']]

STEP 2: REPLACE EACH INTEGER WITH A FUNCTION

HINT: MAKE DIFFERENT BUT TOTALLY SI FUNCTIONS!


1: quine dot
[['single','single']]
[['loner','loner']]

2: line
[['oneway','oneway']]
[['unrequited','unrequited']]

3: triangle
[['A','B'],['B','C'],['C','A']]
[['z','y'],['y','x'],['x','z']]


4: square
[['art','gallery'],['gale','wind'],['gallery','gale'],['wind','art']]
[['tree','cow'],['bird','flight'],['cow','bird'],['flight','tree']]


:try to test the min function as well
[[[['single','single']],[['oneway','oneway']]],[[['oneway','oneway']],[['A','B'],['B','C'],['C','A']]],[[['A','B'],['B','C'],['C','A']],[['single','single']]],[[['A','B'],['B','C'],['C','A']],[['art','gallery'],['gale','wind'],['gallery','gale'],['wind','art']]]]

[['[[\'loner\',\'loner\']]','[[\'unrequited\',\'unrequited\']]'],['[[\'unrequited\',\'unrequited\']]','[[\'z\',\'y\'],[\'y\',\'x\'],[\'x\',\'z\']]'],['[[\'z\',\'y\'],[\'y\',\'x\'],[\'x\',\'z\']]','[[\'loner\',\'loner\']]']]
=================================================================================================

{'0': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], [0'α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '1': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '2': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '3': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '4': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '5': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '6': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '7': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '8': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '9': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '10': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '11': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '12': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '13': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '14': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], '']], '15': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], '']], '16': [[[[["print('"], ["print('"]], [['α0'], ['α0']]], '']], '17': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '18': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '19': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '20': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '21': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '22': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '23': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '24': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '25': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '26': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '27': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '28': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '29': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '30': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '31': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], '']], '32': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], '']], '33': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ki'], ['ki']], [['α1'], ['α1']]], '']], '34': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '35': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '36': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '37': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '38': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '39': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '40': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '41': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '42': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '43': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '44': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '45': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '46': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '47': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '48': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], '']], '49': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], '']], '50': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking '], ['fucking ']], [['α1'], ['α1']], [['i'], ['i']], [['α2'], ['α2']]], '']], '51': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '52': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '53': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '54': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '55': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '56': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '57': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '58': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '59': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '60': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '61': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '62': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '63': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '64': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '65': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], '']], '66': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], '']], '67': [[[[['print('], ['print(']], [['α0'], ['α0']], [['fucking r'], ['fucking r']], [['α1'], ['α1']]], '']], '68': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '69': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '70': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '71': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '72': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '73': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '74': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '75': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '76': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '77': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '78': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '79': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '80': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '81': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '82': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], '']], '83': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], '']], '84': [[[[['print('], ['print(']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], '']], '85': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '86': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '87': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '88': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '89': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '90': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '91': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '92': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '93': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '94': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '95': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '96': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '97': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '98': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '99': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], '']], '100': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], '']], '101': [[[[['print('], ['print(']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], '']], '102': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '103': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '104': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '105': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '106': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '107': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '108': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '109': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '110': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '111': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '112': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '113': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '114': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '115': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '116': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], '']], '117': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], '']], '118': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], '']], '119': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '120': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '121': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '122': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '123': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '124': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '125': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '126': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '127': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '128': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '129': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '130': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '131': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '132': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '133': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], '']], '134': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], '']], '135': [[[[["print('"], ["print('"]], [['α0'], ['α0']], [["')"], ["')"]]], '']], '136': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '137': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '138': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]]], '139': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '140': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]]], '141': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '142': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '143': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking gigantic data scam")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking gigantic data scam")\'', ['None', '']]]]]]], '144': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]]], '145': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '146': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '147': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '148': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '149': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], '150': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], '']], '151': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], '']], 
'152': [[[[["print('fucking rip')"], ["print('fucking rip')"]]], '']]}


{
'0': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'1': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]], 
'2': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("alive nine")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("alive nine")\'', ['None', '']]]]]], 
'3': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]], 
'4': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'5': [[[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'6': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("alive nine")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("alive nine")\'', ['None', '']]]]]], 
'7': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("a'], ['[[\'TOTAL_ARGUMENT == \\\'print("a']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'8': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("alive nine")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("alive nine")\'', ['None', '']]]]]], 
'9': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'10': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'11': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("alive nine")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("alive nine")\'', ['None', '']]]]]], 
'12': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("alive nine")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("alive nine")\'', ['None', '']]]]]]
}















{
'0': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("fucking '], ['[[\'TOTAL_ARGUMENT == \\\'print("fucking ']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['s")\\\'\', [\'None\', \'\']]]'], ['s")\\\'\', [\'None\', \'\']]]']]]], 
'1': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("fucking 0 degen answers")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("fucking 0 degen answers")\'', ['None', '']]]]]], 
'2': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'3': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['?")\\\'\', [\'None\', \'\']]]'], ['?")\\\'\', [\'None\', \'\']]]']]]], 
'4': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("what is suppans?")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("what is suppans?")\'', ['None', '']]]]]], 
'5': [], 
'6': [], 
'7': [], 
'8': [], 
'9': [[[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]], 
'10': [],
'11': [[['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("beegees")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("beegees")\'', ['None', '']]]]]], 
'12': []
}




{
'0': [[[[['print("'], ['print("']], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'1': [[[[['print("'], ['print("']], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'2': [[[[['print("'], ['print("']], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'3': [[[[['print("'], ['print("']], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'4': [[[[['print("'], ['print("']], [['α0'], ['α0']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'5': [[[[['print("'], ['print("']], [['α0'], ['α0']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("at what point does this take a long time?")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("at what point does this take a long time?")\'', ['None', '']]]]]]], 
'6': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['")'], ['")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'7': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['")'], ['")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'8': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['")'], ['")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'9': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['")'], ['")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'10': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['")'], ['")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'11': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['")'], ['")']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("at what point does this take a long time?")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("at what point does this take a long time?")\'', ['None', '']]]]]]], 
'12': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'13': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'14': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'15': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'16': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'17': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['in'], ['in']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("at what point does this take a long time?")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("at what point does this take a long time?")\'', ['None', '']]]]]]], 
'18': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'19': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'20': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'21': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'22': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'23': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['on'], ['on']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("at what point does this take a long time?")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("at what point does this take a long time?")\'', ['None', '']]]]]]], 
'24': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'25': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'26': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'27': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'28': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'29': [[[[['print("'], ['print("']], [['α0'], ['α0']], [['ng '], ['ng ']], [['α1'], ['α1']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("at what point does this take a long time?")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("at what point does this take a long time?")\'', ['None', '']]]]]]], 
'30': [[[[['print("at what point does this take a long time?")'], ['print("at what point does this take a long time?")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'31': [[[[['print("at what point does this take a long time?")'], ['print("at what point does this take a long time?")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'32': [[[[['print("at what point does this take a long time?")'], ['print("at what point does this take a long time?")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'33': [[[[['print("at what point does this take a long time?")'], ['print("at what point does this take a long time?")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'34': [[[[['print("at what point does this take a long time?")'], ['print("at what point does this take a long time?")']]], [[['[[\'TOTAL_ARGUMENT == \\\'print("'], ['[[\'TOTAL_ARGUMENT == \\\'print("']], [['α0'], ['α0']], [['")\\\'\', [\'None\', \'\']]]'], ['")\\\'\', [\'None\', \'\']]]']]]]], 
'35': [[[[['print("at what point does this take a long time?")'], ['print("at what point does this take a long time?")']]], [['TOTAL_ARGUMENT == \'[[\'TOTAL_ARGUMENT == \\\'print("at what point does this take a long time?")\\\'\', [\'None\', \'\']]]\'', [['TOTAL_ARGUMENT == \'print("at what point does this take a long time?")\'', ['None', '']]]]]]]}

