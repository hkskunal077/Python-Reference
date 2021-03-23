class AnonymousSurvey():
	"""Collects anonymous answers to survey questions"""

	def __init__(self,question):
		"""Store a ques and prepare to store responses"""
		self.question = question
		self.responses = []


	def show_question(self):
		print(self.question)

	def store_response(self,new_response):
		self.responses.append(new_response)

	def show_results(self):
		print("Survey Results: \n")

		for response in self.responses:
			print('---'+ response)			 		



# my_new_survey = AnonymousSurvey("Why does universe exist??")
# my_new_survey.show_question() 


class Journal():
	"""This is journal keeping class"""

	def __init__(self,recent_book,num_books=2):
		self.recent_book=recent_book
		self.num_books=num_books

	def show_rbook(self):
		print("\nLatest Issued Book is "+ self.recent_book)

	def total_books(self):
		if self.num_books>3:
			print("U have more than permissible no. of books\n Please return")

		else:
			print("You have "+ str(self.num_books))	



ks_journal=Journal('Lord of the Rings',4)
ks_journal.total_books()
ks_journal.show_rbook()