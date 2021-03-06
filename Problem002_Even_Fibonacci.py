#Project Euler Problem 2
#Michael Claveria

'''
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms
'''

def evenFib (n):
    a, b, res = 0, 1, 0
    while (a < n):
        #add even fibonnaci numbers to result
        if (a % 2 == 0):
            res += a
        a, b = b, a + b
    
    print(str(res))

evenFib(4000000)