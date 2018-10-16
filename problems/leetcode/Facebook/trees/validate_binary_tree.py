# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBSTBool(self, root, rootVal, rightOfRoot=None):
        if root == None:
            return 1
        leftProduct = 1
        if root.left:
            if root.left.val >= root.val:
                leftProduct = 0
        if rightOfRoot == False and root.val >= rootVal:
            print("root.val = %d" % root.val)
            print("rootVal = %d" % rootVal)
            leftProduct = 0

        rightProduct = 1
        if root.right:
            if root.right.val <= root.val:
                print("root.right.val %d <= root.val %d" % (root.right.val, root.val))
                rightProduct = 0
        if rightOfRoot == True and root.val <= rootVal:
                print("rightOfRoot %d" % root.val)
                rightProduct = 0
        print("leftProduct %d rightProduct %d" % (leftProduct, rightProduct))
        return leftProduct * rightProduct * self.isValidBSTBool(root.left, False, )*self.isValidBSTBool(root.right, True, rootVal)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isValidBSTBool(root, root.val) == 1


