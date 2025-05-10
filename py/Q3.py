# Accept all three digits from the user and print all possible combinations of the digits.
# 123
# 132
# 213
# 231
# 312
# 321

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print([a, b, c])
print([a, c, b])
print([b, a, c])
print([b, c, a])
print([c, a, b])
print([c, b, a])
