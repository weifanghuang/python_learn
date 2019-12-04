import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
	"""test the Employee"""

	def setUp(self):
		"""Make an employee to use in test"""
		self.kim = Employee('huang','weifang',10000)
		
	def test_give_default_raise(self):
		"""Test give default raise"""
		self.kim.give_raise()
		self.assertEqual(self.kim.salary,15000)

	def test_give_custom_raise(self):
		self.kim.give_raise(2000)
		self.assertEqual(self.kim.salary,12000)
		
unittest.main()
