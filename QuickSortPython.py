#!/bin/python

import sys



def partition(Arr, low, high):
    pivotVal = Arr[low]
    i = low + 1                 #start from i + 1 because i is our pivot value.
    j = high
    while True:
        while arr[j] > pivotVal:
            j -= 1
        while arr[i] < pivotVal:
            i += 1
        if i < j:
            Arr[i], Arr[j] = Arr[j], Arr[i]
        else:
            Arr[low], Arr[j] = Arr[j], Arr[low]   #swagger
            return j


def quicksort(myArr, lowIndex, highIndex):
    if lowIndex < highIndex:
        midPoint = partition(myArr, lowIndex, highIndex)
        quicksort(myArr,lowIndex, midPoint - 1)
        quicksort(myArr,midPoint + 1, highIndex)



#n = int(raw_input().strip())
#arr = map(int,raw_input().strip().split(' '))
#quicksort(arr, 0, len(arr) - 1)

arr = [1,2,3,4,3,3,2,1]
quicksort(arr, 0, len(arr) - 1)
n=len(arr)
print(arr)

while(max(arr) != 0):
    i = 0
    while(arr[i] == 0):
        i+=1
        if i >= len(arr):
            break
    currCount = n - i
    print currCount

    subVal = arr[i]
    x = i
    while x < n:
        arr[x] -= subVal
        x += 1