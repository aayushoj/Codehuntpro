from re import *
from sys import * 
def array(m):
	s=m.group(0)[4:]
	x=split(r'[a-zA-z0-9_\[\] \n\t]*=[ \n\t]*\{[0-9,]+\}',s)
	for i in range(0,len(x)):
		x[i]=sub(r'[ ;\n\t\r]+','',x[i])
	p=findall(r'[a-zA-z0-9_\[\] \n\t]*=[ \n\t]*\{[0-9,]+\}',s)
	s=''
	for i in range(0,len(x)):
		s=s+x[i]
	s=s.split(',')
	print(p)
	print(s)
	return "detected"

def main():
f=open(argv[1],'r');
progc=f.read();
progc=progc.strip();
progc=sub(r'(int) [a-zA-z0-9_\{\}\[\], \n\t=]*;',array,progc);
