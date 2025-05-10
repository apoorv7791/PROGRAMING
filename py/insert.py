# program to implement the insertion sort algorithm
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr


arr = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print("Array before sorting: ", arr)
print("Array after sorting with insertion sort: ", insertion_sort(arr))

# How does this work?
# The insertion sort algorithm works by dividing the input array into two parts: the sorted part and the unsorted part.
# The sorted part is initially empty, and the unsorted part contains the entire array.
# The algorithm then iterates over the unsorted part of the array, taking each element and inserting it into the correct
# position in the sorted part. This process is repeated until the entire array is sorted.
# The time complexity of the insertion sort algorithm is O(n^2) in the worst case, where n is the number of elements in
# the input array. This is because the algorithm requires two nested loops to iterate over the array and insert each
# element at the correct position.
# The space complexity of the insertion sort algorithm is O(1) because it does not require any additional memory beyond
# the input array itself. This makes it an in-place sorting algorithm, meaning it does not require any additional memory
# to store intermediate results.
# The insertion sort algorithm is more efficient than the selection sort algorithm for small input sizes or when the
# input array is nearly sorted. This is because the insertion sort algorithm only requires one comparison per element
# in the best case, while the selection sort algorithm requires n comparisons per element in all cases.
