from Car import Car

class Battery():
	"""A simple attempt to model an electric car's battery"""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""print a message descriptive battery size"""
		print("This car has a  " + str(self.battery_size) + "-KWh battery.")

	def get_range(self):
		"""Print a atatement about the rang this battery provides"""
		if self.battery_size <= 70:
			range = 240
		elif self.battery_size >= 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge"
		print(message)

	def upgrade_battery(self):
		"""Check the battery capacity"""
		if self.battery_size != 85:
			self.battery_size = 85
			print("Upgrade the battery to 85-KWh.")
		elif self.battery_size == 85:
			print("The battery is already upgraded.")

class ElectricCar(Car):
	"""Model aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initializa attributes of the parent class.
		Then initializa sttributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()





