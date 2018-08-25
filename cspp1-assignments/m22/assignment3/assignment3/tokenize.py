'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dict_ = {}
    a = string_.split(" ")
	for i_ in enumerate(a):
		dict_[i_[1]] = i_[0]
		print(dict_)
            
def main():
    str_output = ""
    input_num_lines = int(input())
    for line_num in range(input_num_lines):
        str_output = str_output + input()
        str_output += '\n'
        line_num += 1
    print(tokenize(str_output))

if __name__ == '__main__':
    main()
