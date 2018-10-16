# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverseToList(self, node):
        if node == None:
            return [None]
        print(node.val)
        return [node.val] + self.traverseToList(node.left) + self.traverseToList(node.right)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # print(self.traverseToList(p))
        # print(self.traverseToList(q))
        return self.traverseToList(p) == self.traverseToList(q)

