#Michael Claveria
#Project Euler 15

'''
Starting at the top left corner of a 2x2 grid and only going right or down, there are 6 paths 
to the lower right corner

How many paths are there to a 20x20 grid?
'''
import math
#This problem doesn't need much programming
#Think of this as finding the combinations of going either right(r) or down(d)

#For 1 x 1 there is only r-d or d-r

#For 2 x 2 there are two rs needed and 2 ds needed
#r-r-d-d, r-d-r-d, r-d-d-r, d-r-r-d, d-r-d-r, d-d-r-r

#basically this is a problem of choosing n rs out of 2n total or 2n choose n
#for n x n grid there are (2 * n)!/(n! * n!)
#The answer should be 

def latPath(n):
    #Get number of values using factorials
    print('For ' + str(n) + 'x' + str(n) + ' grid')
    return int(math.factorial(2*n) / math.factorial(n) / math.factorial(n))

#print(str(latPath(2)))
#print(str(latPath(3)))
print(str(latPath(20)))


