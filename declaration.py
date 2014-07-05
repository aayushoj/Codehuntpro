from re import *
from sys import * 
variables=[]
def replace(m):
	s=m.group(0)
	s=sub(r'\]\[',',',s)
	return s

def array(m):
	s=m.group(0)[4:]
	typ=m.group(1)
	x=split(r'[a-zA-z0-9_\[\] \n\t]*=[ \n\t\{0-9,\}]+',s)
	for i in range(0,len(x)):
		x[i]=sub(r'[ ;\n\t\r]+','',x[i])
	p=findall(r'[a-zA-z0-9_\[\] \n\t]*=[ \n\t\{0-9,\}]+',s)
	s=''
	for i in range(0,len(x)):
		s=s+x[i]
	s=s.split(',')
	print(p)
	print(s)
	total=''
	replace=''
	for x in s:
		if(x==''):
			continue
		size=findall(r'[0-9]+',x)
		print(size)
		count=len(size)
		if(count):
			for j in range(0,count-1):
				replace=replace+','
			replace=typ+'['+replace+'] '
			j=x.index('[')
			name=x[0:j]
			replace=replace+x[0:j]+';\n'+x[0:j]+'=new '+typ+'['
			for k in size:
				replace=replace+k+','
			replace=replace[0:-1]+'];\n'
			total=total+replace;
		else:
			replace=typ+' '+x+';\n'
			total=total+replace
			name=x
		y=[typ,name,count]
		variables.append(y)
	for x in p:
		size=findall(r'\[\d*\]',x)
		j=x.index('[')
		k=x.index('{')
		replace=typ+'['
		count=len(size)
		name=x[0:j]
		for i in range(0,count-1):
			replace=replace+','
		replace=replace+'] '+name+';\n'
		replace=replace+'new '+typ+'['
		for i in range(0,count-1):
			replace=replace+',' 
		replace=replace+'] '+x[k:]+';\n'
		total=total+replace
		y=[typ,name,count]
		variables.append(y)
	return total[0:-1]
f=open(argv[1],'r')
progc=f.read()
progc=progc.strip()
progc=sub(r'(int) [a-zA-z0-9_\{\}\[\], \n\t=]*;',array,progc)
progc=sub(r'(char) [a-zA-z0-9_\{\}\[\], \n\t=]*;',array,progc)
progc=sub(r'(float) [a-zA-z0-9_\{\}\[\], \n\t=]*;',array,progc)

for x in variables:
	s=x[1]+r'(\[\d+\])+'
	ref=compile(s)
	progc=sub(ref,replace,progc)
print(progc)
#print(variables)
