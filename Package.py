class Package:
    def __init__(self, pack_ID, address, city, state, zip, deadline, weight, status):
        self.pack_ID = pack_ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
    
    def update_address(self, address, state, city, zip):
        self.address = address
        self.state = state
        self.city = city
        self.zip = zip

    def set_delivery_time(self, time):
        self.delivery_time = time

    def update_status(self, time_delta):
        if self.departure_time > time_delta:
            self.status = "Hub"
        elif self.delivery_time < time_delta:
            self.status = "Delivered"
        else:
            self.status = "En route"
            
    
    def __str__(self):
        if self.status == "Hub" or self.status == "En route":
            return f"{self.pack_ID}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight} KILO, {self.status}"
        else:
            return f"{self.pack_ID}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight} KILO, {self.status} at {self.delivery_time}"