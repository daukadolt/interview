class Stack:
    def __init__(self):
        self.vals = []
        self.size = 0
    def push(self, val):
        self.vals.append(val)
        self.size += 1
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            val = self.vals.pop()
            return val
    def empty(self):
        return self.size == 0
class Queue:
    def __init__(self):
        self.vals = []
        self.size = 0
    def push(self, val):
        self.vals.append(val)
        self.size+=1
    def get(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            val = self.vals.pop(0)
            return val
    def empty(self):
        return self.size == 0
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ExpressionTree:
    def isExpression(self, char):
        return char in ["+", "-", "*", "/"]
    def __init__(self, array):
        # For now - postfix
        # a*b + c = [a,b,*,c,+]
        stack = Stack()
        for item in array:
            if not self.isExpression(item):
                newNode = TreeNode(item)
                stack.push(newNode)
            else:
                nodeA = stack.pop()
                nodeB = stack.pop()
                nodeExp = TreeNode(item)
                nodeExp.left = nodeA
                nodeExp.right = nodeB
                stack.push(nodeExp)
        self.root = stack.pop()
    def repr_helper(self, root, stack):
        if root == None:
            return
        else:
            if root.left:
                self.repr_helper(root.left, stack)
            stack.push(str(root.val))
            if root.right:
                self.repr_helper(root.right, stack)
    def __repr__(self):
        stack = Stack()
        self.repr_helper(self.root, stack)
        string = ""
        counter = 0
        leftBracket = True
        while not stack.empty():
            val = stack.pop()
            # if counter%3 == 0:
            #     if leftBracket:
            #         string += "("
            #         leftBracket = False
            #     else:
            #         string += ")"
            #         leftBracket = True
            string += val
        return string

if __name__ == "__main__":
    arr = ["a", "b", "+", "c", "*"]
    expTree = ExpressionTree(arr)
    print(expTree)

        
