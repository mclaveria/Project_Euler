#Michael Claveria
#Project Euler Problem 29 Distict powers

'''
Find the number of distinct terms generated by a^b for 2 <= a <= 100 and 
2 <= b <= 100

'''

aList = range(2,101)
bList = range(2,101)

def distPow(list1, list2):
    rList = []
    for i in list1:
        for j in list2:
            #print (str(i ** j))
            rList.append((str(i ** j)))
    #remove duplicates from rList
    result = set(rList)
    return len(result)
        
print(distPow(aList, bList))
