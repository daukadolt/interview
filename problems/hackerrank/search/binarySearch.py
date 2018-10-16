def binarySearch(arr, item, left, right):
    mid = int( (left/2 + right/2 ))
    midValue = arr[ mid ][0]
    if midValue == item:
        return True
    if left>=right:
        return False
    if item<midValue:
        right = mid
        return binarySearch(arr, item, left, right)
    elif item>midValue:
        left = mid+1
        return binarySearch(arr, item, left, right)

def doBinarySearch(arr, item):
    return binarySearch(arr, item, 0, len(arr)-1)

def quicksort(arr, left, right):
    if left>=right:
        return
    pivot = arr[ int((left + (right-left))/2) ] # pivot = price-position pair (list)
    index = partition(arr, left, right, pivot)
    quicksort(arr, left, index-1)
    quicksort(arr, index, right)

def partition(arr, left, right, pivot):
    value = pivot[0]
    while(left<=right):
        while(arr[left][0]<value):
            left+=1
        while(arr[right][0]>value):
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

if __name__ =="__main__":
    arr = [ [1,2], [5,4], [3,6] ] # key == price, value == position
    quicksort(arr, 0, len(arr)-1)
    print(arr)
    print(doBinarySearch(arr, 3))