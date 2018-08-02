'''
@author : saitejasedate
Program to print number of vowels in a given string
'''

#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

def main():
    '''
    Main function prints the number of vowels in given string
    '''
    input_str = raw_input()
    # the input string is in s
    # remove pass and start your code here
    vowel_str = 'aeiou'
    length_l = len(input_str)
    length_b = len(vowel_str)
    co_unt = 0
    for i in range(0, length_l, 1):
        for j in range(0, length_b, 1):
            if input_str[i] == vowel_str[j]:
                co_unt = co_unt+1
    print c

if __name__ == "__main__":
    main()
