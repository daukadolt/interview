# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

def myOrder(item):
    return item[0]

class Solution:
    # @param root, a tree link node
    # @return nothing
    def BST(self, root, list, level = 0):
        if not root:
            return
        else:
            list.append([level, root])
            if root.left:
                self.BST(root.left, list, level+1)
            if root.right:
                self.BST(root.right, list, level+1)
    def connect(self, root):
        if not root:
            return
        level = 0
        list = []                       # unpopulated, yet
        self.BST(root, list)            # populate the list
        list = sorted(list, key=myOrder)
        print([ [item[0], item[1].val] for item in list ])
        while len(list)>=2:
            a = list.pop(0)
            b = list.pop(0)
            levelA = a[0]
            levelB = b[0]
            print(levelA, levelB)
            if levelA != levelB:        # if levels are not equal
                list = [b] + list
                continue
            else:                       # if are
                a[1].next = b[1]
                list = [b] + list


