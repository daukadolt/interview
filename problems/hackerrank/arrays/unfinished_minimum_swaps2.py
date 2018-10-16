def minimumSwaps(arr):
    num = 1
    position = 0
    swaps = 0
    # print("received arr ", arr)
    while(True):
        # print("num = %d, position = %d" % (num, position))
        print(arr)
        if num > len(arr):
            break
        if arr[num-1] == num:
            position = num
            num+=1
        if arr[position] == num:
            # print("Found num = %d @ position = %d" % (num, position))
            if position == num-1:
                position = num
                # print("Now posit = %d" % position)
                num+=1
            else:
                temp = arr[num-1]
                arr[num-1] = num
                arr[position] = temp
                position = num
                # print("Now posit = %d" % position)
                num += 1
                swaps += 1
        position += 1
    return swaps
if __name__ == "__main__":
    arr = [4, 3, 1, 2]
    arr2 = [1, 3, 5, 2, 4, 6, 8]
    minimumSwaps(arr2)