#Michael Claveria
#Problem 024 Project Euler

'''
Find the 1,000,000th lexicographic (ordered) permutation of the digits 0 to 9
'''

import itertools

#Find the permutations of the digits 0 to 9 using itertools.permutations
test = itertools.permutations('0123456789')
#Find the 1,000,000th permutation using itertools.islice
test2 = itertools.islice(test, 999999, 1000000)

for i in test2:
    print(i)