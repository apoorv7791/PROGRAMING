# program to find the second largest element in list nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max = 0
second_max = 0
for num in nums:
    if num > max:
        second_max = max
        max = num
    elif num > second_max:
        second_max = num
print(second_max)
print(max)
