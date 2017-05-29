#Michael Claveria
#Problem 33 Digit Cancelling fractions

'''Find the four 2 digit numerator and 2 digit denominator fractions where cancelling
one digit in the numerator with the same digit in the denominator will return a fraction
of the same value (not counting zeros)

Multiply those 4 together to get a fraction and find the denominator in lowest common FORM
'''

#Given a 2 digit numerator and 2 digit denominator, cancel2DigFrac will 

def cancel2DigFrac(numer, denom):
    nume = str(numer)
    deno = str(denom)
    #Case0: Ignore trivial case when second integers are both zero
    if int(nume[1]) == 0 and int(deno[1]) == 0:
        return 2
    #case1: numerator and denominator have same 1st number but different 2nd number
    # cancel out first numbers and return 2nd / 2nd
    elif nume[0] == deno[0] and nume[1] != deno[1] and int(deno[1]) != 0:
        return float(int(nume[1]) / int(deno[1]))
    #case2: numerator first number is same as denominator 2nd number
    # cancel out numerator first and denominator second
    elif nume[0] == deno[1] and nume[1] != deno[0] and int(deno[0]) != 0:
        return float(int(nume[1]) / int(deno[0]))
    #case3: numerator 2nd is same as denominator 1st
    elif nume[1] == deno[0] and nume[0] != deno[1] and int(deno[1]) != 0:
        return float(int(nume[0]) / int(deno[1]))
    #case4: numerator and denominator have same second number, but different first numbers
    elif nume[1] == deno[1] and nume[0] != deno[0] and int(deno[0]) != 0:
        return float(int(nume[0]) / int(deno[0]))
    else:
        return 2
'''   
for i in cancel2DigFrac(21, 25):
    print (i)
   
for i in cancel2DigFrac(14, 42):
    print (i)
for i in cancel2DigFrac(24, 41):
    print (i)
for i in cancel2DigFrac(12, 20):
    print (i)
for i in cancel2DigFrac(20, 50):
    print (i)
for i in cancel2DigFrac(27, 57):
    print (i)
'''
def findCancelFrac(numer, denom):
    #print(float(numer/denom))
    i = cancel2DigFrac(numer, denom)
    #print(i)
    
    if float(numer/denom) == i:
        print('Numerator is', numer, 'Denominator is', denom)
        #numProd *= numer
        #denomProd *= denom
        #print('Product of Numerators is', numProd, 'Product of Denominators is', denomProd)

def get2DigDCFrac():
    for i in  range (10, 100):
        for j in range (10, 100):
            if j >= i:
                findCancelFrac(i, j)
                
get2DigDCFrac()

finalNum = 16 * 19 * 26 * 49
print(finalNum)
finalDen = 64 * 95 * 65 * 98
print(finalDen)
final = float(finalNum/finalDen)


print(final)