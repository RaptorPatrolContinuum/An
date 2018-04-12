from MiraExternals import *
print("this is argv", argv)

try:
    if len(argv[1:]) > 0:
        inputtext = argv[1:]
    else:
        inputtext = str(input("exit or logout to leave \n"))
except EOFError as e:
    inputtext = str(input("exit or logout to leave \n"))
except Exception as e:
    #FILEinsertAt([memoryname,input,mapcountLINES([memoryname])])
    print("this is the error",e)
    #inputtext = "exit"
    inputtext = str(input("exit or logout to leave \n"))
print("YOUR INPUT IS", inputtext)
'''
while True:
    try:
        if len(argv[1:]) > 0:
            inputtext = argv[1:]
        else:
            inputtext = str(input("exit or logout to leave \n"))
    except EOFError as e:
        inputtext = str(input("exit or logout to leave \n"))
    except Exception as e:
        #FILEinsertAt([memoryname,input,mapcountLINES([memoryname])])
        print("this is the error",e)
        #inputtext = "exit"
        inputtext = str(input("exit or logout to leave \n"))
    print("YOUR INPUT IS", inputtext)
'''
'''
while True:
    inputtext = str(input("THIS IS TESTPROGRAM, exit or logout to leave \n"))
    if inputtext == "exit" or inputtext == "logout":
        break
    else:
        print(inputtext)
'''
