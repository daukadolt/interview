# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, List, offset=0):
        if root == None:
            return
        List.append({offset:root.val})
        if root.left:
            self.helper(root.left, List, offset-1)
        if root.right:
            self.helper(root.right, List, offset+1)
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        List = []
        self.helper(root, List)
        if len(List) == 0:
            return []
        temporaryList = []
        result = []
        prevOffset = None
        for element in List:
            (currentOffset, currentVal), = element.items()
            print(currentOffset, currentVal)
            print(prevOffset)
            if len(temporaryList) == 0:
                print("0, appending")
                temporaryList.append(currentVal)
                prevOffset = currentOffset
            elif prevOffset == currentOffset:
                print("equal, appending")
                temporaryList.append(currentVal)
            else:
                result.append(temporaryList)
                temporaryList = [currentVal]
                prevOffset = currentOffset
        if len(temporaryList) != 0:
            result.append(temporaryList)
        print(result)
        return result

