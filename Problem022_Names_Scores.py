#Michael Claveria
#Problem 22 Project Euler

'''
Calculate the namescore of all names in the file

'''

import re

txt = 'Problem022_names.txt'


#Parse file looks for all instances of names between two double quotes in a text file
#It returns a list of names in string form

def parseFile(txt):
    #test string is a regular expression that looks for the values between two double quotes
    testString = r'\"(.+?)\"'
    try:
        f = open(txt, 'r')
    except OSError:
        print('Can\'t open file:', txt)
    for line in f:
        results = re.findall(testString, line)
    f.close()
    return results

myList = parseFile(txt)
#sortList = sorted(myList)
#testList = ['MARY', 'POPPINS','SOFRESH', 'AND', 'SOCLEAN']

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

def namesScore(myList):
    sortList = sorted(myList)
    score = 0
    for i in sortList:
        score += ((sortList.index(i) + 1) * charSum(i))
        #print(str((sortList.index(i) + 1)))
        #print(str(i))
        #print(str(charSum(i)))
    return score

print(namesScore(myList))

