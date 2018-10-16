#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def quicksort(arr, left, right):
    if left>=right:
        return
    pivot = arr[ int((left + (right-left))/2) ] # pivot = price-position pair (list)
    index = partition(arr, left, right, pivot)
    quicksort(arr, left, index-1)
    quicksort(arr, index, right)

def partition(arr, left, right, pivot):
    value = pivot[0]
    while(left<=right):
        while(arr[left][0]<value):
            left+=1
        while(arr[right][0]>value):
            right-=1
        if(left<=right):
            swap(arr, left, right)
            left+=1
            right-=1
    return left

def swap(arr, indexA, indexB):
    temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp

def binarySearch(arr, item, left, right):
    mid = int( (left/2 + right/2 ))
    midValue = arr[ mid ][0]
    if midValue == item:
        return midValue
    if left>=right:
        return None
    if item<midValue:
        right = mid
        return binarySearch(arr, item, left, right)
    elif item>midValue:
        left = mid+1
        return binarySearch(arr, item, left, right)

def doBinarySearch(arr, item):
    return binarySearch(arr, item, 0, len(arr)-1)

def whatFlavors(cost, money):
    quicksort(cost, 0, len(cost)-1)
    for price in cost:
        toFind = money-price[0]
        result = doBinarySearch(cost, toFind)
        if price[1]<result[1]:
            print(price[1]+1, result[1]+1)
        else:
            print(result[1]+1, price[1]+1)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))
        newCost = []
        for index in range(len(cost)):
            print(type(index))
            newCost.append([cost[index], index])
        print(newCost)
        whatFlavors(newCost, money)
