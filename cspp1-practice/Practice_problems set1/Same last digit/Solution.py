def same_last_digit(x, y):
	'''
	return True, if last digit in both the numbers are equal
	otherwise return False
	'''
	x = str(x)
	y = str(y)
	if x[-1] == y[-1]:
		return True
	else:
		return False

def main():
	x = int(input())
	y = int(input())
	print(same_last_digit(x,y))

main()