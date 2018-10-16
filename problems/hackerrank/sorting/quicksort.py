def quicksort(array, left, right):
    if(left >= right):
        return
    pivot = array[ int(left + (right-left) /2) ]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index-1)
    quicksort(array, index, right)

def partition(array, left, right, pivot):
    while(left <= right):
        while(array[left] < pivot ):
            left+=1
        while(array[right] > pivot):
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
    array = [4, 3, 2, 1]
    array2 = [15, 3, 9, 8, 5, 2, 7, 1, 6]
    quicksort(array2, 0, len(array2)-1)
    print(array2)