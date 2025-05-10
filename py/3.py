# 3.Python Program to Find Element Occurring Odd Number of Times in a List


def find_odd_occurrence(arr):
    result = 0
    for element in arr:
        result ^= element
    return result


# Example usage
if __name__ == "__main__":
    arr = [2, 3, 5, 4, 5, 2, 4, 3, 5]
    print("Element occurring odd number of times is:", find_odd_occurrence(arr))
