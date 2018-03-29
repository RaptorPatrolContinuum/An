import subprocess
import os
#os.path.expanduser('C:\An\MIRA\indepprocesstest.sh')
#p = subprocess.Popen(['/bin/sh', 'C:\An\MIRA\indepprocesstest.sh'])

p = subprocess.Popen(['C:\Personalize\Git\cmd\git.exe', 'C:\An\MIRA\indepprocesstest.sh'])
# look ma, no pipes!
print(p.pid)
# prints 29893
