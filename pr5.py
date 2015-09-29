import argparse

def dividers(number):
	divs = {}
	potential_divs = [2]
	potential_divs += range(3, number / 2 + 1, 2)
	for d in potential_divs:
		while not number % d:
			number /= d
			if not d in divs:
				divs[d] = 0
			divs[d] += 1	
	if not divs:
		divs[number] = 1
	return divs
	
def main():
	parser = argparse.ArgumentParser(description = 'Euler program.')
	parser.add_argument('-n', '--number', help = 'Any number [from 2 to 1000].')
	parser.add_argument('-s', '--numbers', help = 'Any numbers [from 2 to 1000].')	
	args = parser.parse_args()
	
	if args.numbers:
		nm = args.numbers.split(",")
		nm = [int(i) for i in nm]
		nm = sorted(nm)
		nm_divs = []
		for i in nm:
			nm_divs.append(dividers(int(i)))
		amount = len(nm)
		i = 1
		while i < amount:
			d1 = nm_divs[i-1]
			len_d1 = len(d1)
			d2 = nm_divs[i]
			len_d2 = len(d2)
			for k in d1:
				if (not k in d2) or (d2[k] < d1[k]):
					d2[k] = d1[k]
			nm_divs[i] = d2			
			i += 1
		product = nm_divs[-1]
		print "%d" % reduce(lambda res,x: res*pow(x,product[x]), product, 1)
	elif args.number:
		print "divs: %s" % str(dividers(int(args.number)))

main()
	