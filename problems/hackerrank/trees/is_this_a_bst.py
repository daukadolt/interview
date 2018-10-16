""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def BSTtoList(root):
    if not root:
        return []
    return BSTtoList(root.left) + [root.data] + BSTtoList(root.right)

def quicksort(arr, left, right):
    if left>=right:
        return
    pivot = arr[ int(left + (right-left) /2) ]
    index = partition(arr, left, right, pivot)
    quicksort(arr, left, index-1)
    quicksort(arr, index, right)

def partition(arr, left, right, pivot):
    while(left<=right):
        while(arr[left]<pivot):
            left+=1
        while(arr[right]>pivot):
            right-=1
        if(left<=right):
            swap(arr, left, right)
            left+=1
            right-=1
    return left

def swap(arr, indexA, indexB):
    temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp

def checkBST(root):
    List = BSTtoList(root)
    copyOfList = List[:]
    quicksort(copyOfList, 0, len(copyOfList)-1)
    if List != copyOfList:
        return False
    for index in range(len(List)):
        if List[index] in List[index+1:]:
            return False
    return True
