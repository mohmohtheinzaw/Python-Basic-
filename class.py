class Car : 
    # class level attribute
    sterringWheel = 1
    

    # class level method
    @classmethod
    def common(cls) :
        print(f'all car have only one {cls.sterringWheel} steering wheel .')

    # instance level attribute
    def __init__(self,name,wheels):
        self.name = name
        self.wheels= wheels

    # instance level method
    def drive(self):
        print(f'{self.name} is driving ')

car = Car("Honda Fit",4)        
print(car.name)
print(car.wheels)
car.drive()

print(Car.sterringWheel)
print(Car.common())


print(car.sterringWheel)
print(car.common())