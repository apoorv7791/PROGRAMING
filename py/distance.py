class Compare:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == self.value


# Example usage


a = Compare(10)
b = Compare(20)

print("Equal: ", a == b)
print("Not Equal :", a != b)
