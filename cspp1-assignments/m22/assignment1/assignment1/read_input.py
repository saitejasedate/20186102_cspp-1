'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    str = ""
    input_num_lines = int(input())
    for i in range(input_num_lines):
    	str = str + input()
    	i+=1
    print(str)

if __name__ == '__main__':
    main()
