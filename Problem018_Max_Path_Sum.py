#Michael Claveria
#Project Euler Problem 18

'''
find greatest sum traversing down the binary tree displayed below
                    75
                   95 64
                 17 47 82
               18 35 87 10
              20 04 82 47 65
            19 01 23 75 03 34
           88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
       53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
   63 66 04 68 89 53 67 30 73 16 69 87 40 31
  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

#Create a binary tree class        

#Solved with algorithm:
#Compare two child leaves on bottom layer and add larger one to parent
#Repeat for next layer up comparing two child leaves and adding larger one to parent
#Answer is 1074



class BinaryTree():
    
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def getNodeValue(self):
        return self.value
      
    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def setNodeValue(self, val):
        self.value = val
        
    def insertRight(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

def printTree(tree):
    if tree is not None:
        if isinstance(tree.getLeftChild(), int):
            print(str(tree.left))
        else:
            printTree(tree.getLeftChild())
        
        print(tree.getNodeValue())
        
        if isinstance(tree.getRightChild(), int):
            print(str(tree.right))
        else:
            printTree(tree.getRightChild())

def maxPathSum(root):
    #empty root returns 0
    if root is None:
        return 0
    #integer roots return the root integer value
    if isinstance(root, int):
        return root
    val = root.getNodeValue()
    pathSum = val
    leftSum = maxPathSum(root.getLeftChild())
    rightSum = maxPathSum(root.getRightChild())
    if leftSum > rightSum:
        pathSum += leftSum
    else:
        pathSum += rightSum
    return pathSum

testList1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
testList2 = [75,18,10,17,82,35,87,95,64,35,87,47,47,87,35]

#print(str(testList2[1:-1]))

testTree = BinaryTree(testList2[0])
for i in testList1[1:-1:2]:
    testTree.insertLeft(i)
    #print(str(i))
for i in testList1[2::2]:
    testTree.insertRight(i)
    #print(str(i))
printTree(testTree)
print(str(maxPathSum(testTree)))

def testTree():
    '''
    myTree = BinaryTree(75, BinaryTree(95, BinaryTree(17, BinaryTree(18, BinaryTree(20, \
            BinaryTree(19, BinaryTree(88, BinaryTree(99, BinaryTree(41, BinaryTree(41, \
            BinaryTree(53, BinaryTree(70, BinaryTree(91, BinaryTree(63, 4, 62), \
            BinaryTree(66, 62, 98)), BinaryTree(71, BinaryTree(66, 62, 98), BinaryTree(4, 98, 27)\
            )) BinaryTree(
            ))) )
            BinaryTree(                                                                                                                                                                 Binary 35), \
            BinaryTree(47, 35, 87)), 
             BinaryTree(64, BinaryTree(47, 35, 87), BinaryTree(82, 87, 10)))
    '''
    myTree = BinaryTree(75)
    myTree.insertLeft(BinaryTree(95, 17, 47))
    myTree.insertRight(BinaryTree(64, 47, 82))
    printTree(myTree)
    #print(str(myTree.getNodeValue()))
    print(str(maxPathSum(myTree)))
#testTree()