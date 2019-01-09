
def multiplicationTable():
    '''
    DAy6:
    question number 1
    '''
    n = int(input("Enter Number to generate table:"))
    tableList = [x * n for x in range(1,21)]
    print(tableList)
    openFile = open("table1.txt",'w')
    i = 1
    for x in tableList:
        res = str(i) + "*" + str(n) + " = " + str(x) + "\n"
        openFile.write(res)
        i += 1
        print(res)
    openFile.close()

#multiplicationTable()


def withCommandLineArg():
    '''
    DAy6:
    question number 2
    '''
    import sys
    fd = open(sys.argv[1],'w')
    # z = ['%d X %d = %d'%(int(sys.argv[2]),i,int(sys.argv[2])*i) for i in range(1,10)]
    fd.write('\n'.join(['%d X %d = %d'%(int(sys.argv[2]),i,int(sys.argv[2])*i) for i in range(1,10)]))
    #fd.close()

#withCommandLineArg()

class BankAccount:
    '''
    Day7
    Question 3
    '''
    def __init__(self):
        self.accountData = {
            '10001' : {'balance':0,'type':'saving','name':'Rahul','address':'Meerut'},
            '10002' : {'balance':0,'type':'saving','name':'Khan','address':'Delhi'},
            '10003':{'balance':0,'type':'current','name':'Ganga','address':'Mumbai'},
            '10004':{'balance':0,'type':'saving','name':'Jaan','address':'Meeur'},
            }
        print(self.accountData['10001'])
    def deposit(self):
        amount = int(input("Enter amount to deposit:"))
        accountNumnber = input("Enter Account Number:")
        self.accountData[accountNumnber]['balance'] = self.accountData[accountNumnber]['balance'] + amount
        print("Amount %d Deposited Sucessfully" %(amount))
    
    def withdraw(self):
        amount = int(input("Enter amount to Withdraw:"))
        accountNumnber = input("Enter Account Number:")
        self.accountData[accountNumnber]['balance'] = self.accountData[accountNumnber]['balance'] - amount
        print("Amount %d  withdrwal Sucessfully"%(amount))
    
    def accountDetail(self):
        accountNumnber = input("Enter Account Number:")
        print("*****************Accont Detail*************")
        print("Account Number:",accountNumnber)
        print("Name:",self.accountData[accountNumnber]['name'])
        print("Type:",self.accountData[accountNumnber]['type'])
        print("Balance:",self.accountData[accountNumnber]['balance'])
        print("Address:",self.accountData[accountNumnber]['address'])
        print("***************End**************************************")

    def settingAccount(self):
        print("1: for Edit Name")
        print("2: for Edit Account Type")
        print("3: for Edit Address")
        num = int(input("Enter Choise:"))
        accountNumnber = input("Enter Account Number:")
        if accountNumnber not in self.accountData:
            print("Account Number not found:")
            return 0
        if num == 1:
            name = input("Enter name for updation:")
            self.accountData[accountNumnber]['name'] = name
            print("Updated Sucessfully")
        elif num == 2:
            name = input("Enter account Type for updation:")
            self.accountData[accountNumnber]['type'] = name
            print("Updated Sucessfully")
        elif num == 3:
            address = input("Enter address  for updation:")
            self.accountData[accountNumnber]['address'] = address
            print("Updated Sucessfully")
        else:
            print("Plz select above numner")
        
    def createNewAccount(self):
        #'10001' : {'balance':0,'type':'saving','name':'Rahul','address':'Meerut'},
        name = input("Enter Your Name:")
        address = input("Enter your address:")
        newData = {'balance':0,'type':'saving','name':name,'address':address}
        l1 = self.accountData.keys()
        num = int(max(l1))
        newAccountNUm = str(num + 1)
        self.accountData[newAccountNUm] = newData
        print("Account Created Sucessfully")

    def allAcount(self):
        print(self.accountData)



    



s1 = BankAccount();
n = 1
while n != 0:
    print("****************************")
    print("1: Account Detail")
    print("2: Deposit")
    print("3: withdraw")
    print("4: Update Detail")
    print("5: Create New Account")
    print("6: Show All Account")
    
    print("0: Exit")
    n = int(input("Enter choise:"))
    if n == 1:
        s1.accountDetail()
    elif(n == 2):
        s1.deposit()
    elif(n == 3):
        s1.withdraw()
    elif(n == 4):
        s1.settingAccount()
    elif(n == 5):
        s1.createNewAccount()
    elif(n == 6):
        s1.allAcount()
    elif n == 0:
        break;
    else:
        print("Plz select Above Option")




    
    
    