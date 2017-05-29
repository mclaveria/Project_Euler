#Michael Claveria
#Problem 23 Non Abundant sum

'''
Find the sum of all positive integers that can't be written as the sum of two abundant numbers

'''
import numpy

def propDivisors(n):
    half = int(n/2) + 1
    for i in range(1, half):
        if n % i == 0:
            yield i

#isAbundant takes an integer n as input
#calculates the sum of the proper divisors of n
#returns true if the sum of the proper divisors of n is greater than the number n
def isAbundant(n):
    #use propDivisors method to calculate proper divisors of n
    nDiv = propDivisors(n)
    divSum = sum(nDiv)
    if divSum > n:
        return True
    else:
        return False

#findAbundant returns a list of all abundant numbers less than n
def findAbundant(n):
    lst = []
    for i in range(n):
        if isAbundant(i) is True:
            #print(i)
            lst.append(i)
    return lst

abNumList = findAbundant(28124)


#for i in abNumList:
    #print(str(i))

#Get all the numbers that are sums of abundant numbers
#return a list that sets all abundant number sums to 1 and others to 0
def abNumSumList(abList1, abList2, maxVal):
    zeroList = numpy.zeros(28124)
    for x in abList1:
        for y in abList2:
            if x + y < maxVal:
                #print(x + y)
                zeroList[x + y] = 1
    return zeroList

myZeroList = abNumSumList(abNumList, abNumList, 28124)

#interate over the list of sums and add all those that aren't abundant sums
nonSum = 0
for i in range(28124):
    if myZeroList[i] == 0:
        #print(i)
        nonSum += i

print('Final result is', nonSum)