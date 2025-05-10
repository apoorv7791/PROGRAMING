# # given array of integers find those which are occurring twice
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
# array.sort()
# for i in range(len(array) - 1):
#     if array[i] == array[i + 1]:
#         print(array[i])
#     else:
#         continue
# print("we have found duplicate numbers in the given array")
# # The above code snippet is used to find the duplicate numbers in the given array of integers.
# # The array is sorted and then compared with the next element to find the duplicate numbers.


# use of set
s = set()
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
for i in range(len(array)):
    if array[i] in s:
        print(array[i])
    else:
        s.add(array[i])
print("we have found duplicate numbers in the given array")
