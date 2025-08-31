class Car:
	wheels = 4
	doors = 2
	engine = True
	
	def __init__(self, model, year, make="Ford"):
		self.model = model
		self.year = year
		self.make = make
		self.gas = 100
		self.is_moving = False
		
	def stop(self):
		if self.is_moving:
			print("The car has stopped.")
			self.is_moving = False
		else:
			print("The car has already stopped.")
	
	def go(self, speed):
		if self.use_gas():
			if not self.is_moving:
				print("The car started moving.")
				self.is_moving = True
			print(f'The car is going {speed}')
		else:
			print("You have run out of gas.")
			self.stop()
		
	def use_gas(self):
		self.gas -= 50
		if self.gas <= 0:
			return False
		else:
			return True
		
car_one = Car("Model T" , 1908)
car_two = Car("Rolls Royce", "Viper", 2020)

# print(car_one.make)
# print(car_two.doors)
car_one.stop()
car_one.go(10)
car_one.go(20)
car_one.go(10)
car_one.stop()

