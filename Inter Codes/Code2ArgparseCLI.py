import argparse
import sys


def main():
	parser = argparse.ArgumentParser(description= 'Just a Simple Calculator') 
	parser.add_argument('--x', type =float, default = 1.0,help="What is the first number ")
	parser.add_argument('--y', type =float, default = 1.0,help="What is the second number ")
	parser.add_argument('--operation', type =str , default = 'add',help="What operation u want ")
	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))

def calc(args):
	if args.operation == 'add':
		return args.x+args.y
	elif args.operation == 'sub':
		return args.x-args.y
	elif args.operation == 'mul':
		return args.x*args.y
	elif args.operation  == 'div':
		return args.x/args.y						


if __name__ == '__main__':
	main()


 
#We can run this code as a CLI cmd 
#Calling out features of it on cmdd 
#amaking them our own 
