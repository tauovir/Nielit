import sys
writeMode = open(sys.argv[2],"w")
z = ['%d X %d = %d'%(int(sys.argv[1]),i,int(sys.argv[1])*i) for i in range(1,10)]
writeMode.write('\n'.join(z))

