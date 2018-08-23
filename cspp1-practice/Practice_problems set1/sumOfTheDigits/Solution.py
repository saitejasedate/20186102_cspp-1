def sum_of_digits(x):
	'''
	integer parameter x.
	return the sum of all the digits of given number
	'''
	sum_d = 0
	for i in str(x):
		sum_d = sum_d + int(str(i))
	return sum_d


def main():
	x = int(input())
	print(sum_of_digits(x))

main()