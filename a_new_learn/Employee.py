class Employee():
	"""save give raise"""

	def __init__(self, first_name, second_name, salary):
		"""save salary"""
		self.first_name = first_name.title()
		self.second_name = second_name.title()
		self.salary = salary

	def give_raise(self,amount = 5000):
		#默认值添加在函数内
		"""give raise 50000"""
		self.salary += amount
	
	def show_salary(self):
		"""show the new salary"""
		print(self.salary)

