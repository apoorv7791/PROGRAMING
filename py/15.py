# 16.Accept list and key as input and find the index of the key in the list using linear search
# Input: [1, 2, 3, 4, 5], 3
# Output: 2

num = int(input("Enter the number of elements in the list: "))
list = [int(input("Enter element: ")) for i in range(num)]
key = int(input("Enter the key to search: "))
found = False
for i in range(len(list)):
    if list[i] == key:
        print(f"Key found at index {i}")
        found = True
        break
if not found:
    print("Key not found")
