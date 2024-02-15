import timeit 
import random
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import time


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left], 
    arr[low], arr[right] = arr[right], arr[low]
    return right

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the list

def binary_search(arr, target):
    left = 0 
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        if arr[mid] == target:
            return mid  # Return the index of the target if found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Return -1 if the target is not in the list

def binary_search_and_quicksort(arr, target):
    quicksort(arr, 0 ,len(arr)-1)
    binary_search(arr,target)


if __name__ == "__main__":

    #2
    arr = [k for k in range(1000)]
    target = random.randint(0,999)
    linearTimes = []
    binaryTimes = []
    for i in range(0,20):
        random.shuffle(arr)
        tm = timeit.timeit("linear_search(arr, target)", setup="from __main__ import linear_search, arr, target", number=1)            
        linearTimes.append(tm)

        tm = timeit.timeit("binary_search_and_quicksort(arr, target)", setup="from __main__ import binary_search_and_quicksort, arr, target", number=1)                        
        binaryTimes.append(tm)

    print("Average time for binary serach time is", sum(binaryTimes)/ len(binaryTimes))
    print("Average time for Linear serach time is", sum(linearTimes)/ len(linearTimes), "\n")


    #3
    vectorSizes = [10,20,50,100,200,500,1000,2000,5000,10000]
    binaryTimes = []
    linearTimes = []

    for x in vectorSizes:
        arr = [k for k in range(x)]
        target = random.randint(0,x - 1)
        rezLinear = []
        rezBinary = []
        for i in range(0,100):
            random.shuffle(arr)
            tm = timeit.timeit("linear_search(arr, target)", setup="from __main__ import linear_search, arr, target", number=1)            
            rezLinear.append(tm)

            tm = timeit.timeit("binary_search_and_quicksort(arr, target)", setup="from __main__ import binary_search_and_quicksort, arr, target", number=1)                        
            rezBinary.append(tm)

        binaryTimes.append(sum(rezBinary)/ len(rezBinary))
        linearTimes.append(sum(rezLinear)/ len(rezLinear))


    slope, intercept = np.polyfit(vectorSizes, binaryTimes, 1)
    linevalues = [slope * x + intercept for x in vectorSizes]
    plt.scatter(vectorSizes,binaryTimes, c='b')
    plt.plot(vectorSizes, linevalues, 'b', label="Binary Search")

    slope, intercept = np.polyfit(vectorSizes, linearTimes, 1)
    linevalues = [slope * x + intercept for x in vectorSizes]
    plt.scatter(vectorSizes,linearTimes, c='r')
    plt.plot(vectorSizes, linevalues, 'r', label="Linear Search")

    # Save the plot to a file named output.5.3.2.png
    plt.xlabel('Number of Records')
    plt.ylabel('Time')
    plt.title('Comparison Between Linear and Binary Search')
    plt.legend()
    plt.savefig('output.6.4.png')

    #4. 
    #It looks like the Linear search is the faster algorithm.

