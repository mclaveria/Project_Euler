#Michael Claveria
#Project Euler Problem 40

def getString(n):
    result = ''
    for i in range(1, n + 1):
        result += str(i)
    return result

#print(getString(100))

test = getString(1000000)
print(test[0])
print(test[9])
print(test[99])
print(test[999])
print(test[9999])
print(test[99999])
print(test[999999])

print(int(test[0]) * int(test[9]) * int(test[99]) * int(test[999]) * int(test[9999]) * int(test[99999]) * int(test[999999]))