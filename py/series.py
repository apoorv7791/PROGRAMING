# Use a recursive fucntion to print a fibonacci series

# A function which is used  to calculate the fibonacci series with a paramenter n


def fibonacci(n):
    if n <= 1:  # base case
        return n  # return n if n is less than or equal to 1
    else:
        # recursive case which calls the function itself because it is  the sum of the two preceding numbers

        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
