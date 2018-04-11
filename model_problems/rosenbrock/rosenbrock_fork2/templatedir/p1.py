'''
Read tabular values
'''

#f = open('in.txt', 'r')
#f.readline()
#f.close


f = open('ros.in', 'r')

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

ros = (1 - c0)**2 + 100*(c1 - c0**2)**2


#Analytical gradients

grad1 = -2*(1-c0) - 400*c0*(c1 - c0**2)
grad2 = 200*(c1-c0**2)


#f.write('%f' % ros)

s0 = str(ros)
s1 = str(grad1)
s2 = str(grad2)

f.write(s0)
f.write("\n")

#write gradients
#f.write("[ " + s1 + " " + s2 + " ]")
#f.write("\n")



#f.write("[[ " + " 0 " + " " + " 0 " + " ]]")

#f.write("\n")
#f.write("[" + s1 + "]")
#f.write("\n")
#f.write("[" + s2 + "]")

f.close()



#value0 = c0*1
#value1 = c1*1
#value2 = c2*1
#value3 = c3*1
#value4 = c4*1

#s0 = str(value0)
#s1 = str(value1)
#s2 = str(value2)
#s3 = str(value3)
#s4 = str(value4)

#f.write(s0 + " " + s1 + " " + s2 )

#f.write(s0)
#f.write('\n')
#f.write(s1)

#f.close()

