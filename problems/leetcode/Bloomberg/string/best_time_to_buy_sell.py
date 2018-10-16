def profit(arr):
    prev = arr[0]
    bought = []
    sold = []
    falling = False
    for i in range(1, len(arr)):
        if prev>arr[i]:
            if not falling:
                sold.append(prev)
            falling = True
        elif prev<arr[i]:
            falling = False
        print("%d to %d the stocks are %s" % (prev, arr[i], "falling" if falling else "not falling") )
        prev = arr[i]
        print(sold)
    
if __name__ == "__main__":
    arr = [7,1,5,3,6,4]
    arr2 = [1,2,3,4,5]
    profit(arr)