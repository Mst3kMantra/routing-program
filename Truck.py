class Truck:
    def __init__(self, packages, mileage, departure_time, location):
        self.packages = packages
        self.mileage = mileage
        self.time = departure_time
        self.location = location
        self.departure_time = departure_time

    def __str__(self):
        return f"{self.packages}, {self.mileage}, {self.time}, {self.departure_time}, {self.location}"