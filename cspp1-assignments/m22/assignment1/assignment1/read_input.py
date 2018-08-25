'''
@author : saitejasedate
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    program to read multiple lines of text input and store the input into a string.
    '''
    str_output = ""
    input_num_lines = int(input())
    for line_num in range(input_num_lines):
        str_output = str_output + input()
        str_output += '\n'
        line_num += 1
    print(str_output)

if __name__ == '__main__':
    main()
