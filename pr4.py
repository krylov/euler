max_mult = 999
min_mult = 100
m1 = max_mult
m2 = max_mult
product = m1*m2
print "Product: %d*%d = %d" % (m1,m2,product)
palindromes = []
while 1: 
	if int(''.join(list(reversed(str(product))))) == product:
		palindromes.append(product)
	if m1 == m2:
		m1 -= 1
		m2 = max_mult
	else:
		m2 -= 1
	if m1 < min_mult:
		break
	product = m1*m2
	print "Product: %d*%d = %d" % (m1,m2,product)	

print "Max palindrome: %d\n" % max(palindromes)

