# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

def traceTillNode(root, node):
    if not root:
        return []
    if root.info == node:
        return [root]
    else:
        toReturn = [root]
        nextNode = None
        if node < root.info:
            nextNode = root.left
        else:
            nextNode = root.right
        toReturn += traceTillNode(nextNode, node)
        return toReturn

def quicksort(arr, left, right):
    if left>=right:
        return
    pivot = arr[int( (left + (right-left))/2 )].info
    print("left, right = %d, %d" % (left, right))
    print(",".join(str(root.info) for root in arr))
    index = partition(arr, left, right, pivot)
    quicksort(arr, left, index-1)
    quicksort(arr, index, index)

def partition(arr, left, right, pivot):
    while(left<=right):
        while(arr[left].info<pivot):
            left+=1
        while(arr[right].info>pivot):
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

def lca(root, v1, v2):
    list1 = traceTillNode(root, v1)
    list2 = traceTillNode(root, v2)
    # print("".join(str(root.info) for root in list1))
    # print("".join(str(root.info) for root in list2))
    # quicksort(list1, 0, len(list1)-1)
    # quicksort(list2, 0, len(list2)-1)
    longestList = None
    shortestList = None
    if len(list1)>len(list2):
        longestList = list1
        shortestList = list2
    else:
        longestList = list2
        shortestList = list1
    while len(longestList) != 0:
        val = longestList.pop()
        if val in shortestList:
            return val
    return None
  #Enter your code here
