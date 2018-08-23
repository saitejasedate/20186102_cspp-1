def fact(n):
	'''
	Use this function fact(n), which takes n as integer and returns n!
	'''
	factorial = 1
	if n == 0 or n == 1:
		return 1
	else:
		while n>=1:
			factorial = factorial*n
			n = n-1
		return factorial
print(fact(0))


