def dividers(number):
	divs = {}
	if type(number) == type(0.):
		return divs
	if number > 2:
		potential_divs = [2]
		potential_divs += range(3, number / 2 + 1, 2)
		for d in potential_divs:
			while not number % d:
				number /= d
				if not d in divs:
					divs[d] = 0
				divs[d] += 1
	if (not divs) and (number > 0):
		divs[number] = 1
	return divs
	
def is_prime(number):
	d = dividers(number)
	if not d or d == {1: 1}:
		return False
	return d == {number: 1}
		