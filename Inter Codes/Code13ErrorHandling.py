#sys helps in traceback in the system 
import sys
import logging 
#it has a function called exc_info() for handlig traceback errpr information
try:
	a+b
except Exception as e:
	print('Error is {}, {}, Line No. {}'.format(sys.exc_info()[0],
		sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
	# print(sys.exc_info()[0])
	# print(sys.exc_info()[1])
	# print(sys.exc_info()[2].tb_lineno)	
	#using string formatting we do it 
    #We do not know the location of the error
    #we can use it with loggigng too
    