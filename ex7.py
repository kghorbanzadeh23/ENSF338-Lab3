import time
import matplotlib.pyplot as plt
import json
import timeit

def binary_search(arr, target, start_midpoint):
    left = 0
    right = len(arr) - 1

    # Adjust the start midpoint if it's within the bounds
    mid = start_midpoint

    while left <= right:

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return -1  


data = []
with open("ex7data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

targets = []
with open("ex7tasks.json", "r", encoding="utf-8") as file:
    targets = json.load(file)

#2 Find best midpoint
best_midpoints = []
length = len(data) - 1
for i in targets:
    lowest = None
    midpoint = None
    
    for j in range(21):
        k = int(length*j/20)
        tm = timeit.timeit(lambda: binary_search(data, i, k), number=5)/5
        if (lowest == None) or (tm < lowest):
            lowest = tm
            midpoint = k
    best_midpoints.append(midpoint)
    
with open("output.json", "w") as of:
    json.dump(best_midpoints,of, indent=4)

#3
plt.scatter(best_midpoints,targets, c='b')
# Save the plot to a file named output.6.4.png
plt.xlabel('Tasks')
plt.ylabel('Starting Midpoints')
plt.title('Comparison the Best Midpoint and Tasks')
plt.savefig('output.7.3.png')

#4
#I think it does have an affect on performance. As we can see on the graph the tasks have a wide selection of preferred midpoints.
#If the midpoint didn't have an affect on the performance then they would have not so different midpoints choosen between them.
#But since they are spread out we can conclude the starting midpoint does have an affect on performance the program
#choose the midpoint hat gave them the fastest time for that certain task. 