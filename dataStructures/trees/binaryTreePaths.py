# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def myFunction(self, root, List, string = ""):
        if root == None:
            return
        if root.left == None and root.right == None:
            if string:
                string += "->"
            string += str(root.val)
            List.append(string)
            return
        print(string)
        print(not string)
        if not string:
            string += str(root.val)
        else:
            string += "->"
            string += str(root.val)
        if root.left:
            self.myFunction(root.left, List, string)
        if root.right:
            self.myFunction(root.right, List, string)
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        List = []
        self.myFunction(root, List)
        return List
        