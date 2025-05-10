array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_sum(array):
    """
    This function takes an array as input and returns the sum of its elements.
    """
    total = 0
    for num in array:
        total += num
    return total


def get_average(array):
    """
    This function takes an array as input and returns the average of its elements.
    """
    total = get_sum(array)
    avearage = total / len(array)
    return avearage


def get_max(array):
    """
    This function takes an array as input and returns the maximum element in the array.
    """
    max = array[0]
    for num in array:
        if num > max:
            max = num
    return max


def get_min(array):
    """
    This function takes an array as input and returns the minimum element in the array.
    """
    min = array[0]
    for num in array:
        if num < min:
            min = num
    return min


print(get_sum(array))  # Output: 55
print(get_average(array))  # Output: 5.5
print(get_max(array))  # Output: 10
print(get_min(array))  # Output: 1
