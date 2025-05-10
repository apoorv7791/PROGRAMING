# check if a stirng is palidrome or not
# input "reacecar" output "True"
# input "hello" output "False"

# We will use the two pointer technique to solve this problem.
# We will use two pointers, one at the beginning of the string and one at the end of the string.
# We will compare the characters at the two pointers.
# If the characters are the same, we will move the pointers towards each other.
# If the characters are different, we will return "not palindrome".
# If the pointers meet, we will return "palindrome".


def palindorme(str):
    left = 0
    n = len(str)
    right = n - 1
    while left < right:
        if str[left] != str[right]:
            return "not palindrome"
        left += 1
        right -= 1
    return "palindrome"


print(palindorme("racecar"))  # output : true
print(palindorme("hello"))  # output : false
print(palindorme("madam"))  # output : true
