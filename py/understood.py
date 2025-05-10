# functions


def square(x):
    return x * x


def cube(x):
    return x * x * x


def main():
    num = int(input("Enter a number: "))
    print("Square of", num, "is", square(num))
    print("Cube of", num, "is", cube(num))


main()
