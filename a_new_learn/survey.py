class AnonymousSurvey():
	"""save annoymous survey"""

	def __init__(self, question):
		"""save a question, and ready to save the answer"""
		self.question = question
		self.responses = []

	def show_question(self):
		"""show the survey"""
		print(self.question)

	def store_response(self, new_response):
		"""save new answer"""
		self.responses.append(new_response)

	def show_results(self):
		"""show the survey"""
		print("Survey responses:")
		for response in self.responses:
			print("-" + response.title())
