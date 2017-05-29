#Michael Claveria
#Reciprocal cycles

#if a prime p is both a full reptend prime and a safe prime then 1/p will produce 
#a stream of p - 1 repeating digits

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

#A safe prime is a prime number 2p + 1 where p is also a prime
#safePrime is a function that determines if an integer n is a safe prime
def safePrime(n):
    if isPrime(n) and isPrime((n - 1) / 2):
        return True
    else:
        return False

#print(safePrime(5))
#print(safePrime(971))
#print(safePrime(983))

#Found online list of reptend primes under 1000
reptendList = [7, 17, 19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 167, 179, 181, 193,\
               223, 229, 233, 257, 263, 269, 313, 337, 367, 379, 383, 389, 419, 433, 461,\
               487, 491, 499, 503, 509, 541, 571, 577, 593, 619, 647, 659, 701, 709, 727,\
                743, 811, 821, 823, 857, 863, 887, 937, 941, 953, 971, 977, 983]

#get list of prime numbers under 1000 that are reptend and safe primes
primesUnder1000 = []

def pMinusOneRepeatPrimes(repList, alist):
    for x in repList:
        if safePrime(x) is True:
            alist.append(x)

pMinusOneRepeatPrimes(reptendList, primesUnder1000)

print(max(primesUnder1000))




    
