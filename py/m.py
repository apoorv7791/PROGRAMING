# program to implement merge sort
def merge_sort(arr):  # function to implement merge sort
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
    return arr


arr = [12, 11, 13, 5, 6, 7]
print("Given array is", arr)
print("Sorted array is", merge_sort(arr))


# Output:
# Given array is [12, 11, 13, 5, 6, 7]
# Sorted array is [5, 6, 7, 11, 12, 13]

# Explanation:

# In the above program, we have implemented the merge sort algorithm. The merge_sort function takes an array as a parameter and sorts it using the merge sort algorithm. The merge_sort function is a recursive function that divides the array into two halves and calls itself for each half. The merge_sort function then merges the two halves in sorted order.
# The merge_sort function uses the merge function to merge the two halves of the array. The merge function takes two arrays as parameters and merges them in sorted order. The merge function uses three pointers i, j, and k to iterate over the two arrays and the merged array.
# The merge_sort function returns the sorted array.
# The given array is [12, 11, 13, 5, 6, 7]. The sorted array is [5, 6, 7, 11, 12, 13].
# The merge sort algorithm has a time complexity of O(n log n) and a space complexity of O(n).
# The merge sort algorithm is a stable sorting algorithm that is efficient for large datasets.
# The merge sort algorithm is a divide and conquer algorithm that divides the array into two halves and sorts them recursively.
# The merge sort algorithm is a comparison-based sorting algorithm that compares elements to sort them.
