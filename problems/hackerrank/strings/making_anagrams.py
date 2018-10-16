def makeAnagram(a, b):
    hashmap = { 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {} }
    sizeOfFirstString = 0
    for character in a:
        sizeOfFirstString += 1
        _hash = hash(character)
        _bucket_id = _hash%len(hashmap)
        _the_dictionary = hashmap[_bucket_id]
        if _the_dictionary.get(character) == None:
            _the_dictionary[character] = 1
        else:
            _the_dictionary[character] += 1
    sizeOfSecondString = len(b)
    for character in b:
        if sizeOfFirstString == 0 or sizeOfSecondString == 0:
            break
        _hash = hash(character)
        _bucket_id = _hash%len(hashmap)
        _the_dictionary = hashmap[_bucket_id]
        if _the_dictionary.get(character) == None or _the_dictionary.get(character) == 0:
            continue
        else:
            _the_dictionary[character] -= 1
            sizeOfFirstString -= 1
            sizeOfSecondString -= 1
    return sizeOfFirstString + sizeOfSecondString

if __name__ == "__main__":
    a = "cde"
    b = "abc"
    print(makeAnagram(a, b))