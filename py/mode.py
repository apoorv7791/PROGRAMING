class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


c = Car("Toyota", "Corolla", 2020)
c1 = Car("Honda", "Civic", 2021)
c.display_info()
