import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time
import sys
sys.setrecursionlimit(20000)


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

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

if __name__ == "__main__":
    #2
    arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Original array:", arr)

    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)

    sizes = [100, 500, 1000, 2000]  # Sizes of arrays to test
    timings = []
    for size in sizes:
        arr = list(range(size, 0, -1))  # Create an array in descending order
        start_time = time.time()  # Start time
        quicksort(arr, 0, len(arr) - 1)  # Perform quicksort
        end_time = time.time()  # End time
        timings.append(end_time - start_time)
    
    for i in range(len(sizes)):
        print(f"Array size: {sizes[i]}, Time taken: {timings[i]} seconds")
""""
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, timings, 'bo', label='Execution Time')

    # Fit curve
    popt, _ = curve_fit(quadratic, sizes, timings)
    sizes_fit = np.linspace(min(sizes), max(sizes), 100)
    plt.plot(sizes_fit, quadratic(sizes_fit, *popt), 'r-', label='Quadratic Fit')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Time Complexity')
    plt.legend()
    plt.grid(True)
    plt.savefig('output.4.4.png')
"""