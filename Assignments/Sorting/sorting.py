#  File: sorting.py
#  Description: This program prints out the average run
#      times of various sorting algorithms.
#  Student"s Name: David Giles
#  Student"s UT EID: dgg524
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 07/23/17
#  Date Last Modified: 07/28/17

import random
import time
import sys
sys.setrecursionlimit(10000)


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def timeSort(num, lst):
    # determines correct sort function to use, returns elapsed time of sort
    if num == 0:
        # use bubble sort
        startT = time.time()
        bubbleSort(lst)
        stopT = time.time()
        elapsedT = stopT - startT
    if num == 1:
        # use insertion sort
        startT = time.time()
        insertionSort(lst)
        stopT = time.time()
        elapsedT = stopT - startT
    if num == 2:
        # use merge sort
        startT = time.time()
        mergeSort(lst)
        stopT = time.time()
        elapsedT = stopT - startT
    if num == 3:
        # use quick sort
        startT = time.time()
        quickSort(lst)
        stopT = time.time()
        elapsedT = stopT - startT

    return elapsedT


def listType(num):
    # determines what type of list to generate, returns 3 lists of size n
    if num == 0:
        # use random list
        list10 = [i for i in range(10)]
        list100 = [i for i in range(100)]
        list1000 = [i for i in range(1000)]

        random.shuffle(list10)
        random.shuffle(list100)
        random.shuffle(list1000)

        print("Input type = Random")
    if num == 1:
        # use sorted list
        list10 = [i for i in range(10)]
        list100 = [i for i in range(100)]
        list1000 = [i for i in range(1000)]

        print("Input type = Sorted")
    if num == 2:
        # use reversed sorted list
        list10 = [i for i in range(10)]
        list100 = [i for i in range(100)]
        list1000 = [i for i in range(1000)]

        list10.reverse()
        list100.reverse()
        list1000.reverse()

        print("Input type = Reverse")
    if num == 3:
        # use almost sorted list (10% of list is unsorted)
        list10 = [i for i in range(10)]
        list100 = [j for j in range(100)]
        list1000 = [k for k in range(1000)]

        for i in range(len(list10) // 10):
            ran1 = random.randint(0, len(list10)-1)
            ran2 = random.randint(0, len(list10)-1)
            while ran1 == ran2:
                ran2 = random.randint(0, len(list10)-1)
            list10[ran1], list10[ran2] = list10[ran2], list10[ran1]

        for j in range(len(list100) // 10):
            ran1 = random.randint(0, len(list100)-1)
            ran2 = random.randint(0, len(list100)-1)
            while ran1 == ran2:
                ran2 = random.randint(0, len(list100)-1)
            list100[ran1], list100[ran2] = list100[ran2], list100[ran1]

        for k in range(len(list1000) // 10):
            ran1 = random.randint(0, len(list1000)-1)
            ran2 = random.randint(0, len(list1000)-1)
            while ran1 == ran2:
                ran2 = random.randint(0, len(list1000)-1)
            list1000[ran1], list1000[ran2] = list1000[ran2], list1000[ran1]

        print("Input type = Almost sorted")

    return list10, list100, list1000


def sumList(lst):
    # recursively gets sum of list
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sumList(lst[1:])


def main():
    for i in range(4):  # loop for each list type
        list10, list100, list1000 = listType(i)

        print("                    avg time   avg time   avg time")
        print("   Sort function     (n=10)    (n=100)    (n=1000)")
        print("-----------------------------------------------------")

        for j in range(4):  # loop for each sort type
            if j == 0:
                sortType = "bubbleSort"
            if j == 1:
                sortType = "insertionSort"
            if j == 2:
                sortType = "mergeSort"
            if j == 3:
                sortType = "quickSort"

            print("{:>16}".format(sortType), end="")

            timelist10 = []     # list to hold times for n=10 trials
            timelist100 = []    # list to hold times for n=100 trials
            timelist1000 = []   # list to hold times for n=1000 trials

            for k in range(5):  # loop for each trial (5 trials)
                time10 = timeSort(j, list10)
                timelist10.append(time10)      # stores time for n=10 in list

                time100 = timeSort(j, list100)
                timelist100.append(time100)    # stores time for n=100 in list

                time1000 = timeSort(j, list1000)
                timelist1000.append(time1000)  # stores time for n=1000 in list

            avg = sumList(timelist10) / len(timelist10)
            print("{:12.6f}".format(avg), end="")
            avg = sumList(timelist100) / len(timelist100)
            print("{:11.6f}".format(avg), end="")
            avg = sumList(timelist1000) / len(timelist1000)
            print("{:11.6f}".format(avg))

        print("\n")

main()
