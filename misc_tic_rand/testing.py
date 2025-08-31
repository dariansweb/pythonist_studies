class Car:
    # Class Attributes
    wheels = 4
    doors = 2
    engine = True

    # The Initializer
    def __init__(self, model, year, make='Ford', gas=100):
        # Instance Attributes
        self.make = make
        self.model = model
        self.year = year
        self.gas = gas
        self.is_moving = False

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def stop(self):
        if self.is_moving:
            print('The car has stopped.')
            self.is_moving = False
        else:
            print('The car has already stopped.')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car starts moving.')
                self.is_moving = True
            print(f'The car is going {speed}.')
        else:
            print("You've run out of gas!")
            self.stop()

    def use_gas(self):
        self.gas -= 20
        if self.gas <= 0:
            return False
        return True
      

# add your lines to create and test instances here
car_one = Car("Model F", 1901)
print(car_one)
