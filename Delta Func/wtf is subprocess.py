'''
from subprocess import Popen, PIPE

process = Popen(["ls", "-la", "."], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
'''
'''
from subprocess import Popen, PIPE

output = Popen(["python","TestProgram.py"], stdout=PIPE)
#output = proc.communicate()[0]
output.stdout.read()
'''
'''
#THIS WORKS
from subprocess import Popen, PIPE

proc = Popen(["python","TestProgram.py"], stdout=PIPE)
output = proc.communicate()[0]
print(output)
'''
'''
#THIS WORKS
from subprocess import Popen, PIPE

output = Popen(['python', 'TestProgram.py'], stdout=PIPE) 
print(output.stdout.read())
'''
'''
#NOT SURE
from subprocess import Popen, PIPE, STDOUT

cmd = 'ls /etc/fstab /etc/non-existent-file'
p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
output = p.stdout.read()
print (output)
'''

from subprocess import Popen, PIPE
p = Popen(['python', 'TestError.py'], stdout=PIPE, stderr=PIPE) 
stdout, stderr = p.communicate()
print(p.communicate()[0])
print(p.communicate()[1])
