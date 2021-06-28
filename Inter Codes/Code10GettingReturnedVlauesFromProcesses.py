#multiprocessing is useful like we have to use 
#or run same function but with diff args thenn we can run them at the same
#time to compare 

from multiprocessing import Pool

def job(num):
	return num *2

if __name__ == '__main__':
	p = Pool(processes=20)
	data = p.map(job, range(40))
	p.close()
	print(data)
