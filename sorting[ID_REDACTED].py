import time
from random import randint
from random import shuffle
import numpy as np
'''
Report
What I am seeing in the outputs is that of all the sorts, mergesort is
the slowest algorithm and python sort is the fastest algorithm. This is
evident as when the trials were conducted, mergesort took the longest
time to sort the lists and python sort took the shortest time.
As the lists grew larger, the sorts took a longer time to sort out each of the lists.
Most of the sort methods performed better on a fully shuffled list, as they were
able to sort these lists quicker than the partially shuffled lists. However,
as the lists grew larger, heapsort actually performed better on partially
shuffled lists as opposed to fully shuffled lists.  Adding k duplicates
to the lists did not have significant effects on the times that the sorting algorithms
took in order to sort the lists.
Of the three sorts that we implemented (mergesort, heapSort, and quicksort),
quicksort was the fastest sorting algorithm.  

Revision (Question 1)
i. The difference between mergesort and quicksort is that mergesort uses a divide
and conquer technique, where it divides a list into smaller lists, sorts those smaller
lists, and puts them back together. Quicksort also uses divide and conquer, but
it uses pivot numbers in order to help sort the lists, and does not do any list
combination.

ii. The worst case complexity on mergesort is O(n log n).

iii. The space complexity of standard mergesort on an array is O(n). The space
complexity of bottom up mergesort on an array is also O(n).
'''

#Quick Sort shuffling (Question 2)
def shuffle_and_quicksort(mylist):
    n = len(mylist)
    for i in range(len(mylist)):
        j = randint(0, n-1)
        mylist[i], mylist[j] = mylist[j], mylist[i]
    quickSort(mylist, 0, n-1)

#Quick Sort Implementation (Question 2)
def quickSort(myList,start,end):
    if start < end:
        pivotPos = start - 1
        pivotNumber = myList[end]
        for j in range(start , end):
            if myList[j] <= pivotNumber:
                pivotPos += 1
                myList[pivotPos],myList[j] = myList[j],myList[pivotPos]
        myList[pivotPos+1],myList[end] = myList[end],myList[pivotPos+1]
        pivotPos += 1
        quickSort(myList, start, pivotPos-1)
        quickSort(myList, pivotPos+1, end)


#Heap Sort Implementation (Question 3) - Taken from the Lab 1 Solution
def heapSort(inlist):
    """ Heapsort (the list) inlist, in place. """
    # first treat the inlist as the input stream to build a *max* priority queue
    # maintain the PQ in the same list, gradually growing from the front.
    # that means each item to be added will already be in the starting point
    # and so all we have to do is bubble each item up the heap which is earlier
    # than it in the list.
    # Once the PQ is complete, we need to reverse it.
    # Gradually shrink the PQ by removing the *max* item, and place it in the
    # cell at the end of the PQ just vacated
    length = len(inlist)
    # print(inlist, ': initial list')
    for i in range(length):
        # print('   add', inlist[i], 'to the virtual heap')
        bubbleup(inlist,i)
        # print(inlist)
    for i in range(length):
        # elt to be moved up is in position len(list)-1 - i
        # max elt being shifted is in position 0, and is going to len(list)-1-i
        # so start by swapping them, and then bubbling down the new elt in pos 0
        # remembering that hea hap size has shrunk by 1.
        # print('shifting', inlist[0], 'to cell', (length-1-i))
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist, 0, length-2-i)
        # print(inlist)


def bubbleup(inlist, i):
    """ Bubble up item currently in pos i in a max heap. """
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            #print('swapping:', inlist[i], 'with its parent:', inlist[parent])
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0


def bubbledown(inlist, i, last):
    """ Bubble down item currently in pos i in a max heap (stops at last). """
    while last > (i*2):  # so at least one child
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc   # start by assuming left child is the max child
        if last > lc and inlist[rc] > inlist[lc]:  #r c exists and is bigger
            maxc = rc
        if inlist[i] < inlist[maxc]:
            #print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last

#Top Down Merge Sort Implementation (Question 3)
def mergesort(mylist):
    n = len(mylist)
    if n > 1:
        list1 = mylist[:n//2]
        list2 = mylist[n//2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)

#Merge function for MergeSort
def merge(list1, list2, mylist):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(mylist):
        if f1 == len(list1):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            mylist[f1+f2] = list2[f2]
            f2 += 1
        else:
            mylist[f1+f2] = list1[f1]
            f1 += 1

#evaluateall function definition (Question 4)
def evaluateall(n, k):
    numList = []
    for fill in range(0, n-k):
        numList.append(randint(0, n-k-1))
    for add in range(n-k-1, n):
        numList.append(numList[randint(0, n-k-1)])
    avgHeapTime = 0
    avgMergeTime = 0
    avgQuickTime = 0
    avgPyTime = 0
    for copy in range(0, 10):
        ListCopy = numList.copy()
        shuffle(ListCopy)
        heapCopy = ListCopy.copy()
        heapStartTime = time.time()
        heapSort(heapCopy)
        heapEndTime = time.time()
        avgHeapTime += heapEndTime - heapStartTime
        mergeCopy = ListCopy.copy()
        mergeStartTime = time.time()
        mergesort(mergeCopy)
        mergeEndTime = time.time()
        avgMergeTime += mergeEndTime - mergeStartTime
        quickCopy = ListCopy.copy()
        quickStartTime = time.time()
        shuffle_and_quicksort(quickCopy)
        quickEndTime = time.time()
        avgQuickTime += quickEndTime - quickStartTime
        pySortCopy = ListCopy.copy()
        pyStartTime = time.time()
        pySortCopy.sort()
        pyEndTime = time.time()
        avgPyTime += pyEndTime - pyStartTime
    avgHeapTime /= 10
    avgMergeTime /= 10
    avgQuickTime /= 10
    avgPyTime /= 10
    formattedHeapTime = '{:.5f}'.format(avgHeapTime)
    formattedMergeTime = '{:.5f}'.format(avgMergeTime)
    formattedQuickTime = '{:.5f}'.format(avgQuickTime)
    formattedPyTime = '{:.5f}'.format(avgPyTime)
    print(formattedHeapTime + ' heapsort ' + str(n) + ' ' + str(k))
    print(formattedMergeTime + ' mergesort ' + str(n) + ' ' + str(k))
    print(formattedQuickTime + ' quicksort ' + str(n) + ' ' + str(k))
    print(formattedPyTime + ' python ' + str(n) + ' ' + str(k))
    print()

def evaluatepartial(n, k):
    numList = []
    for fill in range(0, n-k):
        numList.append(randint(0, n-k-1))
    for add in range(n-k-1, n):
        numList.append(numList[randint(0, n-k-1)])
    numList.sort()
    for randSelect in range(0, n//20):
        swapLocA = randint(0, n-1)
        swapLocB = randint(0, n-1)
        temp = numList[swapLocB]
        numList[swapLocB] = numList[swapLocA]
        numList[swapLocA] = temp
    avgHeapTime = 0
    avgMergeTime = 0
    avgQuickTime = 0
    avgPyTime = 0
    for copy in range(0, 10):
        ListCopy = numList.copy()
        shuffle(ListCopy)
        heapCopy = ListCopy.copy()
        heapStartTime = time.time()
        heapSort(heapCopy)
        heapEndTime = time.time()
        avgHeapTime += heapEndTime - heapStartTime
        mergeCopy = ListCopy.copy()
        mergeStartTime = time.time()
        mergesort(mergeCopy)
        mergeEndTime = time.time()
        avgMergeTime += mergeEndTime - mergeStartTime
        quickCopy = ListCopy.copy()
        quickStartTime = time.time()
        shuffle_and_quicksort(quickCopy)
        quickEndTime = time.time()
        avgQuickTime += quickEndTime - quickStartTime
        pySortCopy = ListCopy.copy()
        pyStartTime = time.time()
        pySortCopy.sort()
        pyEndTime = time.time()
        avgPyTime += pyEndTime - pyStartTime
    avgHeapTime /= 10
    avgMergeTime /= 10
    avgQuickTime /= 10
    avgPyTime /= 10
    formattedHeapTime = '{:.5f}'.format(avgHeapTime)
    formattedMergeTime = '{:.5f}'.format(avgMergeTime)
    formattedQuickTime = '{:.5f}'.format(avgQuickTime)
    formattedPyTime = '{:.5f}'.format(avgPyTime)
    print(formattedHeapTime + ' heapsort ' + str(n) + ' ' + str(k) + ' p')
    print(formattedMergeTime + ' mergesort ' + str(n) + ' ' + str(k) + ' p')
    print(formattedQuickTime + ' quicksort ' + str(n) + ' ' + str(k) + ' p')
    print(formattedPyTime + ' python ' + str(n) + ' ' + str(k) + ' p')
    print()

def evaluate():
    evaluateall(100, 0)
    evaluatepartial(100, 0)
    evaluateall(1000, 0)
    evaluatepartial(1000, 0)
    evaluateall(10000, 0)
    evaluatepartial(10000, 0)
    evaluateall(100000, 0)
    evaluatepartial(100000, 0)
    evaluateall(100, 20)
    evaluatepartial(100, 20)
    evaluateall(1000, 200)
    evaluatepartial(1000, 200)
    evaluateall(10000, 2000)
    evaluatepartial(10000, 2000)
    evaluateall(100000, 20000)
    evaluatepartial(100000, 20000)
    evaluateall(100, 70)
    evaluatepartial(100, 70)
    evaluateall(1000, 700)
    evaluatepartial(1000, 700)
    evaluateall(10000, 7000)
    evaluatepartial(10000, 7000)
    evaluateall(100000, 70000)
    evaluatepartial(100000, 7000)

'''
#Code used to test the top down mergesort, quicksort, and heapSort
#in order to ensure all sorts are working. (Question 3)
Test_list = [903, 393, 202, 361, 123, 453, 911, 1023, 64, 666]
Test_CopyA = Test_list.copy()
Test_CopyB = Test_list.copy()
print('Original List :: ' + str(Test_list))
heapSort(Test_list)
mergesort(Test_Copy)
print('List after heapSort :: ' + str(Test_list))
print('List after MergeSort :: ' + str(Test_CopyA))
shuffle_and_quicksort(Test_CopyB)
print('List after Quick Sort :: ' + str(Test_CopyB))
'''

#Testing of evaluateall and evaluatepartial
#evaluateall(1000, 0)
#evaluatepartial(1000, 0)
evaluate()
