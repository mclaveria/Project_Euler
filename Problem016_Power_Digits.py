#Michael Claveria
#Project Euler 16

'''
2^15 = 32768 and the sum of the digits is 3 + 2 + 7 + 6 + 8 = 26

Find the sum of the digits of 2^1000

'''

def twoPow(n):
    return 2**n

def digCount(n):
    count = 0
    while n:
        #add last digit to count and 
        count, n = count + n % 10, n // 10
    return count

print(str(digCount(twoPow(1000))))