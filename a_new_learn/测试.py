import unittest
from full_names import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for the name.py"""

	def test_first_last_name(self):
		"""Can correctly handle the name"""
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Can test the name like huang wei fang"""
		formatted_name = get_formatted_name('huang','fang','wei')
		self.assertEqual(formatted_name, 'Huang Wei Fang')

unittest.main()
