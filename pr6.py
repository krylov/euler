import argparse

def product_pairs(numbers):
	p = []
	ix = 1
	for a in numbers:
		cur_ix = ix
		while cur_ix < len(numbers):
			p.append(a * numbers[cur_ix])
			cur_ix += 1
		ix += 1
	return p
	
def main():
	parser = argparse.ArgumentParser(description = 'Euler program.')
	parser.add_argument('-n', '--number', help = 'Any number [from 2 to 1000].')
	args = parser.parse_args()
	
	if args.number:
		numbers = range(1, int(args.number) + 1)
		print "ANSWER: %d" % (2 * sum(product_pairs(numbers)))

main()