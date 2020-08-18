
# Source: https://runestone.academy/runestone/books/published/pythonds/Trees/NodesandReferences.html

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        """
        create a new binary tree object and set the left attribute of the root to refer to this new object.
        """
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            # We insert a node and push the existing child down one level in the tree. 
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        """
        create a new binary tree object and set the right attribute of the root to refer to this new object.
        """
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key