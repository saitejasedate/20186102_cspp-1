# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	# ep_silon and step are initialized
	# don't change these value
	# your code starts here
	x_num = int(input())
	ep_silon = 0.01
	lo_wer = 0.0
	high_er = x_num
	bi_val = (high_er + lo_wer)/2.0
	while abs(bi_val**2 - x_num) > ep_silon:
	    if bi_val**2 < x_num:
	        lo_wer = bi_val
	    else:
	        high_er = bi_val
	    bi_val = (high_er + lo_wer)/2.0
	print(bi_val)

if __name__== "__main__":
	main()
