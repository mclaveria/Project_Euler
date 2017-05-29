#Michael Claveria
#Project Euler Problem 12

#Find value of first triangle number with 500 divisors

#Pseudocode
#Write function to produce triangle numbers
#Write function to calculate divisors of a number

import math
#sum of 1 + 2 + 3 + ... + n = n * (n + 1) / 2
def triNum(n):
    res = int( n * (n + 1) / 2)
    return res

def divisors(n):
    # search from 1 to sqrt of divisors
    limit = math.ceil(n**.5)
    total = 0
    for i in range(1, limit):
        if n % i == 0:
            #add 2 to total for a and b where a x b = n
            total += 2
    #additional check if the number is square then add 1, example 36 has 6 as square root
    if limit * limit == n:
        total += 1
    return total


def getTri(numDiv):
    for i in range(1, 100000, 1):
        print('Index: ' + str(i) + ', Num: ' +  str(triNum(i)) + ', divisors: ' + str(divisors(triNum(i))))
        if divisors(triNum(i)) >= numDiv:
            return triNum(i)

print(str(getTri(500)))
