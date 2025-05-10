# 6.Write a program to determine whether a given string has balanced parenthesis or not.
# # Input: exp = "{()}[]"
# # Output: True


def is_balanced(exp):
    stack = []
    for char in exp:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    if stack:
        return False
    return True


print(is_balanced("{()}[]"))  # True
print(is_balanced("{()}["))  # False
print(is_balanced("{(})"))  # False
