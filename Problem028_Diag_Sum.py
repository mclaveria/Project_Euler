#Michael Claveria
#Number Spiral 28

#Each ring layer of the number spiral has 4 numbers
#I assigned layer 0 to be just the 1
#layer 1 is the numbers 3, 5, 7, 9
#layer 2 is the numbers 13, 17, 21, 25

#For layer 1 the top right diagonal is 9, layer 2 is 25, layer 3 is 49, ....
#The pattern is that for layer n, the top right diagonal is (2n + 1)^2
#The four numbers on each layer n are:
# (2n + 1)^2, (2n + 1)^2 - 2n, (2n + 1)^2 - 4n, (2n + 1)^2 - 6n
#Using algebra, the sum of those numbers are 16n^2 + 4n + 4

#findDiagSum finds the sum of the four numbers given the layer number as a parameter
def findDiagSum(layer):
    if layer < 1:
        return 1
    else:
        return 16 * (layer ** 2) + 4 * layer + 4

#getNumLayers will return the number of layers for a dim x dim spiral.  Note dim is always odd
def getNumLayers(dim):
    return int((dim - 1) / 2)

dim = 1001
numLayers = getNumLayers(dim)
#print(numLayers)

def getDiagSum(NumberOfLayers):
    result = 0
    for i in range(NumberOfLayers + 1):
        result += findDiagSum(i)
        print('Layer',i,'is', findDiagSum(i))
    print('Final sum is', result)

getDiagSum(numLayers)