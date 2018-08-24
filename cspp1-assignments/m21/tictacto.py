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
		# if abs(check_list.count('x') - check_list.count('o')) > 1:
		# 	return False
	return True

def is_check_var(check_list):
	
	transpose = zip(*check_list)
	count_ = 1
	variable = 'x'
	def is_check_real(check_list):
		nonlocal variable
		nonlocal count_
		for row in check_list:
			if row.count(variable) == 3:
				return (True,variable)		#print(True)
		for row in transpose:
			if row.count(variable) == 3:
				return (True,variable)		#print(True)
		if (check_list[0][0] == check_list[1][1] == check_list[2][2] == variable) or\
		(check_list[0][2] == check_list[1][1] == check_list[2][0] == variable):
			return (True,variable)			#print(True)
		else:
			if count_  == 1:
				variable = 'o'
				count_ += 1
				is_check_real(check_list)
	
	is_check_real(check_list)

def read_input():
	tic_tac_to = []
	for _ in range(3):
		tic_tac_to.append(input().split(" "))
	return tic_tac_to

def main():
	matrix = read_input()
	input1 = is_input_valid(matrix)
	if input1:
		valid_res = is_invalid_game(matrix)	
	if valid_res:
		partial_res = is_check_var(matrix)[1]
		print(partial_res)

	# else:
	# 	print("invalid game")




main()
