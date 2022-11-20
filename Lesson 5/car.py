class Car:
    fuel = 20
    rate = 0.1
    traveled = 0

    def __init__(self, fuel=20, rate=0.1):
        self.fuel = fuel
        self.rate = rate

    def __str__(self):
        return f'fuel: {self.fuel}' \
               f'rate: {self.rate}' \
               f'traveled: {self.traveled}\n'

    def drive(self, distance):
        if self.fuel < distance * self.rate:
            raise ValueError('Не хватает топлива!')
        else:
            self.traveled += distance
            self.fuel -= distance * self.rate

car1 = Car()
print(car1)
try:
    car1.drive(202)
except CarNotEnoughFuel:
    print('Не хватает топлива')
print(car1)
