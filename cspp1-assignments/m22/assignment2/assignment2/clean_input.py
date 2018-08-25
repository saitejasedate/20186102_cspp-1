'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
	cleared_string = re.sub(" ", string.replace('\'', ''))
	cleared_string.strip()
	return cleared_string
    

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
