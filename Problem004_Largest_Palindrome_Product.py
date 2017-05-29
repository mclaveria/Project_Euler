#Project Euler Problem 4
#Michael Claveria

'''
A palindromic number reads the same both ways. 

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#The largest possible product of two 3 digit numbers is 999 x 999 = 998001

def isPalindrome(num):
    #convert number to string
    #reverse string
    #check that string is the same when reversed
    myStr = str(num)
    revStr = myStr[::-1]
    #print(revStr)
    if myStr == revStr:
        return True
    else:
        return False

def prodThree():
    numList = ''
    for i in range(900 , 999):
        for j in range (900 , 999):
            if (isPalindrome(i*j)):
                numList += str(i*j)+' '
    print(numList)
        

prodThree()