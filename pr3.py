def prime_factors(number):
	factors = []
	primes = []
	f = 2
	while 1:
		is_prime = True
		for prime in primes:
			if not f % prime:
				is_prime = False
				break
		if is_prime:
			print 'Prime was found: %d' % f
			primes.append(f)
			while 1:
				if number % f:
					break
				print '%d is FACTOR of %d.' % (f, number)					
				number /= f
				factors.append(f)
			if number == 1:
				break
		f += 1
	return factors

#print 'PRIMES: %s' % prime_factors(100)
print 'Max prime of number: %d' % max(prime_factors(600851475143))
	