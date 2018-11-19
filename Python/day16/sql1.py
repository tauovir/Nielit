from Tkinter import *
import MySQLdb as db

def SaveRecord():
    name = name1.get()
    designation = desig.get()
    salary1= salary.get()
    con = db.connect("127.0.0.1",'ai','ai','ai')
    cur = con.cursor()
    query ="insert into emp_ai20 (name,designation,salary)"  + " values('" + name +"','" + designation + "'," + str(salary1) + ")"
    print query
    cur.execute(query)
    con.commit()
    con.close()
    print "inserted 1 row:"
    name1.set('')
    salary.set('')
    desig.set('')

def getData():
    name = name1.get()
    designation = desig.get()
    salary1= salary.get()
    con = db.connect("127.0.0.1",'ai','ai','ai')
    cur = con.cursor()
    query ="Select * from emp_ai20"
    cur.execute(query)
    result = cur.fetchall()
   # print result
    con.close()
    return result
     
    
mainWindow = Tk()
mainWindow.title("Employee Data")
mainWindow.geometry("600x500")

name1 = StringVar()
desig = StringVar()
salary = IntVar()
nameLabel = Label(mainWindow, text="Enter employee Name:")
desigLabel = Label(mainWindow,text = "Enter employee Designation:")
salaryLabel = Label(mainWindow, text = "Enter employee Salary:")


e1 = Entry(mainWindow, textvariable = name1)
e2 = Entry(mainWindow, textvariable = desig)
e3 = Entry(mainWindow, textvariable = salary)

nameLabel.grid(row=0,column=0,columnspan=4)
e1.grid(row=0,column=5,columnspan=4)

desigLabel.grid(row=2,column=0,columnspan=4)
e2.grid(row=2,column=5,columnspan=4)

salaryLabel.grid(row=4,column=0,columnspan=4)
e3.grid(row=4,column=4,columnspan=4)

btn = Button(mainWindow,command = lambda : SaveRecord(),text = "Submit")
btn.grid(row=7,column=4,rowspan = 4)
k = 7

result = getData() # Get data

i = 11
for res in result: #Rows
    print res
    i = i +1
    name1 = StringVar()
    name2 = StringVar()
    name3 = StringVar()
    name1.set(res[1])
    name2.set(res[2])
    name3.set(res[3])
    Entry(mainWindow, textvariable = name1).grid(row=i+1,column=0,columnspan=4)
    Entry(mainWindow, textvariable = name2).grid(row=i+1,column=3,columnspan=4)
    Entry(mainWindow, textvariable = name3).grid(row=i+1,column=6,columnspan=4)
        
mainWindow.mainloop()
