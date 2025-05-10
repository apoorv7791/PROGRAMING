# program to print fibonacci series
a = 0
b = 1
for c in range(10):
    print(a)
    c = a + b
    a = b
    b = c
print("The fibonacci series is: ", c)
# Notes about the code:
# what is a fibonacci series?
# a fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers
