import sys 

sys.setrecursionlimit(20000)

def merge(arr, low, mid, high):
    # Copy data to temporary arrays L[] and R[]
    n1 = mid - low + 1
    n2 = high - mid

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[low + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temporary arrays back into arr[low..high]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = low   # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

if __name__ == "__main__":

    array = [8,42,25,3,3,2,27,3]
    n = len(array)

    merge_sort(array, 0, n-1)

    print(array)