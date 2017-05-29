#Michael Claveria
#Project Euler Problem 7

'''
What is the 10001st prime number?

'''

#use sieve of Erastosthenes to calculate prime numbers in an efficient way
#sieve takes a prime and removes all multiples of that prime then goes to next prime

def nthPrime(n):
    span = 12*n
    #keep track of composite numbers
    isPrime = [False, False] + [True] * span
    count, fin = 0, 0
    top = int( span ** .5 + 1 )
    if n >= 1:
        count += 1
    #span is highest value used to calculate the nth prime, using 12 times the nth prime
    
    for i in range(3, span, 2):
        if (isPrime[i] is False):
            continue
        count+=1
            #stop calculation when the prime number count reaches the desired number
        if count == n:
            fin = i
            print('prime count is: ' + str(count))
            print('Value of ' + str(n) + 'th prime is: ' + str(fin))
            break
        #print(i)
        if i <= top:
            for j in range(i * 3, span, i<<1):
                isPrime[j] = False
       
nthPrime(10001)  
    