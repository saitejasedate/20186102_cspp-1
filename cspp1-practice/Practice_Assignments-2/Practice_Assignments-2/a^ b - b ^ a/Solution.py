def is_power_differences_odd(n, m):
	'''
	return boolean value
	After finding diffrences of the a^b and b^a, If it is odd, return True
	else return False
	'''
	diff_power = finding_a_power_of_b(n,m) - finding_a_power_of_b(m,n)
	return abs(diff_power) % 2 == 1


def finding_a_power_of_b(a, b):
	'''
	return number, which is a^b (a power of b)
	'''
	return a**b



def main():
	'''
	Takes Input and call the function
	'''
	n = int(input())
	m = int(input())
	print(is_power_differences_odd(n, m))

main()