from re import *
from sys import * 
def switch_chan(m):
	#print(m.group(1))
	s=m.group(1)
	s=split(r'case',s)
	y=len(s)
	for x in range(0,y):
		if(x):
			if(findall("break;",s[x-1])):
				12
			else:
				i=s[x].index(':')
				s[x-1]+= "\tgoto case " + s[x][0:i] + ";\n"
	for x in range(0,y):
		s[x]="case " +s[x]
		print('*'+s[x]+'*')
	a=""
	for x in range(0,y):
		a+=s[x]
	return a

def default_chan(m):
	s=m.group(1)
	try :
		i=s.index("default")
		sub=s[i:]
		if(findall("break;",sub)):
			return s
		else:
			j=s.index('}');
			return s[:j]+"break;\n"+s[j:]
	except:
		return s;

f=open(argv[1],'r');
switch_change=compile(r'case(.*case .+:)',DOTALL)
default_change=compile(r'(switch(.*)\})',DOTALL)
progc=f.read();
progc=progc.strip();
progc=sub(switch_change,switch_chan,progc,DOTALL);
progc=sub(default_change,default_chan,progc,DOTALL);
print("\n\n\n\n\n\n\n")

print(progc)
 
