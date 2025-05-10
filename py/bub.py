#  program to iplement the bubble sort algorithm
#  bubble sort is a sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order
#  the pass through the list is repeated until no swaps are needed, which indicates that the list is sorted
#  the algorithm is not efficient for large lists, but it is simple to implement and easy to understand
#  the algorithm has a time complexity of O(n^2) where n is the number of elements in the list
#  the algorithm has a space complexity of O(1) where 1 is the number of elements in the list
#  the algorithm is stable, meaning that the relative order of equal elements is preserved


array = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
n = len(array)
for i in range(n - 1):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print("Arrays after sorting: wth bubble sort", array)
