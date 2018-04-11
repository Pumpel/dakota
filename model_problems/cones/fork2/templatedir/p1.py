'''
Read tabular values
'''

import math

#f = open('in.txt', 'r')
#f.readline()
#f.close


f = open('input.in', 'r')

#for line in f:
#print repr(line)

line = f.readline()

line = line.strip()

columns = line.split()

r = float(columns[0])
h = float(columns[1])

f.close()


f = open('results.txt', 'wb')

#Inputs r ad h
volume = (math.pi/3)*r*r*h
s = math.sqrt(r*r + h*h)
lateral = math.pi*r*s
base = math.pi*r*r
total_area = base + lateral

s0 = str(lateral)
s1 = str(total_area)
s2 = str(volume)

f.write(s0)
f.write("\n")
f.write(s1)
f.write("\n")
f.write(s2)
f.write("\n")
#f.write(s3)

f.close()



#g1 = c0**2 - c1/2
#g2 = c1**2 - c0/2

#f.write('%f' % ros)

#s0 = str(volume)
#s1 = str(s)
#s2 = str(lateral)
#s3 = str(base)
#s1 = str(g1)
#s2 = str(g2)


