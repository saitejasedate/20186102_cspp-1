def is_input_valid(check_list):
	#print(check_list)
	for i in check_list:
		for j in i:
			if j not in "x.o":
				return False
			return True

def is_invalid_game(check_list):
	if check_list.count('x') > 5 or check_list.count('o') > 5:
		return False
		elif check_list.count('x') - check_list.count('o') > 1 or check_list.count('o') - check_list.count('x') > 1:
			return False
	return True		



def read_input():
	tic_tac_to = []
	for _ in range(3):
		tic_tac_to.append(input().split(" "))
	return tic_tac_to

def main():
	input1 = is_input_valid(read_input())
		

	# else:
	# 	print("invalid game")




main()