# Reverse a string and the string is an array of characters.
# Do not modify the input array.
#
# Example 1:
# Input: ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]
#
# Example 2:
# Input: ["H", "a", "n", "n", "a", "h"]
# Output: ["h", "a", "n", "n", "a", "H"]


def reverse_string(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


s = ["h", "e", "l", "l", "o"]
print(reverse_string(s))

s = ["H", "a", "n", "n", "a", "h"]
print(reverse_string(s))
