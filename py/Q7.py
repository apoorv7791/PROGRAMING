# 7.Accept a number n and prints an identity matrix of nXn
num = int(input("Enter the number"))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
