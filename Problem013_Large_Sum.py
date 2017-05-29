#Michael Claveria
#Project Euler 13 Large sum

'''
Find sum of one-hundred 50-digit numbers
'''

def sumLarge(txt):
    mySum = 0
    #read file
    f = open(txt, 'r')
    for line in f: 
        mySum += int(line)
    f.close()
    print(str(mySum))

#Get sum of numbers in Problem013_numb.txt
sumLarge('Problem013_numb.txt')
