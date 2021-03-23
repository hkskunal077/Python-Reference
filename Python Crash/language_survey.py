from survey import AnonymousSurvey 

question = "What lang did u first learn to speak? "
my_survey = AnonymousSurvey(question)

my_survey.show_question()



print("Enter q to quit ")
while True:
	response = input("\nLang: ")
	if response == 'q':
		break
	my_survey.store_response(response)	



print("\n")
my_survey.show_results()	
