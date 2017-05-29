#Michael Claveria
#Project Euler Problem 20
'''
Find the sum of the digits of the number 100!


'''
import math

def sumOfFactorialDig(n):
    numString = str(math.factorial(n))
    #print(numString)
    counter = 0
    for i in numString:
        counter += int(i)
    print(counter)

sumOfFactorialDig(100)