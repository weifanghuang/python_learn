
from User import User


def show_privieges():
	"""Print a message show the admin's privilege"""
	privileges = ['can add post', 'can delete post', 'can ban user']
	print("\nI will show you the admin's privileges.")
	for privilege in privileges:
		print("Admin Privilege: " + privilege)


class Privileges():
	"""Model aspects the privilege of admin."""

	def __init__(self, privileges=None):
		"""Initialize admin privileges attributes."""
		if privileges is None:
			privileges = []
		self.privileges = privileges


class Admin(User):
	"""Model aspects of user specific to admin"""

	def __init__(self,first_name, last_name, username, age, location):
		"""
		Initialize attributes of the parent class.
		Then initialize satiates specific to admin
		"""
		super().__init__(first_name, last_name, username, age, location)
		self.privileges = Privileges()


eric = Admin('eric', 'mattes', 'e_mattheus', '29', 'alaska')
eric.describe_user()
eric.greet_user()
show_privieges()
