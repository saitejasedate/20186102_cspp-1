'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    str_output = ""
    input_num_lines = int(input())
    for i in range(input_num_lines):
    	str_output = str_output + input()
    	str_output += '\n'
    	i+=1
    print(str_output)

if __name__ == '__main__':
    main()
