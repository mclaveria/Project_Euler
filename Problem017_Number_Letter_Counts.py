#Michael Claveria
#Project Euler Problem 17

'''
If numbers are written out in words eg. one, two three, ....
How many letters would be use to write all numbers from one to one thousand (inclusive)?
Note: 342 would be 'three hundred and forty two' which would be 23 letters
'''

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sing_ten = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',\
             'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

#and is used when number from 101 to 999, not used when 1-100 or for 1000
my_and = 'and'
#hundred is used for 100-999 and not used for 1-99 or 1000
hundred = 'hundred'
#thousand is only used for 1000
thousand = 'thousand'

#Create a list called ninety_nine with numbers 1 - 99
ninety_nine = []
ninety_nine = ones + sing_ten
for a in tens:
    for b in ones:
        ninety_nine.append(a + b) 

#print(ninety_nine)

#Create a list with triple digit numbers 100 - 999
tripleDig = []
for i in ones[1:]:
    #create string that says xhundredand
    frontAnd = i + hundred + my_and
    #add first number to list
    tripleDig.append(i + hundred)
    #add next numbers xhundredandone through xhundredandninetynine
    for n in ninety_nine[1:]:
        tripleDig.append(frontAnd + n)

#create a string for 'onethousand'
oneThousand = 'one' + thousand

def charLength(lst):
    total = 0
    for i in lst:
        total += len(i)
    return total

print(str(charLength(ninety_nine)))
print(str(charLength(tripleDig)))
print(str(charLength(oneThousand)))

result = charLength(ninety_nine) + charLength(tripleDig) + charLength(oneThousand)

print('Result is: ' + str(result))
