#Michael Claveria
#Problem 27


#create function to check if a number n is prime
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

def numConsecutivePrimes(a, b):
    count = 0
    for n in range(100):
        eqat = n**2 + (a * n) + b
        if isPrime(eqat):
            count += 1
        else:
            break
    return count

print(numConsecutivePrimes(1, 41))
print(numConsecutivePrimes(-79, 1601))        
            
def findMostConsecPrimes():
    for i in range(-999,1000):
        for j in range(-1000,1001):
            if (numConsecutivePrimes(i,j) > 39):
                print("a is ", i, "b is ", j, "total is: ", numConsecutivePrimes(i,j))
        
findMostConsecPrimes()