#Project Euler Problem 5
#Michael Claveria

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from collections import Counter

#for i in range (1,21):
    
#2, 3, 5, 7, 11, 13 17, 19

#4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20

primList = [2, 3, 5, 7, 11, 13, 17, 19]

#create function to get the prime factorization of a number

def pfact(val):
    for p in primList:
        while (val % p == 0):
            yield p
            val = val//p
            if (val == 1):
                return
            
#find the largest exponent value for each prime factorization for numbers from 1 - 20
mlist = []
for i in range(2,21):
    mlist = Counter(mlist) | Counter(list(pfact(i)))
  
print(mlist)
#Result is on next line below
#Counter({2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1})

#multiply together the largest exponent values
test = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print(str(test))