

import module1
x = input("1: initialize,2:show,3:reloade,0:exit")
while x >0 :
    x = input("1: initialize,2:show,3:reloade,0:exit")
    if x == 1 :
        import module1
    elif x == 2 :
       con = module1.a + 10 * module1.b * module1.c - 5 * module1.c / module1.e
       print con
    elif x == 3 :
        reload(module1)

