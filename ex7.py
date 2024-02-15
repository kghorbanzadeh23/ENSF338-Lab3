import numpy as np
import time
import matplotlib.pyplot as plt


arr = np.loadtxt('C:\Users\bi_77\Downloads\ex7data.json')

def binary_search(arr, target, start_midpoint=0):
    left = 0
    right = len(arr) - 1

    # Adjust the start midpoint if it's within the bounds
    start_midpoint = max(0, min(start_midpoint, right))

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

# Function to time the performance of binary search with different midpoints
def time_binary_search(arr, target, start_midpoints):
    times = []
    for midpoint in start_midpoints:
        start_time = time.time()
        binary_search(arr, target, midpoint)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Perform binary searches with different midpoints
target = 42  
num_tasks = 10
start_midpoints = np.linspace(0, len(arr) - 1, num_tasks, dtype=int)
search_times = time_binary_search(arr, target, start_midpoints)

# Choose the best midpoint for each task
best_midpoints = [start_midpoints[np.argmin(search_times)] for _ in range(num_tasks)]

# Produce scatterplot 
plt.scatter(range(num_tasks), search_times, label='Search Times')
plt.scatter(range(num_tasks), [search_times[i] for i in best_midpoints], color='red', label='Best Midpoints')
plt.xlabel('Task')
plt.ylabel('Time (seconds)')
plt.title('Performance of Binary Search with Different Midpoints')
plt.legend()
plt.show()
