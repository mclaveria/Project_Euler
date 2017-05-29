#Michael Claveria
#Project Euler Problem 14

def collatz(n):
    length = 0
    while n != 1:
        #print (str(n))
        length += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int((3 * n) + 1)
    #print ('1')
    return length


tracker, value = 0, 0
for i in range (1, 1000000):
    if collatz(i) > tracker:
        tracker = collatz(i)
        value = i
print(str('longest value is: ' + str(value) + ' with chain of ' + str(tracker)))

#longest value is: 837799 with chain of 524