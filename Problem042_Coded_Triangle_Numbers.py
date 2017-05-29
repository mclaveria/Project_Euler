#Michael Claveria
#Problem 042

import re

txt = 'Problem042_words.txt'

def readText(txtFile):
    #testString is a regular expression that looks for the values between two double quotes
    testString = r'\"(.+?)\"'
    try:
        f = open(txt, 'r')
    except OSError:
        print('Can\'t open file, txt')
    for line in f:
        results = re.findall(testString, line)
    f.close()
    return results
    
wordList = readText(txt)

#charSum takes a string, converts each character in the string to a number and returns
#the value of the sum of those numbers
#the numerical conversion is A = 1, B = 2, .... Z = 26
#Note, this only works for names with all Caps
#example: 
def charSum(string):
    counter = 0
    for char in string:
        num = ord(char) - 64
        #print(char)
        #print(str(num))
        counter += num
    return counter

#get the first n triangle numbers
def getTriangle(n):
    myList = []
    for i in range(1, n+1):
        myList.append(int((i * (i + 1)) / 2))
    return myList
        

#Find number of triangle numbers in list
#note the largest value in list is 192 which is less than triangle number 20: 210
def findNumberofTriNum(lst):
    triList = getTriangle(20)
    counter = 0
    for entry in lst:
        if charSum(entry) in triList:
            counter += 1
    return counter

print(findNumberofTriNum(wordList))
        
'''
tracker = 0
for entry in wordList:
    if charSum(entry) > tracker:
        tracker = charSum(entry)
print (tracker)
    #print(entry, charSum(entry))

a = getTriangle(20)
for i in a:
    print(i)
'''    
