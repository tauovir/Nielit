from  Tkinter import *
import math
stmt = ''
def calc(param):
    global stmt
    if param == '=':
        textInput.set(eval(stmt))
        stmt = str(eval(stmt))
    elif param == 'del':
         textInput.set(0)
         stmt = ''
    elif param == 'sqr':
        num = eval(stmt)
        stmt = num * num
        textInput.set(stmt)
    elif param == 'sqrt':
        num = eval(stmt)
        stmt = math.sqrt(num)
        textInput.set(stmt)
    else:
        stmt = str(stmt)
        stmt += param
        textInput.set(stmt)
        
mainWindow = Tk()
mainWindow.title("Best Calculater")
mainWindow.geometry("300x200")
textInput = StringVar()
e1 = Entry(mainWindow, textvariable = textInput,fg='green')
#e1.pack()

b1 = Button(mainWindow,command = lambda : calc('1'),text = "1")
b2 = Button(mainWindow,command = lambda : calc('2'),text = "2")
b3 = Button(mainWindow,command = lambda : calc('3'), text = "3")
b4 = Button(mainWindow,command = lambda : calc('4'),text = "4")
b5 = Button(mainWindow,command = lambda : calc('5'),text = "5")
b6 = Button(mainWindow,command = lambda : calc('6'),text = "6")

b7 = Button(mainWindow,command = lambda : calc('7'),text = "7")
b8 = Button(mainWindow,command = lambda : calc('8'),text = "8")
b9 = Button(mainWindow,command = lambda : calc('9'),text = "9")

b10 = Button(mainWindow,command = lambda : calc('.'),text = ".")
b11 = Button(mainWindow,command = lambda : calc('0'),text = "0")
b12 = Button(mainWindow,command = lambda : calc('='),text = "=")


plus = Button(mainWindow,command = lambda : calc('+'),text = "+")
minus = Button(mainWindow,command = lambda : calc('-'),text = "-")
multi = Button(mainWindow,command = lambda : calc('8'),text = "*")
divide = Button(mainWindow,command = lambda : calc('/'),text = "/")
delete = Button(mainWindow,command = lambda : calc('del'),text = "C")
sqr = Button(mainWindow,command = lambda : calc('sqr'),text = "sqr")
sqrt = Button(mainWindow,command = lambda : calc('sqrt'),text = "sqrt")




e1.grid(row=0,column=2,columnspan=4)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)

b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)

b10.grid(row=5,column=0)
b11.grid(row=5,column=1)
b12.grid(row=5,column=2)

plus.grid(row=2,column=3)
minus.grid(row=3,column=3)
multi.grid(row=4,column=3)
divide.grid(row=5,column=3)

delete.grid(row=2,column=4)
sqr.grid(row=3,column=4)
sqrt.grid(row=4,column=4)




mainWindow.mainloop()

