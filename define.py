from re import *
import sys
define=[]
def define_conv(m):
	s=(m.group(1)).split()
	define.append(s)
	return ' '
f=open(sys.argv[1], 'r')
progc=f.read();
progc=sub(r'#define(.*)', define_conv ,progc)
for x in define:
	prog=compile(x[0])
	progc=sub(prog,x[1],progc)
print(progc)
#print(define)
f.close()
