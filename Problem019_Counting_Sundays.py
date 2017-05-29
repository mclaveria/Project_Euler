#Michael Claveria
#Project Euler 19
'''
Count number of Sundays that fell on first of month between
January 1st 1901 (Monday) to Dec 31st 2000
'''

#Pseudocode:
#Check first day of month each year (12 checks)
#Add 1 to counter if the day is sunday
#repeat for 100 years



#Input: a year in integer form, eg. 1991

#Output: 
#This function will return a list that contains the first days of each month based on a 365
#or 366 day calendar year
#for example it might be [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

def firstOfMonth(year):
    #initialize list of first days for each month to 0 (12 0s)
    test = [0,0,0,0,0,0,0,0,0,0,0,0]
    leap = 0
    if year % 4 == 0:
        leap = 1
    #set number of days in each month from january to dec
    jan = 31
    feb = 28 + leap
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    octo = 31
    nov = 30
    dec = 31
    #initialize count
    count = 0
    daysOfMonth = [1, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]
    for i in range(12):
        #print('month is ' + str(i + 1))
        count += daysOfMonth[i]
        test[i] = count
        #print('first day of month is ' + str(count))
    return test
        
#for i in test:
#    print(str(i))

def dayCheck(lst, val):
    count = 0
    for i in lst:
        #print(str(i))
        if i % 7 == val:
            count += 1
    #print(str( count))
    return count

#myDays = firstOfMonth(1901)
#print(str(dayCheck(myDays, 6)))

def calcDays(start, end, dayOfWeek):
    counter = 0
    for i in range(start, end + 1):
        myDays = firstOfMonth(i)
        counter += dayCheck(myDays, dayOfWeek)
    #Each year, the first of the month will be 1 day ahead of the previous year if not a leap year
    #for example 1901 January 1st is a Tuesday, but in 1902, January 1st will be a Wednesday
    #This is because 365 % 7 = 1
    #However on leap years, January 1st will be 2 days ahead of the previous year
    #Thus on leap years we subtract 2 from seek, while non leap years subtract 1
        if i % 4 == 0:
            dayOfWeek -= 2
        else:
            dayOfWeek -= 1
        if dayOfWeek < 0:
            dayOfWeek += 7
    return counter

#January 1st 1901 is a Tuesday, so first Sunday is 6th day and all sundays are n mod 7 = 6
#initialize seeking the mod 7 to be 6    
result = calcDays(1901, 2000, 6)
print('Final answer is: ' + str(result))
    
            


