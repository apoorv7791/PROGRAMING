# how can i build something with python?
# with what i  have learned so far, i can build a simple calculator


# build a simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation: ")

if operation == "+":
    print("Addition:", a + b)
elif operation == "-":
    print("Subtraction:", a - b)
elif operation == "*":
    print("Product:", a * b)
elif operation == "/":
    print("Division:", a / b)
else:
    print("Invalid operation")
