#Michael Claveria
#Problem 21
'''
Amicable numbers

Evaluate the sum of the Amicable numbers under 10000

Amicable numbers are numbers where the sum of the proper divisors d(a) = b and d(b) = a for different
numbers a and b

For example d(220) = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
d(284) = 1 + 2 + 4 + 71 + 142 = 220
So 220 and 284 are amicable numbers
'''
#Write function to get proper divisors of an integer n
def propDivisors(n):
    half = int(n/2) + 1
    for i in range(1, half):
        if n % i == 0:
            yield i

#amiableTest is a function that return true if two numbers are amicable and false if they are not
def amicableTest(a, b):
    sum1 = sum(propDivisors(a))
    #print(str(sum1))
    sum2 = sum(propDivisors(b))
    #print(str(sum2))
    if (b == sum1 and a == sum2 and a != b):
        return True
    else:
        return False

#amicableSum adds up all amicable numbers less than the input n
def amicableSum(n):
    total = 0
    for i in range(1, n):
        mySum = sum(propDivisors(i))
        if amicableTest(i, mySum) is True:
            print(str(i) + ' and ' + str(mySum) + ' are amicable numbers')
            total += i
    return total

#print(str(amicableSum(10000)))       
            
        