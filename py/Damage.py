class Distance:
    def __init__(self, km):
        self.km = km

    def __sub__(self, other):
        return Distance(self.km - other.km)

    def __str__(self):
        return f"{self.km} km"


# Example usage
d1 = Distance(100)
d2 = Distance(40)

d3 = d1 - d2
print("Distance after subtraction:", d3)
