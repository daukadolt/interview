def quicksort(arr, left, right):
    if(left>=right):
        return
    pivot = arr[ int( left/2 + right/2 ) ]
    index = partition(arr, left, right, pivot)
    quicksort(arr, left, index-1)
    quicksort(arr, index, right)

def swap(arr, indexA, indexB):
    temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp

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

def minimumAbsoluteDifference(arr):
    if(len(arr)==2):
        return abs(arr[0]-arr[1])
    quicksort(arr, 0, len(arr)-1)
    print(arr)
    diff = abs(arr[1] - arr[0])
    for index in range(2, len(arr)):
        if abs(arr[index]-arr[index-1])<diff:
            diff = abs(arr[index]-arr[index-1])
    return diff


if __name__ == "__main__":
    arr = [0, 21, 29, 2, 9, 19, -30]
    arr2 = [3, -7, 0]
    minDiff = minimumAbsoluteDifference(arr2)
    print(minDiff)