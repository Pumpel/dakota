'''
Read tabular values
'''

#import numpy as np
import math

#f = open('in.txt', 'r')
#f.readline()
#f.close


f = open('branin.in', 'r')

#for line in f:
#print repr(line)

line = f.readline()

line = line.strip()

columns = line.split()

c0 = float(columns[0])
c1 = float(columns[1])
#c2 = float(columns[2])

#	print c0, c1, c2, c3, c4

f.close()

#
#
f = open('results.txt', 'wb')

branin = (c1 - 5.1/(4*math.pi**2)*c0**2 + (5/math.pi)*c0-6)**2 + 10*(1 - 1/(8*math.pi))*math.cos(c0) + 10




#f.write('%f' % ros)

s0 = str(branin)

f.write(s0)
f.write("\n")

f.close()


