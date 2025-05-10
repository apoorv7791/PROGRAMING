# Print all numbers in a range divisible by a given number
n = int(input("Enter the number"))
for i in range(1, 27):
    if i % n == 0:
        print(i)
