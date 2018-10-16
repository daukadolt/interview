# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def depthOfTree(self, root):
        if root == None:
            return 0
        return 1 + self.depthOfTree(root.left) + self.depthOfTree(root.right)
    def diameterOfTreeToList(self, root, List):
        if root == None:
            return
        List.append(max(self.depthOfTree(root.left), self.depthOfTree(root.right)))
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        List = []
        self.diameterOfTreeToList(root, List)
        print(List)
        if len(List) == 0:
            return 0
        elif len(List) == 1:
            return List[0]
        else:
            if root.left and root.right:
                List.append(List[0] + List[1])
            else:
                List.append(List[0])
            print(List)
            return sorted(List).pop()

if __name__ == "__main__":
    sol = Solution()
    a = TreeNode(3)
    a.left = TreeNode(1)
    a.right = TreeNode(2)
    sol.diameterOfBinaryTree(a)
        