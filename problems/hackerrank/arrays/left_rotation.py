def rotLeft(a, d):
    d = d%len(a)
    items = a
    num_to_be_saved = 0
    the_list = []
    while(num_to_be_saved<d):
        print(num_to_be_saved)
        the_list.append(a[num_to_be_saved])
        num_to_be_saved+=1
    k = 0
    while(num_to_be_saved<len(items)):
        items[k]=items[num_to_be_saved]
        num_to_be_saved+=1
        k+=1
    i = 0
    while(i<len(the_list)):
        items[k] = the_list[i]
        k+=1
        i+=1
    return items

if __name__ == "__main__":
    a = [1,2,3,4,5]
    d = 5
    rotLeft(a, d)