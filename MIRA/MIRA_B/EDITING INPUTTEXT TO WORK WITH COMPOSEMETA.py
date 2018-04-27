#!/usr/bin/python3.6.3
from MiraExternals import *

while True:
    inputtext = str(input("exit or logout to leave \n"))
    if inputtext == "exit" or inputtext == "logout":
        raise SystemExit
        break
    else:
        print("what is OG inputtext?",inputtext)
        #YOU HAVE TO MODIFY INPUTTEXT TO ESCAPE ALL THE FUCKING " FOR COMPOSEMETA TO WORK PROPERLY ON print("X")
        #MAYBE NOT, I NEEED TO FUCKING SLEEP
        inputtext = inputtext.replace('"', '\\'+'"')
        print("inputtext check",inputtext)
        try:
            eval(inputtext)
        except Exception as e:
            print("wtf is wrong",e)
