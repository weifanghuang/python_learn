import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):
	"""Test for city_function.py"""

	def test_city_country_name(self):
		living = city_country('santigo','chile')
		self.assertEqual(living, 'Santiago,Chile')

unittest.main()