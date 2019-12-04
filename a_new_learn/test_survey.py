import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""test the AnonymousSurvey"""

	def setUp(self):
		"""
		Create a survey object and a set of answers
		for use by the test method uesd
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Japanese','Chinese']

	def test_store_single_response(self):
		"""test single response"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_much_response(self):
		"""test many responses"""
		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()
