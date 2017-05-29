#Michael Claveria
#Problem 37 Truncatable primes

'''
Find the sum of the only 11 eleven primes that are truncatable
left to right and right to left
Note: 2, 3, 5, 7 are not considered truncatable primes
'''

def truncLeft(strg, n):
    return strg[n:]

def truncRight(strg, n):
    return strg[:n]

#print(truncLeft('3797', 1))
#print(truncRight('3797', 3))

#Get all the truncatable combinations of a number string, both left
#and right including the string itself
def getTruc(strg):
    lst = [strg]
    n = len(strg)
    for i in range(1, n):
        lst.append(truncLeft(strg, i))
        lst.append(truncRight(strg, i))
    return lst

trunc = getTruc('3797')

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

#check if all the truncations of a number n are prime
def isTruncPrime(n):
    testList = getTruc(str(n))
    for i in testList:
        if isPrime(i) is False:
            return False
    return True

#find the sum of all 11 truncatable primes
def findTruncPrimes():
    primeList = []
    count = 0
    for i in range(9, 100000000, 2):
        if isTruncPrime(i):
            #print(i)
            primeList.append(i)
            count += i
        #Stop when the list hits all 11 truncatable primes
        if len(primeList) == 11:
            return count
        
print('Sum is:', findTruncPrimes())