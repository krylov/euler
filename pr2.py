fib = [1,2]
threshold = 4000000
while 1:
  n = fib[-1] + fib[-2]
  if n > threshold:
    break
  fib.append(n)
even_fib = [v for v in fib if not v % 2]
print sum(even_fib)

