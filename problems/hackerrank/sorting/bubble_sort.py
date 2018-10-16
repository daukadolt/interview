def swap(arr, indexA, indexB):
    temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp

def countSwaps(arr):
    upperBoundary = len(arr)-1
    isSorted = False
    swapCounter = 0
    while not isSorted:
        isSorted = True
        for index in range(0, upperBoundary):
            if arr[index]>arr[index+1]:
                swap(arr, index, index+1)
                swapCounter += 1
                isSorted = False
        upperBoundary -= 1
    print("Array is sorted in %d swaps." % swapCounter)
    print("First Element: %d" % arr[0])
    print("Last Element: %d" % arr[len(arr)-1])

if __name__ == "__main__":
    arr = [6, 4, 1]
    countSwaps(arr)