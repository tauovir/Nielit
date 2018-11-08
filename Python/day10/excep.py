def show(cn, noh=0):
    print '-'*noh ,cn.__name__
    for scn in cn.__subclasses__():
        show(scn,noh+2)
        

show(Exception)
#print Exception.__subclasses__()
#help(Exception)
