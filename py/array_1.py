# insertion and deletion in array
array = [1, 2, 3, 4, 5]
print(array)
array.insert(2, 100)
print(array)

array.remove(4)
print(array)

print(array[2])

array[2] = 200
print(array)

print(len(array))


if 4 in array:
    print("yes")
else:
    print("no")


# string and it's functions

s = "hello"
b = s + " world"
print(b)
