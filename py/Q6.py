# Print all the integers that are not divisible by either 2 or 3 and lie between 1 and 50

for i in range(1, 51):
    if i % 2 != 0 and i % 3 != 0:
        print(i)
    else:
        continue
print("Numbers which are not divisible by 2 and 3 are: ", i)
