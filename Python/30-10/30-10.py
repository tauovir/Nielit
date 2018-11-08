d1 = dict()
d1 = {'name':'khan','salary':1000,'phone':'8010339935'}
print(d1)
key = d1.keys()
val = d1.values()
print(key)
print(val)


lt = [('khan',20),('pathan',1001),('bana',500)]
print(lt)

d2 = dict(a=20,b=60,c=50)
print(d2)

d3 = dict(lt)
print(d3)

print(d3['khan'])
d3['khan'] = 501
print(d3['khan'])

#print(d1)
#print(d1.pop('salary'))

print(d1.items())
d1.clear()

print(d1)

#Reverse a given sentance without reversing words
def reverseSentance():
    stmt = input('enter sentance=')
    str = stmt.split(' ')
    result = ' '.join((str[::-1]))
    print(result)
#reverseSentance()   

#Print Number of palindrom words in given sentence
def palindrom():
    stmt = input('enter sentence to check palindrom=')
    str = stmt.split(' ')
    sum = 0
    for word in str :
        if word == word[::-1]:
            sum = sum + 1
    print("Number of Plaindrom words",sum)
#palindrom()

#Count Letter of Given String
def letterCount():
    str = input('enter any string to count letter')
    dic = dict()
    for ch in str :
        if ch in dic:
            dic[ch] =  dic[ch] + 1
        else:
             dic[ch] =  1
    print(dic)
    
#letterCount()

#Count Words of Given sentence
def wordCount():
    stmt = input('enter any sentence to count letter')
    dic = dict()
    str = stmt.split(' ')
    for word in str :
        if word in dic:
            dic[word] =  dic[word] + 1
        else:
             dic[word] =  1
    print(dic)
    
wordCount()



