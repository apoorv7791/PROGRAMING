# Program to implement the selection sort algorithm
def selection_sort(arr):  # Function to implement selection sort
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print("Array before sorting: ", arr)
print("Array after sorting with selection sort: ", selection_sort(arr))


# How does this work?
# The selection sort algorithm works by dividing the input array into two parts: the sorted part and the unsorted part.
# The sorted part is initially empty, and the unsorted part contains the entire array.
# The algorithm then iterates over the unsorted part of the array, finding the minimum element and swapping it with the
# first element of the unsorted part. This process is repeated until the entire array is sorted.
# The time complexity of the selection sort algorithm is O(n^2) in the worst case, where n is the number of elements in
# the input array. This is because the algorithm requires two nested loops to iterate over the array and find the minimum
# element at each step.
# The space complexity of the selection sort algorithm is O(1) because it does not require any additional memory beyond
# the input array itself. This makes it an in-place sorting algorithm, meaning it does not require any additional memory
# to store intermediate results.
