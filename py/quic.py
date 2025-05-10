# implementing quicksort


# a function to find the partition position
def partition(arr, low, high):
    # a pivot element which will shift the low and high elements of the array
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# a function to implement quicksort which is recursive and uses the partition function
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array: ", arr)
