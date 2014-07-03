from re import *
from sys import *



prog=compile(r'/\*(.*)\*/',DOTALL)
prog2=compile(r'//.*')
f=open(argv[1],'r')
progc=f.read()
progc=progc.strip()
progc=sub(prog,'',progc)
progc=sub(prog2,'',progc)
print(progc)
purge()
