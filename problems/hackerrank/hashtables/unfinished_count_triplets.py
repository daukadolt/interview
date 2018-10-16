def searchFor(thisOrNextLargest, r,  hashtable):
    _hash = hash(thisOrNextLargest)
    first_bucket = _hash%len(hashtable)
    # print("thisOrNext = ",thisOrNextLargest)
    while(True):
        _hash = hash(thisOrNextLargest)
        bucket_id = _hash%len(hashtable)
        if bucket_id < first_bucket:
            return None
        if hashtable[bucket_id].get(thisOrNextLargest) != None:
            # print("found new _min = %d" % hashtable[bucket_id].get(thisOrNextLargest))
            return thisOrNextLargest
        thisOrNextLargest *= r
        
def countBetween(begin, r, hashtable):
    triplets = 1
    temp = begin
    value = 0
    for _ in range(3):
        _hash = hash(temp)
        bucket_id = _hash%len(hashtable)
        value = hashtable[bucket_id].get(temp)
        if value == None:
            return 0
        triplets *= value
        temp *= r
    return triplets
def countTriplets(arr, r):
    hashtable = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}}
    _min = 1
    _max = 1
    for i in range(0, len(arr)):
        if i == 0:
            _max = arr[i]
            _min = arr[i]
        if arr[i]>_max:
            _max = arr[i]
        elif arr[i]<_min:
            _min = arr[i]
        _hash = hash(arr[i])
        bucket_id = _hash%len(hashtable)
        the_dict = hashtable[bucket_id]
        if the_dict.get(arr[i]) == None:
            the_dict[arr[i]] = 1
        else:
            the_dict[arr[i]] += 1
    triplets = 0
    # print(hashtable)
    while(True):
        if _min == None:
            break
        triplets += countBetween(_min, r, hashtable)
        _min = searchFor(_min*r, r, hashtable)
    return triplets
    # [1, 5, 25, 125, 625]
    # len = 6, trip = 4
    # len = 5, trip = 3 
    # len = 4, trip = 2 
    # len = 3, trip = 1

if __name__ == "__main__":
    r = 5
    arr = [1, 5, 5, 25, 125]
    r2 = 3
    arr2 = [1, 3, 9, 9, 27, 81]
    ans = countTriplets(arr2, r2)
    print(ans)
