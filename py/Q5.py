# Program to find the samllesst divisior of a number(other than 1)
num = int(input("Enter a number: "))
for i in range(2, num + 1):
    if num % i == 0:
        print("The smallest divisor of number is: ", i)
        break
