'''
@author : saitejasedate
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''
    clear the string
    '''
    regex = re.compile('[^a-zA-z0-9]')
    cleared_string = regex.sub('', string).replace('^', '')
    return cleared_string


def main():
    '''
    function to take input and call the function clean_string
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
