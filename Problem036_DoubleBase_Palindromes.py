#Michael Claveria
#Find the sum of all numbers up to 1,000,000 that are palindromes in base 10 and base 2


#Check if a string is a palindrome by comparing it to its reverse
def isPalin(strg):
    if strg == strg[::-1]:
        return True
    else:
        return False
    
#print(isPalin('5005'))
#print(str(bin(101))[2:])

def sumPalin(maxim):
    counter = 0
    for i in range(1, maxim + 1):
        #add number if it is a palindrome in base 10 and in base 2
        if isPalin(str(i)) and isPalin(str(bin(i))[2:]):
            counter += i
    return counter
        
print(sumPalin(1000000))