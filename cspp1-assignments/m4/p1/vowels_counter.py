#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

def main():
    input_str = input()
    # the input string is in s
    # remove pass and start your code here
    vowel_str = 'aeiou'
    var_b = len(vowel_str)
    var_l = len(input_str)
    var_c = 0
    for i in range(0, var_l, 1):
        for j in range(0, var_b, 1):
            if input_str[i] == vowel_str[j]:
                var_c = var_c+1
    print(var_c)

if __name__ == "__main__":
    main()

