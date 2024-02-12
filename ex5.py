import random
import timeit
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


def binarySearch(a, item, low, high):

    if (high == low):
        if(item > a[low]):
            return (low + 1)
        else:
            return low

    if low > high:
        return low
    
    mid = (low + high) // 2
 
    if (item == a[mid]):
        return mid + 1
    elif (item > a[mid]):
        return binarySearch(a, item, mid + 1, high)
    elif item < a[mid]:
        return binarySearch(a,item, low, mid-1)
    
 
def insertionSortBinary(arr, n):
    i = 0
    loc = 0
    j = 0
    k = 0
    selected = 0
 
    for i in range (1,n):
        j = i - 1
        selected = arr[i]
 
        loc = binarySearch(arr, selected, 0, j)
 
        arr[loc+1:i+1] = arr[loc:i]
        arr[loc] = selected
    
    return arr
    

def insertionSort(arr, n):
    i = 0
    key = 0
    j = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i -1

        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j += -1
        
        arr[j+1]= key
    return arr

vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
binaryTimes = []
regularTimes = []
sizes = []

for size in vector_sizes:
    for i in range(0,5):
        arr = [random.randint(1, size*10) for _ in range(size)]  # Create a random vector

        binaryTimes.append(timeit.timeit(lambda: insertionSortBinary(arr.copy(), size), number=1))
        regularTimes.append(timeit.timeit(lambda: insertionSort(arr.copy(), size), number=1))
        sizes.append(size)


#Produce a linear regression plot
def linear(x, a, b):
    return a*x + b
constants = curve_fit(linear, sizes, binaryTimes)
linevalues = [constants[0][0] * x + constants[0][1] for x in vector_sizes]
plt.plot(vector_sizes, linevalues, 'r')

# Save the plot to a file named output.5.3.1.png
plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.title('Binary Insertion Sort')

def quad(x, a, b):
    return a*np.power(x,2) + b
constants = curve_fit(quad, sizes, regularTimes)
linevalues = [constants[0][0] * np.power(x,2) + constants[0][1] for x in vector_sizes]
plt.plot(vector_sizes, linevalues, 'r')

# Save the plot to a file named output.5.3.2.png
plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.title('Regular Insertion Sort')
plt.savefig('output.5.3.png')


#4
#The insertion sort with the binary sort is faster. Because instead of looking for the spot where the selected int fits.
#It's using binary search to speed up the process to find where the selected int fits in the array.