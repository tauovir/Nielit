import numpy as np
def greatestAmongThree():
    '''
    Day2:
    Write a function to find the gretest number among three given numbers.
    '''
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    num3 = int(input("Enter Third Number:"))
    #First Appraoch
    # list1 = [num1,num2,num3]
    # print("********Before sort*******")
    # print(list1)
    # print("*****After Sordt******")
    # list1.sort()
    # print(list1)
    # print("Greastest Number:",max(list1))
    #**********Second Appriach***********
    # ndArr = np.array([num1,num2,num3])
    # print(ndArr)
    # print("Greatest Number:",ndArr.max())
    #*******Thisr Appraoch**********
    if num1 >= num2 and num1 >= num3:
        print("Greatest:",num1)
    elif num2 >= num1 and num2 >= num3:
        print("Greatest Num:",num2)
    else:
        print("Greatest:",num3)
    
def decendingOrder():
    '''
    Day2
    Write a script to print numbers in descending order starting 
    '''
    num = int(input("Enter Start Number:"))
    list1 = [x for x in range(num,100)]
    list1.sort(reverse = True)
    print(list1)

def factorial(num):
    '''
    Day2
    Write a script to print factorial of a number (without using loop).
    '''
    if num == 0 or num == 1:
        return 1
    fact1 = num * factorial(num - 1)
    return fact1

def checkPrime():
    '''
    DAY2
    Write a script to check whether an input number is prime or not.
    '''
    num = int(input("Enter number to check prime:"))
    i = 2
    flg = 1
    while i < num/2:
        if num % i == 0:
            flg = 0
        i = i +1
    print("Flag",flg)
    if flg == 1:
        print("Number is prime")
    else:
        print("Number is not prime")

    
def reverseStr():
    '''
    Day3:
     Write a program to reverse a given string.
     '''
    print("Reverse")
    l1 = []
    str1 = input("Enter String:")
    st = ""
    for ch in str1:
        st = ch + st
    print(st)
    print(str1[::-1]) # Second Approach

def occurenceOfChar():
    '''
    Day3
    Write a program to print the no. of occurences of a given character in a given string.
    '''
    text = input("Enter string:")
    containner = dict()
    list1 = []
    for ch in text:
        if ch in list1:
            containner[ch] = containner[ch] + 1
        else:
            list1.append(ch)
            containner[ch] = 1
    print("*********Occurence of Charecter********")
    print(containner)

def atleastTwoVowel():
    '''
    Day3:
    Write a program to check for at least two vowels in a given string. 
    '''
    text = input("Enter string:")
    vowelList = ['a','e','i','o','u']
    i = 0
    for ch in text:
        if ch in vowelList:
            i += 1
    if i >= 2:
        print("Exptected String")
    else:
        print("Atleast Two vowel Required")

def reverseWord():
    '''
    Day4:
    Write a script to reverse a given sentence without reversing words.
    '''
    sentence = input("Enter sentence:")
    reverseWord = ""
    for word in sentence.split(" "):
        reverseWord = word +" " + reverseWord
    print("Reverse Words:",reverseWord)
    #Second Approach
    wordList = sentence.split(" ")
    print("Reverse Words:",wordList[::-1])

def numberOfPalindrom():
    '''
    Day4:
     Write a script to print the no. of palindrome words in a given sentence.
    '''
    sentence = input("Enter sentence:")
    count = 0
    listofWords = sentence.split(" ")
    for word in listofWords:
        reverseWords = word[::-1]
        if reverseWords == word:
            count += 1
    print("No: of Palindrom in sentence:",count)

def countLettersUsingDict():
    '''
    Day4:
     Write a script to count letters in a given string(using dict).
     Write a script to count words in a given sentence (using dict).
     '''
def divident(divident,divisor = 2):
    '''
    Day5:
    Question number 1,2
    '''
    x = divident / divisor
    reminder = divident % divisor
    return reminder,round(x,2)

def importModule():
    '''
    Day5:
    Third Question
    '''
    from importlib import reload
    n = 1
    while n != 0:
        print("**************************************")
        print("1. Initialize")
        print("2. Show ")
        print("3. Reload")
        print("0. Exit")
        n = int(input("Enter your choise:"))
        if n == 1:
            import module1 as md
            print("Module Imported successfully")
            
        elif n==2:
            con = md.a + 10 * md.b * md.c - 5 * md.d / md.e
            print("Resull:",con)
        elif n== 3:
            md = reload(md)
            print("Reloaded Sucessfully")
        elif n == 0:
            print("See you again,bye bye")
        else:
            print("Plz select abouve number")


#greatestAmongThree()
#decendingOrder()
#print(factorial(num=7))
#checkPrime()
#reverseStr()
#occurenceOfChar()
#atleastTwoVowel()
# reverseWord()
# numberOfPalindrom()
#print("Result:",divident(divident = 10,divisor = 3))
importModule()