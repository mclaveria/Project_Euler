#Michael Claveria
#Project Euler Problem 9

'''
A pythagorean triplet is a set of natural numbers: a, b, c such that a^2 + b^2 = c^2
for example 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one pythagorean triplet such that a + b + c = 1000
Find the product abc
'''
import itertools
#For any triangle, the largest side can't be longer than the sum of the other two sides
#So c is under 500

#Note this is pretty horrible and inefficient code
#Please refactor this to look nice later

def pyTri(summ):
    top = int((summ/2))
    bot = int((summ/4))
#    abot = int((summ/5))
    for a,b,c in itertools.product(range(0, top), range(bot, top), range(bot, top)):
        #print(str(a) + ' ' + str(b) + ' ' + str(c))
        if ((a**2 + b**2 == c**2) and (a + b + c == summ)):
            print('py trip found for ' + str(a) + ' ' + str(b) + ' ' + str(c))
            prod = a * b * c
            print('Product is: ' + str(prod))
            break
    print('reached end')
    
pyTri(1000)