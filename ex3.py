import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math
import numpy as np
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0,n-i-1):
            comparisons += 1
            if(arr[j] > arr[j+1]):
                swaps += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print("Swaps:", swaps)
    print("Comparisons", comparisons, "\n")
    return swaps,comparisons


vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
swapList = []
comparisonsList = []
for size in vector_sizes:
    arr = [random.randint(1, size*10) for _ in range(size)]  # Create a random vector
    swap, comparison = bubble_sort(arr)

    swapList.append(swap)
    comparisonsList.append(comparison)
    
#Produce a quadratic regression plot
def quad(x, a, b):
    return a*np.power(x,2) + b
constants = curve_fit(quad, vector_sizes, swapList)
plt.scatter(vector_sizes, swapList)
linevalues = [constants[0][0] * np.power(x,2) + constants[0][1] for x in vector_sizes]
plt.plot(vector_sizes, linevalues, 'r')

# Save the plot to a file named output.3.2.png
plt.xlabel('Number of Records')
plt.ylabel('Number of Swaps')
plt.title('Size of Array Compared to Swaps')
plt.savefig('output.3.4.1.png')

plt.clf()
constants = curve_fit(quad, vector_sizes, comparisonsList)
plt.scatter(vector_sizes, comparisonsList)
linevalues = [constants[0][0] * np.power(x,2) + constants[0][1] for x in vector_sizes]
plt.plot(vector_sizes, linevalues, 'r')

# Save the plot to a file named output.3.2.png
plt.xlabel('Number of Records')
plt.ylabel('Number of Comparisons')
plt.title('Size of Array Compared to Comparisons')
plt.savefig('output.3.4.2.png')