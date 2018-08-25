'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dict_out = {}
    string_split_list = string.split(" ")
    for element_ in (string_split_list):
        if element_ not in string_split_list:
            dict_out[element_] = 1
        else:
            dict_out[element_] += 1
    return dict_out
            
def main():
    input_num_lines = int(input())
    str_output = ""
    for line_num in range(input_num_lines):
        str_output = str_output + input()
        line_num += 1
    print(tokenize(str_output))

if __name__ == '__main__':
    main()
