# Given an non negative integer x, compute and return the square root of x.
# example:
# Input: x = 4
# Output: 2
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
# Note: You are not allowed to use any built-in function which directly computes the square root, such as sqrt.


def sqrt(x):
    if x == 0:
        return 0
    left = 1
    right = x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


print(sqrt(4))
print(sqrt(8))
