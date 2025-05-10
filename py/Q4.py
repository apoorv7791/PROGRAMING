# Program to find the digits of a number
num = int(input("Enter a number: "))
sum = 0
for i in str(num):
    sum += int(i)
print("The sum of digits of number is: ", sum)
