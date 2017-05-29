#Michael Claveria
#Project Euler Problem 25

'''
What is the index of the first term in a Fibonacci sequence to contain 1000 digits?

'''

#fibSeq takes an integer input nDig and returns the sequence number of the first 
#Fibonnaci number that has nDig digits

def fibSeq(nDig):
    a, b, seq, aDig = 0, 1, 0, 0
    while aDig < nDig:
        a, b = b, a + b
        seq += 1
        aDig = len(str(a))
        #print(str(a))
    return seq

print(str(fibSeq(1000)))


    
        
    
    
