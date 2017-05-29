#Project Euler Problem 3
#Michael Claveria

from math import sqrt, floor

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#Only have to check prime numbers less than sqrt of number

def primeFactors(num):
    myList = []
    top = floor(sqrt(num))
    for i in range(2,top):
        if (num % i == 0 and isPrime(i)):
            myList.append(i)
    return myList
 
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
   
#for val in primeFactors(600851475143):
#    print(str(val))
    
pfList = primeFactors(600851475143)
result = str(max(pfList))
print(result)
