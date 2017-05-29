#Michael Claveria
#Problem 30 Project Euler

'''
Find the sum of all numbers that can be written as the sum of the
fifth powers of the digits
'''


def sumOfPowerDigits(n, power):
    mySum = 0
    numString = str(n)
    for i in numString:
        mySum += int(i)**power
    return mySum

def sumOfFifthPower(low, high):
    counter = 0
    for i in range(low, high):
        if sumOfPowerDigits(i,5) == i:
            #print(i)
            counter += i
    return counter

print(sumOfFifthPower(2, 1000000))