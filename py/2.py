# 2.Write a Python code to delete all odd numbers and negative numbers from a given numeric list.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
count_dict: dict[int, int] = {}
filtered_list = []
for i in num:
    if i % 2 == 1 or i >= 0:
        filtered_list.append(i)
        if i in count_dict:
            count_dict[i] += 1
    else:
        count_dict[i] = 1
print("List: ", filtered_list)
print("Count: ", count_dict)
print("Even numbers: ", filtered_list)
