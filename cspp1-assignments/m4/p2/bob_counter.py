'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

def main():
    # the input string is in s
    # remove pass and start your code here
    '''
    program to print number of times bob occurs in a string
    '''
    str_lwr = raw_input() 
    len_str = len(str_lwr)
    i = 0
    c_len = 0
    for i in range(0, len_str-2, 1):
        if(str_lwr[i] == 'b' and str_lwr[i+1] == 'o' and str_lwr[i+2] == 'b'):
            c_len = c_len+1
    print(c_len)

if __name__ == "__main__":
    main()
