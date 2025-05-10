# permutations
# Given an array of integers, return all the permutations of the array.
#
# Example:
# Input: [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# The output is a list of lists containing all possible permutations of the input array.
# The permutations function takes an array as input and returns a list of lists containing all possible permutations of the input array.


def permutations(arr):
    if len(arr) == 1:
        return [arr]
    perms = []
    for i in range(len(arr)):
        elem = arr[i]
        remaining = arr[:i] + arr[i + 1 :]
        for perm in permutations(remaining):
            perms.append([elem] + perm)
    return perms


arr = [1, 2, 3]
print(permutations(arr))


# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Explanation:
# In the above program, we have implemented the permutations function that returns all possible permutations of an input array.
# The permutations function takes an array as input and returns a list of lists containing all possible permutations of the input array.
# The permutations function uses recursion to generate all possible permutations of the input array.
# The base case of the recursion is when the input array has only one element, in which case the function returns a list containing the input array.
# The permutations function iterates over each element in the input array and generates permutations by recursively calling the function on the remaining elements.
# The permutations function appends the current element to the permutations generated from the remaining elements.
# The permutations function returns the list of all possible permutations of the input array.
