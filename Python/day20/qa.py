import numpy as np

dataType = np.dtype({'names':['name','emp_id','designation','salary','phone'],
                     'formats':['S20','i8','S20','f8','S20']
                     })
file1 = np.loadtxt('emp.csv',delimiter=',',skiprows = 1, dtype = dataType)
print file1
print "================="

#=====tOTAL sALARY
salary = file1['salary'].sum()
print salary

#Display name of officer
#b = file1['designation'] == 'officer'
officer = file1[file1['designation'] == 'officer']
print officer['name']
#========Scientist recorrd=====
print "========Scientist============="
scientist = file1[file1['designation'] == 'scientist']
print scientist
#============Average Salary of Engineer=========
print "========Engineer============="
eng = file1[file1['designation'] == 'engineer']
print "avarage salary of engineer:",eng['salary'].mean()

#==========List of Employee by order of salary=========
print "========Ordering==========="
emp2 = file1.copy()
x = emp2.argsort(order = 'salary')
print emp2[x]
#=======
#==========List of Employee by order of salary and designation=========
print "========Ordering by salary and designation==========="
emp2 = file1.copy()
x = emp2.argsort(order = 'salary')
b1 = emp2[x]
y= b1.argsort(order='designation')
print b1[y]
#=======
#========Lowes salary for scientis designation========
print "===========Scienrist lowest salary================"
x =scientist['salary'].min()
print x
#========Scientist with lower slalry========
print "============Lowest salary scientist========="
ll = scientist[scientist['salary'] == x]
print ll

