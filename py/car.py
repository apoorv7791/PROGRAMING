class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")
        return f"The {self.year} {self.make} {self.model} is starting."

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")
        return f"The {self.year} {self.make} {self.model} is stopping."

    def accelerate(self):
        print(f"The {self.year} {self.make} {self.model} is accelerating.")
        return f"The {self.year} {self.make} {self.model} is accelerating."

    def brake(self):
        print(f"The {self.year} {self.make} {self.model} is braking.")
        return f"The {self.year} {self.make} {self.model} is braking."


c = Car("Toyota", "Corolla", 2020)
print(c.start())
print(c.stop())
print(c.accelerate())
print(c.brake())
