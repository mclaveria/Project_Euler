#Michael Claveria
#Project Euler 32

'''
Find the sum of all products whose multiplicand, multiplier, product identity can
be written as 1 - 9 pandigital
For example 39 x 186 = 7254, is a multiplicand, multiplier and product identity that is 1-9
pandigital
'''

#determine if a number numb is 1-9 pandigital

#print(sorted(str(798123465)))

#print([str(x) for x in range(1,10)])



def isPandigital(numb,n):
    #Pandigital must have number length equal to n and be equivalent to the first 1 - n digits when sorted
    if len(str(numb)) == n and sorted(str(numb)) == [str(x) for x in range(1, n + 1)]:
        return True
    else:
        return False

def getPropDivisors(n):
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            yield i

'''
print(isPandigital(123,3))
print(isPandigital(123,4))
print(isPandigital(15423,5))
print(isPandigital(15523,5))
print(isPandigital(391867254,9))
print(isPandigital(399867254,9))
'''

#Combine three numbers multiplicand, multiplier and product into one large number            
def combineProd(mult1, mult2, prod):
    return int(str(mult1) + str(mult2) + str(prod))


#print(combineProd(50,60,300))

def findProducts(bot, top, pandig):
    counter = 0
    for i in range (bot, top + 1):
        divs = getPropDivisors(i)
        for mult in divs:
            full = combineProd(mult, int(i / mult), i)
            if isPandigital(full, pandig):
                counter += i
                break
    print('Final result is', counter)

findProducts(1234, 9876, 9)