#Michael Claveria
#Problem 10 

'''
Find the sum of all all prime numbers under 2 million

'''
#Note first implementation too slow to calculate 2 million, use yield 

def primeNum(n):
    #keep track of composite numbers
    if n < 0:
        raise ValueError("Value must be 0 or greater")
    if n >= 2:
        yield 2
    #Set top limit of multiples to sqrt of n
    top = int(n ** .5 + 1)
    #Initialize all numbers 2 or greater to true state
    isPrime = [False, False] + [True] * (n - 2)
    #Check over all odd starting from 3
    for i in range(3, n, 2):
        if isPrime[i] is False:
            continue
        yield i
        # remove add multiples of existing primes to composite list
        if i <= top:
            for j in range (i * 3, n, i<<1):
                isPrime[j] = False 

print(sum(primeNum(2000000)))