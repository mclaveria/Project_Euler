#Michael Claveria
#Project Euler Problem 6

'''
Sum of squares of first 10 numbers is:
1^2 + 2^2 + ... + 10^2 = 385

Square of sum of first 10 numbers is:
(1 + 2 + 3 + ... + 10)^2 = 55^2 = 3025

The difference is 3025 - 385 = 2640

Find the difference between the sum of squares of the first 100 natural numbers and the square of the sum
'''

#Sum of squares of first 100 numbers

def sumSq (rng):
    return sum(i ** 2 for i in rng)

x = range(101)
xSumSq = sumSq(x)

#Square of sum of first 100 numbers

def sqSum (rng):
    return sum(rng) ** 2

y = range(101)
ySqSum = sqSum(y)

#Calculate difference
diff = abs(xSumSq - ySqSum)

print(diff)