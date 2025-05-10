# Read a number n and compute n+nn+nnn.
# For example, if n=5, then 5+55+555=615.

n = int(input("Enter a number: "))
square = n * n
cube = n * n * n
print("Square:", square)
print("Cube:", cube)
print("Sum:", n + square + cube)
# What is the output of the following code?
# Enter a number: 5
# Square: 25
# Cube: 125
# Sum: 155
