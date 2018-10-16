#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hashtable = { 0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [] }
    for i in range(0, len(magazine)):
        _hash = hash(magazine[i])
        bucket_id = _hash%len(hashtable)
        hashtable[bucket_id].append(magazine[i])
    for i in range(0, len(note)):
        # print("Looking for word ", note[i])
        word = note[i]
        _hash = hash(word)
        bucket_id = _hash%len(hashtable)
        found = False
        the_list = hashtable[bucket_id]
        # print("Trying to find in ", the_list)
        for j in range(0, len( the_list )):
            if word == the_list[j]:
                found = True
                the_list.remove(word)
                break
        if not found:
            print("No")
            return
    print("Yes")
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)