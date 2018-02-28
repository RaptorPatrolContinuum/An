import fileinput

def FILEinsertAtPERMERROR(ArgList):
    '''
    function to insert text at a specific line in file
    arg1 = filestream
    arg2 = string to insert
    needs 'import fileinput'
    '''
    arg1 = ArgList[0].name
    #have to close this for fileinput to work
    ArgList[0].close()
    arg2 = ArgList[1]
    i = 0
    for line in fileinput.input(arg1, inplace=1):
        if i == 3:
            print(arg2)
        i += 1
        print(line, end='')
FILEinsertAtPERMERROR([open('1.txt','r+'),"ok inserted at 3 (fixed)?"])
