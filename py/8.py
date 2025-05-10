# 9.Python Program to Remove the Given Key from a Dictionary

# Input: {'a': 1, 'b': 2, 'c': 3}, key = 'b'
# Output: {'a': 1, 'c': 3}

my_dict = {"a": 1, "b": 2, "c": 3}
key = "b"
if key in my_dict:
    del my_dict[key]
print(my_dict)  # {'a': 1, 'c': 3}
# Output: {'a': 1, 'c': 3}
