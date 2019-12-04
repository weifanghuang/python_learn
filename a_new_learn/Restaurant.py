class Restaurant():
	"""A class reprenting a restaurant."""
	
	def __init__(self, name, cuisine_type):
		"""Initializa restaurant_name and cuisine_type attributes"""
		self.name = name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Display a summary of the restaurant"""
		msg = self.name.title() + " serves wonderful " + self.cuisine_type + " ! "
		print("\n" + msg)
		
	def open_restaurant(self):
		"""Display business hours of the restaurant"""
		msg = self.name+ " is open. Come on in!"
		print("\n" + msg)

	def set_number_served(self, number_served):
		"""Allow user to set the numberb of customers that have been served."""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served

class IceCreamStand(Restaurant):
	"""Model aspects of a restaurant, specific to Ice Cream stand"""

	def __init__(self, name, cuisine_type):
		"""
		Initialize attributes of the parent class.
		Then initialize stributes specific to an Ice Cream stand
		"""
		super().__init__(name, cuisine_type)
		self.flavors =[ ]

	def show_flavors(self):
		"""Display the flavors available"""
		print("\nWe will show the flavors of us ice cream")
		for flavor in flavors:
			print("\tflavors :" + flavor.title() + " Ice Cream")
