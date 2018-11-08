import sys
fd = open(sys.argv[1])
print fd.read()[:-1]

n = 5
writeMode = open("readF","w")
z = ['%d X %d = %d'%(n,i,n*i) for i in range(1,10)]
writeMode.write('\n'.join(z))
writeMode.close()
