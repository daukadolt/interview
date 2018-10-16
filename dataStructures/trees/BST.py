class Queue:
    def __init__(self):
        self.vals = []
        self.size = 0
    def pushBack(self, val):
        self.vals.append(val)
        self.size += 1
    def popFront(self):
        if self.size == 0:
            return None
        else:
            val = self.vals.pop(0)
            self.size -= 1
            return val
    def __repr__(self):
        return str(self.vals)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.val < other.val
    def __gt__(self, other):
        return self.val > other.val
class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            self.size += 1
            return True
        else:
            parentNode = self.root
            while(True):
                if val == parentNode.val:
                    return False
                if val < parentNode.val:
                    if parentNode.left:
                        parentNode = parentNode.left
                    else:
                        break
                elif val > parentNode.val:
                    if parentNode.right:
                        parentNode = parentNode.right
                    else:
                        break
            if val < parentNode.val:
                parentNode.left = Node(val)
            else:
                parentNode.right = Node(val)
            self.size += 1
            return True
    def getNodeCount(self):
        return self.size
    def deleteValue(self, val):
        if self.root == None:
            return False
        else:
            theNode = self.root
            parentNode = self.root
            while(True):
                if theNode.val == val:
                    break
                elif val < theNode.val:
                    if theNode.left:
                        parentNode = theNode
                        theNode = theNode.left
                    else:
                        return False
                elif val > theNode.val:
                    if theNode.right:
                        parentNode = theNode
                        theNode = theNode.right
                    else:
                        return False
            if theNode.left == None and theNode.right == None:
                if theNode < parentNode:
                    parentNode.left = None
                else:
                    parentNode.right = None
                self.size -= 1
                return True
            elif theNode.left == None and theNode.right != None:
                if theNode < parentNode:
                    parentNode.left = theNode.right
                else:
                    parentNode.right = theNode.right
                self.size -= 1
                return True
            elif theNode.left != None and theNode.right == None:
                if theNode < parentNode:
                    parentNode.left = theNode.left
                else:
                    parentNode.right = theNode.left
                self.size -= 1
                return True
            else:
                substVal = self.substitute(theNode)
                theNode.val = substVal
                return True
    def substitute(self, node):
        node = node.right
        parentNode = node
        while(True):
            if node.left == None:
                parentNode.left = None
                self.size -= 1
                return node.val
            else:
                parentNode = node
                node = node.left
    def isInTree(self, val):
        if self.root == None:
            return False
        else:
            node = self.root
            while(True):
                if val == node.val:
                    return True
                elif val < node.val:
                    if node.left:
                        node = node.left
                    else:
                        return False
                elif val > node.val:
                    if node.right:
                        node = node.right
                    else:
                        return False
    def getHeight(self):
        if self.root == None:
            return 0
        else:
            return self.recursiveHeight(self.root, True)
    def recursiveHeight(self, root, isRoot = False):
        if root == None:
            return 0
        else:
            sum = 1
            if isRoot:
                sum = 0
            return sum + max(self.recursiveHeight(root.left), self.recursiveHeight(root.right))
    def getMin(self):
        node = self.root
        while(True):
            if node == None:
                return None
            if node.left == None:
                return node.val
            else:
                node = node.left
    def getMax(self):
        node = self.root
        while(True):
            if node == None:
                return None
            if node.right == None:
                return node.val
            else:
                node = node.right
    def isBinarySearchTree(self):
        return self.isBinarySearchTreeHelper(self.root) == 1
    def isBinarySearchTreeHelper(self, root):
        if root == None:
            return True
        product = 1
        if not root.left == None:
            product *= root.left < root
        if not root.right == None:
            product *= root.right > root
        return product * self.isBinarySearchTreeHelper(root.left) * self.isBinarySearchTreeHelper(root.right)
    def deleteTree(self):
        self.deleteTreeRecursive(self.root)
        self.root = None
        self.size = 0
    def deleteTreeRecursive(self, root):
        if not root.left == None:
            self.deleteTreeRecursive(root.left)
        if not root.right == None:
            self.deleteTreeRecursive(root.right)
        root.left = None
        root.right = None
    def reprHelper(self, root, queue):
        if root == None:
            return
        else:
            queue.pushBack(root.val)
            if root.left:
                self.reprHelper(root.left, queue)
            if root.right:
                self.reprHelper(root.right, queue)
    def getSuccessor(self, val):
        node = self.root
        while(True):
            if node == None:
                return -1
            if node.val == val:
                break
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    return -1
            elif val > node.val:
                if node.right:
                    node = node.right
                else:
                    return -1
        if node.right:
            return node.right.val
        else:
            return -1
    def __repr__(self):
        queue = Queue()
        self.reprHelper(self.root, queue)
        return queue.__repr__()

if __name__ == "__main__":
    bst = BST()
    vals = [8, 4, 14, 2, 6, 10, 16, 1, 3, 5, -99, 7, -1]
    for val in vals:
        bst.insert(val)
    print(bst.isInTree(4))
    bst.deleteValue(4)
    print(bst.isInTree(4))
    print(bst)
    print(bst.getHeight())
    print(bst.getMin())
    print(bst.getMax())
    print(bst.isBinarySearchTree())
    print(bst.deleteTree())
    print(bst)

    #
    #
    #

    for val in vals:
        bst.insert(val)
    print(bst)
    print(bst.getSuccessor(2))