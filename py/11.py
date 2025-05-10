# 12.Python Program to Find the Total Sum of a Nested List Using Recursion
# Input: [1, 2, [3, 4, [5, 6]], 7]
# Output: 28


def total_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += total_sum(element)
        else:
            total += element
    return total


print(total_sum([1, 2, [3, 4, [5, 6]], 7]))  # 28
# Output: 28
