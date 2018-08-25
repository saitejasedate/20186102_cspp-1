'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    final_dict = {}
    list_a = string.split(" ")
    for var_i in list_a:
        if var_i not in final_dict:
            final_dict[var_i] = 1
        else:
            final_dict[var_i] += 1
    return final_dict
            
def main():
    str_output = ""
    input_num_lines = int(input())
    for line_num in range(input_num_lines):
        str_output = str_output + input()
    print(tokenize(str_output))

if __name__ == '__main__':
    main()
