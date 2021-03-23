import unittest
from survey import AnonymousSurvey


# Any objects created in the setUp() method
# are then available in each test method you write.
class TestAS(unittest.TestCase):

	def setUp(self):
		question = "what lang did u learn first?? "
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Spanish','Mandarin']

	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		for res in self.responses:
			self.my_survey.store_response(res)

		for res in self.responses:
			self.assertIn(res, self.my_survey.responses)		



class TestAnonymousSurvey(unittest.TestCase):
	""" Test for the class Anonymous survey"""

	def test_store_single_response(self):
		question = "What lang did u learn first?? "
		my_survey =  AnonymousSurvey(question)
		my_survey.store_response('English')

		self.assertIn('English',my_survey.responses)

	def test_store_three_responses(self):
		question = "What lang did u learn first?? "
		my_survey = AnonymousSurvey(question)
		responses=['English','Spanish','Mandarin']
		for res in responses:
			my_survey.store_response(res)
		for r in responses:
			self.assertIn(r,my_survey.responses)

			


unittest.main()
