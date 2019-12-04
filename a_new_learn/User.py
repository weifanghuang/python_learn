class User():
	"""docstring for User"""
	
	def __init__(self, first_name, last_name, username, age, location):
		"""Initializa user profile attributes"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username.title()
		self.age = age
		self.location =location.title()
		self.login_attempts = 0

	def describe_user(self):
		"""Display a summary of the user's information."""
		print("\n" + self.first_name.title() + " " + self.last_name.title())
		print("Username :" + self.username.title())
		print("Age :" + self.age)
		print("Location :" +self.location.title())

	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print("Hello " + self.username.title() + " Welcome!")

	def increment_login_attempts(self):
		"""Increment the value of login_attempts"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login attempts to 0"""
		self.login_attempts = 0





