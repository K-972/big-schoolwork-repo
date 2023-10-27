class vehicle:
    def __init__(self, name, speed, mileage):
        self.mileage = mileage
        self.name = name
        self.speed = speed
    def __str__(self):
        return f'{self.name}, {self.speed}, {self.mileage}'

tony = vehicle('toyota', '45', '125')
print(tony)

class bus(vehicle):
    

    def __str__(self):
        return f'{self.name}, {self.speed}, {self.mileage}, {self.capacity}'
    
school = bus('toyota', '45', '125')
print(tony)