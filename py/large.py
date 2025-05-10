# 1.Program to find the second largest element in a list ‘Num’.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max = 0
second_max = 0
for i in num:
    if i > max:
        second_max = max
        max = i
    elif i > second_max:
        second_max = i
    else:
        continue
print("List: ", num)
print("Largest element in the list: ", max)
print("Second largest element in the list: ", second_max)
