import re
def isInteger(digit):
    pattern = r'^\d+$'
    if re.search(pattern, digit):
        return True
    else:
        return False
#Check Number is float
def isFloat(digit):
    pattern = r'^\d+\.\d+$'
    if re.search(pattern, digit):
        return True
    else:
        return False

def hasVowel(text):
    pattern = r'[aeiou]'
    if re.search(pattern, text):
        return True
    else:
        return False

def checkDate(text):
    #DD-MM-YYYY
    pattern = r'\d{2}-\w{2}-\d{4}$'
    if re.search(pattern, text):
        return True
    else:
        return False
def isValidPassword(password):
    #True is the given string containas - 8 to 16 alphanumerics,at least 2 digits,at least 2 lowercase letters
	#and atleast two uppercase letters  
    regexPattern = r'(?=.*[a-z].*[a-z].*)(?=.*[A-Z].*[A-Z].*)(?=.*[0-9]{2}.*)\w{8,16}'

def isValidEmail():
    pattern = '^[a-zA-z0-9-+\.]+\@[a-z]+\.[a-z]{2,5}$'
    if re.search(pattern, text):
        return True
    else:
        return False

def replaceSpace(inputStr):
    pattern = '\s+'
    result = re.sub(pattern,' ', inputStr)
    return result
#print("Integer:",isInteger("5454wdwsd"))
#print("Float:",isFloat("25.30"))
#print("Has Vowel:",hasVowel("khnnjjn"))
#print("Date format:",checkDate("2015-05-20"))
print("Result:",replaceSpace("taukir   khan   is here"))
