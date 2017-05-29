#Michael Claveria
#Problem 41 Pandigital prime
'''
What is the largest n digit pandigital prime that exists?
'''
import itertools
    
#check if a number is prime
def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    #Even numbers are not prime
    if n % 2 == 0:
        return False
    #check for divisibility of odd numbers up to sqrt of n
    for i in range(3, int(n**.5 + 1), 2):
        if n % i == 0:
            return False
    return True

#Generate pandigital permutations using itertools
def genPandigital(strg):
    return list(itertools.permutations(strg))

#Find the largest pandigital prime of length n
def findLargestPandPrime(strg):    
    test = genPandigital(strg)
    track = -1
    for i in range(0,len(test)):
        check = int(''.join(test[i]))
        if isPrime(check):
            #print ('The value', check, 'is prime')
            track = check
    return track
    
print(findLargestPandPrime('123456789'))
print(findLargestPandPrime('12345678'))
print(findLargestPandPrime('1234567'))