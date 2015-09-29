import argparse
import euler
import pdb

def main():
	parser = argparse.ArgumentParser(description = 'Euler program.')
	parser.add_argument('-n', '--number', help = 'Any number.')
	args = parser.parse_args()
	
	if args.number:
		d = 2
		prime_number = 1
		while 1:
			if euler.is_prime(d):
				print "%d. PRIME NUMBER: %d" % (prime_number, d)
				pdb.set_trace()
				prime_number += 1
			if prime_number == int(args.number):
				break
			d += 1
		print "ANSWER: %d" % d

main()
