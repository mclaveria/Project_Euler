#Michael Claveria
#Circular primes



def rotate(strg, n):
    return strg[n:] + strg[:n]

#get a list of all rotations of digits for a number n 
def getRotations(strg):
    lst = []
    n = len(strg)
    for i in range(n):
        lst.append(rotate(strg, i))
    return lst

'''
test = '987654'

numlist = getRotations(test)

for i in numlist:
    print(i)
'''

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

#isCircular calculates if n is a circular prime number, returns true if circular prime
#otherwise returns false
def isCircular(n):
    rots = getRotations(str(n))
    for i in rots:
        if isPrime(i) is False:
            return False
    return True
'''
for i in range(1,101):
    if isCircular(i):
        print(i)
'''

def countCPrimes(rng):
    counter = 0
    for i in range(2, rng + 1):
        if isCircular(i):
            counter += 1
    print (counter)

countCPrimes(1000000)
