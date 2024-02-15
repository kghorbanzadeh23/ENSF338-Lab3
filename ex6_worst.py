import timeit 
import random
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import sys
sys.setrecursionlimit(1500)

def partition(array, low, high):
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
  
 
def quicksort(array, low, high):
    if low < high:

        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the list

def binary_search_quicksort(arr, target):
    quicksort(arr, 0 ,len(arr)-1)
    binary_search(arr,target)

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



if(__name__ == "__main__"):
    #5
    vectorSizes = [10,20,50,100,200,500,1000]
    binaryTimes = []
    linearTimes = []

    for x in vectorSizes:
        arr = [k for k in range(x,0,-1)]
        target = random.randint(0,x - 1)
        rezLinear = []
        rezBinary = []
        for i in range(0,1):

            tm = timeit.timeit("linear_search(arr, target)", setup="from __main__ import linear_search, arr, target", number=1)            
            rezLinear.append(tm)

            tm = timeit.timeit("binary_search_quicksort(arr.copy(), target)", setup="from __main__ import binary_search_quicksort, arr, target", number=1)                        
            rezBinary.append(tm)

        binaryTimes.append(sum(rezBinary)/ len(rezBinary))
        linearTimes.append(sum(rezLinear)/ len(rezLinear))

        print("Binary search time for", x, "is", sum(rezBinary)/ len(rezBinary))
        print("Linear search time for", x, "is", sum(rezLinear)/ len(rezLinear), "\n")

    def quad(x, a, b):
        return a*np.power(x,2) + b
    constants = curve_fit(quad, vectorSizes, binaryTimes)
    linevalues = [constants[0][0] * np.power(x,2) + constants[0][1] for x in vectorSizes]
    plt.scatter(vectorSizes,binaryTimes, c='b')
    plt.plot(vectorSizes, linevalues, 'b', label="Binary Search")

    slope, intercept = np.polyfit(vectorSizes, linearTimes, 1)
    linevalues = [slope * x + intercept for x in vectorSizes]
    plt.scatter(vectorSizes,linearTimes, c='r')
    plt.plot(vectorSizes, linevalues, 'r', label="Linear Search")

    # Save the plot to a file named output.5.3.2.png
    plt.xlabel('Number of Records')
    plt.ylabel('Time')
    plt.title('Comparison Between Linear and Binary Search (Worst Case QuickSort)')
    plt.legend()
    plt.savefig('output.6.5.png')
