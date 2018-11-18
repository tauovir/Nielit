import re
'''
@Description: This function used to identify whether it is Integer or not
'''
def isInteger(inputStr):
    regexPattern = r'^[0-9]+$'
    try:
        patternObj = re.compile(regexPattern)
        #print patternObj.pattern
        if re.match(patternObj, inputStr):
            return True
        return False
    except Exception,e:
        print "Exception occure=",e
'''
@Description: This function used to identify whether it is Float or not
'''
def isFloat(inputStr):
    regexPattern = r'^[0-9]+\.+[0-9]+$'
    try:
        patternObj = re.compile(regexPattern)
        #print patternObj.pattern
        if re.match(patternObj, inputStr):
            return True
        return False
    except Exception,e:
        print "Exception occure=",e
'''
@Description: This function used to identify whether input string contain vowel or not
'''
def hasVowel(inputStr):
    regexPattern = r'[aeiou]'
    try:
        patternObj = re.compile(regexPattern)
        print patternObj.pattern
        if re.match(patternObj, inputStr):
            return True
        return False
    except Exception,e:
        print "Exception occure=",e
'''
@Description: This function used to identify whether date is in correct formate or not
'''
def checkDate(inputStr):
    regexPattern = r'^\d{2}-\d{2}-\d{4}$'
    try:
        patternObj = re.compile(regexPattern)
        #print patternObj.pattern
        if re.match(patternObj, inputStr):
            return True
        return False
    except Exception,e:
        print "Exception occure=",e
'''
@Description: This function used to identify whether password is in correct
format or not
'''        
def isValidPassword(inputStr):
    regexPattern = r'(?=.*[a-z].*[a-z].*)(?=.*[A-Z].*[A-Z].*)(?=.*[0-9]{2}.*)\w{8,16}'
    try:
        patternObj = re.compile(regexPattern)
        print patternObj.pattern
        if re.match(patternObj, inputStr):
            return True
        return False
    except Exception,e:
        print "Exception occure=",e
'''
@Description: This function used to identify whether email is valid or not
'''     
def isValidEmial(inputStr):
    regexPattern = r'^([0-9a-z_\.-]+)@([0-9a-z_\.-]+)\.([a-z0-9\.]{2,6})+$'
    try:
        patternObj = re.compile(regexPattern)
        print patternObj.pattern
        if re.match(patternObj, inputStr):
            return True
        return False
    except Exception,e:
        print "Exception occure=",e
        
#print isInteger('80ddd')
#print isFloat('8.520')              
#print hasVowel('khan')  #not working
#print checkDate('02-06-2018')
#print isValidPassword('taukirKhaN115')
print isValidEmial('taukir707@gmail.com')



