'''
Read tabular values
'''

#f = open('in.txt', 'r')
#f.readline()
#f.close


f = open('input.in', 'r')

#for line in f:
#print repr(line)

line = f.readline()

line = line.strip()

columns = line.split()

x0 = float(columns[0])
#x1 = float(columns[1])

f.close()

#
#
f = open('results.txt', 'wb')

function1 = x0**2

function2 = (x0-2)**2
#function2 = (x1-2)**2

#g1 = c0**2 - c1/2

#g2 = c1**2 - c0/2


f.write('%f' % function1 +  '\n'  + '%f' % function2)

#s0 = str(function1)
#s1 = str(function1)

#f.write(s0)
#f.write("\n")
#f.write(s1)
#f.write("\n")
#f.write(s2)



f.close()





