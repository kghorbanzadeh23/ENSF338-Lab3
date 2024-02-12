import random
import time
import sys
import matplotlib.pyplot as plt

# Set recursion limit to avoid stack overflow
sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Function to generate arrays for different scenarios
def generate_arrays(size, scenario):
    if scenario == "best":
        return list(range(size))
    elif scenario == "worst":
        return list(range(size, 0, -1))
    elif scenario == "average":
        return [random.randint(0, 1000) for _ in range(size)]

# Function to measure time taken by sorting algorithm
def measure_time(sort_function, arr, low=None, high=None):
    start_time = time.time()
    if low is not None and high is not None:
        sort_function(arr, low, high)
    else:
        sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Test both algorithms on arrays of various sizes and scenarios
sizes = [10, 50, 100, 500, 1000, 5000, 10000]
scenarios = ["best", "worst", "average"]

for scenario in scenarios:
    bubble_times = []
    merge_times = []
    quick_times = []
    for size in sizes:
        arr = generate_arrays(size, scenario)
        bubble_time = measure_time(bubble_sort, arr.copy())
        merge_time = measure_time(merge_sort, arr.copy())
        quick_time = measure_time(quick_sort, arr.copy(), 0, size - 1)
        bubble_times.append(bubble_time)
        merge_times.append(merge_time)
        quick_times.append(quick_time)
    
    plt.plot(sizes, bubble_times, label='Bubble Sort')
    plt.plot(sizes, merge_times, label='Merge Sort')
    plt.plot(sizes, quick_times, label='Quick Sort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title(f'Scenario: {scenario.capitalize()}')
    plt.legend()
    plt.grid(True)
    plt.show()
