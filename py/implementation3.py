# check if a number is plaindormme or not
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if temp == rev:
    print("The number is plaindrome")
else:
    print("The number is not plaindrome")
