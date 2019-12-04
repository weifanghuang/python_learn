import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):
	"""Test for city_function.py"""

	def test_city_country_name(self):
		living = city_country('santigo', 'chile',5000000)
		self.assertEqual(living, 'Santigo,Chile,5000000')

unittest.main()
