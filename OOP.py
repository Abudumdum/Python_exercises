


class Vehicle:
    color = 'Blue' 
    def __init__(self, max_speed, mileage, name, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        self.capacity = capacity
    
    def seating_capacity(self):
        return f'the seating capacity of a {self.name} is {self.capacity} passengers'


    def fare(self):
        return self.capacity * 1000



class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)
    
    def fare(self):
        amount = super().fare()
        amount += amount * 0.1 
        return '$'+ str(amount)


mitsubishi = Bus(100, 15, 'Big School bus', 50)
audi = Vehicle(100, 15, 'Audi R8', 5)

# print( 'color: ', audi.color ,'Vehicle name: ' , audi.name, 'speed: ', audi.max_speed,' Mileage: ', audi.mileage)

print(audi.seating_capacity())
print(mitsubishi.fare())
print(isinstance(mitsubishi, Vehicle))