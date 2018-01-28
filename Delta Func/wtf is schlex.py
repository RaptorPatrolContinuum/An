import shlex
from subprocess import Popen, PIPE

cmd = ...
process = Popen(shlex.split(cmd), stdout=PIPE)
process.communicate()
exit_code = process.wait()
