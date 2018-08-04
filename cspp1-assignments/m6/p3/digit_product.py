'''
@author : saitejasedate
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    a = list(str(int_input))
    l_list = len(a)
    tem_p = 1
    c_t = 0
    while c_t !=l_list:
        re_m = int_input%10
        tem_p = tem_p*re_m
        c_t = c_t+1
        mo_d = int_input//10
        int_input = mo_d
    print(tem_p)


if __name__ == "__main__":
    main()
