import re
'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
	cleared_string = re.compile('[^a-zA-z0-9]')
	cleared_string = regex.sub('',string)
	return cleared_string
    

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
