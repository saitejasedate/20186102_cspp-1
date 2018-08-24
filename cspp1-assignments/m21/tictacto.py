def is_input_valid(check_list):
    #print(check_list)
    for i in check_list:
        for j in i:
            if j not in "x.o":
                return False
    return True

def is_invalid_game(check_lists):
    count_x_variable = 0
    count_o_variable = 0
    for row in check_lists:
        count_x_variable += row.count('x')
        count_o_variable += row.count('o')
    if count_x_variable > 5 or count_o_variable > 5 or count_x_variable == count_o_variable:
        print("invalid game")
        return None
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
                return True,variable        #print(True)
        for row1 in transpose:
            if row1.count(variable) == 3:
                return True,variable        #print(True)
        if (check_list[0][0] == check_list[1][1] == check_list[2][2] == variable) or\
        (check_list[0][2] == check_list[1][1] == check_list[2][0] == variable):
            return True,variable            #print(True)
        else:
            if count_  == 1:
                variable = 'o'
                count_ += 1
                return is_check_real(check_list)
    
    return is_check_real(check_list)

def read_input():
    tic_tac_to = []
    for _ in range(3):
        tic_tac_to.append(input().split(" "))
    return tic_tac_to

def main():
    matrix = read_input()
    input1 = is_input_valid(matrix)
    if input1 == False:
        print("invalid input")
    else:
        valid_res = is_invalid_game(matrix) 
        if valid_res:
            partial_res = is_check_var(matrix)
            if partial_res[1] in 'xo':
                print(partial_res[1])
main()
