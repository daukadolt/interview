def swap(arr, indexA, indexB):
    temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp

def insertion_sort(arr):
    for index in range(1, len(arr)):
        currentElement = index
        elementIndexToBeComparedTo = index-1
        while elementIndexToBeComparedTo >= 0 and arr[currentElement]<arr[elementIndexToBeComparedTo]:
            swap(arr, currentElement, elementIndexToBeComparedTo)
            currentElement -= 1
            elementIndexToBeComparedTo -= 1
    print("Finished sorting, %s" % arr)
    return arr

def maximumToys(prices, k):
    numberOfToys = 0
    sumOfPrices = 0
    insertion_sort(prices)
    for price in prices:
        if price + sumOfPrices > k:
            print("price + sumOfprices = %d > k = %d" % (price + sumOfPrices, k) )
            return numberOfToys
        sumOfPrices += price
        numberOfToys += 1
        print("Incrementing, sumOfPrices = %d, numberOfToys = %d" % (sumOfPrices, numberOfToys) )

if __name__ == "__main__":
    num_input = "7 50"
    arr_input = "1 12 5 111 200 1000 10"
    # _, k = list( map(int, num_input.rstrip().split()) )
    # arr = list( map( int, arr_input.rstrip().split() ) )
    arr = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    print(maximumToys(arr, k))
    
            