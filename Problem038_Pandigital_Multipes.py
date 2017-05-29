#Michael Claveria
#Pandigital Multipes Problem 38

'''
What is the largest pandigital 9 digit number that is a concatinated
product of an integer and (1, 2, ..., n)
'''

#Since the concatinated product of 9 and (1, 2, 3, 4, 5) is 918273645
#to get a larger value it must be that the number is 9xxx and (1, 2)
#because 9xx and (1, 2, 3) won't be a pandigital 9 digit number and 
#any other value will also not give 9 digits when concatinated

#check if a number is pandigital

def isPandigital(numb,n):
    #Pandigital must have number length equal to n and be equivalent to the first 1 - n digits when sorted
    if len(str(numb)) == n and sorted(str(numb)) == [str(x) for x in range(1, n + 1)]:
        return True
    else:
        return False
    
def combineProd(numb):
    #return int(str(mult1) + str(mult2) + str(prod))
    return int(str(numb) + str(numb * 2))


def findPanCat(n):
    tracker = 0
    for i in range(9123, 9877):
        value = combineProd(i)
        if isPandigital(value, n) and value > tracker:
            print(i, 'has a value of', value)
            tracker = value
    return tracker

print('Final result is', findPanCat(9))
            
        
    