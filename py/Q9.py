#  Compute the euler’s number . Use the formula e = 1 + 1/1! 1/2! + ……


def euler_number(terms):
    e = 1
    factorial = 1
    for i in range(1, terms):
        factorial *= i
        e += 1 / factorial
    return e


terms = int(input("Enter the number of terms: "))
euler_number = euler_number(terms)
print(f"Euler's number (e) calculated with {terms} terms is: {euler_number}")
