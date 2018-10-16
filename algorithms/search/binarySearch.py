def binarySearch(key, array, min, max):
    if min>max:
        return False
    else:
        print("min = %d, max = %d" % (min, max))
        midpoint = (min + max)//2
        print("midpoint = %d" % midpoint)
        if key == array[midpoint] or key == array[min] or key == array[max]:
            return True
        elif key < array[midpoint]:
            return binarySearch(key, array, min, midpoint+1)
        elif key > array[midpoint]:
            return binarySearch(key, array, midpoint-1, max)

def quicksort(array, left, right):
    if left>=right:
        return
    else:
        pivot = array[ (left + (right-left))//2 ]
        index = partition(array, left, right, pivot)
        quicksort(array, left, index-1)
        quicksort(array, index+1, right)

def partition(array, left, right, pivot):
    while(left<=right):
        while(array[left]<pivot):
            left+=1
        while(array[right]>pivot):
            right-=1
        if(left<=right):
            swap(array, left, right)
            left+=1
            right-=1
    return left

def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3,2,1]
    quicksort(arr, 0, len(arr)-1)
    print(arr)
    print(binarySearch(4, arr, 0, len(arr)-1))