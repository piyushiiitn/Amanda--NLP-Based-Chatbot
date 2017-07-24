import sys

f1 = open('create_aiml.py','r')

f2 = open(sys.argv[1],'r')
lines = f2.readlines()
print len(lines)

g = open('cpy_aiml.py','w')

i = 1
for line in f1:
	if (i <= 22):
		g.write(lines[i-1]);
		i = i+1
	else:
		g.write(line)

g.close()
f2.close()
f1.close()
