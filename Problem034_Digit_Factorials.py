#Michael Claveria
#Digital factorials

'''
Find the sum of all numbers that are equal to the sum of the factorials of the digits
'''

import math

#get the sum of the digit factorials of a number n
#for example 145 is 1! + 4! + 5! = 1 + (4 * 3 * 2 * 1) + (5 * 4 * 3 * 2 * 1) = 145
def digFactorial(n):
    nString = str(n)
    fSum = 0
    for i in nString:
        fSum += math.factorial(int(i))
    return fSum

#Count the number of curious numbers from 3 to span
def findCurious(span):
    cSum = 0
    for i in range(3, span + 1):
        if digFactorial(i) == i:
            print(i)
            cSum += i
    return cSum

print('final sum is', findCurious(1000000))
