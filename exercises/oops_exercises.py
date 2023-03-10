#1
'''
class Vehicle:
    def __init__(self,name,mileage,speed):
        self.name=name
        self.mileage=mileage
        self.speed=speed
    def fun(self):
        print(self.name)

class Child(Vehicle):
    pass

bus=Child('volvo',10,"150KM\hr")
print(f'vehicle name:{bus.name}\tmilage:{bus.mileage}\tspeed:{bus.speed}')


#2
class Vehicle:
    color='white'
    def __init__(self,name,mileage,speed):
        self.name=name
        self.mileage=mileage
        self.speed=speed

class Car(Vehicle):
    pass
class Bus(Vehicle):
    pass

bus=Car('volvo',10,"150KM\hr")
car=Bus('audi q8',6,'170KM\hr')
print(f'color:{Bus.color}\tvehicle name:{bus.name}\tmilage:{bus.mileage}\tspeed:{bus.speed}')
print(f'color:{Car.color}\tvehicle name:{car.name}\tmilage:{car.mileage}\tspeed:{car.speed}')

'''

#3
class Vehicle:
    color='white'
    def __init__(self,name,mileage,capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity*100


class Bus(Vehicle):
    def fare(self):
        total=super().fare()
        total=total+total*10/100
        return total
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


#4
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))

#5


