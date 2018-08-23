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



def sum_of_fact(n):
	'''
	argument : n, integer type.
	return type: integer, which is the sum of factorial of each digit in n.
	example : 123 = 1! + 2! + 3! = 1 + 2 + 6 = 9
	Your task is to write code here and use fact(n) to find factorial for each digit.
	'''
	# str_n = str(n)
	sum_ = 0
	for i in str(n):
		sum_ = sum_ + fact(int(i))
	return sum_


def main():
	print(sum_of_fact(int(input())))

main()