#GIL Global Interpret Lock
#memory management safeguard
#junior CPU = 1 Core
#muliprocess libraries helps in
#carrying multiple  process that may/may not talk to each other 

import multiprocessing 

def spawn(num, num2):
	print('Spawned! {} {}'.format(num, num2))


if __name__ == '__main__':
	for i in range(50):
		#Here we are doing almost the same process
		p = multiprocessing.Process(target=spawn, args = (i,i+1))
		#syntax (i,)
		p.start()
		#p.join()
		#if we use p.join we can make sure it is in order
#Their order of processing can be different