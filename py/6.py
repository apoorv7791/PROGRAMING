# 7.Display Letters which are in the First String but not in the Second
# Input: str1 = "Python", str2 = "Java"
# Output: P y t h o n

str1 = "Python"
str2 = "Java"
for char in str1:
    if char not in str2:
        print(char, end=" ")
print()
# Output: P y t h o n
