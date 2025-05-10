# 8.Write a program that reads a string and then prints a string that capitalizes every other letter in the string. E.g., corona becomes cOrOnA.


def capitalize_every_other_letter(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result


print(capitalize_every_other_letter("corona"))  # cOrOnA
print(capitalize_every_other_letter("python"))  # pYtHoN
print(capitalize_every_other_letter("java"))  # jAvA
