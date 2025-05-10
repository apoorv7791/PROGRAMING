# what is a dictionary?
# a dictionary is a collection of key-value pairs
# what is a key-value pair?
# a key-value pair is a pair of a key and a value
# what is a key?
# a key is a unique identifier for a value in a dictionary
# what is a value?
# a value is the data associated with a key in a dictionary


# how to find a missing number in a list of numbers
# we can find a missing number in a list of numbers by using the formula
# sum of all numbers - sum of all numbers in the list
# example:
# numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
# sum of all numbers = 55
# sum of all numbers in the list = 40
# missing number = 15


list = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = 10
sum_of_all_numbers = n * (n + 1) // 2
sum_of_all_numbers = sum(list)
sum_of_all_numbers_in_the_list = sum(list)
missing_number = sum_of_all_numbers - sum_of_all_numbers_in_the_list
print(missing_number)
