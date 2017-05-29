#Project Euler Problem 1
#Michael Claveria

'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sumOfMult (int1, int2, rng):
    res = 0
    for i in range(rng):
        if(i % int1 == 0 or i % int2 == 0):
            res += i
    print('The sum of multiples of', int1, 'and', int2, 'below',\
          rng,'is', res)

sumOfMult(3, 5, 1000)

