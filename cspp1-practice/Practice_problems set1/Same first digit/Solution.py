def same_first_digit(x, y):
	'''
	return True, if first digit in both the numbers are equal
	otherwise return False
	'''
	x = str(abs(x))
	y = str(abs(y))
	if x[0] == y[0]:
		return True
	else:
		return False

def main():
	x = int(input())
	y = int(input())
	print(same_first_digit(x,y))

main()