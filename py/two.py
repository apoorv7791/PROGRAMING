# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

my_list = [3, 2, 2, 3]
val = 3
while val in my_list:
    my_list.remove(val)
print("List after removing the value: ", my_list)

# input: [3, 2, 2, 3], 3
# output: [2, 2]
