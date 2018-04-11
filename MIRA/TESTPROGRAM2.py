from MiraExternals import *
#print("this is argv", argv)

with Popen(['python', 'testprogram.py', 'whatabouthtis'], stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        print(line, end='')
    pass
