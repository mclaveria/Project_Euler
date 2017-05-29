#Michael Claveria
#Project Euler 39 Integer Right triangles

'''
find the perimeter value p, with p <= 1000 for a right triangle with integer lengths a,b,c
that contains the most number of solutions that add up to that perimeter
'''

def isRightTri(a, b, c):
    if a ** 2 + b ** 2 == c ** 2 and a!= 0 and b != 0 and a < b < c:
        return True
    else:
        return False

#Find the number of integer solutions for the lengths of a right triangle that
#add up to a certain perimeter p value
def findSolutions(p):
    count = 0
    low = int(p / 3)
    high = int(p / 2)
    for c in range(low, high):
        for b in range(low, c):
            for a in range(low):
                if isRightTri(a, b, c) and a + b + c == p:
                    print('a =', a, 'b =', b, 'c =', c)
                    count += 1
    return count

    
def getMost(max_p):
    m_sol = 0
    #solutions for max p must be even integer and best are multiples of 120
    for p in range(120, max_p + 1, 120):
        res = findSolutions(p)
        print('for p =', p, 'num of solutions is', res)
        if res > m_sol:
            m_sol = res
            best = p
    print(best)

getMost(1000)